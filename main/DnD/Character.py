from .AbilityScores import AbilityScores
from .Backgrounds import Background
from .Races import Race


class Character():

    #Ability Scores
    abilityScores = {}

    race = None

    speed = 0

    background = None

    skillProficiencies = set()

    def __init__(self, race: Race,background:Background):
        self.abilityScores = {
            AbilityScores.STRENGTH:0,
            AbilityScores.DEXTERITY:0,
            AbilityScores.CONSTITUTION:0,
            AbilityScores.INTELLIGENCE:0,
            AbilityScores.WISDOM:0,
            AbilityScores.CHARISMA:0
        }
        self.skillProficiencies = set()
        self.race = race
        for ability in self.race.getAbilities():
            ability.concreteEffect(self)
        self.background = background
        for proficiency in background.getSkillProficiencies():
            self.skillProficiencies.add(proficiency)
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
    from .Backgrounds.Acolyte import Acolyte
    from.Races.Human import Human
    print(Character(Human(),Acolyte()))

if __name__ == "__main__":
    main()