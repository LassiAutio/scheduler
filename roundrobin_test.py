import roundrobin
import unittest
import datetime
import re    # regular expression

# Unit test class for RoundRobin-class
class TestRoundRobin(unittest.TestCase):
    
    def testGetGamesCountOneRound(self):
        self.assertEqual( roundrobin.getGamesCountOneRound(4), 6 )
        self.assertEqual( roundrobin.getGamesCountOneRound(5), 10 )
        self.assertEqual( roundrobin.getGamesCountOneRound(6), 15 )
    
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
    
    def testGetRoundRobin(self):
        teams = roundrobin.generateTeams(4)
        schedule = roundrobin.getRoundRobin(teams)
        self.assertEqual(str(schedule[0]), "A vs D")
        self.assertEqual(str(schedule[1]), "B vs C")
        self.assertEqual(str(schedule[2]), "A vs C")
        self.assertEqual(str(schedule[3]), "D vs B")
        self.assertEqual(str(schedule[4]), "A vs B")
        self.assertEqual(str(schedule[5]), "C vs D")
        
        schedule_switched = roundrobin.getRoundRobin(teams, True)
        self.assertEqual(str(schedule_switched[0]), "D vs A")
        self.assertEqual(str(schedule_switched[1]), "C vs B")
        self.assertEqual(str(schedule_switched[2]), "C vs A")
        self.assertEqual(str(schedule_switched[3]), "B vs D")
        self.assertEqual(str(schedule_switched[4]), "B vs A")
        self.assertEqual(str(schedule_switched[5]), "D vs C")

if __name__ == '__main__':
    unittest.main()
