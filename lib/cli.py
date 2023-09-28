# lib/cli.py

from helpers import (
    exit_program,
    add_player,
    list_players,
    delete_player,
    update_player,
    player_stats,
    update_stats,
    view_goals,
    view_assists,
    view_points
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice is "E":#how to do upercase and lowercase
            exit_program()
        elif choice == "L":
            list_players()
            player_submenu()
            choice = input("> ")
            if choice == "B":##need help with this
                exit()
            elif choice == "A":
                add_player()
            elif choice == "D":
                delete_player() 
            elif choice == "U":
                update_player()
            elif choice == "S":
                player_stats()
            else:
                print("Invalid choice")
        elif choice == "S":
            stats_submenu()
            choice = input("> ")
            if choice == "B":
                exit()
            elif choice == "U":
                update_stats()
            elif choice == "V":
                view_stats()
                choice = input("> ")
                if choice == "A":
                    view_goals()
                elif choice == "D":
                    view_assists()
                elif choice == "U":
                    view_points()
                else:
                    print("Invalid choice")
            else:
                print("Invalid choice")
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("Type E to exit the program")
    print("Type L to see a list of players")
    print("Type S to handle stats")

def player_submenu():
    print("Type B to go back")#need help with this
    print("Type A to add a player")
    print("Type D to delete a player")
    print("Type U to update a player")
    print("Type S to view a specific players stats")

def stats_submenu():
    print("Type B to go back")
    print("Type U to update a players stats")
    print("Type V to view stats")

def view_stats():
    print("Type G to view goals")
    print("Type A to view assists")
    print("Type P to view points")



if __name__ == "__main__":
    main()
