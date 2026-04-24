"""
OOP Problem: Library & Book System

Question
Design a system where a Library contains multiple Books.

- Library has a name and a list of books
- Book (inner class) has a title
- Book should:
- register itself into the library
- display: "<book_title> is available in <library_name>"

Constraints
- Book must access the library name from the outer class
- Do not store the library name separately inside Book
- Book should not auto-register on creation
- Registration must happen via a method
- Maintain clean OOP design (no hacks or globals)"""


class Library:
    def __init__(self):
        self.name = "City Library"
        self.books = []

    class Book:
        def __init__(self, title, outer):
            self.title = title
            self.outer = outer

        def register(self):
            self.outer.books.append(self.title)

        def display(self):
            if self.title in self.outer.books:
                print(f"{self.title} is available in {self.outer.name}")

            else:
                print(f"{self.title} is not available in {self.outer.name}")


lib = Library()

b1 = lib.Book("Python basics", lib)
b2 = lib.Book("AI Fundamentals", lib)

b1.register()
b2.register()

b1.display()
b2.display()

print(lib.books)
