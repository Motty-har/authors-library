# lib/cli.py

from helpers import (
    exit_program,
    add_player
    list_players
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E":
            exit_program()
        elif choice == "A":
            add_player()
        elif choice == "L":
            list_players()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type E to exit the program")
    print("Type A to add a player")
    print("Type L to see a list of players")


if __name__ == "__main__":
    main()
