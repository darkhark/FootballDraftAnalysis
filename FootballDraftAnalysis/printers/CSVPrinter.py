# Allows us to read and write to a csv
import csv
from nodes.College import College
from nodes.NFLTeam import NFLTeam


class CSVPrinter:

    def __init__(self):
        return

    @staticmethod
    def printAllEdgesCSVAndLabelsCSV(playersList, edgeCSVLocation, labelCSVLocation):
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age",
                         "Round Selected", "Pick In Round", "Position"]]
        for player in playersList:
            nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
            edgeCSVRows.append([player.collegeID, player.uniqueID])
            edgeCSVRows.append([player.uniqueID, nflID])
            labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                 player.draftAge, player.roundSelected, player.pickInRound, player.position])
        for college in College.teamCache:
            labelCSVRows.append([college.uniqueID, college.name, "College", 0, 0, 0, 0, 0, "0"])
        for team in NFLTeam.teamCache:
            labelCSVRows.append([team.uniqueID, team.name, "NFL Team", 0, 0, 0, 0, 0, "0"])
        with open(edgeCSVLocation, "w") as edgesCSV:
            writer = csv.writer(edgesCSV)
            writer.writerows(edgeCSVRows)
        edgesCSV.close()
        with open(labelCSVLocation, "w") as labelCSV:
            writer = csv.writer(labelCSV)
            writer.writerows(labelCSVRows)
        labelCSV.close()

    @staticmethod
    def printAwardedEdgesCSVAndLabelsCSV(playersList, edgeCSVLocation, labelCSVLocation):
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []
        for player in playersList:
            if int(player.proBowls) >= 1 or int(player.allPros) >= 1:
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.roundSelected, player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printRoundRangeEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, minimum, maximum):
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []
        for player in playersList:
            if minimum <= int(player.roundSelected) <= maximum:
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.roundSelected, player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printPositionEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, position):
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []
        for player in playersList:
            if player.position == position:
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.roundSelected, player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printPlayersAndEdgesToCSV(collegeList, NFLTeamList, edgeCSVLocation, labelCSVLocation,
                                  edgeCSVRows, labelCSVRows):
        for collegeID in collegeList:
            college = College.getCachedTeam(collegeID)
            labelCSVRows.append([college.uniqueID, college.name, "College", 0, 0, 0, 0, 0, "0"])
        for teamID in NFLTeamList:
            team = NFLTeam.getCachedTeam(teamID)
            labelCSVRows.append([team.uniqueID, team.name, "NFL Team", 0, 0, 0, 0, 0, "0"])
        with open(edgeCSVLocation, "w") as edgesCSV:
            writer = csv.writer(edgesCSV)
            writer.writerows(edgeCSVRows)
        edgesCSV.close()
        with open(labelCSVLocation, "w") as labelCSV:
            writer = csv.writer(labelCSV)
            writer.writerows(labelCSVRows)
        labelCSV.close()

    @staticmethod
    def getModernNFLID(nflID):
        if nflID == "NFL32":
            nflID = "NFL22"
        if nflID == "NFL33" or nflID == "NFL34":
            nflID = "NFL30"
        if nflID == "NFL35":
            nflID = "NFL3"
        if nflID == "NFL36":
            nflID = "NFL0"
        return nflID
