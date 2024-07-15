# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    library = Library()
    
    # Adding books to the library
    book1 = Book("Pride and Prejudice", "Jane Austen")
    ebook1 = EBook("Snow Crash", "Neal Stephenson", 500)
    printbook1 = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)
    
    library.add_book(book1)
    library.add_book(ebook1)
    library.add_book(printbook1)

    # Listing all books in the library
    print("Listing all books in the library:")
    library.list_books()

if __name__ == "__main__":
    main()
