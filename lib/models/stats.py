from models.__init__ import CURSOR, CONN
from models.players import Player

class Stats:
    all = {}

    def __init__(self, goals, assists, player_id, id=None):
        self.id = id
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
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
            stats INTEGER,
            points INTEGER,
            player_id INTEGER,
            FOREIGN KEY (player_id) REFERENCES players(id))
        """
        CURSOR.execute(sql)
        CONN.commit()