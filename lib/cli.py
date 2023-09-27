# lib/cli.py

from helpers import (
    exit_program,
    add_player,
    list_players,
    delete_player,
    update_player,
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "E":
            exit_program()
        elif choice == "L":
            #list_players()
            player_submenu()
            choice = input("> ")
            if choice == "B":
                exit()
            elif choice == "A":
                add_player()
            elif choice == "D":
                delete_player()
            elif choice == "U":
                update_player()
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type E to exit the program")
    print("Type L to see a list of players")

def player_submenu():
    print("Type B to go back")#need help with this
    print("Type A to add a player")
    print("Type D to delete a player")
    print("Type U to update a player")



if __name__ == "__main__":
    main()
