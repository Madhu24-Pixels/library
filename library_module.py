# library_module.py

import csv
import os

class Book:
    def __init__(self, book_id, title, author, copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.copies = copies

    def show_info(self):
        print(f"{self.book_id} | {self.title} | {self.author} | Copies: {self.copies}")


class Library:

    BOOK_FILE = "library.csv"
    TXN_FILE = "transactions.csv"

    def __init__(self):
        self.books = {}
        self.load_books()

    # ---------------- LOAD & SAVE ----------------
    def load_books(self):
        if not os.path.exists(self.BOOK_FILE):
            self.create_default()

        with open(self.BOOK_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                book_id, title, author, copies = row
                self.books[book_id] = Book(book_id, title, author, int(copies))

    def save_books(self):
        with open(self.BOOK_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Title", "Author", "Copies"])
            for b in self.books.values():
                writer.writerow([b.book_id, b.title, b.author, b.copies])

    def create_default(self):
        books = [
            ["1", "Python Basics", "John Smith", "5"],
            ["2", "AI for Beginners", "Emma Brown", "3"],
            ["3", "Data Science 101", "William Lee", "4"],
            ["4", "Machine Learning", "Andrew Ng", "6"],
            ["5", "Deep Learning", "Ian Goodfellow", "2"],
            ["6", "Computer Vision", "Richard Hartley", "3"],
            ["7", "NLP Essentials", "Jacob Devlin", "5"],
            ["8", "Database Systems", "Navathe", "4"],
            ["9", "Operating Systems", "Galvin", "6"],
            ["10", "Algorithms", "CLRS", "3"],
        ]

        with open(self.BOOK_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Title", "Author", "Copies"])
            writer.writerows(books)

    # ---------------- TRANSACTION LOG ----------------
    def save_transaction(self, user_id, book_id, action):
        file_exists = os.path.isfile(self.TXN_FILE)
        with open(self.TXN_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["UserID", "BookID", "Action"])
            writer.writerow([user_id, book_id, action])

    # ---------------- OPERATIONS ----------------

    def show_books(self):
        print("\n========= AVAILABLE BOOKS =========")
        for b in self.books.values():
            b.show_info()

    def borrow(self, user_id):
        book_id = input("Enter Book ID to borrow: ")

        if book_id not in self.books:
            print("❌ Invalid Book ID!")
            return

        if self.books[book_id].copies == 0:
            print("❌ No copies available!")
            return

        self.books[book_id].copies -= 1
        self.save_books()
        self.save_transaction(user_id, book_id, "BORROW")
        print(f"✔ Book borrowed: {self.books[book_id].title}")

    def return_book(self, user_id):
        book_id = input("Enter Book ID to return: ")

        if book_id not in self.books:
            print("❌ Invalid Book ID!")
            return

        self.books[book_id].copies += 1
        self.save_books()
        self.save_transaction(user_id, book_id, "RETURN")
        print(f"✔ Book returned: {self.books[book_id].title}")
