# user_module.py

import re
import csv
import os

class UserSystem:

    USER_FILE = "users.csv"

    @staticmethod
    def validate_name(name):
        return re.match(r'^[A-Za-z ]{2,}$', name)

    @staticmethod
    def validate_id(user_id):
        return re.match(r'^[0-9]{4,10}$', user_id)

    @staticmethod
    def register_user():
        print("\n=== USER REGISTRATION ===")

        while True:
            name = input("Enter your name: ")
            if not UserSystem.validate_name(name):
                print("❌ Invalid name! Only letters & spaces allowed.")
                continue
            break

        while True:
            user_id = input("Enter User ID (4–10 digits): ")
            if not UserSystem.validate_id(user_id):
                print("❌ Invalid ID! Only numbers (4–10 digits).")
                continue
            break

        UserSystem.save_user_record(name, user_id)
        print("✔ User successfully registered!")
        return user_id

    @staticmethod
    def save_user_record(name, user_id):
        file_exists = os.path.isfile(UserSystem.USER_FILE)

        with open(UserSystem.USER_FILE, "a", newline="") as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["UserID", "Name"])
            writer.writerow([user_id, name])

    @staticmethod
    def verify_user(user_id):
        """Check if user exists in users.csv"""
        if not os.path.exists(UserSystem.USER_FILE):
            return False

        with open(UserSystem.USER_FILE, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                if row[0] == user_id:
                    return True
        return False
