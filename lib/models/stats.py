from models.__init__ import CURSOR, CONN
from models.players import Player

class Stats:
    all = {}

    def __init__(self, goals, assists, player_id, id=None):
        self.id = id
        self.goals = goals
        self.assists = assists
        self.player_id = player_id

    def __repr__(self):
        return (
            f"<Stats {self.id}, {self.goals}: {self.assists}, {self.points}, " +
            f"Player ID: {self.player_id}>"
        )
    
    @property
    def goals(self):
        return self._goals

    @goals.setter
    def goals(self, goals):
        if isinstance(goals, int):
            self._goals = goals
        else:
            raise ValueError(
                "Goals must be a number"
            )

    @property
    def assists(self):
        return self._assists

    @assists.setter
    def assists(self, assists):
        if isinstance(assists, int):
            self._assists = assists
        else:
            raise ValueError(
                "Assist must be a number"
            )
    
    @property
    def player_id(self):
        return self._player_id

    @player_id.setter
    def player_id(self, player_id):
        if type(player_id) is int and Player.find_by_id(player_id):
            self._player_id = player_id
        else:
            raise ValueError(
                "Player id must reference a player in the database")
        
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Stats instances """
        sql = """
            CREATE TABLE IF NOT EXISTS stats (
            id INTEGER PRIMARY KEY,
            goals INTEGER,
            assists INTEGER,
            player_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES players(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the goals, assists, points, and players id values of the current Stats object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO stats (goals, assists, player_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.goals, self.assists, self.player_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, goals, assists, player_id):
        """ Initialize a new Stats instance and save the object to the database """
        stats = cls(goals, assists, player_id)
        stats.save()
        return stats  