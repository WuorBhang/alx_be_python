# library_management.py

class Book:
    """A class representing a book in the library."""
    
    def __init__(self, title, author):
        """Initialize the book with a title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available for checkout."""
        return not self._is_checked_out


class Library:
    """A class representing a library that contains books."""
    
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book from the library by its title."""
        for book in self._books:
            if book.title == title and book.is_available():
                if book.check_out():
                    print(f"Checked out '{title}'.")
                    return True
        print(f"'{title}' is not available for checkout.")
        return False

    def return_book(self, title):
        """Return a book to the library by its title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                if book.return_book():
                    print(f"Returned '{title}'.")
                    return True
        print(f"'{title}' was not checked out.")
        return False

    def list_available_books(self):
        """List all books that are available for checkout."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books available.")

