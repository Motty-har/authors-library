# lib/helpers.py
from models.players import Player

def add_player():
    name = input("Please enter the players name: ")
    number = input("Please enter the players number: ")
    player = Player.create(name, number)
    print(f'Success: {player}')

def list_players():
    pass

def delete_player():
    pass 

def update_player():
    pass

def update_stats():
    pass

def view_goals():
    pass

def view_assists():
    pass

def view_points():
    pass

def exit_program():
    print("Goodbye!")
    exit()
