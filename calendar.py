import datetime

def IsSpecialDay(date):
    if IsMothersDay(date):
        return True
    elif IsGraduateDay(date):
        return True
    elif IsAscensionThursday(date):
        return True
    elif IsMidSummer(date):
        return True
    else:
        return False

# Returns (Finnish) Mothers' day
def GetMothersDay(year):
    assert(year>=1980 and year < 2100)
    for day in range(8, 14+1):
        date = datetime.date(year, 5, day)
        if date.weekday() == 6:
            break
    return date

def IsMothersDay(date):
    return date == GetMothersDay(date.year)

    # Returns Finnish schools' graduate day (kevatjuhla)
def GetGraduateDay(year):
    assert(year>=2015 and year < 2100)
    if year == 2015:
        return datetime.date(2015, 5, 30)
    elif year == 2016:
        return datetime.date(2016, 6, 4)
    elif year == 2017:
        return datetime.date(2017, 6, 3)
    else:
        raise ValueError("Graduate day isn't yet specified for year " + str(year) )

def IsGraduateDay(date):
    return date == GetGraduateDay(date.year)

"Returns Easter as a date object."
"Copied from http://code.activestate.com/recipes/576517-calculate-easter-western-given-a-year/ "
"MIT license"
def GetEasterSunday(year):
    a = year % 19
    b = year // 100
    c = year % 100
    d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
    e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
    f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
    month = f // 31
    day = f % 31 + 1    
    return datetime.date(year, month, day)

def GetAscensionThursday(year):
    return GetEasterSunday(year) + datetime.timedelta(days = 39)

def IsAscensionThursday(date):
    return date == GetAscensionThursday(date.year)

# Returns Finnish mid summer "juhannus"
def GetMidsummer(year):
    assert(year>=1980 and year < 2100)
    for day in range(20, 26+1):
        date = datetime.date(year, 6, day)
        if date.weekday() == 5:
            break
    return date

def IsMidSummer(date):
    return date == GetMidsummer(date.year)