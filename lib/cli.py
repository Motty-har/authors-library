# lib/cli.py

from helpers import (
    exit_program,
    add_player
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E" or "e":
            exit_program()
        elif choice == "A" or "a":
            add_player()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type E or e to exit the program")
    print("Type A or a to add a player")


if __name__ == "__main__":
    main()
