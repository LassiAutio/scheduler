import string
from game import Game

class RoundRobin(object):
    
    def __init__(self, teams_count):
        self.teams = generateTeams(teams_count)
        self.current_round = 0
    
    def getRound(self):
        games = []
        teams_count = len(self.teams)
        home_away_index = self.current_round // (teams_count-1)
        for i in range(0, teams_count, 2):
            if home_away_index%2 == 0:
                game = Game( self.teams[i], self.teams[i+1] )
            else:
                game = Game( self.teams[i+1], self.teams[i] )
            games.append( game )
        return games
    
    def getNextRound(self):
        self.rotate()
        return self.getRound()
    
    def rotate(self):
        head = self.teams[0]
        tail = self.teams[1: len(self.teams)-1]
        second = self.teams[len(self.teams)-1]
        self.teams = []
        self.teams.append(head)
        self.teams.append(second)
        self.teams = self.teams + tail
        self.current_round += 1
    
    def getSchedule(self, rounds_count):
        schedule = []
        for i in range(rounds_count):
            games = self.getRound()
            schedule.append(games)
            self.rotate()
        return schedule
    
    def printSchedule(self, rounds_count):
        schedule = self.getSchedule(rounds_count)
        for day in range(len(schedule)):
            print "== Day #" + str(day+1)
            games = schedule[day]
            for game in games:
                print game
            self.rotate()
    
def generateTeams(teams_count):
    teams = list(string.ascii_uppercase)[:teams_count]
    if teams_count%2 != 0:
        teams.append(" ")
    return teams
