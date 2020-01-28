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
    atm = max(filter(lambda p:type(p) is uoyweek.Term and p.name is "Autumn" and today >= p.start, uoyweek.dates), key=lstart)
    spr = min(filter(lambda p:p.name is "Spring" and p.start > atm.start, uoyweek.dates), key=lstart)
    smm = min(filter(lambda p:p.name is "Summer" and p.start > atm.start, uoyweek.dates), key=lstart)
    return (atm,spr,smm)

(atm,spr,smm) = getAcademicTerms()    
print("!termdates.set {} {} {}".format(
    atm.start.isoformat(),
    spr.start.isoformat(),
    smm.start.isoformat()
))