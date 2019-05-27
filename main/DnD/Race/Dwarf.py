from array import array

from DnD.Abilities.AbilityScoreIncrease import AbilityScoreIncrease
from DnD.Abilities.Darkvision import Darkvision
from DnD.Abilities.Speed import Speed
from DnD.Phenotype import AbilityScores
class Dwarf():
    def getAbilities(self)->set:
        return {
            AbilityScoreIncrease(array('b',[AbilityScores.CONSTITUTION,AbilityScores.CONSTITUTION])),
            Speed(25),
            Darkvision()
            }
class HillDwarf(Dwarf):
    def __init__(self):
        super(HillDwarf,self).__init__()
    def __str__(self)->str:
        return "Hill Dwarf"
    