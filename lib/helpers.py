# lib/helpers.py
from models.players import Player
from models.stats import Stats

def add_player():
    name = input("Please enter the players name: ")
    number = input("Please enter the players number: ")
    goals = input("Enter the goals: ")
    assists = input("Enter the assists: ")
    player = Player.create(name, number)
    stats = Stats.create(goals, assists, player.id)
    print(f'Success: {player}, {stats}')


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
    Stats.find_player_by_id(1)
    stats = Stats.get_all()
    for stat in stats:
        print(stat)

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
