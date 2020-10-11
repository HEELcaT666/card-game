from os import path
from bcrypt import hashpw, checkpw, gensalt
from getpass import getpass
from random import shuffle


class Menu():
    def __init__(self):
        self.users_path = "users.txt"
        self.highscores_path = "highscores.txt"

        self.main()

    def main(self):
        print("\nWelcome!\n1. Play Game\n2. Show Leaderboard\n3. Exit")
        while True:
            selector = input(">>> ")
            if selector == "1":
                if not self.auth():
                    exit()
                else:
                    Game()
            elif selector == "2":
                print("This feature is yet to be implemented")  # This needs to be implemented
            elif selector == "3":
                exit()
            else:
                print("Invalid input. Please, try again.")

    def auth(self):
        if not path.exists(self.users_path):
            print("\nUsers not found. Creating new user...")
            self.create_user()
            print("\nNew user created.")

        userlist = self.parse_file(self.users_path)

        for i in range(5):
            username = input("\nUsername: ")
            password = getpass("Password: ")

            for user in userlist:
                if username == user[0] and checkpw(password.encode(), user[1].encode()):
                    print("\nLogin successful!")
                    return True
                else:
                    continue

        print("\nAuthentication failed.")
        return False

    def create_user(self):
        new_username = input("\nNew username: ")
        new_password = getpass("New password: ")

        with open(self.users_path, "a") as f:
            f.write(new_username + ":" + hashpw(new_password.encode(), gensalt()).decode())

    def parse_file(self, filepath):
        with open(filepath, "r") as f:
            data = f.read()
        return [line.split(":") for line in data.split("\n")]


class Game():
    def __init__(self):
        print("Welcome to the Card Game!\n")
        self.player1 = Player(input("Player 1 name: "))
        self.player2 = Player(input("Player 2 name: "))
        self.deck = Deck()


class Deck():
    def __init__(self):
        self.cards = [(number, colour) for number in range(1, 11) for colour in ["red", "yellow", "black"]]
        shuffle(self.cards)


class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.hand = []


if __name__ == "__main__":
    Menu()
