# FormatGames.py ReadMe:

This script takes in a .csv file representing the play-by-play of a baseball game as provided by www.baseball-reference.com, and with the given information, calculates the names of the runners on base for any given play. To obtain data in a compatible format, go to http://www.baseball-reference.com/boxes/, select the desired season, and on the following page select the data/team. If you select a team, under "Team Game-by-Game Schedule and Results," click "Boxscore" for the desired game. Scroll down to "Play By Play," and click the link "CSV" in the menu on top. The table should convert to csv format. Select the text starting from where it says "Inn" to the end of the last line (the last line should begin `,,,,,,,,,x runs x hits x errors x LOB.` etc.). Copy and past into a text editor, and save the file with the extension .csv, under any desired filename. Run FormatGames.py
and enter ShowBaserunners(`filepath/filename.csv`), and all plays and baserunner configurations will print. Any plays that fail because they are not consistent with the original data will print at the top, and any bugs reported would be appreciated, as only a relatively small number of games have been tested. In order to see the failures by themselves, run the program and enter ShowFailures(`filepath/filename.csv`). To test a list of games, create a list of `filepath/filename.csv` files in-between the follow lines of code:

    >############# LISTS #############
    >
    >############# LISTS #############

Add the name of your new list to the string in line 202. Then run `TestListsOfGame.py`, and follow the on-screen instructions. Lists of all the games I have tested so far are already included in the appropriate location.
