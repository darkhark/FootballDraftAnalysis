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
            edgeCSVRows.append([player.collegeID, player.uniqueID])
            edgeCSVRows.append([player.uniqueID, nflID])
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


    @staticmethod
    def printBipartiteHTML(playersList, htmlLocation, awardedOnly):
        outerDict = {}
        tempCounterDict = {}
        counterDict = {}
        for player in playersList:
            playerHasAward = int(player.allPros) > 0 or int(player.proBowls) > 0
            if (awardedOnly and playerHasAward) or not awardedOnly:
                nflName = NFLTeam.getCachedTeam(CSVPrinter.getModernNFLID(player.nflTeamID)).name.encode('utf-8')
                collegeName = College.getCachedTeam(player.collegeID).name.encode('utf-8')
                if nflName not in outerDict:
                    innerDict = {collegeName: 1}
                    outerDict[nflName] = innerDict
                elif collegeName not in outerDict[nflName]:
                    outerDict[nflName][collegeName] = 1
                else:
                    outerDict[nflName][collegeName] += 1
                if collegeName not in tempCounterDict:
                    innerCounterDict = {nflName: 1}
                    tempCounterDict[collegeName] = innerCounterDict
                elif nflName not in tempCounterDict[collegeName]:
                    tempCounterDict[collegeName][nflName] = 1
                else:
                    tempCounterDict[collegeName][nflName] += 1

        for clg in tempCounterDict:
            totalDraftees = 0
            for nfl in tempCounterDict[clg]:
                totalDraftees += tempCounterDict[clg][nfl]
            counterDict[clg] = totalDraftees
        topOfHTML = """
<!DOCTYPE html>\n
<meta charset="utf-8">\n
<style>\n
.mainBars rect{\n
  fill-opacity: 0;\n
  stroke-width: 0.5px;\n
  stroke: rgb(0, 0, 0);\n
  stroke-opacity: 0;\n
}\n
.subBars{\n
	shape-rendering:crispEdges;\n
}\n
.header{\n
	text-anchor:middle;\n
	font-size:16px;\n
}\n
</style>\n
<body>\n
<script src="https://d3js.org/d3.v4.min.js"></script>\n
<script src="http://vizjs.org/viz.v1.3.0.min.js"></script>\n
<script>\n
"""
        dictionaryToString = '\nvar data = ['
        for nflTeam in outerDict:
            for college in outerDict[nflTeam]:
                if counterDict[college] > 3:
                    replacementCollegeName = college
                    if "'" in college:
                        replacementCollegeName = replacementCollegeName.replace("'", "`")
                    dictionaryToString += "['" + nflTeam + "','" + replacementCollegeName + "'," \
                                          + str(outerDict[nflTeam][college]) + "], " + "\n"
        dictionaryToString += "]; "
        dictionaryToString.replace("], \n];", "]];\n")
        bottomOfHTML = """
var svg = d3.select("body").append("svg").attr("width", 960).attr("height", 2300);\n
\n
svg.append("text").attr("x",300).attr("y",70)\n
	.attr("class","header").text("Awarded Players Drafted");\n
\n
var g =[svg.append("g").attr("transform","translate(150,100)")];\n
\n
var bp= [viz.biPartite()\n
		.data(data)\n
		.pad(1)\n
		.height(900)\n
		.width(300)\n
		.barSize(50)];\n
\n
[0].forEach(function(){\n
	g[0].call(bp[0])\n
	\n
	g[0].append("text").attr("x",-50).attr("y",-8).style("text-anchor","middle").text("NFL Team");\n
	g[0].append("text").attr("x", 325).attr("y",-8).style("text-anchor","middle").text("College");\n
	\n
	g[0].selectAll(".mainBars")\n
		.on("mouseover",mouseover)\n
		.on("mouseout",mouseout);\n
\n
<!--Labels -60 = NFL 50 = College-->\n
	g[0].selectAll(".mainBars").append("text").attr("class", "label")\n
		.attr("x",d=>(d.part=="primary"? -60: 50))\n
		.attr("y",d=>+6)\n
		.text(d=>d.key)\n
		.attr("text-anchor",d=>(d.part=="primary"? "end": "start"));\n
<!--Percentages-->\n
	g[0].selectAll(".mainBars").append("text").attr("class", "perc")\n
		.attr("x",d=>(d.part=="primary"? -100: 150))\n
		.attr("y",d=>+6)\n
		.text(function(d){ return d3.format("0.0%")(d.percent)})\n
		.attr("text-anchor",d=>(d.part=="primary"? "end": "start"));\n
});\n
\n
function mouseover(d){\n
	[0].forEach(function(){\n
		bp[0].mouseover(d);\n
		\n
		g[0].selectAll(".mainBars").select(".perc")\n
		.text(function(d){ return d3.format("0.0%")(d.percent)});\n
	});\n
}\n
function mouseout(d){\n
	[0].forEach(function(){\n
		bp[0].mouseout(d);\n
		\n
		g[0].selectAll(".mainBars").select(".perc")\n
		.text(function(d){ return d3.format("0.0%")(d.percent)});\n
	});\n
}\n
d3.select(self.frameElement).style("height", "800px");\n
</script>\n
</body>\n
</html>
        """

        entireHTML = topOfHTML + dictionaryToString + bottomOfHTML
        with open(htmlLocation, "w") as htmlwriter:
            htmlwriter.write(entireHTML)
        htmlwriter.close()

