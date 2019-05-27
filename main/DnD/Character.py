class Character():
    def __init__(self, baseStats:dict, abilities:set, level:int=1):
        self.abilityScores = baseStats
        self.abilities = abilities
        self.level = level
        self.armorClass = 0
        self.speed = 0
        self.flightSpeed = 0
        self.senses=dict()
        self.resistances=set()
        self.hitPoints = 0
        self.weaponProficiencies = set()