from Races import Race

class Character():

    #Ability Scores
    strength_score = 0
    dexterity_score = 0
    constitution_score = 0
    intelligence_score = 0
    wisdom_score = 0
    charisma_score = 0

    race = None

    def __init__(self, race:Race.Race):
        self.race = race
    def __str__(self)->str:
        ret = f"Race:\t\t{self.race}\
            \nStrength:\t{self.strength_score}\
            \nDexterity:\t{self.dexterity_score}\
            \nConstitution:\t{self.constitution_score}\
            \n:Intelligence:\t{self.intelligence_score}\
            \nWisdom:\t\t{self.wisdom_score}\
            \nCharisma:\t{self.charisma_score}"
        return ret
def main():
    print(Character(Race.Race.BLACK_DRAGONBORN))

if __name__ == "__main__":
    main()