import unittest
from array import array
from main.GeneticAlgorithm import mutation

class TestCrossoverMethod(unittest.TestCase):
    def test_mutation_switches_only_desired_gene(self):
        #Arrange
        individual = array('b',[0]*10)
        mutationPoint = 5
        #Act
        mutation(individual,mutationPoint)
        #Assert
        self.assertEqual(1,individual[mutationPoint])
        for gene in range(mutationPoint):
            self.assertEqual(individual[gene],0)
        for gene in range(mutationPoint+1,len(individual)):
            self.assertEqual(individual[gene],0)
    def test_mutation_switches_from_zero_to_one(self):
        #Arrange
        individual = array('b',[0])
        mutationPoint = 0
        #Act
        mutation(individual,mutationPoint)
        #Assert
        self.assertEqual(1,individual[mutationPoint])
    def test_mutation_switches_from_one_to_zero(self):
        #Arrange
        individual = array('b',[1])
        mutationPoint = 0
        #Act
        mutation(individual,mutationPoint)
        #Assert
        self.assertEqual(0,individual[mutationPoint])
if __name__ == '__main__':
    unittest.main()