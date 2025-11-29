# main.py

from user_module import UserSystem
from library_module import Library

def main():

    print("\n===== WELCOME TO LIBRARY SYSTEM =====")
    print("1. Register User")
    print("2. Login User")
    choice = input("Enter option: ")

    if choice == "1":
        user_id = UserSystem.register_user()

    elif choice == "2":
        user_id = input("Enter your User ID: ")
        if not UserSystem.verify_user(user_id):
            print("❌ User not found. Register first.")
            return
        print("✔ Login successful!")

    else:
        print("Invalid choice!")
        return

    lib = Library()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. View all books")
        print("2. Borrow a book")
        print("3. Return a book")
        print("4. Exit")

        option = input("Enter choice: ")

        if option == "1":
            lib.show_books()

        elif option == "2":
            lib.borrow(user_id)

        elif option == "3":
            lib.return_book(user_id)

        elif option == "4":
            print("✔ Thank you for using the library!")
            break

        else:
            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()
