import string
import datetime
import math
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
        self.current_game_round = 0
        self.current_day = date_start
        self.current_game = -1
    
    def getGamesCountOneRound(self):
        return getGamesCountOneRound(len(self.teams))
    
    def getDaysInSeason(self):
        return (self.date_end - self.date_start).days + 1
    
    def getAvgDaysBetweenGames(self):
        return getAvgDaysBetweenGames(self.getGamesCount(), self.getDaysInSeason())
    
    def getGamesCount(self):
        return getGamesCount(len(self.teams), self.rounds_count)
    
def generateTeams(teams_count):
    teams = list(string.ascii_uppercase)[:teams_count]
    if teams_count%2 != 0:
        teams.append(None)
    return teams

def getGamesCountOneRound(teams_count):
    assert(teams_count>=3)
    return int( (float(teams_count)/2) * (teams_count-1) )

def getGamesCount(teams_count, rounds_count):
    assert(rounds_count>=1)
    return getGamesCountOneRound(teams_count) * rounds_count

# Returns how many days there would be between each games if they are separated evenly.
def getAvgDaysBetweenGames(games_count, days_count):
    x = days_count - games_count
    divider = games_count-1
    return math.floor( (float(x) / divider)+1 )

def getRoundRobin(teams_count):
    teams = generateTeams(teams_count)
    half = len(teams) / 2
    schedule = []
    for turn in range(len(teams)-1):
        for i in range(half):
            home = teams[i]
            away = teams[len(teams)-i-1]
            if (home != None) and (away != None):
                schedule.append( str(home) + " vs " + str(away) )
        last_team = teams.pop()
        teams.insert(1, last_team)
    return schedule

if __name__ == '__main__':
    printRoundRobin(6)