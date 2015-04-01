import calendar
import unittest
import datetime

# Unit test class for calendar.py's functions
class TestCalendar(unittest.TestCase):
    
    def testIsSpecialDay(self):
        self.assertTrue( calendar.IsSpecialDay(datetime.date(2015, 5, 30)) )
    
    def testGetSpecialDaysCount(self):
        self.assertEqual( calendar.GetSpecialDaysCount( datetime.date(2015, 5, 1), datetime.date(2015, 5, 31) ), 4)
        self.assertEqual( calendar.GetSpecialDaysCount( datetime.date(2015, 6, 1), datetime.date(2015, 6, 30) ), 6)
        self.assertEqual( calendar.GetSpecialDaysCount( datetime.date(2016, 6, 1), datetime.date(2016, 7, 31) ), 7)
        with self.assertRaises( AssertionError ):
            calendar.GetSpecialDaysCount( datetime.date(2016, 6, 1), datetime.date(2016, 6, 1) )
        with self.assertRaises( AssertionError ):
            calendar.GetSpecialDaysCount( datetime.date(2016, 6, 1), datetime.date(2015, 7, 1) )
    
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
    
    def testGetEasterSunday(self):
        self.assertEqual( calendar.GetEasterSunday(2015), datetime.date(2015, 4, 5) )
        self.assertEqual( calendar.GetEasterSunday(2016), datetime.date(2016, 3, 27) )
    
    def testGetAscensionThursday(self):
        self.assertEqual( calendar.GetAscensionThursday(2015), datetime.date(2015, 5, 14) )
        self.assertEqual( calendar.GetAscensionThursday(2016), datetime.date(2016, 5, 5) )
    
    def testIsMayDayOrEve(self):
        self.assertTrue( calendar.IsMayDayOrEve(datetime.date(2015, 5, 1)) )
        self.assertTrue( calendar.IsMayDayOrEve(datetime.date(2020, 5, 1)) )
        self.assertTrue( calendar.IsMayDayOrEve(datetime.date(2010, 4, 30)) )
        self.assertFalse( calendar.IsMayDayOrEve(datetime.date(2015, 5, 2)) )
        self.assertFalse( calendar.IsMayDayOrEve(datetime.date(2018, 6, 1)) )
    
    def testGetMidsummer(self):
        self.assertEqual( calendar.GetMidsummer(2015), datetime.date(2015, 6, 20) )
        self.assertEqual( calendar.GetMidsummer(2016), datetime.date(2016, 6, 25) )
    
    def testIsInMidsummerDays(self):
        self.assertFalse( calendar.IsInMidsummerDays( datetime.date(2015, 6, 16) ) )
        self.assertTrue( calendar.IsInMidsummerDays( datetime.date(2015, 6, 17) ) )
        self.assertTrue( calendar.IsInMidsummerDays( datetime.date(2015, 6, 22) ) )
        self.assertFalse( calendar.IsInMidsummerDays( datetime.date(2015, 6, 23) ) )
        self.assertTrue( calendar.IsInMidsummerDays( calendar.GetMidsummer(2020) ) )

if __name__ == '__main__':
    unittest.main()
