pyuoyweek
===
pyuoyweek is a (much nicer) Python reimplementation of one of my previous projects, [uoyweek]. It gives the current date string as formatted by the [University of York][uoy]. For example, `spr/2/thu` would refer to Thursday on the 2nd week of Spring term.

## Installation
pyuoyweek uses Python 3 -- it is not compatible with Python 2.  
If you just want to use pyuoyweek, you can simply download [uoyweek.py][main] - it's all self-contained. If you'd like, you can copy `uoyweek.py` to a folder on your `$PATH` and rename it to `uoyweek`, basically turning it into a command that you'd call with `uoyweek`.  
You can also clone the repository if you'd like to add new term dates (there's a helpful script in `tools/` for that) or otherwise contribute :)

## Usage
Simply run `./uoyweek.py` or `python3 uoyweek.py`. More options can be found with the `-h` flag, such as lowercase (`-l`) or short output (`-s`).

## As a library
You may want to use this in your own python projects instead of just calling the script - while the source is fairly straightforward, here are some points you may be interested in:

```py
# uoyweek.py should be in the directory as the script you're importing it from
import uoyweek, date
```

### Getting the week
```py
period = uoyweek.getPeriod(date.today()) 

print(period.name) # term or holiday name
print(period.date) # start date of term or holiday
```

### Getting the week number (terms)
```py
if type(period) is Term:
    print("Week " + period.getWeekNum(date.today()))
    # If you're specifying something other than date.today(),
    # it needs to be the same date you provided to getPeriod()
```

### Getting a formatted string
```py
print(period.toString(date.today()))
# as with getWeekNum(), this needs to be the same date you 
# provided to getPeriod()
```

### Using term dates directly
The `dates` list is also importable, and is in chronological order. If you select a Period from the list, you can assume that it ends at the start of the next Period in the list.

## Building an executable
Although the python script with a shebang is arguably more portable than an executable, you can create one if you'd like:  
With `cython` and `gcc`:
```
$ cython3 uoyweek.py --embed
$ ls *.c
uoyweek.c
$ gcc uoyweek.c -I<include directory for Python> -L<library containing libpython> -l<libpython* without the lib> -o uoyweek
```

## Contributing
If you see anything that needs fixing, do check the issues to see if it's known and if anyone's working on it. If not, make an issue or even submit a PR!  
Also, check out [milestones] to see what features are planned.

## License
This project is licensed under the [BSD 3-Clause][license] license.

[uoyweek]: https://github.com/LukeMoll/uoyweek "uoyweek on GitHub"
[uoy]: https://www.york.ac.uk/ "University of York"
[main]: https://raw.githubusercontent.com/LukeMoll/pyuoyweek/master/uoyweek.py "uoyweek.py on GitHub"
[milestones]: https://github.com/LukeMoll/pyuoyweek/milestones
[license]: https://github.com/LukeMoll/pyuoyweek/blob/master/LICENSE