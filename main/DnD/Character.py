from AbilityScores import AbilityScores
from Races import Race

class Character():

    #Ability Scores
    abilityScores = {
        AbilityScores.STRENGTH:0,
        AbilityScores.DEXTERITY:0,
        AbilityScores.CONSTITUTION:0,
        AbilityScores.INTELLIGENCE:0,
        AbilityScores.WISDOM:0,
        AbilityScores.CHARISMA:0
    }

    race = None

    def __init__(self, race):
        self.race = race
    def __str__(self)->str:
        ret = f"Race:\t\t{self.race}\
            \nStrength:\t{self.abilityScores[AbilityScores.STRENGTH]}\
            \nDexterity:\t{self.abilityScores[AbilityScores.DEXTERITY]}\
            \nConstitution:\t{self.abilityScores[AbilityScores.CONSTITUTION]}\
            \n:Intelligence:\t{self.abilityScores[AbilityScores.INTELLIGENCE]}\
            \nWisdom:\t\t{self.abilityScores[AbilityScores.WISDOM]}\
            \nCharisma:\t{self.abilityScores[AbilityScores.CHARISMA]}"
        return ret
def main():
    print(Character(Race.RACES[0]))

if __name__ == "__main__":
    main()