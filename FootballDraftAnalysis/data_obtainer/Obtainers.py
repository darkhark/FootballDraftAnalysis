from printers.CSVPrinter import CSVPrinter
from scraper.NFLDataScraper import NFLPlayerScraper
from generators.ProFootballReferenceURLGenerator import ProFootballReferenceURLGenerator


class DraftDataObtainer:

    @staticmethod
    def obtainAllPlayers():
        print("Gathering URLs")
        urlList = ProFootballReferenceURLGenerator.createURLList()
        scraper = NFLPlayerScraper(urlList)
        if len(scraper.playerList) == 0:
            print("Scraping data from each URL's HTML")
            scraper.scrape()
        print("Printing data to CSVs")
        CSVPrinter.printAllEdgesCSVAndLabelsCSV(scraper.playerList, "../../printedCSVs/edgesCSV.csv",
                                                "../../printedCSVs/labelsCSV.csv")
        print("All done :)")

    @staticmethod
    def obtainAwardedPlayers():
        print("Gathering URLs")
        urlList = ProFootballReferenceURLGenerator.createURLList()
        scraper = NFLPlayerScraper(urlList)
        if len(scraper.playerList) == 0:
            print("Scraping data from each URL's HTML")
            scraper.scrape()
        print("Printing data to CSVs")
        CSVPrinter.printAwardedEdgesCSVAndLabelsCSV(scraper.playerList, "../../printedCSVs/awardedEdgesCSV.csv",
                                                    "../../printedCSVs/awardedLabelsCSV.csv")
        print("All done :)")

    @staticmethod
    def obtainRoundsRange(minimum, maximum):
        print("Gathering URLs")
        urlList = ProFootballReferenceURLGenerator.createURLList()
        scraper = NFLPlayerScraper(urlList)
        if len(scraper.playerList) == 0:
            print("Scraping data from each URL's HTML")
            scraper.scrape()
        print("Printing data to CSVs")
        edgesCSVName = "../../printedCSVs/rounds" + str(minimum) + "To" + str(maximum) + "EdgesCSV.csv"
        labelsCSV = "../../printedCSVs/rounds" + str(minimum) + "To" + str(maximum) + "LabelsCSV.csv"
        CSVPrinter.printRoundRangeEdgesAndLabelsCSVs(scraper.playerList, edgesCSVName, labelsCSV, minimum, maximum)
        print("All done :)")

    @staticmethod
    def obtainPosition(position):
        print("Gathering URLs")
        urlList = ProFootballReferenceURLGenerator.createURLList()
        scraper = NFLPlayerScraper(urlList)
        if len(scraper.playerList) == 0:
            print("Scraping data from each URL's HTML")
            scraper.scrape()
        print("Printing data to CSVs")
        edgesCSVName = "../../printedCSVs/position" + position + "EdgesCSV.csv"
        labelsCSV = "../../printedCSVs/position" + position + "LabelsCSV.csv"
        CSVPrinter.printPositionEdgesAndLabelsCSVs(scraper.playerList, edgesCSVName, labelsCSV, position)
        print("All done :)")


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
