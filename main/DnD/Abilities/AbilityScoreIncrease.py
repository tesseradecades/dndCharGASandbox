from array import array
try:
    from Dnd.Abilities.Ability import Ability
except ModuleNotFoundError:
    from main.DnD.Abilities.Ability import Ability

from ..Character import Character
from ..Phenotype import AbilityScores
class AbilityScoreIncrease(Ability):


    def __init__(self, increases:array):
        super(AbilityScoreIncrease,self).__init__()
        self.increases = {
            AbilityScores.STRENGTH : 0,
            AbilityScores.DEXTERITY : 0,
            AbilityScores.CONSTITUTION : 0,
            AbilityScores.INTELLIGENCE : 0,
            AbilityScores.WISDOM : 0,
            AbilityScores.CHARISMA : 0
        }
        for increase in increases:
            self.increases[increase]+=1
    def executeConcreteAbility(self, character:Character):
        for increase in self.increases.keys():
            character.abilityScores[increase]+=self.increases[increase]
            if(character.abilityScores[increase] > 20):
                character.abilityScores[increase] = 20