class Book:
    def __init__(self, title: str):
        self.title = title

    def __del__(self):
        print (f"Book object destroyed: '{self.title}'")

class Library:
    def __init__(self, books: list[Book] = None):
        self.books = books if books else []

    def __del__(self):
        print("Library object destroyed")

book1 = Book("The Hobbit")
book2 = Book("1984")
my_library = Library([book1, book2])
print(f"Library contains: {[book.title for book in my_library.books]}")