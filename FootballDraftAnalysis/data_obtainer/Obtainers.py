from printers.CSVPrinter import CSVPrinter
from scraper.NFLDataScraper import NFLPlayerScraper
from generators.ProFootballReferenceURLGenerator import ProFootballReferenceURLGenerator


class DraftDataObtainer:

    @staticmethod
    def obtainAllPlayers():
        print("Gathering URLs")
        urlList = ProFootballReferenceURLGenerator.createURLList()
        print("Scraping data from each URL's HTML")
        scraper = NFLPlayerScraper(urlList)
        scraper.scrape()
        print("Printing data to CSVs")
        CSVPrinter.printAllEdgesCSVAndLabelsCSV(scraper.playerList, "../../printedCSVs/edgesCSV.csv",
                                                "../../printedCSVs/labelsCSV.csv")
        print("All done :)")

    @staticmethod
    def obtainAwardedPlayers():
        print("Gathering URLs")
        urlList = ProFootballReferenceURLGenerator.createURLList()
        print("Scraping data from each URL's HTML")
        scraper = NFLPlayerScraper(urlList)
        scraper.scrape()
        print("Printing data to CSVs")
        CSVPrinter.printAwardedEdgesCSVAndLabelsCSV(scraper.playerList, "../../printedCSVs/awardedEdgesCSV.csv",
                                                    "../../printedCSVs/awardedLabelsCSV.csv")
        print("All done :)")


DraftDataObtainer.obtainAllPlayers()
DraftDataObtainer.obtainAwardedPlayers()
