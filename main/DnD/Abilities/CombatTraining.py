try:
    from Dnd.Abilities.Ability import Ability
    from DnD.Character import Character
    from DnD.Weapons import Weapons
except ModuleNotFoundError:
    from main.DnD.Abilities.Ability import Ability
    from main.DnD.Character import Character
    from main.DnD.Weapons import Weapons

class CombatTraining(Ability):
    def __init__(self):
        super(CombatTraining,self).__init__()
    def getWeaponProficiencies(self)->set:
        return set()
    def executeConcreteAbility(self, character:Character):
        character.weaponProficiencies |= self.getWeaponProficiencies()
class DwarvenCombatTraining(CombatTraining):
    def __init__(self):
        super(DwarvenCombatTraining,self).__init__()
    def getWeaponProficiencies(self)->set:
        return {Weapons.BATTLEAXE, Weapons.HANDAXE, Weapons.LIGHTHAMMER, Weapons.WARHAMMER}