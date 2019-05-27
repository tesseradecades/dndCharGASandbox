from unittest import TestCase
from main.DnD.Abilities.Darkvision import Darkvision, SuperiorDarkvision
from main.DnD.Character import Character
class test_Darkvision(TestCase):
    def test_darkvision_assignment(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        darkvision = Darkvision()
        #Act
        darkvision.executeConcreteAbility(character)
        #Assert
        self.assertEqual(character.senses["Darkvision"],60)
    def test_superior_darkvision_assignment(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        darkvision = SuperiorDarkvision()
        #Act
        darkvision.executeConcreteAbility(character)
        #Assert
        self.assertEqual(character.senses["Darkvision"],120)