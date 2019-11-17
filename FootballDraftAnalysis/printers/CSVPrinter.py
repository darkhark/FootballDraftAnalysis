# Allows us to read and write to a csv
import csv
from nodes.College import College
from nodes.NFLTeam import NFLTeam


class CSVPrinter:
    edgeCSVRowsHeader = [["Source", "Target"]]
    labelCSVRowsHeader = [["ID", "Label", "Node Type", "All Pros", "Pro Bowls", "Draft Age", "Year Drafted",
                           "Round Selected", "Pick In Round", "Position", "College", "NFLTeam"]]
    def __init__(self):
        return

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
        edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)
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
                                     player.pickInRound, player.position,
                                     College.getCachedTeam(player.collegeID).name, NFLTeam.getCachedTeam(player.nflTeamID).name])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printRoundRangeEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, minimum, maximum,
                                          awardedOnly):
        edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)
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
                                     player.pickInRound, player.position,
                                     College.getCachedTeam(player.collegeID).name, NFLTeam.getCachedTeam(player.nflTeamID).name])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printPositionEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, position, awardedOnly):
        edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)
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
                                     player.pickInRound, player.position,
                                     College.getCachedTeam(player.collegeID).name, NFLTeam.getCachedTeam(player.nflTeamID).name])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation, labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def printOLEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        offensiveLine = ["T", "G", "C", "OL"]
        edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)
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
                                     player.pickInRound, player.position,
                                     College.getCachedTeam(player.collegeID).name, NFLTeam.getCachedTeam(player.nflTeamID).name])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation,
                                             labelCSVLocation,
                                             edgeCSVRows, labelCSVRows)

    @staticmethod
    def print4_3LBsEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        lbs4_3 = ["OLB", "ILB"]
        edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)
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
                                     player.pickInRound, player.position,
                                     College.getCachedTeam(player.collegeID).name, NFLTeam.getCachedTeam(player.nflTeamID).name])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, edgeCSVRows, labelCSVRows)

    @staticmethod
    def printDBsEdgesAndLabelsCSVs(playersList, edgeCSVLocation, labelCSVLocation, awardedOnly):
        defensiveBacks = ["CB", "DB", "S"]
        edgeCSVRows = list.copy(CSVPrinter.edgeCSVRowsHeader)
        labelCSVRows = list.copy(CSVPrinter.labelCSVRowsHeader)
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
                                     player.pickInRound, player.position,
                                     College.getCachedTeam(player.collegeID).name, NFLTeam.getCachedTeam(player.nflTeamID).name])
        CSVPrinter.printPlayersAndEdgesToCSV(tempCollegeIDList, tempNFLTeamIDList, edgeCSVLocation,
                                             labelCSVLocation, edgeCSVRows, labelCSVRows)

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

    @staticmethod
    def printBipartiteHTML(playersList, htmlLocation, awardedOnly):
        outerDict = {}
        tempCounterDict = {}
        counterDict = {}
        for player in playersList:
            playerHasAward = int(player.allPros) > 0 or int(player.proBowls) > 0
            if (awardedOnly and playerHasAward) or not awardedOnly:
                nflName = NFLTeam.getCachedTeam(CSVPrinter.getModernNFLID(player.nflTeamID)).name
                collegeName = College.getCachedTeam(player.collegeID).name
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
<!DOCTYPE html>
<meta charset="utf-8">
<style>
.mainBars rect{
  fill-opacity: 0;
  stroke-width: 0.5px;
  stroke: rgb(0, 0, 0);
  stroke-opacity: 0;
}
.subBars{
	shape-rendering:crispEdges;
}
.header{
	text-anchor:middle;
	font-size:16px;
}
</style>
<body>
<script src="https://d3js.org/d3.v4.min.js"></script>
<script src="http://vizjs.org/viz.v1.1.0.min.js"></script>
<script>
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
var color ={ARI:"#f03535", ATL:"#ab0909",  BAL:"#64017d", BUF:"#166af2", CAR:"#50b4f2",
 CHI:"#013263", CIN:"#f58905", CLE:"#b35b04", DAL:"#ada9a5", DEN:"#FF990A",
 DET:"#0AB6FF", GNB:"#FFD20A", HOU:"#012A7D", IND:"#E1F5FA", JAX:"#146B02",
 KAN:"#F7070F", LAC:"#2FD1FA", LAR:"#024BAB", MIA:"#07E88E", MIN:"#A835F0",
 NOR:"#B58610", NWE:"#002EAB", NYG:"#4768C4", NYJ:"#039C27", OAK:"#000000",
 PHI:"#02BA2D", PIT:"#FFEA05", SEA:"#05FF09", SFO:"#E80725", TAM:"#F71936",
 TEN:"#2D95F7", WAS:"#B83D5F"};
var svg = d3.select("body").append("svg").attr("width", 700).attr("height", 2200);
var g = svg.append("g").attr("transform","translate(200,50)");

var bp=viz.bP()
        .data(data)
        .pad(1)
        .min(8)
        .height(2000)
        .width(300)
        .barSize(35)
        .fill(d=>color[d.primary]);
g.call(bp);

g.selectAll(".mainBars")
    .on("mouseover",mouseover)
    .on("mouseout",mouseout)

<!--Names-->
g.selectAll(".mainBars").append("text").attr("class","label")
    .attr("x",d=>(d.part=="primary"? -30: 30))
    .attr("y",d=>+6)
    .text(d=>d.key)
    .attr("text-anchor",d=>(d.part=="primary"? "end": "start"));
<!--Percent-->
g.selectAll(".mainBars").append("text").attr("class","perc")
    .attr("x",d=>(d.part=="primary"? -90: 180))
    .attr("y",d=>+6)
    .text(function(d){ return d3.format("0.0%")(d.percent)})
    .attr("text-anchor",d=>(d.part=="primary"? "end": "start"));

function mouseover(d){
    bp.mouseover(d);
    g.selectAll(".mainBars")
    .select(".perc")
    .text(function(d){ return d3.format("0.0%")(d.percent)})
}
function mouseout(d){
    bp.mouseout(d);
    g.selectAll(".mainBars")
        .select(".perc")
        .text(function(d){ return d3.format("0.0%")(d.percent)})
}
d3.select(self.frameElement).style("height", "800px");
</script>
</body>
</html>
        """

        entireHTML = topOfHTML + dictionaryToString + bottomOfHTML
        with open(htmlLocation, "w") as htmlwriter:
            htmlwriter.write(entireHTML)
        htmlwriter.close()

