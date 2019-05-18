import unittest
from main.DnD.AbilityScores import AbilityScores
from main.DnD.Abilities.AbilityScoreIncrease import AbilityScoreIncrease
from main.DnD.Backgrounds.Background import Background
from main.DnD.Character import Character
from main.DnD.Races.Race import Race

class TestConcreteMethod(unittest.TestCase):
    def test_ability_score_increases(self):
        #Arrange
        asi = AbilityScoreIncrease(AbilityScores.STRENGTH,2)
        character = Character(Race(),Background())
        initialStrength = character.abilityScores[AbilityScores.STRENGTH]
        #Act
        asi.concreteEffect(character)
        #Assert
        self.assertEqual(initialStrength+2,character.abilityScores[AbilityScores.STRENGTH])

if __name__ == '__main__':
    unittest.main()