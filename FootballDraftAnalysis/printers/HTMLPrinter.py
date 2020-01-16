# Allows us to read and write to a csv
import csv
from nodes.College import College
from nodes.NFLTeam import NFLTeam
from printers.CSVPrinter import CSVPrinter


class HTMLPrinter:

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