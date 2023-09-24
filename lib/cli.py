# lib/cli.py

from helpers import (
    exit_program,
    list_authors
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E" or "e":
            exit_program()
        elif choice == "A" or "a":
            list_authors()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("E or e. Exit the program")
    print("A or a. View list of authors")


if __name__ == "__main__":
    main()
