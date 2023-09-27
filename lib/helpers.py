# lib/helpers.py
from models.players import Player

def add_player():
    name = input("Please enter the players name: ")
    number = input("Please enter the players number: ")
    player = Player.create(name, number)
    print(f'Success: {player}')

def list_players():
    pass


def exit_program():
    print("Goodbye!")
    exit()
