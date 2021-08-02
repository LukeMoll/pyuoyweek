"""
    csbot.py

    generates the command for [csbot](https://github.com/HackSoc/csbot/)'s
    `!termdates` plugin to set the three upcoming terms.

    Usage: `python3 tools/csbot.py`
"""

# messy import code to allow us to import from parent
import os.path as path, sys
dirname = path.dirname(path.realpath(__file__))
sys.path.append(dirname + ('/' if not dirname.endswith('/') else '') + '../')
import uoyweek

from datetime import date
today = date.today()

def lstart(p): return p.start # replaces a load of `lambda p:p.start` in sorts - might be useful in uoyweek.py

def getAcademicTerms():    
    # Get the nearest {aut,spr,smm} term that hasn't started yet
    atm = min(filter(lambda p:type(p) is uoyweek.Term and p.name is "Autumn" and today < p.start, uoyweek.dates), key=lstart)
    spr = min(filter(lambda p:type(p) is uoyweek.Term and p.name is "Spring" and today < p.start, uoyweek.dates), key=lstart)
    smm = min(filter(lambda p:type(p) is uoyweek.Term and p.name is "Summer" and today < p.start, uoyweek.dates), key=lstart)

    period = uoyweek.getPeriod(today)
    if type(period) is uoyweek.Term:
        # We're in a term time, so one of (atm,spr,smm) should be overridden
        if period.name is "Autumn":
            atm = period
        elif period.name is "Spring":
            spr = period
        elif period.name is "Summer":
            smm = period
        else:
            raise RuntimeError("Unexpected term name '%s' for current period".format(period.name))

    # at most one of these should be current
    # the rest should be upcoming
    return (atm,spr,smm)

(atm,spr,smm) = getAcademicTerms()    
print("!termdates.set {} {} {}".format(
    atm.start.isoformat(),
    spr.start.isoformat(),
    smm.start.isoformat()
))