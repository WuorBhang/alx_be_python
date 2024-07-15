# library_system.py
class Book:
    #base class representing a book with title and author.
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"{self.title} by {self.author}, File Size: {self.file_size}KB"

class PrintBook(Book):
   
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"{self.title} by {self.author}, Page Count: {self.page_count}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        #Add a book to the library collection
        self.books.append(book)

    def list_books(self):
        #List all books in the library
        for book in self.books:
            print(book)
