from models.__init__ import CONN, CURSOR
from models.players import Player
from models.stats import Stats
def seed_database():
    Player.create_table()
    Player.create("Motty", 93)
    Player.create("Yossi", 18)
    Stats.create_table()
    Stats.create(2, 3, 1)
    Stats.create(1, 0, 2)

seed_database()
print("seeded database")