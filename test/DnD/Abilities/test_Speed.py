import unittest
from main.DnD.Abilities.Speed import Speed
from main.DnD.Backgrounds.Background import Background
from main.DnD.Character import Character
from main.DnD.Races.Race import Race

class TestConcreteMethod(unittest.TestCase):
    def test_ability_score_increases(self):
        #Arrange
        speed = Speed(30)
        character = Character(Race(),Background())
        #Act
        speed.concreteEffect(character)
        #Assert
        self.assertIs(character.speed,30)

if __name__ == '__main__':
    unittest.main()