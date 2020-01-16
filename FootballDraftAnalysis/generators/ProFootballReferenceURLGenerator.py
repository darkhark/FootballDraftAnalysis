# This library helps us retrieve a web page in html format
import requests

# This library makes it easier to dissect html and retrieve the strings between
# the tags.
from bs4 import BeautifulSoup


class ProFootballReferenceURLGenerator:

    # This function will create a list of all 134 pages of player tables
    def __init__(self):
        pass

    @staticmethod
    def allTimeURLList():
        print("URL Printer Activated")
        fullURLList = []
        initialURL = "https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min=1936" \
                     "&year_max=2019&draft_slot_min=1&draft_slot_max=500&pick_type=overall&pos%5B%5D=qb&pos%5B%5D=" \
                     "rb&pos%5B%5D=wr&pos%5B%5D=te&pos%5B%5D=e&pos%5B%5D=t&pos%5B%5D=g&pos%5B%5D=c&pos%5B%5D=o" \
                     "l&pos%5B%5D=dt&pos%5B%5D=de&pos%5B%5D=dl&pos%5B%5D=ilb&pos%5B%5D=olb&pos%5B%5D=lb&pos%5B%5D=" \
                     "cb&pos%5B%5D=s&pos%5B%5D=db&pos%5B%5D=k&pos%5B%5D=p&conference=any&show=all&order_by=default"

        fullURLList.append(initialURL)
        additionalPlayersURL = "&offset="
        # Increment the page number by 300 starting from 300 until 25800 is reached
        for pageNum in range(300, 25801, 300):
            fullURL = initialURL + additionalPlayersURL + str(pageNum)
            fullURLList.append(fullURL)
        return fullURLList

    @staticmethod
    def createURLList():
        fullURLList = []
        initialURL = "https://www.pro-football-reference.com/play-index/draft-finder.cgi?request=1&year_min" + \
                     "=1936&year_max=2019&draft_slot_min=1&draft_slot_max=500&pick_type=overall&pos%5B%5D=qb&" + \
                     "pos%5B%5D=rb&pos%5B%5D=wr&pos%5B%5D=te&pos%5B%5D=t&pos%5B%5D=g&pos%5B%5D=c&pos%5B%5D=ol" + \
                     "&pos%5B%5D=dt&pos%5B%5D=de&pos%5B%5D=dl&pos%5B%5D=ilb&pos%5B%5D=olb&pos%5B%5D=lb&pos%5B" + \
                     "%5D=cb&pos%5B%5D=s&pos%5B%5D=db&pos%5B%5D=k&pos%5B%5D=p&conference=any&show=all&order_b" + \
                     "y=default"

        fullURLList.append(initialURL)
        additionalPlayersURL = "&offset="
        # Increment the page number by 300 starting from 300 until 134 is reached
        for pageNum in range(300, 13500, 300):
            fullURL = initialURL + additionalPlayersURL + str(pageNum)
            fullURLList.append(fullURL)
        return fullURLList

