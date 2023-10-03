from models.__init__ import CURSOR, CONN

class Player():

    all = {}

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
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Player object having the attribute values from the table row."""
        player = cls.all.get(row[0])
        if player:
            player.name = row[1]
            player.number = row[2]
        else:
            player = cls(row[1], row[2])
            player.id = row[0]
            cls.all[player.id] = player
        return player

    @classmethod
    def get_all(cls):
        """Return a list containing a Player object per row in the table"""
        sql = """
            SELECT *
            FROM players
        """

        rows = CURSOR.execute(sql).fetchall()
        all_rows = [cls.instance_from_db(row) for row in rows] 
        return all_rows

    @classmethod
    def find_by_id(cls, id):
        """Return a Player object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM players
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def delete(self):
        """Delete the table row corresponding to the current Player instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM players
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]

        self.id = None

    def update(self):
        """Update the table row corresponding to the current Player instance."""
        sql = """
            UPDATE players
            SET name = ?, number = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.number, self.id))
        CONN.commit()


    



    
    
