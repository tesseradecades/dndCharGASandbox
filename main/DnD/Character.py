class Character():
    def __init__(self, baseStats:dict, abilities:set):
        self.abilityScores = baseStats
        self.abilities = abilities
        self.armorClass = 0
        self.speed = 0
        self.flightSpeed = 0
        self.senses=dict()