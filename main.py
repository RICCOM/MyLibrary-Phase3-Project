from datetime import datetime
from models import User, Book, session

# Adding a new user
def add_user(name, email):
    try:
        new_user = User(name=name, email=email)
        session.add(new_user)
        session.commit()
        print("User added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

# Viewing all users
def view_users():
    users = session.query(User).all()
    for user in users:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")

# Finding a user by ID
def find_user_by_id(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")
    else:
        print("User not found!")

# Deleting a user by ID
def delete_user(user_id):
    user = session.query(User).filter(User.id == user_id).first()
    if user:
        session.delete(user)
        session.commit()
        print("User deleted successfully!")
    else:
        print("User not found!")

# Adding a new book with an associated user ID
def add_book(title, author, publication_date, user_id):
    try:
        pub_date = datetime.strptime(publication_date, "%Y-%m-%d").date()
        new_book = Book(title=title, author=author, publication_date=pub_date, user_id=user_id)
        session.add(new_book)
        session.commit()
        print("Book added successfully!")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

# Viewing all books
def view_books():
    books = session.query(Book).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_date}, User ID: {book.user_id}")

# Finding a book by ID
def find_book_by_id(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_date}, User ID: {book.user_id}")
    else:
        print("Book not found!")

# Deleting a book by ID
def delete_book(book_id):
    book = session.query(Book).filter(Book.id == book_id).first()
    if book:
        session.delete(book)
        session.commit()
        print("Book deleted successfully!")
    else:
        print("Book not found!")

# Viewing books associated with a particular user
def view_books_by_user(user_id):
    books = session.query(Book).filter(Book.user_id == user_id).all()
    for book in books:
        print(f"ID: {book.id}, Title: {book.title}, Author: {book.author}, Publication Date: {book.publication_date}")

if __name__ == "__main__":
    while True:
        print("\nMyLibrary Menu:")
        print("1. Add User")
        print("2. View Users")
        print("3. Find User by ID")
        print("4. Delete User")
        print("5. Add Book")
        print("6. View Books")
        print("7. Find Book by ID")
        print("8. Delete Book")
        print("9. View Books by User")
        print("10. Exit")

        choice = input("Enter your choice: ")
        if choice == '1':
            name = input("Enter user name: ")
            email = input("Enter user email: ")
            add_user(name, email)
        elif choice == '2':
            view_users()
        elif choice == '3':
            user_id = int(input("Enter user ID to find: "))
            find_user_by_id(user_id)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            publication_date = input("Enter publication date (YYYY-MM-DD): ")
            user_id = int(input("Enter associated user ID: "))
            add_book(title, author, publication_date, user_id)
        elif choice == '6':
            view_books()
        elif choice == '7':
            book_id = int(input("Enter book ID to find: "))
            find_book_by_id(book_id)
        elif choice == '8':
            book_id = int(input("Enter book ID to delete: "))
            delete_book(book_id)
        elif choice == '9':
            user_id = int(input("Enter user ID to view books: "))
            view_books_by_user(user_id)
        elif choice == '10':
            break
        else:
            print("Invalid choice, please try again.")
