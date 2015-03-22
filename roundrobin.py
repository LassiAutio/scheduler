import string
import datetime
from game import Game

'''
Generates Round-robin schedule for given number of teams and round.
'''
class RoundRobin(object):
    
    def __init__(self, teams_count, rounds_count=2, date_start = datetime.date(2015, 5, 4), date_end = datetime.date(2015, 9, 13)):
        assert(teams_count>=3)
        assert(rounds_count>=1)
        self.teams = generateTeams(teams_count)
        self.rounds_count = rounds_count
        self.date_start = date_start
        self.date_end = date_end
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
    
    '''
    Returns array of schedule where
    schedule[0] = list of first round games = [Game-obj, Game-obj, ...]
    schedule[1] = list of second round games
    '''
    def getSchedule(self):
        schedule = []
        for i in range(self.rounds_count):
            games = self.getRound()
            schedule.append(games)
            self.rotate()
        return schedule
    
    def printSchedule(self):
        schedule = self.getSchedule()
        for day in range(len(schedule)):
            print "== Day #" + str(day+1)
            games = schedule[day]
            for game in games:
                print game
            self.rotate()
    
    def getDaysInSeason(self):
        return (self.date_end - self.date_start).days + 1
    
    def getAvgDaysBetweenGames(self):
        days = self.getDaysInSeason()
        games = self.getGameCount()
        return float(games) / (days-1)
    
    def getGameCount(self):
        return getGameCount(len(self.teams), self.rounds_count)
    
def generateTeams(teams_count):
    teams = list(string.ascii_uppercase)[:teams_count]
    if teams_count%2 != 0:
        teams.append(" ")
    return teams

def getGameCountOneRound(teams_count):
    assert(teams_count>=3)
    return (teams_count/2) * (teams_count-1)

def getGameCount(teams_count, rounds_count):
    assert(rounds_count>=1)
    return getGameCountOneRound(teams_count) * rounds_count

def getAvgDaysBetweenGames(games_count, days_count):
    return float(days_count) / (games_count-1)