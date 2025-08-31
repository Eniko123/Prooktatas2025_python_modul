class SimpleTextComparer:
    def __init__(self):
        self.processor = TextProcessor()

    def compare_texts(self, text1: str, text2: str) -> float:
        words1 = self.processor.prepare_text(text1)
        words2 = self.processor.prepare_text(text2)

        set1 = set(words1)
        set2 = set(words2)

        union = len(set1 | set2)
        result = len(set1 & set2) / union * 100

        ResultPrinter.print_result(result)
        return result

class TextComparer:
    def __init__(self):
        self.comparer = SimpleTextComparer()

    def compare_texts(self, text1: str, text2: str) -> float: #float a visszatérési érték, a két szöveg egyezése százalékos formátumban
        return self.comparer.compare_texts(text1, text2)

class TextProcessor:
    @staticmethod
    def load_file(file_path):
        with open (file_path, "r", encoding="utf-8") as file:
            content = file.read()
            return content

    @staticmethod
    def prepare_text(text):
        words = text.lower().split()
        return words

class FileComparer:
    def __init__(self):
        self.processor = TextProcessor()
        self.comparer = SimpleTextComparer()

    def compare_files(self, file1, file2):
        content1 = self.processor.load_file(file1)
        content2 = self.processor.load_file(file2)
        return self. comparer.compare_texts(content1, content2)

class ResultPrinter:
    @staticmethod
    def print_result(result):
        print(f'{round(result,2)}% percent of the texts are similar')







