from array import array
from unittest import TestCase

from main.DnD.Abilities.AbilityScoreIncrease import AbilityScoreIncrease
from main.DnD.Character import Character
from main.DnD.Phenotype import AbilityScores
class test_AbilityScoreIncrease(TestCase):
    def test_score_increase(self):
        #Arrange
        baseStats = {
            AbilityScores.STRENGTH:12,
            AbilityScores.DEXTERITY:12,
            AbilityScores.CONSTITUTION:12,
            AbilityScores.INTELLIGENCE:13,
            AbilityScores.WISDOM:13,
            AbilityScores.CHARISMA:13
            }
        character = Character(baseStats, set())
        asi = AbilityScoreIncrease(array('b',[AbilityScores.STRENGTH]))
        #Act
        asi.executeConcreteAbility(character)
        #Assert
        self.assertEqual(character.abilityScores[AbilityScores.STRENGTH],13)
        self.assertEqual(character.abilityScores[AbilityScores.DEXTERITY],12)
        self.assertEqual(character.abilityScores[AbilityScores.CONSTITUTION],12)
        self.assertEqual(character.abilityScores[AbilityScores.INTELLIGENCE],13)
        self.assertEqual(character.abilityScores[AbilityScores.WISDOM],13)
        self.assertEqual(character.abilityScores[AbilityScores.CHARISMA],13)
    def test_multiple_score_increase(self):
        #Arrange
        baseStats = {
            AbilityScores.STRENGTH:12,
            AbilityScores.DEXTERITY:12,
            AbilityScores.CONSTITUTION:12,
            AbilityScores.INTELLIGENCE:13,
            AbilityScores.WISDOM:13,
            AbilityScores.CHARISMA:13
            }
        character = Character(baseStats, set())
        asi = AbilityScoreIncrease(array('b',[AbilityScores.STRENGTH, AbilityScores.DEXTERITY]))
        #Act
        asi.executeConcreteAbility(character)
        #Assert
        self.assertEqual(character.abilityScores[AbilityScores.STRENGTH],13)
        self.assertEqual(character.abilityScores[AbilityScores.DEXTERITY],13)
        self.assertEqual(character.abilityScores[AbilityScores.CONSTITUTION],12)
        self.assertEqual(character.abilityScores[AbilityScores.INTELLIGENCE],13)
        self.assertEqual(character.abilityScores[AbilityScores.WISDOM],13)
        self.assertEqual(character.abilityScores[AbilityScores.CHARISMA],13)
    def test_multiples_of_same_score_increase(self):
        #Arrange
        baseStats = {
            AbilityScores.STRENGTH:12,
            AbilityScores.DEXTERITY:12,
            AbilityScores.CONSTITUTION:12,
            AbilityScores.INTELLIGENCE:13,
            AbilityScores.WISDOM:13,
            AbilityScores.CHARISMA:13
            }
        character = Character(baseStats, set())
        asi = AbilityScoreIncrease(array('b',[AbilityScores.STRENGTH,AbilityScores.STRENGTH]))
        #Act
        asi.executeConcreteAbility(character)
        #Assert
        self.assertEqual(character.abilityScores[AbilityScores.STRENGTH],14)
        self.assertEqual(character.abilityScores[AbilityScores.DEXTERITY],12)
        self.assertEqual(character.abilityScores[AbilityScores.CONSTITUTION],12)
        self.assertEqual(character.abilityScores[AbilityScores.INTELLIGENCE],13)
        self.assertEqual(character.abilityScores[AbilityScores.WISDOM],13)
        self.assertEqual(character.abilityScores[AbilityScores.CHARISMA],13)