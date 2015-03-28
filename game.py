import datetime

class Game(object):
    def __init__(self, team_home, team_away, datetime=datetime.datetime.now()):
        self.team_home = team_home
        self.team_away = team_away
        self.date = datetime
    
    # this is what will be printed when object is printed like "print object"
    def __str__(self):
        return self.team_home + " vs " + self.team_away
    
    def printGame(self):
        return str(self.date) + ": " + self.team_home + " vs " + self.team_away