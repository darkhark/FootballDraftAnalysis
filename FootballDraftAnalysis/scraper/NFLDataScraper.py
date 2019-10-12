# -- external libraries --
# requests allows us to access a web page and get it in html form
import requests
# BeautifulSoup is a great tool that assists in scraping html data
from bs4 import BeautifulSoup

# --Our code--
from generators.ProFootballReferenceURLGenerator import ProFootballReferenceURLGenerator as pfrGenerator
from nodes.Player import Player
from nodes.College import College
from nodes.NFLTeam import NFLTeam


class NFLPlayerScraper:
    _playerList = []

    def __init__(self, urlList):
        self.urlList = urlList

    def scrape(self):
        for url in self.urlList:
            html = requests.get(url).content
            soup = BeautifulSoup(html, "html.parser")
            table = soup.find("table", {"class": "sortable stats_table"})
            rowsInTable = table.findAll('tr')
            NFLPlayerScraper._categorizeDataAndCreatePlayerList(self, rowsInTable)

    def _categorizeDataAndCreatePlayerList(self, rows):
        for row in rows:
            playerData = []
            # td represents a cell in a row.
            cells = row.findAll("td")
            i = 0
            college = None
            nflTeam = None
            for cell in cells:
                if i <= 5 or i == 9 or i == 10:
                    playerInfo = cell.text
                    # checks if the string is not empty, i.e contains data
                    playerData.append(cell.text)
                elif i == 6:
                    nflTeamName = cell.text
                    if nflTeamName != "":
                        nflTeam = NFLTeam(nflTeamName)
                elif i == 29:
                    collegeName = cell.text
                    if collegeName != "":
                        college = College(collegeName)
                i += 1
            if college is not None and nflTeam is not None:
                player = Player(playerData, college.uniqueID, nflTeam.uniqueID)
                self._playerList.append(player)

