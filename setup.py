from distutils.core import setup

setup(
    name="uoyweek",
    version="1.1",
    description="Calculate and print formatted University of York term dates",
    author="Luke Moll",
    url="https://github.com/LukeMoll/pyuoyweek",
    packages=["uoyweek"],
    python_requires=">3.6", # for fstrings
    entry_points={
        "console_scripts":["uoyweek=uoyweek:main"]
    }
)