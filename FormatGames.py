import csv
import numpy

class Game(object):
    """
    An object accepting a csv file as an argument for
    formatting purposes.
    """

    def __init__(self, csv_file):
        """
        Opens and read a csv file with dialect 'excel' and
        converts said file into a list of lists for each row--
        eliminating irrelevant rows--referenced within the
        class as self.list.

        csv_file is a str of a csv file name
        """
        File = csv.reader(open(csv_file, 'U'), 'excel')
        fileList = []
        for row in File:
            if len(row) == 12:
                fileList.append(row)
        self.list = fileList
        self.game = csv_file
             
    def formatFile(self):
        """
        Returns an array of self.list.
        """
        for row in self.list:
            return numpy.array(self.list)

    def formatIndices(self):
        """
        Returns dictionary of the first row in self.list, which
        labels the data, as {'label':index} to allow the user to
        look up information using the label name instead of
        remembering each index.
        """
        col = self.list[0]
        index = {}
        for key in col:
            index[key] = col.index(key)
        return index

    def getLabels(self):
        """
        Prints every catagory in database.
        """
        for label in self.list[0]:
            print label

    def lookUp(self, row, key):
        """
        Displays catagory key for every
        line in the database.

        key is str
        """
        array = self.formatFile()
        dictionary = self.formatIndices()
        return array[row, dictionary[key]]
    
    def checkBaserunners(self, names, numbers, array, dictionary):
        """
        Tests whether formatBaserunners(self) is consistent
        with the database's original baserunner indication

        Failure prints with following format:
        
            ROW, RoB BEFORE PLAY (names and numbers), BATTER, PLAY,
            RoB AFTER PLAY (names and numbers)/ FAILED!
        """
        failures = []
        for row in range(len(names)):
            play = array[row-1, dictionary['Play Description']]
            name = names[row]
            number = numbers[row]
            row2 = row
            while play == array[row2-1, dictionary['Play Description']]:
                play = array[row2, dictionary['Play Description']]
                batter = str(array[row2, dictionary['Batter']]).split()
                if batter != []: 
                    batter = batter[-1]
                else:
                    batter = ''
                row2 -= 1
            for base in range(len(name)):
                if name[base] == ''\
                   and number[base] == '':
                    break  
                elif (name[base] != ''\
                      and number[base] == '-')\
                      or (name[base] == ''\
                      and number[base] != '-'):
                    failure =  "row "\
                              + str(row) + ', '\
                              + str(array[row2, dictionary['Inn']]) + ' '\
                              + str(names[row2]) + ' '\
                              + str(numbers[row2]) + ' '\
                              + batter + ': '\
                              + play + '  '\
                              + str(name) + ' '\
                              + str(number) + '/'\
                              + ' FAILED!'
                    print failure
                    print
                    failures.append(failure)
                    break
        if len(failures) == 0:
            print "No failures in this game!"
        return failures
   
    def moveRunnerOnThird(self, runnerOnThird, newOnBase, play):
        if runnerOnThird != '':
            newOnBase[2] = runnerOnThird
            if runnerOnThird + ' Scores' in play\
               or runnerOnThird + ' Steals Hm' in play\
               or runnerOnThird + ' Caught Stealing' in play\
               or runnerOnThird + ' out at' in play\
               or runnerOnThird + ' Picked off 3B' in play\
               or 'Ground Ball Double Play' in play:
                newOnBase[2] = ''    
        return newOnBase

    def moveRunnerOnSecond(self, runnerOnSecond, newOnBase, play):
        if runnerOnSecond != '':
            newOnBase[1] = runnerOnSecond
            if runnerOnSecond + ' Caught Stealing' in play\
               or runnerOnSecond + ' out at' in play\
               or 'Ground Ball Double Play' in play\
               or runnerOnSecond + ' Picked off 2B' in play:
                newOnBase[1] = ''
            if runnerOnSecond + ' to 3B' in play\
               or runnerOnSecond + ' Steals 3B' in play:
                newOnBase[2] = runnerOnSecond
                newOnBase[1] = ''
            if runnerOnSecond + ' Scores' in play:
                newOnBase[2] = ''
                newOnBase[1] = ''
            if runnerOnSecond + ' stays at 2B' in play:
                newOnBase[1] = runnerOnSecond
        return newOnBase

    def moveRunnerOnFirst(self, runnerOnFirst, newOnBase, play):
        if runnerOnFirst != '':
            newOnBase[0] = runnerOnFirst
            if runnerOnFirst + ' Caught Stealing' in play\
                 or 'Ground Ball Double Play' in play\
                 or runnerOnFirst + ' out at' in play\
                 or runnerOnFirst + ' Picked off 1B' in play:
                newOnBase[0] = ''
            if runnerOnFirst + ' to 2B' in play\
               or runnerOnFirst + ' Steals 2B' in play:
                newOnBase[1] = runnerOnFirst
                newOnBase[0] = ''
            if runnerOnFirst + ' to 3B' in play:
                newOnBase[2] = runnerOnFirst
                newOnBase[1] = ''
                newOnBase[0] = ''
            if runnerOnFirst + ' Scores' in play:
                newOnBase[2] = ''
                newOnBase[1] = ''
                newOnBase[0] = ''
            if runnerOnFirst + ' stays at 1B' in play:
                newOnBase[0] = runnerOnFirst
        return newOnBase

    def moveBatter(self, batter, batter2, newOnBase, play):
        if 'Walk;' in play\
           or 'Intentional Walk' in play\
           or play == 'Walk'\
           or 'Walk ' in play\
           or 'Single' in play\
           or 'Reached on E' in play\
           or "Fielder's Choice" in play\
           or "Hit By Pitch" in play\
           or "Forceout at" in play\
           or batter + ' to 1B' in play:
            newOnBase[0] = batter2   
        if 'Double to' in play\
           or 'Double;' in play\
           or play == 'Double'\
           or 'Ground-rule Double' in play\
           or batter + ' to 2B' in play:
            newOnBase[0] = ''
            newOnBase[1] = batter2
        if 'Triple to' in play\
           or 'Triple;' in play\
           or play == 'Triple'\
           or batter + ' to 3B' in play:
            newOnBase[0] = ''
            newOnBase[1] = ''
            newOnBase[2] = batter2
        if 'Home Run' in play or batter + ' Scores' in play\
           or batter + ' out at 3B' in play\
           or batter + ' out at Hm' in play:
            newOnBase = ['','','']
        if batter + ' out at 1B' in play:
            newOnBase[0] = ''
        if batter + ' out at 2B' in play:
            newOnBase[0] = ''
            newOnBase[1] = ''
        return newOnBase

    def moveBaserunners(self, array, dictionary, row, onBase):
        """
        Moves all baserunners according to the play.

        array: an array representing a game as determined
            by formatFile(self).
        row: an integer representing the horizontal index
            of array i.e. array[row, collumn].
        onBase: A list of length 3 representing runners on base.
            i.e. [runnerOnFirst, runnerOnSecond, runnerOnThird].
            Bases that are empty are filled with an empty string'
        """
        play = array[row-1, dictionary['Play Description']]
        row2 = row-1
        while array[row2, dictionary['Inn']] == '':
            row2 -= 1
            play = array[row2, dictionary['Play Description']]
        batter = str(array[row2, dictionary['Batter']]).split()[-1] 
        runnerOnFirst = onBase[0]
        runnerOnSecond = onBase[1]
        runnerOnThird = onBase[2]
        newOnBase = ['', '', '']

        # This block of code guards against
        # two players on the same team with
        # the same last name. 
        ###################################        
        batter2 = batter
        if (runnerOnFirst == batter\
           or runnerOnSecond == batter\
           or runnerOnThird == batter)\
           and (runnerOnFirst in play\
                or runnerOnSecond in play
                or runnerOnThird in play):
            batter += ' ' 
        ###################################

        newOnBase = self.moveRunnerOnThird(runnerOnThird, newOnBase, play)
        newOnBase = self.moveRunnerOnSecond(runnerOnSecond, newOnBase, play)
        newOnBase = self.moveRunnerOnFirst(runnerOnFirst, newOnBase, play)
        newOnBase = self.moveBatter(batter, batter2, newOnBase, play)

        return newOnBase

    def formatBaserunners(self):
        """
        Determines by name the runners on base
        """
        array = self.formatFile()
        dictionary = self.formatIndices()
        names = ['', '', '']
        namesList = [['RoB']]
        numbersList = [['RoB']]
        testNames = []
        testNumbers = [] 
        for row in range(1, array.shape[0]):
         
            # Filters out separator rows which do not contain a play
            # and always fill the specified cells with indential content
            if array[row, dictionary['RoB']] != array[row, dictionary['Inn']]:
                names = self.moveBaserunners(array, dictionary, row, names)

                # Determines whether the previous play is part of
                # the same half inning as the current play 
                PlayInning = array[row, dictionary['Inn']]
                PrevPlayInning = array[row-1, dictionary['Inn']]
                row2 = row-1
                while PrevPlayInning == ''\
                      or "Top of the" in PrevPlayInning\
                      or "Bottom of the" in PrevPlayInning:
                    row2 -= 1
                    PrevPlayInning = array[row2, dictionary['Inn']]   

                # Resets baserunner configuration at the start of each half inning
                if PrevPlayInning != PlayInning:
                    names = ['', '', '']

                # Checks for pinch runners and replaces accordingly
                elif array[row-1, dictionary['Play Description']]\
                     == array[row-1, dictionary['Play Description']-1]:
                    names1 = names
                    replacement = array[row-1, dictionary['Play Description']] 
                    if 'pinch runs' in replacement:
                        splitReplace = replacement.split()
                        index = splitReplace.index('runs')
                        pinchRunner = splitReplace[index-2]
                        splitPinch = pinchRunner.split()
                        runner = splitReplace[index+3]
                        namesIndex = names.index(runner)
                        names[namesIndex] = pinchRunner

                # Compiles data
                numbers = array[row, dictionary['RoB']]
                namesList.append([str(names)])
                numbersList.append([str(numbers)])
                testNames.append(names)
                testNumbers.append(numbers)

            # Separator rows go here    
            else:
                namesList.append([''])
                numbersList.append([''])
                testNames.append([''])
                testNumbers.append([''])

        # Replaces original baserunner data with new data
        col = dictionary['RoB']
        array = numpy.delete(array, numpy.s_[col:col+1], 1)
        array = numpy.insert(array, [col], namesList, 1)
        
        # Tests whether new baserunner data is consistent with
        # the original data and returns failures
        failures = self.checkBaserunners(testNames, testNumbers, array, dictionary)        
        NumFailures = len(failures)
        return (array, NumFailures)
            
    def displayGame(self):
        """
        Displays the game array
        in its entirety.
        """
        array = self.formatBaserunners()[0]
        for row in array:
            print row

    def displayBaserunners(self):
        """
        Displays the baserunners
        for each play in given game.
        """
        array = self.formatBaserunners()[0]
        dictionary = self.formatIndices()
        print
        for row in range(array.shape[0]):
            print 'row: ' + str(row)\
                  + ' ' + str(array[row, dictionary['Inn']])\
                  + ' ' + str(array[row, dictionary['RoB']])\
                  + ' ' + str(array[row, dictionary['Batter']])\
                  + ': ' + str(array[row, dictionary['Play Description']])

# End Class "Games"

def ShowFailures(csv_file):
    """
    Displays all failed rows for all
    filenames in "csv_file."

    csv_file = string of csv filename.
    """
    numFailures = 0
    game = Game(csv_file)
    array = game.formatFile()[0]
    dictionary = game.formatIndices()
    game.formatBaserunners()


def ShowBaserunners(csv_file):
    """
    For each row in "csv_file,"
    displays row number, inning
    runners on base, batter, play.

    csv_file = string of csv filename
    """
    game = Game(csv_file)
    array = game.formatFile()[0]
    print
    dictionary = game.formatIndices()
    game.displayBaserunners()








