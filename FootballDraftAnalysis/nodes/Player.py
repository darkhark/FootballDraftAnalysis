from nodes import Node


# Node is in parenthesis so that it can inherit the abstract class and all of its methods.
class Player(Node):
    # This is a static variable. The same value exists for every instance of this class.
    uniqueIDNumber = 0

    # This is the constructor for the class. The constructor is called anytime we need this object.
    def __init__(self, name, position, collegeID, roundSelected, yearDrafted, nflTeamID, allPros, proBowls):
        # This is how python creates local variables that can used in other method of the class.
        self.name = name
        self.position = position
        self.collegeID = collegeID
        self.roundSelected = roundSelected
        self.yearDrafted = yearDrafted
        self.nflTeamID = nflTeamID
        self.allPros = allPros
        self.proBowls = proBowls
        self.uniqueID = "PL" + str(self.uniqueIDNumber)
        # This increases the static variable by 1. Doing this will make each ID different, even though it looks like
        # every object will have an ID of PL0.
        Player.uniqueIDNumber += 1

    # This method overrides the same method in Node. Because the method is abstract in Node.py, it is required here.
    def getName(self):
        return self.name

    # This method overrides the same method in Node. Because the method is abstract in Node.py, it is required here.
    def getUniqueID(self):
        return self.uniqueID

