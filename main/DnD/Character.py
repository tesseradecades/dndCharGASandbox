class Character():
    def __init__(self, baseStats:dict, abilities:set):
        self.abilityScores = baseStats
        self.abilities = abilities