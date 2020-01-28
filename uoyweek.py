#!/usr/bin/env python3

from datetime import date, timedelta
from calendar import day_name, day_abbr
from argparse import ArgumentParser

def main(short=False, lower=False):
    print(getPeriod(date.today()).toString(date.today(),short=short, lowerC=lower))

class Period:
    def __init__(self, date: date, name: str):
        self.start = date
        self.name = name
    
    def toString(self, today: date):
        if self.start <= today:
            return self.name
        else:
            return None
    def __str__(self):
        return "{} \"{}\" at {}".format(self.__class__.__name__, self.name, self.start)

    def __repr__(self): return self.__str__()

class Term(Period):
    def __init__(self, date: date, name: str):
        date = date - timedelta(days=date.weekday())
        Period.__init__(self, date, name)

    def getWeekNum(self, today: date):
        return (today - self.start).days // 7 + 1

    def toString(self, today: date, short=False, lowerC=False):
        weeknum = self.getWeekNum(today)
        t = self.name[:3] if short else self.name
        d = day_abbr[today.weekday()] if short else day_name[today.weekday()]
        result = "{}/{}/{}".format(t, self.weeknum(today), d)
        return result.lower() if lowerC else result

class Holiday(Period):
    def __init__(self, date: date, name: str):
        Period.__init__(self, date, name)

    def toString(self, today: date, short=False, lowerC=False):
        result = self.name + ("" if short else " Holidays")
        return result.lower() if lowerC else result

# Term dates can be found at https://www.york.ac.uk/about/term-dates/ 
# When updating these, the term begins on the same day listed on the 
# website, and holidays begin on the last day listed.
#
# For example, for Spring Term 2019/2020, the website lists:
#  Spring Term: Monday 6 January 2020 - Friday 13 March 2020
# Which would would tranlate to:
#  Term(    date(2020, 1,  6), "Spring" ),
#  Holiday( date(2020, 3, 13), "Easter" )
#
# The tools/ folder in the git repository contains regex.py which should
# assist you with this.

dates = sorted([
    Term(date(2018,9,24),"Autumn"),
    Holiday(date(2018,11,30),"Christmas"),
    Term(date(2019,1,7),"Spring"),
    Holiday(date(2019,3,15), "Easter"),
    Term(date(2019,4,15),"Summer"),
    Holiday(date(2019,6,21),"Summer"),
    Term(date(2019,9,30),"Autumn"),
    Holiday(date(2019,12,6),"Christmas"),
    Term(date(2020,1,6),"Spring"),
    Holiday(date(2020,3,13),"Easter"),
    Term(date(2020,4,14),"Summer"),
    Holiday(date(2020,6,19),"Summer"),
    Term(date(2020,9,28),"Autumn"),
    Holiday(date(2020,12,4),"Christmas"),
    Term(date(2021,1,11),"Spring"),
    Holiday(date(2021,3,19),"Easter"),
    Term(date(2021,4,19),"Summer"),
    Holiday(date(2021,6,25),"Summer"),
    Term(date(2021,9,27),"Autumn"),
    Holiday(date(2021,12,3),"Christmas"),
    Term(date(2022,1,10),"Spring"),
    Holiday(date(2022,3,18),"Easter"),
    Term(date(2022,4,19),"Summer"),
    Holiday(date(2022,6,24),"Summer"),
    Term(date(2022,9,26),"Autumn"),
    Holiday(date(2022,12,2),"Christmas"),
    Term(date(2023,1,9),"Spring"),
    Holiday(date(2023,3,17),"Easter"),
    Term(date(2023,4,17),"Summer"),
    Holiday(date(2023,6,23),"Summer"),
    Term(date(2023,9,25),"Autumn"),
    Holiday(date(2023,12,1),"Christmas"),
    Term(date(2024,1,8),"Spring"),
    Holiday(date(2024,3,15), "Easter"),
    Term(date(2024,4,15), "Summer"),
    Holiday(date(2024,6,21), "Summer"),
    Term(date(2024,9,23),"Autumn"),
    Holiday(date(2024,11,29),"Christmas"),
    Term(date(2025,1,6),"Spring"),
    Holiday(date(2025,3,14),"Easter"),
    Term(date(2025,4,22),"Summer"),
    Holiday(date(2025,6,27),"Summer"),
    Term(date(2025,9,29),"Autumn"),
    Holiday(date(2025,12,5),"Christmas"),
    Term(date(2026,1,12),"Spring"),
    Holiday(date(2026,3,20),"Easter"),
    Term(date(2026,4,20),"Summer"),
    Holiday(date(2026,6,26),"Summer"),
    Term(date(2026,9,28),"Autumn"),
    Holiday(date(2026,12,4),"Christmas"),
    Term(date(2027,1,11),"Spring"),
    Holiday(date(2027,3,19),"Easter"),
    Term(date(2027,4,19),"Summer"),
    Holiday(date(2027,6,25),"Summer"),
    Term(date(2027,9,27),"Autumn"),
    Holiday(date(2027,12,3),"Christmas"),
    Term(date(2028,1,10),"Spring"),
    Holiday(date(2028,3,17),"Easter"),
    Term(date(2028,4,24),"Summer"),
    Holiday(date(2028,6,30),"Summer")
], key=lambda p:p.start)

def getPeriod(today: date) -> Period:
    """Returns the Period in which a given date falls
    
    Args:
        today (date): which date to search for
    
    Returns:
        Period: Term or Holiday which this date falls in
    """
    return max(filter(lambda p:p.start <= today, dates), key=lambda p:p.start)
    # we can probably optimise this, since `dates` is known to be in chronological order,
    # to return the last date from the start that is before today

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--short", help="Prints a shortened version of the date, abbreviating the term and day.", action="store_true")
    parser.add_argument("-l", "--lower", help="Converts to lowercase.", action="store_true")
    args = parser.parse_args()
    main(**vars(args))