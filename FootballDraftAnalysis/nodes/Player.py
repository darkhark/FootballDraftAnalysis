# Node is in parenthesis so that it can inherit the abstract class and all of its methods.
class Player:
    # This is a static variable. The same value exists for every instance of this class.
    uniqueIDNumber = 0

    # This is the constructor for the class. The constructor is called anytime we need this object.
    def __init__(self, playerData, collegeID, nflTeamID):
        # This is how python creates local variables that can used in other method of the class.
        self.yearDrafted = playerData[0]
        self.roundSelected = playerData[1]
        self.pickInRound = playerData[2]
        self.name = playerData[3]
        self.position = playerData[4]
        self.draftAge = playerData[5]
        self.allPros = playerData[6]
        self.proBowls = playerData[7]
        self.collegeID = collegeID
        self.nflTeamID = nflTeamID
        self.uniqueID = "PL" + str(self.uniqueIDNumber)
        # This increases the static variable by 1. Doing this will make each ID different, even though it looks like
        # every object will have an ID of PL0.
        Player.uniqueIDNumber += 1

    def getCharacteristicsOfPlayerAsList(self):
        return [self.allPros, self.proBowls, self.draftAge, self.roundSelected, self.pickInRound, self.position]

