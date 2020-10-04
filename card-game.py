import os
import bcrypt
from getpass import getpass


class Menu():
    def __init__(self):
        self.users_path = "users.txt"
        self.highscores_path = "highscores.txt"

        open(self.users_path, "a")
        open(self.highscores_path, "a")

        self.main(self.users_path, self.highscores_path)

    def main(self, users_path, highscores_path):
        if os.stat(self.users_path).st_size == 0:
            print("\nUsers not found. Creating new user...")
            self.create_user(self.users_path)
            print("\nNew user created.")

        userlist = self.parse_file(users_path)

        self.auth(userlist)

    def auth(self, userlist):
        self.authenticated_users = []

        for i in range(5):
            username = input("\nUsername: ")
            password = getpass("Password: ")

            for user in userlist:
                if username == user[0] and bcrypt.checkpw(password.encode(), user[1].encode()):
                    self.authenticated_users.append(user)
                    print("\nAuthenticated.")
                    return True
                else:
                    continue

        print("\nAuthentication failed.")
        exit()

    def create_user(self, users_path):
        new_username = input("\nNew username: ")
        new_password = getpass("New password: ")

        with open(users_path, "a") as f:
            f.write(new_username + ":" + bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode())

    def parse_file(self, filepath):
        with open(filepath, "r") as f:
            data = f.read()
        return [line.split(":") for line in data.split("\n")]


if __name__ == "__main__":
    Menu()
