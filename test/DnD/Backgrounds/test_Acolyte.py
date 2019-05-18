import unittest
from main.DnD.Backgrounds.Acolyte import Acolyte
from main.DnD.Character import Character
from main.DnD.Races.Race import Race
from main.DnD.Skills import Skills
class TestAcolyteSkillAssignment(unittest.TestCase):
    def test_character_should_be_proficient_in_insight_and_religion(self):
        #Act
        character = Character(Race(),Acolyte())
        #Assert
        self.assertIn(Skills.Insight, character.skillProficiencies)
        self.assertIn(Skills.Religion, character.skillProficiencies)
if __name__ == '__main__':
    unittest.main()