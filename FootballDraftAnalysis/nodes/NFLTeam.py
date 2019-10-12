# Node is in parenthesis so that it can inherit the abstract class and all of its methods.
class NFLTeam:
    # This is a static variable. The same value exists for every instance of this class.
    uniqueIDNumber = 0
    teamCache = []

    @classmethod
    def __getCachedTeam(cls, name):
        for team in NFLTeam.teamCache:
            if team.name == name:
                return team
        return None

    # This is the constructor for the class. The constructor is called anytime we need this object.
    def __new__(cls, name):
        # This is how python creates local variables that can used in other method of the class.
        team = cls.__getCachedTeam(name)
        if team:
            return team
        team = super(NFLTeam, cls).__new__(cls)
        return team

    def __init__(self, name):
        if self in self.teamCache:
            return
        self.teamCache.append(self)
        self.uniqueID = "NFL" + str(NFLTeam.uniqueIDNumber)
        self.name = name
        # This increases the static variable by 1. Doing this will make each ID different, even though it looks
        # like every object will have an ID of PL0.
        NFLTeam.uniqueIDNumber += 1

