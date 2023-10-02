from models.__init__ import CURSOR, CONN
from models.players import Player

class Stats:
    all = {}

    def __init__(self, goals, assists, points, player_id, id=None):
        self.id = id
        self.goals = goals
        self.assists = assists
        self.points = goals + assists
        self.player_id = player_id

    def __repr__(self):
        return (
            f"<Employee {self.id}: {self.name}, {self.job_title}, " +
            f"Department ID: {self.department_id}>"
        )