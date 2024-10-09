# Menus
import book
import user
import author

books = book.Book()

bible = books.add_book("Bible", "God", "Religion", "0", "available")
harry_potter = books.add_book("Harry Potter", "J. K. Rowling", "Fantasy", "1997", "available")
print(books)

def main_menu():
    print("Welcome to the Library Management System!")
    keep_going = True
    while keep_going:
        print("\nMain Menu:\n1. Book Operations\n2. User Operations\n3. Author Operations\n4. Quit")
        which_operation = input()
        if which_operation == "1":
            book_menu()
        elif which_operation == "2":
            user_menu()
        elif which_operation == "3":
            author_menu()
        elif which_operation == "4":
            keep_going = False
        else:
            print("Invalid input. Please enter a number from 1 to 4.")

def book_menu():
    print("\nBook Operations:\n1. Add a new book\n2. Borrow a book\n3. Return a book\n4. Search for a book\n5. Display all books")
    which_operation = input()
    if which_operation == "1":
        book.new_book(books)
    elif which_operation == "2":
        pass
#        book.borrow_book()
    elif which_operation == "3":
        pass
    elif which_operation == "4":
        pass
    elif which_operation == "5":
        pass
    else:
        print("Invalid input. Please enter a number from 1 to 5.")

def user_menu():
    print("\nUser Operations:\n1. Add a new user\n2. View user details\n3. Display all users")
    which_operation = input()
    if which_operation == "1":
        pass
    elif which_operation == "2":
        pass
    elif which_operation == "3":
        pass
    else:
        print("Invalid input. Please enter a number from 1 to 3.")
def author_menu():
    print("\nAuthor Operations:\n1. Add a new author\n2. View author details\n3. Display all authors")
    which_operation = input()
    if which_operation == "1":
        pass
    elif which_operation == "2":
        pass
    elif which_operation == "3":
        pass
    else:
        print("Invalid input. Please enter a number from 1 to 3.")