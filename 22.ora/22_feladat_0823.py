from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import os

class ImageDownloader():
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.images = None
        self.soup = None

    def html_downloader(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            self.soup = BeautifulSoup(response.text, 'html.parser')
        else:
            print("Something is wrong.")

    def image_finder(self):
        if self.soup is None:
            print("No HTML loaded. Call html_downloader() first.")
            self.images = []
            return

        self.images = self.soup.find_all('img')
        os.makedirs(self.path, exist_ok=True)

    def download_all(self):
        if not self.images:
            print("No images to download.")
            return

        for img in self.images:
            src = img.get("src")
            if src:
                img_url = urljoin(self.url, src)
                img_response = requests.get(img_url, stream=True)
                if img_response.status_code == 200:
                    file_name = os.path.join(self.path, os.path.basename(img_url))
                    with open(file_name, "wb") as file:
                        for chunk in img_response.iter_content(4096):
                            file.write(chunk)
        print("All images are saved")

def main():
    downloader = ImageDownloader("http://books.toscrape.com", "url_images")
    downloader.html_downloader()
    downloader.image_finder()
    downloader.download_all()


main()
