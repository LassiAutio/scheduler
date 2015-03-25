import roundrobin
import unittest
import datetime
import re    # regular expression

# Unit test class for RoundRobin-class
class TestRoundRobin(unittest.TestCase):
    def testRotate(self):
        robin = roundrobin.RoundRobin(6)
        self.assertEqual( robin.teams, ["A", "B", "C", "D", "E", "F"] )
        robin.rotate()
        self.assertEqual( robin.teams, ["A", "F", "B", "C", "D", "E"] )
        robin.rotate()
        self.assertEqual( robin.teams, ["A", "E", "F", "B", "C", "D"] )
    
    def testGetRound(self):
        robin = roundrobin.RoundRobin(6)
        games = robin.getGameRound()
        for game in games:
            self.assertIsNotNone(re.match(r'^\d{4}-\d{2}-\d{2}: \w+ vs \w+$', str(game)))
    
    def testGetSchedule(self):
        teams_count = 4
        rounds_count = 2 * (teams_count-1)
        robin = roundrobin.RoundRobin(teams_count, rounds_count)
        schedule = robin.getSchedule()
        self.assertEqual( len(schedule), rounds_count)
        
        # test every team has same number home/away games for even rounds
        home = {}
        away = {}
        for day in schedule:
            self.assertEqual( len(day), teams_count/2)
            for game in day:
                home[game.team_home] = home.get(game.team_home, 0) + 1
                away[game.team_away] = away.get(game.team_away, 0) + 1
        self.assertEqual( home.values(), [rounds_count/2]*teams_count )
        self.assertEqual( away.values(), [rounds_count/2]*teams_count )
    
    def testGetGameCountOneRound(self):
        self.assertEqual( roundrobin.getGameCountOneRound(4), 6 )
        self.assertEqual( roundrobin.getGameCountOneRound(6), 15 )
    
    def testGetGamesCount(self):
        self.assertEqual( roundrobin.getGamesCount(4, 2), 12 )
        self.assertEqual( roundrobin.getGamesCount(6, 3), 45 )
    
    def testGetDaysInSeason(self):
        robin = roundrobin.RoundRobin(6, 2, datetime.date(2015, 5, 1), datetime.date(2015, 5, 2))
        self.assertEqual( robin.getDaysInSeason(), 2)
        robin = roundrobin.RoundRobin(6, 2, datetime.date(2015, 5, 1), datetime.date(2015, 6, 1))
        self.assertEqual( robin.getDaysInSeason(), 32)
    
    def testGetAvgDaysBetweenGames(self):
        games = 5
        days = 5
        self.assertEqual( roundrobin.getAvgDaysBetweenGames(games, days), 1 )
        days = 13
        games = 7
        self.assertEqual( roundrobin.getAvgDaysBetweenGames(games, days), 2 )
        games = 5
        self.assertEqual( roundrobin.getAvgDaysBetweenGames(games, days), 3 )
        days = 14
        self.assertEqual( roundrobin.getAvgDaysBetweenGames(games, days), 3 )

if __name__ == '__main__':
    unittest.main()
