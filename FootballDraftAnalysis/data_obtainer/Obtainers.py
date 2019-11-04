from printers.CSVPrinter import CSVPrinter
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
    def obtainRoundsRange(minimum, maximum):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing Rounds " + str(minimum) + "-" + str(maximum) + " Player Data to CSVs.")
        edgesCSV = DraftDataObtainer.baseCSVDirectory + "rounds" + str(minimum) + "To" + str(maximum) + "EdgesCSV.csv"
        labelsCSV = DraftDataObtainer.baseCSVDirectory + "rounds" + str(minimum) + "To" + str(maximum) + "LabelsCSV.csv"
        CSVPrinter.printRoundRangeEdgesAndLabelsCSVs(DraftDataObtainer.scraper.playerList, edgesCSV,
                                                     labelsCSV, minimum, maximum)
        print(DraftDataObtainer.finishedMessage)

    @staticmethod
    def obtainPosition(position):
        if len(DraftDataObtainer.urlList) == 0:
            print(DraftDataObtainer.gatherURL)
            DraftDataObtainer.urlList = ProFootballReferenceURLGenerator.createURLList()
        if DraftDataObtainer.scraper is None:
            DraftDataObtainer.scraper = NFLPlayerScraper(DraftDataObtainer.urlList)
        if len(DraftDataObtainer.scraper.playerList) == 0:
            print(DraftDataObtainer.scraping)
            DraftDataObtainer.scraper.scrape()
        print("Printing " + position + " Player Data to CSVs.")
        edgesCSV = DraftDataObtainer.baseCSVDirectory + "position" + position + "EdgesCSV.csv"
        labelsCSV = DraftDataObtainer.baseCSVDirectory + "position" + position + "LabelsCSV.csv"
        CSVPrinter.printPositionEdgesAndLabelsCSVs(DraftDataObtainer.scraper.playerList, edgesCSV,
                                                   labelsCSV, position)
        print(DraftDataObtainer.finishedMessage)


DraftDataObtainer.obtainAllPlayers()
DraftDataObtainer.obtainAwardedPlayers()
DraftDataObtainer.obtainRoundsRange(1, 3)
DraftDataObtainer.obtainRoundsRange(4, 7)
DraftDataObtainer.obtainRoundsRange(1, 2)
DraftDataObtainer.obtainRoundsRange(3, 4)
DraftDataObtainer.obtainRoundsRange(5, 7)
DraftDataObtainer.obtainPosition("QB")
DraftDataObtainer.obtainPosition("RB")
DraftDataObtainer.obtainPosition("DE")
DraftDataObtainer.obtainPosition("LB")
