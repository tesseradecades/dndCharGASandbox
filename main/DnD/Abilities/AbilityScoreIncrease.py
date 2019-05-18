from .Abilities import Ability
from ..AbilityScores import AbilityScores
from ..Character import Character

class AbilityScoreIncrease(Ability):
    score = None
    increase = 0
    def __init__(self, score:AbilityScores, increase:int):
        super(AbilityScoreIncrease,self).__init__()
        self.score=score
        self.increase=increase
    def concreteEffect(self,character:Character):
        character.abilityScores[self.score]+=self.increase
    def __str__(self)->str:
        return f"Increase {self.score} by {self.increase}"
