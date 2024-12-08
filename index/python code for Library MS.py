# For class Library
class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Book '{book.title}' added to the library.")

    def remove_book(self, book):
        self.books.remove(book)
        print(f"Book '{book.title}' removed from the library.")

    def register_member(self, member):
        self.members.append(member)
        print(f"Member '{member.name}' registered.")

    def issue_book(self, member, book):
        if book in self.books and book.status == "available":
            book.status = "issued"
            member.borrow_book(book)
            print(f"Book '{book.title}' issued to {member.name}.")
        else:
            print(f"Book '{book.title}' is not available.")


# For class Book
class Book:
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.status = "available"

    def view_details(self):
        return f"Title: {self.title}, ISBN: {self.isbn}, Status: {self.status}"

    def check_availability(self):
        return self.status == "available"


# For class Member
class Member:
    def __init__(self, member_id, name, phone_no):
        self.member_id = member_id
        self.name = name
        self.phone_no = phone_no
        self.borrowed_books = []

    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            book.status = "available"
            print(f"{self.name} returned '{book.title}'.")


# For class Librarian
class Librarian:
    def __init__(self, name):
        self.name = name

    def add_book(self, library, book):
        library.add_book(book)

    def remove_book(self, library, book):
        library.remove_book(book)


# For class Loan
class Loan:
    def __init__(self, book, member, issue_date):
        self.book = book
        self.member = member
        self.issue_date = issue_date

    def complete_transaction(self):
        self.book.status = "available"
        print(f"Loan completed for book '{self.book.title}' by member '{self.member.name}'.")


# For class User
class User:
    def __init__(self, name, email, member_id):
        self.name = name
        self.email = email
        self.member_id = member_id

    def login(self):
        print(f"{self.name} logged in.")

    def logout(self):
        print(f"{self.name} logged out.")
