# lib/helpers.py
from models.players import Player

def add_player():
    name = input("Please enter the players name: ")
    number = input("Please enter the players number: ")
    player = Player.create(name, number)
    print(f'Success: {player}')

def list_players():
    players = Player.get_all()
    for player in players:
        print(player)

def delete_player():
    id_ = input("Enter the players id: ")
    if player := Player.find_by_id(id_):
        player.delete()
        print(f'Player {id_} succesfully deleted')
    else:
        print(f'Player {id_} not found')

def update_player():
    id_ = input("Enter the players id: ")
    if player := Player.find_by_id(id_):
        try:
            name = input("Enter the players updated name: ")
            player.name = name
            number = input("Enter the players updated number: ")
            player.number = number

            player.update()
            print(f'Success: {player}')
        except Exception as exc:#what is the functinality of this
            print("Error updating player: ", exc)
    else:
        print(f'Player ({id_} not found)')

def player_stats():
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
