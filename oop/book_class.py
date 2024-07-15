# book_class.py

class Book:
    #class representing a book with title, author, and publication year.

    def __init__(self, title, author, year):
        #Initialize the book
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        #Print a message 
        print(f"Deleting {self.title}")

    def __str__(self):
        #Return a string representation
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        #Return an official string representation
        return f"Book('{self.title}', '{self.author}', {self.year})"