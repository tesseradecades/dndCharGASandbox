try:
    from Dnd.Abilities.Ability import Ability
    from DnD.Character import Character
    from DnD.DamageTypes import DamageTypes
except ModuleNotFoundError:
    from main.DnD.Abilities.Ability import Ability
    from main.DnD.Character import Character
    from main.DnD.DamageTypes import DamageTypes

class Resistance(Ability):
    def __init__(self,damageType:int):
        super(Resistance,self).__init__()
        self.damageType = damageType
    def executeAbstractAbility(self,character:Character):
        level = character.level
        if(level < 5):
            character.hitPoints = character.hitPoints*2
        elif(level < 11):
            character.hitPoints = character.hitPoints*1.5
        elif(level < 17):
            character.hitPoints = character.hitPoints*1.25
    def executeConcreteAbility(self,character:Character):
        character.resistances.add(self.damageType)
    def __str__(self)->str:
        return f"{str(self.damageType)} Resistance"
class PoisonResistance(Resistance):
    def __init__(self):
        super(PoisonResistance,self).__init__(DamageTypes.POISON)