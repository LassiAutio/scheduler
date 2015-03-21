import roundrobin
import unittest

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
        games = robin.getRound()
        self.assertEqual( str(games[0]), "A vs B")
        self.assertEqual( str(games[1]), "C vs D")
        self.assertEqual( str(games[2]), "E vs F")
    
    def testGetSchedule(self):
        teams_count = 4
        rounds_count = 2 * (teams_count-1)
        robin = roundrobin.RoundRobin(teams_count)
        schedule = robin.getSchedule(rounds_count)
        self.assertEqual( len(schedule), rounds_count)
        home = {}
        away = {}
        for day in schedule:
            self.assertEqual( len(day), teams_count/2)
            for game in day:
                home[game.team_home] = home.get(game.team_home, 0) + 1
                away[game.team_away] = away.get(game.team_away, 0) + 1
        self.assertEqual( home.values(), [rounds_count/2]*teams_count )
        self.assertEqual( away.values(), [rounds_count/2]*teams_count )
        

if __name__ == '__main__':
    unittest.main()
