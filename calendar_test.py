import calendar
import unittest
import datetime

# Unit test class for calendar.py's functions
class TestCalendar(unittest.TestCase):
    
    def testGetMothersDay(self):
        self.assertEqual( calendar.GetMothersDay(2016), datetime.date(2016, 5, 8) )
        self.assertEqual( calendar.GetMothersDay(2015), datetime.date(2015, 5, 10) )
        self.assertEqual( calendar.GetMothersDay(2014), datetime.date(2014, 5, 11) )
    
    def testIsMothersDay(self):
        self.assertTrue( calendar.IsMothersDay(datetime.date(2015, 5, 10)) )
        self.assertTrue( calendar.IsMothersDay(datetime.date(2016, 5, 8)) )
        self.assertFalse( calendar.IsMothersDay(datetime.date(2015, 5, 11)) )
        self.assertFalse( calendar.IsMothersDay(datetime.date(2015, 5, 7)) )
    
    def testGetGraduateDay(self):
        self.assertEqual( calendar.GetGraduateDay(2016), datetime.date(2016, 6, 4) )
        self.assertEqual( calendar.GetGraduateDay(2015), datetime.date(2015, 5, 30) )
        with self.assertRaises( AssertionError ):
            calendar.GetGraduateDay(1800)
        with self.assertRaises( ValueError ):
            calendar.GetGraduateDay(2020)
    
    def testIsGraduateDay(self):
        self.assertTrue( calendar.IsGraduateDay(datetime.date(2015, 5, 30)) )
        self.assertTrue( calendar.IsGraduateDay(datetime.date(2016, 6, 4)) )
        self.assertFalse( calendar.IsGraduateDay(datetime.date(2015, 5, 29)) )
        self.assertFalse( calendar.IsGraduateDay(datetime.date(2016, 6, 5)) )
    
    def testIsSpecialDay(self):
        self.assertTrue( calendar.IsSpecialDay(datetime.date(2015, 5, 30)) )
    
    def testGetEasterSunday(self):
        self.assertEqual( calendar.GetEasterSunday(2015), datetime.date(2015, 4, 5) )
        self.assertEqual( calendar.GetEasterSunday(2016), datetime.date(2016, 3, 27) )
    
    def testGetAscensionThursday(self):
        self.assertEqual( calendar.GetAscensionThursday(2015), datetime.date(2015, 5, 14) )
        self.assertEqual( calendar.GetAscensionThursday(2016), datetime.date(2016, 5, 5) )
    
    def testGetMidsummer(self):
        self.assertEqual( calendar.GetMidsummer(2015), datetime.date(2015, 6, 20) )
        self.assertEqual( calendar.GetMidsummer(2016), datetime.date(2016, 6, 25) )

if __name__ == '__main__':
    unittest.main()
