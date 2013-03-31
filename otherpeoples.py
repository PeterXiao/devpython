#-*- coding: utf-8 -*-
"""
    name: gcal.py
  author: apache
function: print calendar for (year, month)
 version: 1.0
   uasge: python gcal.py [year] [month]
"""
import sys, time
MIN_YEAR = 0
MAX_YEAR = 100000
MIN_MONTH = 1
MAX_MONTH = 12
mdict = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6,
         "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
# get year and month
def getYearMonth():
    """
    Get year and month from time moudle or user's input.
    Return year, month
    """
    argc = len(sys.argv)
    if len(sys.argv) == 1:
        temp = time.ctime().split()
        return int(temp[4]), mdict[temp[1]]
    else:
        if not sys.argv[1].isdigit():
            return -1, 0
        else:
            year = int(sys.argv[1])
            if argc == 3:
                if not sys.argv[2].isdigit():
                    return -2, 0
                else:
                    return year, int(sys.argv[2])
            else:
                return year, 1

# is the year and month illegal? illegal return True and print information else return True
def isIllegal(year, month):
    """
    Check the value of year and month.
    If it's illegal return true and print illegal information else return false.
    """
    info = {-1 : "The year should be an enterger!", -2 : "The month should be an enterger"}
    if year == -1 or year == -2:
        print (info[year])
        return True
    else:
        if year < MIN_YEAR or year > MAX_YEAR:
            print( "The year should between %d..%d" % (MIN_YEAR, MAX_YEAR))
            return True
        if month < MIN_MONTH or month > MAX_MONTH:
            print ("The month should between %s..%d" % (MIN_MONTH, MAX_MONTH))
            return True
    return False

# get the days of year, month
def getDays(year, month):
    """Return the days of year, month"""
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
            return 29
        else:
            return 28
# get the week of year, month, 1
def getWeek(year, month, day):
    """Return a number of week. 0 as Sunday."""
    t = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if month < 3:
        year = year - 1
    return (year + year / 4 - year / 100 + year / 400 + t[month - 1] + day) % 7

# print calendar
def printCalendar(year, month, days, week):
    """Print the calendar."""
    print ("      %d  %s" % (year, str(month).zfill(2)))
    print( "Su Mo Tu We Th Fr Sa")
    for i in range(int(week)):
        sys.stdout.write("   ")
    count = week
    temp = time.ctime().split()
    cruyear = int(temp[4])
    crumonth = int(mdict[temp[1]])
    cruday = int(temp[2])
    for i in range(1, days + 1):
        if cruyear == year and crumonth == month:
            if i + 1 == cruday:
                sys.stdout.write(str(i).zfill(2).ljust(2))
            elif i == cruday:
                sys.stdout.write(("(" + str(i).zfill(2) + ")").ljust(3))
            else:
                sys.stdout.write(str(i).zfill(2).ljust(3))
        else:
            sys.stdout.write(str(i).zfill(2).ljust(3))
        count = count + 1
        if count % 7 == 0:
            print
    print

# Wrap all functions
def main():
    """Wrap all functions."""
    year, month = getYearMonth()
    if isIllegal(year, month):
        sys.exit(1)
    days = getDays(year, month)
    week = getWeek(year, month, 1)
    printCalendar(year, month, days, week)

if __name__ == "__main__":
     main()
