import json

class Book:
    def __init__(self, title, author, year, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def to_dic(self):
        return {
            'title': self.title,
            'author': self.author,
            'year': self.year,
            'isbn': self.isbn,
        }

class Library:
    def __init__(self, title):
        self.title = title
        self.books = []

    def add_book(self, book):
        self.books.append(Book(book.title, book.author, book.year, book.isbn).to_dic())

    def remove_book(self, isbn):
        del self.books[isbn] #itt az egészet kitörlni vagy csak az isbn-t?

    def list_books(self):
        print(self.books)

    def sort_books_by_year(self, year):
        sorted_by_year = [book for book in self.books if book.year == year]
        print(f'The books from {year} are: {sorted_by_year}')

    def get_books_by_author(self, author):
        sorted_by_author = [book for book in self.books if book.author == author]
        print(f'The books from {author} are: {sorted_by_author}')

    def write_json(self):
        with open("data/books.json", "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=True)



