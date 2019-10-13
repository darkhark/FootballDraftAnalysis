class College:
    uniqueIDNumber = 0
    teamCache = []

    @classmethod
    def __getCachedTeam(cls, name):
        for team in College.teamCache:
            if team.name == name:
                return team
        return None

    def __new__(cls, name):
        team = cls.__getCachedTeam(name)
        if team:
            return team
        team = super(College, cls).__new__(cls)
        team.name = name
        team.uniqueID = "CG" + str(College.uniqueIDNumber)
        team.teamCache.append(team)
        College.uniqueIDNumber += 1
        return team

