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
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                         "Round Selected", "Pick In Round", "Position"]]
        for player in playersList:
            nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
            #edgeCSVRows.append([player.collegeID, player.uniqueID])
            #edgeCSVRows.append([player.uniqueID, nflID])
            labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls, player.yearDrafted,
                                 player.draftAge, player.roundSelected, player.pickInRound, player.position])
        for college in College.teamCache:
            labelCSVRows.append([college.uniqueID, college.name, "College", 0, 0, 0, 0, 0, 0, "0"])
        for team in NFLTeam.teamCache:
            labelCSVRows.append([team.uniqueID, team.name, "NFL Team", 0, 0, 0, 0, 0, 0, "0"])
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
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
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
                                     player.draftAge, player.yearDrafted, player.roundSelected,
                                     player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printRoundRangeEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, minimum, maximum,
                                          awardedOnly):
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []

        for player in playersList:
            if minimum <= int(player.roundSelected) <= maximum and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.yearDrafted, player.roundSelected,
                                     player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printPositionEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, position, awardedOnly):
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []
        for player in playersList:
            if player.position == position and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.yearDrafted, player.roundSelected,
                                     player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printOLEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        offensiveLine = ["T", "G", "C", "OL"]
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []
        for player in playersList:
            if player.position in offensiveLine and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.yearDrafted, player.roundSelected,
                                     player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation,
                                             labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def print4_3LBsEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        lbs4_3 = ["OLB", "ILB"]
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []
        for player in playersList:
            if player.position in lbs4_3 and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.yearDrafted, player.roundSelected,
                                     player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, edgeCSVRows, labelCSVRows)

    @staticmethod
    def printDBsEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        defensiveBacks = ["CB", "DB", "S"]
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                         "Round Selected", "Pick In Round", "Position"]]
        tempCollegeIDList = []
        tempNFLTeamIDList = []
        for player in playersList:
            playerHasAward = int(player.allPros) > 0 or int(player.proBowls) > 0
            if player.position in defensiveBacks and ((awardedOnly and playerHasAward) or not awardedOnly):
                collegeID = player.collegeID
                if collegeID not in tempCollegeIDList:
                    tempCollegeIDList.append(collegeID)
                nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
                if nflID not in tempNFLTeamIDList:
                    tempNFLTeamIDList.append(nflID)
                edgeCSVRows.append([collegeID, player.uniqueID])
                edgeCSVRows.append([player.uniqueID, nflID])
                labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                     player.draftAge, player.yearDrafted, player.roundSelected,
                                     player.pickInRound, player.position])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, edgeCSVRows, labelCSVRows)

    @staticmethod
    def printPlayersAndEdgesToCSV(collegeList, NFLTeamList, edgeCSVLocation, labelCSVLocation,
                                  edgeCSVRows, labelCSVRows):
        for collegeID in collegeList:
            college = College.getCachedTeam(collegeID)
            labelCSVRows.append([college.uniqueID, college.name, "College", 0, 0, 0, 0, 0, 0, "0"])
        for teamID in NFLTeamList:
            team = NFLTeam.getCachedTeam(teamID)
            labelCSVRows.append([team.uniqueID, team.name, "NFL Team", 0, 0, 0, 0, 0, 0, "0"])
        with open(edgeCSVLocation, "w") as edgesCSV:
            writer = csv.writer(edgesCSV)
            writer.writerows(edgeCSVRows)
        edgesCSV.close()
        with open(labelCSVLocation, "w") as labelCSV:
            writer = csv.writer(labelCSV)
            writer.writerows(labelCSVRows)
        labelCSV.close()

    @staticmethod
    def printBarChartCSV(playersList, csvLocation):
        data = {}
        header = ["college_team"]
        years = []
        csvArray = []
        for player in playersList:
            if player.yearDrafted not in years:
                 years.append(player.yearDrafted)
            college = College.getCachedTeam(player.collegeID)
            if college.name not in data:
                yearData = {player.yearDrafted: 1}
                data[college.name] = yearData
            elif player.yearDrafted not in data[college.name]:
                data[college.name][player.yearDrafted] = 1
            else:
                data[college.name][player.yearDrafted] += 1
        years = list(reversed(years))
        for year in years:
            header.append(year)
        csvArray.append(header)
        for collegeName in data:
            collegeSums = []
            collegeSums.append(collegeName)
            for year in list(years):
                print("Year: " + year)
                if year not in sorted(data[collegeName]):
                    print("Year not in that colleges years!!!!!!!!!!!!!!!!!!!!!!!!!")
                    collegeSums.append(0)
                else:
                    print("Year in data ========================================")
                    collegeSums.append(data[collegeName][year])
            csvArray.append(collegeSums)
        with open(csvLocation, "w") as barChartCSV:
            writer = csv.writer(barChartCSV)
            writer.writerows(csvArray)
        barChartCSV.close()

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

