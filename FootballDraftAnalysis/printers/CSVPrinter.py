# Allows us to read and write to a csv
import csv
from nodes.College import College
from nodes.NFLTeam import NFLTeam


class CSVPrinter:

    def __init__(self):
        return

    @staticmethod
    def printEdgesCSVAndLabelsCSV(playersList, edgeCSVLocation, labelCSVLocation):
        edgeCSVRows = [["Source", "Target"]]
        labelCSVRows = [["ID", "Label"]]
        for player in playersList:
            edgeCSVRows.append([player.collegeID, player.uniqueID])
            edgeCSVRows.append([player.uniqueID, player.nflTeamID])
            labelCSVRows.append([player.uniqueID, player.name])
        for college in College.teamCache:
            labelCSVRows.append([college.uniqueID, college.name])
        for team in NFLTeam.teamCache:
            labelCSVRows.append([team.uniqueID, team.name])
        with open(edgeCSVLocation, "w") as edgesCSV:
            writer = csv.writer(edgesCSV)
            writer.writerows(edgeCSVRows)
        edgesCSV.close()
        with open(labelCSVLocation, "w") as labelCSV:
            writer = csv.writer(labelCSV)
            writer.writerows(labelCSVRows)
        labelCSV.close()

