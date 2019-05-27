import unittest
import main.DnD.Phenotype as p

from array import array

class TestGetStats(unittest.TestCase):
    def test_no_stats_over_18(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[1]*p.GENOME_LENGTH),1)
        #Act
        stats = phenotype.getStats(array('b',[1]*p.ABILITY_SCORE_GENOME_LENGTH))
        #Assert
        for stat in p.AbilityScores:
            self.assertLessEqual(stats[stat],18)
        
    def test_No_Stats_Under_8(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        #Act
        stats = phenotype.getStats(array('b',[0]*p.ABILITY_SCORE_GENOME_LENGTH))
        #Assert
        for stat in p.AbilityScores:
            self.assertGreaterEqual(stats[stat],8)
    def test_No_Misassigned_Stats(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        str_of_18 = [0]*5*19
        con_of_14 = [1,1,0,0,0]*7
        int_of_9 = [1,1,1,0,0]
        #Act
        stats = phenotype.getStats(array('b',str_of_18+con_of_14+int_of_9))
        #Assert
        self.assertEqual(stats[p.AbilityScores.STRENGTH],18)
        self.assertEqual(stats[p.AbilityScores.DEXTERITY],8)
        self.assertEqual(stats[p.AbilityScores.CONSTITUTION],14)
        self.assertEqual(stats[p.AbilityScores.INTELLIGENCE],9)
        self.assertEqual(stats[p.AbilityScores.WISDOM],8)
        self.assertEqual(stats[p.AbilityScores.CHARISMA],8)
class TestGetClass(unittest.TestCase):
    def test_gets_appropriate_class_from_all_0(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        #Act
        characterClass = phenotype.getClass(array('b',[0]*p.CLASSES_GENOME_LENGTH))
        #Assert
        self.assertEqual(characterClass,p.CLASSES[0])
    def test_gets_appropriate_class_from_all_1(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        #Act
        characterClass = phenotype.getClass(array('b',[1]*p.CLASSES_GENOME_LENGTH))
        #Assert
        self.assertEqual(characterClass,p.CLASSES[p.CLASSES_GENOME_LENGTH])
class TestGetRace(unittest.TestCase):
    def test_gets_appropriate_race_from_all_0(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        #Act
        race = phenotype.getRace(array('b',[0]*p.RACES_GENOME_LENGTH))
        #Assert
        self.assertEqual(race,p.RACES[0])
    def test_gets_appropriate_race_from_all_1(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        #Act
        race = phenotype.getRace(array('b',[1]*p.RACES_GENOME_LENGTH))
        #Assert
        self.assertEqual(race,p.RACES[p.RACES_GENOME_LENGTH])
class TestGetBackground(unittest.TestCase):
    def test_gets_appropriate_background_from_all_0(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        #Act
        background = phenotype.getBackground(array('b',[0]*p.BACKGROUNDS_GENOME_LENGTH))
        #Assert
        self.assertEqual(background,p.BACKGROUNDS[0])
    def test_gets_appropriate_background_from_all_1(self):
        #Arrange
        phenotype = p.Phenotype(array('b',[0]*p.GENOME_LENGTH),1)
        #Act
        background = phenotype.getBackground(array('b',[1]*p.BACKGROUNDS_GENOME_LENGTH))
        #Assert
        self.assertEqual(background,p.BACKGROUNDS[p.BACKGROUNDS_GENOME_LENGTH])
class TestGetFeats(unittest.TestCase):
    def test_gets_appropriate_feats_from_all_0(self):
        #Arrange
        #Act
        #Assert
        self.assertTrue(False)
    def test_gets_appropriate_feats_from_all_1(self):
        #Arrange
        #Act
        #Assert
        self.assertTrue(False)