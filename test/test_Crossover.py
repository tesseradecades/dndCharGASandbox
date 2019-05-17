import unittest
from array import array
from main.GeneticAlgorithm import crossover

class TestCrossoverMethod(unittest.TestCase):
    def test_genes_exchanged_up_to_crossover_point(self):
        #Arrange
        genomeLength = 199
        parent1 = array('b',[0]*genomeLength)
        parent2 = array('b',[1]*genomeLength)
        crossoverPoint = genomeLength // 2
        #Act
        children = crossover(parent1,parent2, crossoverPoint)
        #Assert
        child1 = children[0]
        child2 = children[1]
        for gene in range(crossoverPoint):
            self.assertEqual(parent1[gene],child1[gene])
            self.assertEqual(parent2[gene],child2[gene])
        for gene in range(crossoverPoint,genomeLength):
            self.assertEqual(parent1[gene],child2[gene])
            self.assertEqual(parent2[gene],child1[gene])
if __name__ == '__main__':
    unittest.main()