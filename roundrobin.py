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
        if len(self.teams)%2 != 0:
            self.teams.append(None)
        self.date_start = date_start
        self.date_end = date_end
        self.date_current = None
        self.rounds_count = rounds_count
        self.reverse_home_away = False
        self.schedule = []
    
    def getGamesCountOneRound(self):
        return getGamesCountOneRound(len(self.teams))
    
    def getGamesCount(self):
        return getGamesCount(len(self.teams), self.rounds_count)
    
    def getDaysInSeason(self):
        return (self.date_end - self.date_start).days + 1
    
    def getAvgDaysBetweenGames(self):
        return getAvgDaysBetweenGames(self.getGamesCount(), self.getDaysInSeason())
    
    def generateSchedule(self):
        self.schedule = []
        for i in range(self.rounds_count):
            self.schedule.extend( self.getNextRoundRobin() )
    
    
    def getSchedule(self):
        if self.schedule == []:
            self.generateSchedule()
        return self.schedule
    
    def getNextRoundRobin(self):
        half = len(self.teams) / 2
        schedule = []
        for turn in range(len(self.teams)-1):
            for i in range(half):
                home = self.teams[i]
                away = self.teams[len(self.teams)-i-1]
                if self.reverse_home_away == True:
                    temp = home
                    home = away
                    away = temp
                if (home != None) and (away != None):
                    game = Game(home, away, self.getNextDate() )
                    schedule.append( game )
            last_team = self.teams.pop()
            self.teams.insert(1, last_team)
        self.reverse_home_away = not self.reverse_home_away
        return schedule
    
    def getNextDate(self):
        if self.date_current == None:
            self.date_current = self.date_start
        else:
            self.date_current += datetime.timedelta(days = self.getAvgDaysBetweenGames()+1 )
        return self.date_current
    
def generateTeams(teams_count):
    assert(teams_count>=3)
    return list(string.ascii_uppercase)[:teams_count]

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

def getRoundRobin(teams, reverse_home_away=False):
    if len(teams)%2 != 0 :
        teams.append(None)
    half = len(teams) / 2
    schedule = []
    for turn in range(len(teams)-1):
        for i in range(half):
            home = teams[i]
            away = teams[len(teams)-i-1]
            if reverse_home_away == True:
                temp = home
                home = away
                away = temp
            if (home != None) and (away != None):
                game = Game(home, away)
                schedule.append( game )
        last_team = teams.pop()
        teams.insert(1, last_team)
    return schedule

if __name__ == '__main__':
    printRoundRobin(6)