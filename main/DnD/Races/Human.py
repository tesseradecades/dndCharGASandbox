from .Race import Race
from ..AbilityScores import AbilityScores
from ..Abilities.AbilityScoreIncrease import AbilityScoreIncrease
from ..Abilities.Speed import Speed
class Human(Race):
    def __init__(self):
        super(Human,self).__init__()
        
    def getAbilities(self)->set:
        abilities = {
            AbilityScoreIncrease(AbilityScores.STRENGTH,1),
            AbilityScoreIncrease(AbilityScores.DEXTERITY,1),
            AbilityScoreIncrease(AbilityScores.CONSTITUTION,1),
            AbilityScoreIncrease(AbilityScores.INTELLIGENCE,1),
            AbilityScoreIncrease(AbilityScores.WISDOM,1),
            AbilityScoreIncrease(AbilityScores.CHARISMA,1),
            Speed(30)
            }
        return abilities
    def __str__(self):
        return "Human"