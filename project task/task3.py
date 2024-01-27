import hashlib
import getpass

class PasswordManager:
    PASSWORD_FILE = "C:/Users/Dell/Documents/password.txt"

    def __init__(self):
        self.lines = self.read_password_file()

    @staticmethod
    def encrypt_password(password):
        return hashlib.md5(password.encode()).hexdigest()

    def read_password_file(self):
        try:
            with open(self.PASSWORD_FILE, "r") as file:
                lines = file.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            return []

    def write_password_file(self):
        with open(self.PASSWORD_FILE, "w") as file:
            file.write("\n".join(self.lines))

    def get_user_info(self, username):
        for line in self.lines:
            fields = line.split(":")
            if fields[0] == username:
                return fields
        return None

    def add_user(self):
        new_username = input("Enter new username: ").strip()
        if self.get_user_info(new_username) is not None:
            print("Cannot add. Most likely username already exists.")
            return

        real_name = input("Enter real name: ").strip()
        password = getpass.getpass("Enter password: ")
        password = self.encrypt_password(password)

        new_entry = f"{new_username}:{real_name}:{password}"

        self.lines.append(new_entry)

        self.write_password_file()
        print("User Created.")

    def delete_user(self):
        username_to_delete = input("Enter username to delete: ").strip()

        user_info = self.get_user_info(username_to_delete)

        if user_info is not None:
            confirmation = input(f"Are you sure you want to delete the user {username_to_delete}? (y/n): ").strip().lower()
            
            if confirmation == "y":
                self.lines.remove(":".join(user_info))
                self.write_password_file()
                print("User Deleted.")
            else:
                print("Please enter 'y' or 'n' in order to proceed!!")
        else:
            print("User not found.")

            
    def change_password(self):
        username = input("User: ").strip()
        current_password = self.encrypt_password(getpass.getpass("Current Password: "))
        
        user_info = self.get_user_info(username)

        if user_info is not None and user_info[2] == current_password:
            new_password = self.encrypt_password(getpass.getpass("New Password: "))
            confirm_password = self.encrypt_password(getpass.getpass("Confirm: "))

            if new_password == confirm_password:
                index = self.lines.index(":".join(user_info))
                self.lines[index] = ":".join([user_info[0], user_info[1], new_password])

                # Write the changes back to the password file
                self.write_password_file()

                print("Password changed.")
            else:
                print("New password and confirmation do not match. Password change canceled.")
        else:
            print("Invalid user or current password.")


    def login(self):
        username = input("User: ").strip()
        password = self.encrypt_password(getpass.getpass("Password: "))

        user_info = self.get_user_info(username)

        if user_info is not None and user_info[2] == password:
            print("Access granted.")
        else:
            print("Access denied.")


if __name__ == "__main__":
    manager = PasswordManager()

    while True:
        print("\n1. Add User\n2. Delete User\n3. Change Password\n4. Login\n5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            manager.add_user()
        elif choice == "2":
            manager.delete_user()
        elif choice == "3":
            manager.change_password()
        elif choice == "4":
            manager.login()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
