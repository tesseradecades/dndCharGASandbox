from unittest import TestCase
from main.DnD.Abilities.Resistance import Resistance
from main.DnD.Character import Character
from main.DnD.DamageTypes import DamageTypes
class test_Resistance(TestCase):
    def test_concrete_change(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        resistance = Resistance(DamageTypes.POISON)
        #Act
        resistance.executeConcreteAbility(character)
        #Assert
        self.assertSetEqual(character.resistances,{DamageTypes.POISON})
    def test_abstract_change(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        expected = character.hitPoints * 2
        resistance = Resistance(DamageTypes.POISON)
        #Act
        resistance.executeAbstractAbility(character)
        #Assert
        self.assertEqual(character.hitPoints,expected)