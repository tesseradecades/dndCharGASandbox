import unittest
from main.DnD.AbilityScores import AbilityScores
from main.DnD.Backgrounds.Background import Background
from main.DnD.Character import Character
from main.DnD.Races.Human import Human
class TestHumanAbilityAssignment(unittest.TestCase):
    def test_character_has_human_traits(self):
        #Arrange
        #Act
        character = Character(Human(),Background())
        #Assert
        self.assertIs(character.speed,30)
        self.assertIs(character.abilityScores[AbilityScores.STRENGTH],1)
        self.assertIs(character.abilityScores[AbilityScores.DEXTERITY],1)
        self.assertIs(character.abilityScores[AbilityScores.CONSTITUTION],1)
        self.assertIs(character.abilityScores[AbilityScores.INTELLIGENCE],1)
        self.assertIs(character.abilityScores[AbilityScores.WISDOM],1)
        self.assertIs(character.abilityScores[AbilityScores.CHARISMA],1)

if __name__ == '__main__':
    unittest.main()