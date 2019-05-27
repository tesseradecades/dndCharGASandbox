from unittest import TestCase
from main.DnD.Abilities.CombatTraining import DwarvenCombatTraining
from main.DnD.Character import Character
class test_DwarvenCombatTraining(TestCase):
    def test_proficiencies_get_added(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        combatTraining = DwarvenCombatTraining()
        #Act
        combatTraining.executeConcreteAbility(character)
        #Assert
        self.assertSetEqual(character.weaponProficiencies,combatTraining.getWeaponProficiencies())