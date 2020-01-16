from printers.CSVPrinter import CSVPrinter
from printers.HTMLPrinter import HTMLPrinter
from scraper.NFLDataScraper import NFLPlayerScraper
from generators.ProFootballReferenceURLGenerator import ProFootballReferenceURLGenerator


class DraftDataObtainer:
    urlList = []
    scraper = None
    baseCSVDirectory = "../../printedCSVs/"
    finishedMessage = "----------All done :)------------"
    gatherURL = "Gathering URLs"
    scraping = "Scraping data from each URL's HTML"

    @staticmethod
    def obtainAllTimeDrafted():
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.allTimeURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing All Time Players Data to CSVs.")
        CSVPrinter.printAllEdgesCSVAndLabelsCSV(DraftDataObtainer.scraper.playerList,
                                                DraftDataObtainer.baseCSVDirectory + "AllTimeEdgesCSV.csv",
                                                DraftDataObtainer.baseCSVDirectory + "AllTimeLabelsCSV.csv")
        print(DraftDataObtainer.finishedMessage)

    def 
    @staticmethod
    def obtainAllPlayers():
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing All Player Data to CSVs.")
        CSVPrinter.printAllEdgesCSVAndLabelsCSV(DraftDataObtainer.scraper.playerList,
                                                DraftDataObtainer.baseCSVDirectory + "edgesCSV.csv",
                                                DraftDataObtainer.baseCSVDirectory + "labelsCSV.csv")
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainAwardedPlayers():
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing All Awarded Players' Data to CSVs.")
        CSVPrinter.printAwardedEdgesCSVAndLabelsCSV(DraftDataObtainer.scraper.playerList,
                                                    DraftDataObtainer.baseCSVDirectory + "awardedEdgesCSV.csv",
                                                    DraftDataObtainer.baseCSVDirectory + "awardedLabelsCSV.csv")
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainRoundsRange(minimum, maximum, awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing Rounds " + str(minimum) + "-" + str(maximum) + " Player Data to CSVs.")
        edgesCSV = DraftDataObtainer.baseCSVDirectory + "rounds" + str(minimum) + "To" + str(maximum) + "EdgesCSV"
        labelsCSV = DraftDataObtainer.baseCSVDirectory + "rounds" + str(minimum) + "To" + str(maximum) + "LabelsCSV"
        if awardedOnly:
            edgesCSV = edgesCSV + "Awarded"
            labelsCSV = labelsCSV + "Awarded"
        edgesCSV = edgesCSV + ".csv"
        labelsCSV = labelsCSV + ".csv"
        CSVPrinter.printRoundRangeEdgesAndLabelsCSVs(DraftDataObtainer.scraper.playerList, edgesCSV,
                                                     labelsCSV, minimum, maximum, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainPosition(position, awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing " + position + " Player Data to CSVs.")
        edgesCSV = DraftDataObtainer.baseCSVDirectory + "position" + position + "EdgesCSV"
        labelsCSV = DraftDataObtainer.baseCSVDirectory + "position" + position + "LabelsCSV"
        if awardedOnly:
            edgesCSV = edgesCSV + "Awarded"
            labelsCSV = labelsCSV + "Awarded"
        edgesCSV = edgesCSV + ".csv"
        labelsCSV = labelsCSV + ".csv"
        CSVPrinter.printPositionEdgesAndLabelsCSVs(DraftDataObtainer.scraper.playerList, edgesCSV,
                                                   labelsCSV, position, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainOffensiveLinemen(awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing Offensive Linemen Player Data to CSVs.")
        edgesCSV = DraftDataObtainer.baseCSVDirectory + "positionOLEdgesCSV"
        labelsCSV = DraftDataObtainer.baseCSVDirectory + "positionOLLabelsCSV"
        if awardedOnly:
            edgesCSV = edgesCSV + "Awarded"
            labelsCSV = labelsCSV + "Awarded"
        edgesCSV = edgesCSV + ".csv"
        labelsCSV = labelsCSV + ".csv"
        CSVPrinter.printOLEdgesAndLabelsCSVs(DraftDataObtainer.scraper.playerList, edgesCSV, labelsCSV, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtain4_3LBs(awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing 4-3 LBs Player Data to CSVs.")
        edgesCSV = DraftDataObtainer.baseCSVDirectory + "position4-3LBsEdgesCSV"
        labelsCSV = DraftDataObtainer.baseCSVDirectory + "position4-3LBsLabelsCSV"
        if awardedOnly:
            edgesCSV = edgesCSV + "Awarded"
            labelsCSV = labelsCSV + "Awarded"
        edgesCSV = edgesCSV + ".csv"
        labelsCSV = labelsCSV + ".csv"
        CSVPrinter.print4_3LBsEdgesAndLabelsCSVs(DraftDataObtainer.scraper.playerList, edgesCSV, labelsCSV, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainDBs(awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing DBs Player Data to CSVs.")
        edgesCSV = DraftDataObtainer.baseCSVDirectory + "positionDBsEdgesCSV"
        labelsCSV = DraftDataObtainer.baseCSVDirectory + "positionDBsLabelsCSV"
        if awardedOnly:
            edgesCSV = edgesCSV + "Awarded"
            labelsCSV = labelsCSV + "Awarded"
        edgesCSV = edgesCSV + ".csv"
        labelsCSV = labelsCSV + ".csv"
        CSVPrinter.printDBsEdgesAndLabelsCSVs(DraftDataObtainer.scraper.playerList, edgesCSV, labelsCSV, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainBarChartDataDBs(awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.allTimeURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing Bar Chart Data to CSVs.")
        bartChartCSV = DraftDataObtainer.baseCSVDirectory + "BarChartCSVDBs"
        if awardedOnly:
            bartChartCSV = bartChartCSV + "Awarded"
        bartChartCSV = bartChartCSV + ".csv"
        CSVPrinter.printBarChartCSVDBs(DraftDataObtainer.scraper.playerList, bartChartCSV, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainBarChartData(awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing Bar Chart Data to CSVs.")
        bartChartCSV = DraftDataObtainer.baseCSVDirectory + "BarChartCSV"
        if awardedOnly:
            bartChartCSV = bartChartCSV + "Awarded"
        bartChartCSV = bartChartCSV + ".csv"
        CSVPrinter.printBarChartCSV(DraftDataObtainer.scraper.playerList, bartChartCSV, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainBarChartAllTimeData(awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing Bar Chart Data to CSVs.")
        bartChartCSV = DraftDataObtainer.baseCSVDirectory + "BarChartAllTimeCSV"
        if awardedOnly:
            bartChartCSV = bartChartCSV + "Awarded"
        bartChartCSV = bartChartCSV + ".csv"
        CSVPrinter.printBarChartCSV(DraftDataObtainer.scraper.playerList, bartChartCSV, awardedOnly)
        print(DraftDataObtainer.finishedMessage)


    @staticmethod
    def obtainBipartite(awardedOnly):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing Bipartite Player Data to HTML.")
        html = DraftDataObtainer.baseCSVDirectory + "bipartite"
        if awardedOnly:
            html = html + "Awarded"
        html = html + ".html"
        HTMLPrinter.printBipartiteHTML(DraftDataObtainer.scraper.playerList, html, awardedOnly)
        print(DraftDataObtainer.finishedMessage)

"""
DraftDataObtainer.obtainAllPlayers()
DraftDataObtainer.obtainAwardedPlayers()
DraftDataObtainer.obtainRoundsRange(1, 3, False)
DraftDataObtainer.obtainRoundsRange(4, 7, False)
DraftDataObtainer.obtainRoundsRange(1, 2, False)
DraftDataObtainer.obtainRoundsRange(3, 4, False)
DraftDataObtainer.obtainRoundsRange(5, 7, False)
DraftDataObtainer.obtainPosition("QB", False)
DraftDataObtainer.obtainPosition("RB", False)
DraftDataObtainer.obtainPosition("WR", False)
DraftDataObtainer.obtainPosition("TE", False)
DraftDataObtainer.obtainOffensiveLinemen(False)
DraftDataObtainer.obtainPosition("DE", False)
DraftDataObtainer.obtainPosition("DT", False)
DraftDataObtainer.obtainPosition("LB", False)
DraftDataObtainer.obtain4_3LBs(False)
DraftDataObtainer.obtainDBs(False)
DraftDataObtainer.obtainRoundsRange(1, 3, True)
DraftDataObtainer.obtainRoundsRange(4, 7, True)
DraftDataObtainer.obtainRoundsRange(1, 2, True)
DraftDataObtainer.obtainRoundsRange(3, 4, True)
DraftDataObtainer.obtainRoundsRange(5, 7, True)
DraftDataObtainer.obtainPosition("QB", True)
DraftDataObtainer.obtainPosition("RB", True)
DraftDataObtainer.obtainPosition("WR", True)
DraftDataObtainer.obtainPosition("TE", True)
DraftDataObtainer.obtainOffensiveLinemen(True)
DraftDataObtainer.obtainPosition("DE", True)
DraftDataObtainer.obtainPosition("DT", True)
DraftDataObtainer.obtainPosition("LB", True)
DraftDataObtainer.obtain4_3LBs(True)
DraftDataObtainer.obtainDBs(True)
DraftDataObtainer.obtainBarChartData(True)
DraftDataObtainer.obtainBarChartData(False)
DraftDataObtainer.obtainBipartite(True)
DraftDataObtainer.obtainBipartite(False)
"""
