import unittest
from main.GeneticAlgorithm import generateInitialPopulation

class TestInitialPopulationMethod(unittest.TestCase):
    def test_initial_population_genome_length(self):
        #Arrange
        genomeLength = 199
        #Act
        initialPopulation = generateInitialPopulation(genomeLength)
        #Assert
        actual =len(initialPopulation[0])
        self.assertEqual(genomeLength,actual)
    def test_initial_population_size_is_four(self):
        #Arrange
        genomeLength = 199
        #Act
        initialPopulation = generateInitialPopulation(genomeLength)
        #Assert
        actual = len(initialPopulation)
        self.assertEqual(4,actual)
    def test_initial_population_has_same_size_genomes(self):
        #Arrange
        genomeLength = 199
        #Act
        initialPopulation = generateInitialPopulation(genomeLength)
        #Assert
        self.assertGreater(len(initialPopulation),0)
        for individual in initialPopulation:
            actual =len(individual)
            self.assertEqual(genomeLength,actual)
    
if __name__ == '__main__':
    unittest.main()