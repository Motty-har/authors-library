from models.__init__ import CURSOR, CONN

class Player():
    def __init__(self, name, number, id=None):
        self.id = id
        self.name = name
        self.number = number

    def __repr__(self):
        return f"<Player {self.id}: {self.name}, {self.number}>"

    
    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Player instances """
        sql = """
            CREATE TABLE IF NOT EXISTS players (
            id INTEGER PRIMARY KEY,
            name TEXT,
            number INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Player instances """
        sql = """
            DROP TABLE IF EXISTS players;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and location values of the current Player instance.
        Update object id attribute using the primary key value of new row.
        """
        sql = """
            INSERT INTO players (name, number)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.number))
        CONN.commit()

        self.id = CURSOR.lastrowid
    
    @classmethod
    def create(cls, name, number):
        """ Initialize a new Player instance and save the object to the database """
        player = cls(name, number)
        player.save()
        return player
