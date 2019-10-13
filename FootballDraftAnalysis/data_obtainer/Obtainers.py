from printers.CSVPrinter import CSVPrinter
from scraper.NFLDataScraper import NFLPlayerScraper
from generators.ProFootballReferenceURLGenerator import ProFootballReferenceURLGenerator


class DraftDataObtainer:

    @staticmethod
    def obtain():
        print("Gathering URLs")
        urlList = ProFootballReferenceURLGenerator.createURLList()
        print("Scraping data from each URLs' HTML")
        scraper = NFLPlayerScraper(urlList)
        scraper.scrape()
        print("Printing data to CSVs")
        CSVPrinter.printEdgesCSVAndLabelsCSV(scraper.playerList, "../../printedCSVs/edgesCSV.csv",
                                             "../../printedCSVs/labelsCSV.csv")
        print("All done :)")


DraftDataObtainer.obtain()
