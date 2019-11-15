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

    '''@staticmethod
    def printBipartiteGraph(playersList, csvLocation):
        bipartiteCSVHeader = ["College", "NFL Team", "Number of Players"]
        csvRows = [bipartiteCSVHeader]

        for college in College.teamCache:
            sum = 0
            nflTeams = []
            collegeName = ""
            collegeID = college.uniqueID
            for player in playersList:
                if collegeID == player.collegeID:
                    collegeName = college.name
                    sum += 1
                    nflTeamName = NFLTeam.getCachedTeam(player.nflTeamID).name
                    if nflTeamName not in nflTeams:
                        nflTeams.append(nflTeamName)
            for nflTeamName in nflTeams:
                csvRows.append([collegeName, nflTeamName, sum])'''





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
    def printBipartiteHTML(playersList, htmlLocation):
        totalPlayers = 0
        outerDict = {}
        for player in playersList:
            nflName = NFLTeam.getCachedTeam(player.nflTeamID).name.encode('utf-8')
            collegeName = College.getCachedTeam(player.collegeID).name.encode('utf-8')
            if collegeName not in outerDict:
                innerDict = {nflName: 1}
                outerDict[collegeName] = innerDict
                totalPlayers += 1
            elif nflName not in outerDict[collegeName]:
                outerDict[collegeName][nflName] = 1
                totalPlayers += 1
            else:
                outerDict[collegeName][nflName] += 1
                totalPlayers += 1
        print(outerDict)
        print("Total Players " + str(totalPlayers))

        topOfHTML = '< !DOCTYPE html > < meta charset = "utf-8" > < style > text {font - size: 12px;}.mainBars rect{'\
                    +'shape - rendering: auto; fill - opacity: 0; stroke - width: 0.5px; stroke: rgb(0, 0, 0); stroke'\
                    +' - opacity: 0; }.subBars { shape - rendering: crispEdges; }.edges { stroke: none; '\
                    +'fill - opacity:0.5; }.header { text - anchor: middle; font - size:16 px; } line { stroke: grey;'\
                    +'} < / style > < body > < script src = "https://d3js.org/d3.v4.min.js" > < / script > < script '\
                    +'src = "http://vizjs.org/viz.v1.1.0.min.js" > < / script > < script >'
        dictionaryToString = 'var data = ['
        for college in outerDict:
            for nflteam in outerDict[college]:
                dictionaryToString += "['" + college + "','" + nflteam + "'," + str(outerDict[college][nflteam]) + "], "
        dictionaryToString += "]; "
        bottomOfHTML = 'var svg = d3.select("body").append("svg").attr("width", 960).attr("height", 800); '\
                       +'svg.append("text").attr("x",250).attr("y",70).attr("class","header").text("Sales Attempt");'\
                       +'svg.append("text").attr("x",750).attr("y",70).attr("class","header").text("Sales"); '\
                       +'var g =[svg.append("g").attr("transform","translate(150,100)"),svg.append("g").attr('\
                       +'"transform","translate(650,100)")]; var bp=[ viz.bP().data(data).min(12).pad(1).height(600)'\
                       +'.width(200).barSize(35).fill(d=>color[d.primary]) ,viz.bP().data(data).value(d=>d[3]) '\
                       +'.min(12).pad(1).height(600).width(200).barSize(35).fill(d=>color[d.primary]) ]; [0,1]'\
                       +'.forEach(function(i){ g[i].call(bp[i]) g[i].append("text").attr("x",-50).attr("y",-8).style'\
                       +'("text-anchor","middle").text("Channel"); g[i].append("text").attr("x", 250).attr("y",-8)'\
                       +'.style("text-anchor","middle").text("State"); g[i].append("line").attr("x1",-100).attr("x2",0)'\
                       +'; g[i].append("line").attr("x1",200).attr("x2",300); g[i].append("line").attr("y1",610).attr'\
                       +'("y2",610).attr("x1",-100).attr("x2",0); g[i].append("line").attr("y1",610).attr("y2",610)'\
                       +'.attr("x1",200).attr("x2",300); g[i].selectAll(".mainBars").on("mouseover",mouseover).on'\
                       +'("mouseout",mouseout); g[i].selectAll(".mainBars").append("text").attr("class","label") '\
                       +'.attr("x",d=>(d.part=="primary"? -30: 30)).attr("y",d=>+6).text(d=>d.key).attr("text-'\
                       +'anchor",d=>(d.part=="primary"? "end": "start")); g[i].selectAll(".mainBars").append("text")'\
                       +'.attr("class","perc").attr("x",d=>(d.part=="primary"? -100: 80)).attr("y",d=>+6).text'\
                       +'(function(d){ return d3.format("0.0%")(d.percent)}).attr("text-anchor",d=>(d.part=="primary"'\
                       +'? "end": "start")); }); function mouseover(d){ [0,1].forEach(function(i){ bp[i].mouseover(d);'\
                       +' g[i].selectAll(".mainBars").select(".perc").text(function(d){ return d3.format("0.0%")'\
                       +'(d.percent)}); }); } function mouseout(d){ [0,1].forEach(function(i){ bp[i].mouseout(d);'\
                       +' g[i].selectAll(".mainBars").select(".perc").text(function(d){ return d3.format("0.0%")'\
                       +'(d.percent)}); }); } d3.select(self.frameElement).style("height", "800px"); </script> </body>'\
                       +' </html>'

        entireHTML = topOfHTML + dictionaryToString + bottomOfHTML
        with open(htmlLocation, "w") as htmlwriter:
            htmlwriter.write(entireHTML)
        htmlwriter.close()







#College is the class. Team cache is the object that gets filled with team name and team unique ID


#class.object
#College.teamCache



#matching players who have the same college ID and football team
    '''@staticmethod
    def Bipartite( )

        csvHeader = ["College", "NFLTeam", "Number of Players"]
        college = []
        sum = 0
        NFLTeam = []
        for player in playerList:
            if player.collegeID = uniqueID && player.NFLTeam
        for college in collegelist:'''

