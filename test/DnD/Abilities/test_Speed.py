from unittest import TestCase
from main.DnD.Abilities.Speed import FlightSpeed, Speed 
from main.DnD.Character import Character
class test_Speed(TestCase):
    def test_speed_assigned(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        speed = Speed(30)
        #Act
        speed.executeConcreteAbility(character)
        #Assert
        self.assertEqual(character.speed,30)
    def test_flight_speed_assigned(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        speed = FlightSpeed(30)
        #Act
        speed.executeConcreteAbility(character)
        #Assert
        self.assertEqual(character.flightSpeed,30)
    def test_flight_speed_abstract(self):
        #Arrange
        baseStats = {}
        character = Character(baseStats, set())
        speed = FlightSpeed(30)
        #Act
        speed.executeAbstractAbility(character)
        #Assert
        self.assertEqual(character.armorClass,2)