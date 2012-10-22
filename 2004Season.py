# All files taken from www.baseball-reference.com

from FormatGames import *
"""
FormatDatabases calculates by name
which baserunners are on base on any
given play.
"""

def failures(games):
    """
    Displays all failed rows for all
    filenames in "games."

    games = list of csv filename strings
    """
    gms = []
    for game in games:
        print
        print game
        gm = ShowFailures(game)
    
def baserunners(games):
    """
    For each row in all filenames in
    "games," displays row number, inning
    runners on base, batter, play.

    games = list of csv filename strings
    """
    gms = []
    for game in games:
        print
        print
        print game
        gm = ShowBaserunners(game)

postseason2004 =\
[\
"2004Postseason/2004ALDSaG1.csv",\
"2004Postseason/2004ALDSaG2.csv",\
"2004Postseason/2004ALDSaG3.csv",\
"2004Postseason/2004ALDSaG4.csv",\
"2004Postseason/2004ALDSbG1.csv",\
"2004Postseason/2004ALDSbG2.csv",\
"2004Postseason/2004ALDSbG3.csv",\
"2004Postseason/2004NLDSaG1.csv",\
"2004Postseason/2004NLDSaG2.csv",\
"2004Postseason/2004NLDSaG3.csv",\
"2004Postseason/2004NLDSaG4.csv",\
"2004Postseason/2004NLDSaG5.csv",\
"2004Postseason/2004NLDSbG1.csv",\
"2004Postseason/2004NLDSbG2.csv",\
"2004Postseason/2004NLDSbG3.csv",\
"2004Postseason/2004NLDSbG4.csv",\
"2004Postseason/2004ALCSG1.csv",\
"2004Postseason/2004ALCSG2.csv",\
"2004Postseason/2004ALCSG3.csv",\
"2004Postseason/2004ALCSG4.csv",\
"2004Postseason/2004ALCSG5.csv",\
"2004Postseason/2004ALCSG6.csv",\
"2004Postseason/2004ALCSG7.csv",\
"2004Postseason/2004NLCSG1.csv",\
"2004Postseason/2004NLCSG2.csv",\
"2004Postseason/2004NLCSG3.csv",\
"2004Postseason/2004NLCSG4.csv",\
"2004Postseason/2004NLCSG5.csv",\
"2004Postseason/2004NLCSG6.csv",\
"2004Postseason/2004NLCSG7.csv",\
"2004Postseason/2004WSG1.csv",\
"2004Postseason/2004WSG2.csv",\
"2004Postseason/2004WSG3.csv",\
"2004Postseason/2004WSG4.csv",\
 ]

regSeason2004 =\
[\
"2004Season/BOS@BAL4-4-2004.csv",\
"2004Season/BOS@BAL4-6-2004.csv",\
"2004Season/BOS@BAL4-7-2004.csv",\
"2004Season/BOS@BAL4-8-2004.csv",\
"2004Season/TOR@BOS4-9-2004.csv",\
"2004Season/TOR@BOS4-10-2004.csv",\
"2004Season/TOR@BOS4-11-2004.csv",\
"2004Season/BAL@BOS4-15-2004.csv",\
"2004Season/NYY@BOS4-16-2004.csv",\
"2004Season/NYY@BOS4-17-2004.csv",\
"2004Season/NYY@BOS4-18-2004.csv",\
"2004Season/NYY@BOS4-19-2004.csv",\
"2004Season/BOS@TOR4-20-2004.csv",\
"2004Season/BOS@TOR4-21-2004.csv",\
"2004Season/BOS@TOR4-22-2004.csv",\
"2004Season/BOS@NYY4-23-2004.csv",\
"2004Season/BOS@NYY4-24-2004.csv",\
"2004Season/BOS@NYY4-25-2004.csv",\
"2004Season/TB@BOS4-28-2004.csv",\
"2004Season/TB@BOS4-29-2004.csv",\
"2004Season/TB@BOSb4-29-2004.csv",\
"2004Season/BOS@TEXa5-1-2004.csv",\
"2004Season/BOS@TEXb5-1-2004.csv",\
"2004Season/BOS@TEX5-2-2004.csv",\
"2004Season/BOS@CLE5-3-2004.csv",\
"2004Season/BOS@CLE5-4-2004.csv",\
"2004Season/BOS@CLE5-5-2004.csv",\
"2004Season/BOS@CLE5-6-2004.csv",\
"2004Season/KC@BOS5-7-2004.csv",\
"2004Season/KC@BOS5-8-2004.csv",\
"2004Season/KC@BOS5-9-2004.csv",\
"2004Season/KC@BOS5-10-2004.csv",\
"2004Season/CLE@BOS5-11-2004.csv",\
"2004Season/CLE@BOS5-12-2004.csv",\
"2004Season/BOS@TOR5-13-2004.csv",\
"2004Season/BOS@TOR5-14-2004.csv",\
"2004Season/BOS@TOR5-15-2004.csv",\
"2004Season/BOS@TOR5-16-2004.csv",\
"2004Season/BOS@TB5-18-2004.csv",\
"2004Season/BOS@TB5-19-2004.csv",\
"2004Season/BOS@TB5-20-2004.csv",\
"2004Season/TOR@BOS5-21-2004.csv",\
"2004Season/TOR@BOS5-22-2004.csv",\
"2004Season/TOR@BOS5-23-2004.csv",\
"2004Season/OAK@BOS5-25-2004.csv",\
"2004Season/OAK@BOS5-26-2004.csv",\
"2004Season/OAK@BOS5-27-2004.csv",\
"2004Season/SEA@BOS5-28-2004.csv",\
"2004Season/SEA@BOS5-29-2004.csv",\
"2004Season/SEA@BOS5-30-2004.csv",\
"2004Season/SEA@BOS5-31-2004.csv",\
"2004Season/BOS@ANA6-1-2004.csv",\
"2004Season/BOS@ANA6-2-2004.csv",\
"2004Season/BOS@KC6-4-2004.csv",\
"2004Season/BOS@KC6-5-2004.csv",\
"2004Season/BOS@KC6-6-2004.csv",\
"2004Season/SD@BOS6-8-2004.csv",\
"2004Season/SD@BOS6-9-2004.csv",\
"2004Season/SD@BOS6-10-2004.csv",\
"2004Season/LAD@BOS6-11-2004.csv",\
"2004Season/LAD@BOS6-12-2004.csv",\
"2004Season/LAD@BOS6-13-2004.csv",\
"2004Season/BOS@COL6-15-2004.csv",\
"2004Season/BOS@COL6-16-2004.csv",\
"2004Season/BOS@COL6-17-2004.csv",\
"2004Season/BOS@SF6-18-2004.csv",\
"2004Season/BOS@SF6-19-2004.csv",\
"2004Season/BOS@SF6-20-2004.csv",\
"2004Season/MIN@BOS6-22-2004.csv",\
"2004Season/MIN@BOS6-23-2004.csv",\
"2004Season/MIN@BOS6-24-2004.csv",\
"2004Season/PHI@BOS6-25-2004.csv",\
"2004Season/PHI@BOS6-26-2004.csv",\
"2004Season/PHI@BOS6-27-2004.csv",\
"2004Season/BOS@NYY-29-2004.csv",\
"2004Season/BOS@NYY-30-2004.csv",\
"2004Season/BOS@NYY7-1-2004.csv",\
"2004Season/BOS@ATL7-2-2004.csv",\
"2004Season/BOS@ATL7-3-2004.csv",\
"2004Season/BOS@ATL7-4-2004.csv",\
"2004Season/OAK@BOS7-6-2004.csv",\
"2004Season/OAK@BOS7-7-2004.csv",\
"2004Season/OAK@BOS7-8-2004.csv",\
"2004Season/TEX@BOS7-9-2004.csv",\
"2004Season/TEX@BOS7-10-2004.csv",\
"2004Season/TEX@BOS7-11-2004.csv",\
"2004Season/BOS@ANA7-15-2004.csv",\
"2004Season/BOS@ANA7-16-2004.csv",\
"2004Season/BOS@ANA7-17-2004.csv",\
"2004Season/BOS@ANA7-18-2004.csv",\
"2004Season/BOS@SEA7-19-2004.csv",\
"2004Season/BOS@SEA7-20-2004.csv",\
"2004Season/BAL@BOS7-21-2004.csv",\
"2004Season/BAL@BOS7-22-2004.csv",\
"2004Season/BAL@BOS7-22b-2004.csv",\
"2004Season/NYY@BOS7-23-2004.csv",\
"2004Season/NYY@BOS7-24-2004.csv",\
"2004Season/NYY@BOS7-25-2004.csv",\
"2004Season/BOS@BAL7-26-2004.csv",\
"2004Season/BOS@BAL7-28-2004.csv",\
"2004Season/BOS@MIN7-30-2004.csv",\
"2004Season/BOS@MIN7-31-2004.csv",\
]

x = 0
print "Options:"
while x == 0:
    print
    print "Functions: baserunners, failures"
    try:
        fun = input('Enter function:')
        x = 1
    except NameError, e:
        print e
        print "Please try again"
        x = 0
x = 0
while x == 0:
    print
    print "lists of games: postseason2004, regSeason2004 (Red Sox April-July only for now)"
    try:
        games = input('Enter list of games:')
        x = 1
    except NameError, e:
        print e
        print "Please try again"
        x = 0
fun(games)
