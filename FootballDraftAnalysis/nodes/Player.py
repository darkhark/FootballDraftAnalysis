from nodes import Node


class Player(Node):
    uniqueIDNumber = 0

    def __init__(self, name, position, college, roundSelected, yearDrafted, nflTeam, allPros, proBowls):
        self.name = name
        self.position = position
        self.college = college
        self.roundSelected = roundSelected
        self.yearDrafted = yearDrafted
        self.nflTeam = nflTeam
        self.allPros = allPros
        self.proBowls = proBowls
        self.uniqueID = "PL" + str(self.uniqueIDNumber)
        self.uniqueIDNumber = self.uniqueIDNumber + 1

    def getName(self):
        return self.name

    def getUniqueID(self):
        return self.uniqueID