import os
import time

class User:
    @staticmethod
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def __init__(self, first_name, last_name, email, password, status='inactive') -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.status = status

    def display_user(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Password: {self.password}")
        print(f"Status: {self.status}")
        print("=" * 30)

    @staticmethod
    def create_user():
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        return User(first_name, last_name, email, password)


new_users = []

while True:
    User.clear_screen()
    print("Welcome to User Management")
    print("1: Add new user")
    print("2: Display all users")
    print("3: Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_user = User.create_user()
        new_users.append(new_user)
        print("User added successfully!")
        time.sleep(4)

    elif choice == "2":
        User.clear_screen()
        if new_users:
            print("Displaying all new users:\n")
            for i in new_users:
                i.display_user()
            time.sleep(5)
        else:
            print("No users to display.")
            time.sleep(5)

    elif choice == "3":
        print("Exiting...")
        time.sleep(4)
        break

    else:
        print("Invalid choice, please try again.")
        time.sleep(5)
