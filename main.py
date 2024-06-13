from datetime import datetime
from models import Book, session


def add_book(title,author,publication_date):

    try:
        pub_date = datetime.strptime(publication_date, "%Y-%m-%d").date()
        new_book = Book(title=title, author=author, publication_date=pub_date)
        session.add(new_book)
        session.commit()
        print("Book added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

def view_books():
    books = session.query(Book).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Publication Date:{book.publication_date}")         
def update_book(book_id, title=None, author=None, publication_date=None):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        if title:
            book.title = title
        if author:
            book.author = author
        if publication_date:
            book.publication_date = datetime.strptime(publication_date, "%Y-%m-%d").date()
        session.commit()
        print("Book updated successfully!")
    else:
        print("Book not found!")

def delete_book(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print("Book deleted successfully!")
    else:
        print("Book not found!")

if __name__ == "__main__":
    while True:
        print("\nMyLibrary Menu:")
        print("1. Add Book")
        print("2. View Books")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            add_book(title, author, publication_date)
        elif choice == '2':
            view_books()
        elif choice == '3':
            book_id = int(input("Enter book ID to update: "))
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            publication_date = input("Enter new publication date (YYYY-MM-DD, leave blank to keep current): ")
            update_book(book_id, title, author, publication_date)
        elif choice == '4':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice, please try again.")       