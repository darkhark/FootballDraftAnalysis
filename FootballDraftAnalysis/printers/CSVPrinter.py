# Allows us to read and write to a csv
import csv
from nodes.College import College
from nodes.NFLTeam import NFLTeam


class CSVPrinter:
    edgeCSVRowsHeader = [["Source", "Target"]]
    labelCSVRowsHeader = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                           "Round Selected", "Pick In Round", "Position", "College", "NFLTeam"]]
    cumulColPlaysOverYears = {}
    collegeIDList = []
    nflTeamIDList = []
    years = []
    edgeCSVRows = []
    labelCSVRows = []

    @staticmethod
    def printAllEdgesCSVAndLabelsCSV(playersList, edgeCSVLocation, labelCSVLocation):
        edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)
        for player in playersList:
            nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
            edgeCSVRows.append([player.collegeID, player.uniqueID])
            edgeCSVRows.append([player.uniqueID, nflID])
            labelCSVRows.append([player.uniqueID, player.name, "Player", player.allPros, player.proBowls, player.yearDrafted,
                                 player.draftAge, player.roundSelected, player.pickInRound, player.position,
                                 College.getCachedTeam(player.collegeID).name, NFLTeam.getCachedTeam(player.nflTeamID).name])
        for college in College.teamCache:
            labelCSVRows.append([college.uniqueID, college.name, "College", 0, 0, 0, 0, 0, 0, "0", "0", "0"])
        for team in NFLTeam.teamCache:
            labelCSVRows.append([team.uniqueID, team.name, "NFL Team", 0, 0, 0, 0, 0, 0, "0", "0", "0"])
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
        CSVPrinter._readyCSVRowLists()
        for player in playersList:
            if int(player.proBowls) >= 1 or int(player.allPros) >= 1:
                CSVPrinter._placePlayerDataIntoCSVForm(player)
        CSVPrinter.printPlayersAndEdgesToCSV(CSVPrinter.collegeIDList, CSVPrinter.nflTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, CSVPrinter.edgeCSVRows, CSVPrinter.labelCSVRows)

    @staticmethod
    def printRoundRangeEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, minimum, maximum,
                                          awardedOnly):
        CSVPrinter._readyCSVRowLists()
        for player in playersList:
            if minimum <= int(player.roundSelected) <= maximum and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                CSVPrinter._placePlayerDataIntoCSVForm(player)
        CSVPrinter.printPlayersAndEdgesToCSV(CSVPrinter.collegeIDList, CSVPrinter.nflTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, CSVPrinter.edgeCSVRows, CSVPrinter.labelCSVRows)

    @staticmethod
    def printPositionEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, position, awardedOnly):
        CSVPrinter._readyCSVRowLists()
        for player in playersList:
            if player.position == position and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                CSVPrinter._placePlayerDataIntoCSVForm(player)
        CSVPrinter.printPlayersAndEdgesToCSV(CSVPrinter.collegeIDList, CSVPrinter.nflTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, CSVPrinter.edgeCSVRows, CSVPrinter.labelCSVRows)

    @staticmethod
    def printOLEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        offensiveLine = ["T", "G", "C", "OL"]
        CSVPrinter._readyCSVRowLists()
        for player in playersList:
            if player.position in offensiveLine and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                CSVPrinter._placePlayerDataIntoCSVForm(player)
        CSVPrinter.printPlayersAndEdgesToCSV(CSVPrinter.collegeIDList, CSVPrinter.nflTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, CSVPrinter.edgeCSVRows, CSVPrinter.labelCSVRows)

    @staticmethod
    def print4_3LBsEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        lbs4_3 = ["OLB", "ILB"]
        CSVPrinter._readyCSVRowLists()
        for player in playersList:
            if player.position in lbs4_3 and \
                    ((awardedOnly and (int(player.allPros) > 0 or int(player.proBowls) > 0)) or not awardedOnly):
                CSVPrinter._placePlayerDataIntoCSVForm(player)
        CSVPrinter.printPlayersAndEdgesToCSV(CSVPrinter.collegeIDList, CSVPrinter.nflTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, CSVPrinter.edgeCSVRows, CSVPrinter.labelCSVRows)

    @staticmethod
    def printDBsEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        defensiveBacks = ["CB", "DB", "S"]
        CSVPrinter._readyCSVRowLists()
        allDBs = CSVPrinter._getPositionalPlayers(playersList, defensiveBacks)
        for player in allDBs:
            playerHasAward = int(player.allPros) > 0 or int(player.proBowls) > 0
            if (awardedOnly and playerHasAward) or not awardedOnly:
                CSVPrinter._placePlayerDataIntoCSVForm(player)
        CSVPrinter.printPlayersAndEdgesToCSV(CSVPrinter.collegeIDList, CSVPrinter.nflTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, CSVPrinter.edgeCSVRows, CSVPrinter.labelCSVRows)

    @staticmethod
    def _readyCSVRowLists():
        CSVPrinter.collegeIDList.clear()
        CSVPrinter.nflTeamIDList.clear()
        CSVPrinter.edgeCSVRows.clear()
        CSVPrinter.labelCSVRows.clear()
        CSVPrinter.edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        CSVPrinter.labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)

    @staticmethod
    def _placePlayerDataIntoCSVForm(player):
        collegeID = player.collegeID
        if collegeID not in CSVPrinter.collegeIDList:
            CSVPrinter.collegeIDList.append(collegeID)
        nflID = CSVPrinter.getModernNFLID(player.nflTeamID)
        if nflID not in CSVPrinter.nflTeamIDList:
            CSVPrinter.nflTeamIDList.append(nflID)
        CSVPrinter.edgeCSVRows.append([collegeID, player.uniqueID])
        CSVPrinter.edgeCSVRows.append([player.uniqueID, nflID])
        CSVPrinter.labelCSVRow = [player.uniqueID, player.name, "Player", player.allPros, player.proBowls,
                                  player.draftAge, player.yearDrafted, player.roundSelected,
                                  player.pickInRound, player.position,
                                  College.getCachedTeam(player.collegeID).name,
                                  NFLTeam.getCachedTeam(player.nflTeamID).name]

    @staticmethod
    def printBarChartCSV(playersList, csvLocation, awardedOnly):
        CSVPrinter._getPlayersDraftedFromCollegeByYear(playersList, awardedOnly)
        CSVPrinter._writeCumulDataToCSV(csvLocation)

    @staticmethod
    def printBarChartCSVDBs(playersList, csvLocation, awardedOnly):
        defensiveBacks = ["CB", "DB", "S"]
        allDBs = CSVPrinter._getPositionalPlayers(playersList, defensiveBacks)
        CSVPrinter._getPlayersDraftedFromCollegeByYear(allDBs, awardedOnly)
        CSVPrinter._writeCumulDataToCSV(csvLocation)

    @staticmethod
    def _getPositionalPlayers(playersList, positionList):
        positionPlayers = []
        for player in playersList:
            if player.position in positionList:
                positionPlayers.append(player)
        return positionPlayers

    @staticmethod
    def _writeCumulDataToCSV(csvLocation):
        CSVPrinter.years = list(reversed(CSVPrinter.years))
        CSVPrinter.years = range(min(CSVPrinter.years), max(CSVPrinter.years))
        CSVPrinter._getCumulativePlayersPerCollegeByYear()
        CSVPrinter._writeToBarchartCSV(csvLocation)

    @staticmethod
    def _getPlayersDraftedFromCollegeByYear(playerList, awardedOnly):
        CSVPrinter.years.clear()
        CSVPrinter.cumulColPlaysOverYears.clear()
        for player in playerList:
            playerHasAward = int(player.allPros) > 0 or int(player.proBowls) > 0
            if (awardedOnly and playerHasAward) or not awardedOnly:
                if player.yearDrafted not in CSVPrinter.years:
                    CSVPrinter.years.append(int(player.yearDrafted))
                college = College.getCachedTeam(player.collegeID)
                if college.name not in CSVPrinter.cumulColPlaysOverYears:
                    yearData = {int(player.yearDrafted): 1}
                    CSVPrinter.cumulColPlaysOverYears[college.name] = yearData
                elif player.yearDrafted not in CSVPrinter.cumulColPlaysOverYears[college.name]:
                    CSVPrinter.cumulColPlaysOverYears[college.name][int(player.yearDrafted)] = 1
                else:
                    CSVPrinter.cumulColPlaysOverYears[college.name][player.yearDrafted] += 1

    @staticmethod
    def _getCumulativePlayersPerCollegeByYear():
        for year in CSVPrinter.years:
            for college in CSVPrinter.cumulColPlaysOverYears:
                if year not in CSVPrinter.cumulColPlaysOverYears[college] and year == min(CSVPrinter.years):
                    CSVPrinter.cumulColPlaysOverYears[college][year] = 0
                elif year not in CSVPrinter.cumulColPlaysOverYears[college]:
                    CSVPrinter.cumulColPlaysOverYears[college][year] \
                        = CSVPrinter.cumulColPlaysOverYears[college][year - 1]
                elif int(year) != min(CSVPrinter.years):
                    CSVPrinter.cumulColPlaysOverYears[college][year] \
                        += CSVPrinter.cumulColPlaysOverYears[college][year - 1]

    @staticmethod
    def _writeToBarchartCSV(csvLocation):
        header = ["college_team"]
        csvArray = []
        for year in CSVPrinter.years:
            header.append(year)
        csvArray.append(header)
        for collegeName in CSVPrinter.cumulColPlaysOverYears:
            collegeSums = [collegeName]
            for year in CSVPrinter.years:
                collegeSums.append(CSVPrinter.cumulColPlaysOverYears[collegeName][year])
            csvArray.append(collegeSums)
        with open(csvLocation, "w") as barChartCSV:
            writer = csv.writer(barChartCSV)
            writer.writerows(csvArray)
        barChartCSV.close()

    @staticmethod
    def printPlayersAndEdgesToCSV(collegeList, NFLTeamList, edgeCSVLocation, labelCSVLocation,
                                  edgeCSVRows, labelCSVRows):
        for collegeID in collegeList:
            college = College.getCachedTeam(collegeID)
            labelCSVRows.append([college.uniqueID, college.name, "College", 0, 0, 0, 0, 0, 0, "0", "0", "0", "0", "0"])
        for teamID in NFLTeamList:
            team = NFLTeam.getCachedTeam(teamID)
            labelCSVRows.append([team.uniqueID, team.name, "NFL Team", 0, 0, 0, 0, 0, 0, "0", "0", "0"])
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
