class NFLTeam(object):
    uniqueIDNumber = 0
    teamCache = []

    @classmethod
    def __getCachedTeam(cls, name):
        for team in NFLTeam.teamCache:
            if team.name == name:
                return team
        return None

    @staticmethod
    def getCachedTeam(teamID):
        for team in NFLTeam.teamCache:
            if team.uniqueID == teamID:
                return team
        return None

    def __new__(cls, name):
        team = cls.__getCachedTeam(name)
        if team:
            return team
        team = super(NFLTeam, cls).__new__(cls)
        team.name = name
        team.uniqueID = "NFL" + str(NFLTeam.uniqueIDNumber)
        team.teamCache.append(team)
        NFLTeam.uniqueIDNumber += 1
        return team

