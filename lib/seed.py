from models.__init__ import CONN, CURSOR
from models.players import Player

def seed_database():
    Player.create_table()

seed_database()
print("seeded database")