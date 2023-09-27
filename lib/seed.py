from models.__init__ import CONN, CURSOR
from models.players import Player

def seed_database():
    Player.create_table()
    Player.create("Motty", 93)

seed_database()
print("seeded database")