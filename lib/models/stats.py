from models.__init__ import CURSOR, CONN
from models.players import Player

class Stats:
    all = {}

    def __init__(self, goals, assists, player_id, id=None):
        self.id = id
        self.goals = goals
        self.assists = assists
        self.player_id = player_id
    
    def find_player_by_id(id):
        player = Player.find_by_id(id)
        return player
    
    def __repr__(self):
        return (
            f"< Goals: {self.goals}, Assists: {self.assists}, Player Id: {self.player_id}>"
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
    
    @classmethod
    def instance_from_db(cls, row):
        """Return an Employee object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        stats = cls.all.get(row[0])
        if stats:
            # ensure attributes match row values in case local instance was modified
            stats.goals = row[1]
            stats.assists = row[2]
            stats.player_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            stats = cls(row[1], row[2], row[3])
            stats.id = row[0]
            cls.all[stats.id] = stats
        return stats
    
    @classmethod
    def get_all(cls):
        """Return a list containing one Stat object per table row"""
        sql = """
            SELECT *
            FROM stats
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]