import calendar, datetime

def getAllWeeks(season):
    # Find the date of Labor Day as it corresponds to the start of the NFL season
    cal = calendar.Calendar(0).monthdatescalendar(int(season), 9)
    if cal[0][0].month == 9:
        laborDay = cal[0][0]
    else:
        laborDay = cal[1][0]

    # NFL weeks start on Tuesday and end on Monday
    nflCal = calendar.Calendar(1)
    weeksCalWithDups = []

    # Create list of weeks from September through February
    i = 1
    m = 9
    while i <= 4:
        for w in nflCal.monthdatescalendar(int(season), m):
            weeksCalWithDups.append(w)
        i += 1
        m += 1

    m = 1
    while i <= 6:
        for w in nflCal.monthdatescalendar(int(season)+1, m):
            weeksCalWithDups.append(w)
        i += 1
        m += 1

    # Remove duplicates weeks from when a week spans across months
    weeksCal = []
    for w in weeksCalWithDups:
        if w not in weeksCal:
            weeksCal.append(w)

    # First week of list is Tue-Mon week including Labor Day, season starts the week after this week (week0)
    index = 1
    for week in weeksCal:
        if laborDay in week:
            break
        else:
            index += 1

    # This data set is currently only correct for 2021 season with addition of 17th game
    allWeeks = {
        'week1':weeksCal[index],
        'week2':weeksCal[index+1],
        'week3':weeksCal[index+2],
        'week4':weeksCal[index+3],
        'week5':weeksCal[index+4],
        'week6':weeksCal[index+5],
        'week7':weeksCal[index+6],
        'week8':weeksCal[index+7],
        'week9':weeksCal[index+8],
        'week10':weeksCal[index+9],
        'week11':weeksCal[index+10],
        'week12':weeksCal[index+11],
        'week13':weeksCal[index+12],
        'week14':weeksCal[index+13],
        'week15':weeksCal[index+14],
        'week16':weeksCal[index+15],
        'week17':weeksCal[index+16],
        'week18':weeksCal[index+17],
        'wildcard':weeksCal[index+18],
        'divisional':weeksCal[index+19],
        'conference':weeksCal[index+20],
        'championship':weeksCal[index+22]
    }

    return allWeeks

def getThisSeason():
    today = datetime.datetime.now()
    season = today.year if today.month in range(3,12) else today.year - 1
    return season     

def getThisWeek(allWeeks):
    today = datetime.datetime.now().date()
    for k,v in allWeeks.items():
        if today in v:
            return k
    print('There are no NFL games this week. Defaulting to week1.')
    return 'week1'

def getPrevWeek(allWeeks, selectedWeek):
    backsev = allWeeks[selectedWeek][0] - datetime.timedelta(7)
    for k,v in allWeeks.items():
        if backsev in v:
            return k
    