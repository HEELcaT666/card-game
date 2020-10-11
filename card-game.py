import os
import bcrypt
from getpass import getpass


class Menu():
    def __init__(self):
        self.users_path = "users.txt"
        self.highscores_path = "highscores.txt"

        self.main()

    def main(self):
        print("\nWelcome!\n1. Login\n2. Show Leaderboard\n3. Exit")
        while True:
            selector = input(">>> ")
            if selector == "1":
                self.auth()
                break
            elif selector == "2":
                print("This feature is yet to be implemented")  # This needs to be implemented
            elif selector == "3":
                exit()
            else:
                print("Invalid input. Please, try again.")

    def auth(self):
        if not os.path.exists(self.users_path):
            print("\nUsers not found. Creating new user...")
            self.create_user()
            print("\nNew user created.")

        userlist = self.parse_file(self.users_path)

        for i in range(5):
            username = input("\nUsername: ")
            password = getpass("Password: ")

            for user in userlist:
                if username == user[0] and bcrypt.checkpw(password.encode(), user[1].encode()):
                    print("\nAuthenticated.")
                    return True
                else:
                    continue

        print("\nAuthentication failed.")
        return False

    def create_user(self):
        new_username = input("\nNew username: ")
        new_password = getpass("New password: ")

        with open(self.users_path, "a") as f:
            f.write(new_username + ":" + bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode())

    def parse_file(self, filepath):
        with open(filepath, "r") as f:
            data = f.read()
        return [line.split(":") for line in data.split("\n")]


if __name__ == "__main__":
    Menu()
