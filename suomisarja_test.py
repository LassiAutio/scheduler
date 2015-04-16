import unittest
import suomisarja
import string

class TestSuomiSarja(unittest.TestCase):
    
    def setUp(self):
        teams = generateTeams(6)
        teams_div_a = teams[0:3]
        teams_div_b = teams[3:]
        self.suomi_sarja = suomisarja.SuomiSarja(teams_div_a, teams_div_b, rounds_count_division=3, rounds_count_inter=2)
        print "foo"
    
    def testGamesCount(self):
        self.assertEqual( self.suomi_sarja.getGamesCount(), 36 )

def generateTeams(teams_count):
    assert(teams_count>=3)
    return list(string.ascii_uppercase)[:teams_count]
        
if __name__ == '__main__':
    unittest.main()