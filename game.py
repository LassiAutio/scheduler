class Game(object):
    def __init__(self, team_home, team_away):
        self.team_home = team_home
        self.team_away = team_away
    
    # this is what will be printed when object is printed like "print object"
    def __str__(self):
        return self.team_home + " vs " + self.team_away
