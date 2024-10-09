class Book():
    def __init__(self):
        self.library = {}

    def add_book(self, title, author, genre, pub_date, available):
        self.library[title] = {}
        self.library[title]["title"] = title
        self.library[title]["author"] = author
        self.library[title]["genre"] = genre
        self.library[title]["pub_date"] = pub_date
        self.library[title]["available"] = available

    def update_availability(self, available):
        self.available = available

    def borrow_book(self, title):
        if self.library[title]:
            if self.library[title]["available"] == "available":
                self.library[title]["available"] = "unavailable"
                print(f"{title} borrowed.")
            else:
                print(f"{title} is unavailable. Sorry.")
        else:
            print(f"{title} not found.")

    def display_book(self):
        print(f"Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Published on {self.pub_date}, is {self.available}")

def new_book(books):
    title = input("What is the title of the book? ").title()
    if title in books:
        print("That book is already in the library.")
        return
    author = input("Who is the author of the book? ").title()
    genre = input("What is the genre of the book? ").title()
    if genre == "":
        genre = "General"
    pub_date = input("When was the book published? ").title()
    available = "available"
    books.add_book(title, author, genre, pub_date, available)

# def borrow():
#     title = input("What book would you like to borrow? ").title()
#     if title in books:
#         if Book.check_availability(title) == "available":
#             Book.update_availability("unavailable")
#             print(f"{books[title]} checked out.")
#         else:
#             print(f"{books[title]} is not available right now. Sorry.")
#     else:
#         print("Doesn't look like the library has that book.")