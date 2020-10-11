from os import path
from bcrypt import hashpw, checkpw, gensalt
from getpass import getpass
from random import shuffle, choice


class Player():
    def __init__(self, player_name: str):
        self.name = player_name
        self.hand = []


class Deck():
    def __init__(self):
        self.cards = [(number, colour) for number in range(1, 11) for colour in ["red", "yellow", "black"]]
        shuffle(self.cards)
        self.card_buffer = []

    def choose_card(self):
        card = choice(self.cards[0])
        self.move_card(card, self.card_buffer)
        self.cards.remove(card)
        return card

    def move_cards(self, src_deck: list, dst_deck: list):
        dst_deck.append(*src_deck)
        src_deck.clear()


class Game():
    def __init__(self, player1: Player, player2: Player, deck: Deck):
        pass


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
            f.write(new_username + ":" + hashpw(new_password.encode(), gensalt()).decode())

    def parse_file(self, filepath: str):
        with open(filepath, "r") as f:
            data = f.read()
        return [line.split(":") for line in data.split("\n")]


if __name__ == "__main__":
    # Menu()
    deck = Deck()
