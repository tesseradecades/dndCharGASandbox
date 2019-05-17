import unittest
from array import array
from main.GeneticAlgorithm import selection

class TestSelectionMethod(unittest.TestCase):
    def test_chooses_fittest_individuals(self):
        #Arrange
        genomeLength = 199
        fittest = array('b',[0]*genomeLength)
        secondFittest = array('b',[0]*genomeLength)
        secondFittest[0] = 1
        population = [fittest, secondFittest, [1]*genomeLength, [1]*genomeLength]
        #Define fitness as having more 0's in the genome
        def fitnessFunction(genome: array)-> float:
            f = 0
            for gene in genome:
                if(gene == 0):
                    f+=1
            return f
        #Act
        fittestTwo = selection(population, fitnessFunction)
        #Assert
        self.assertSequenceEqual((fittest,secondFittest),fittestTwo)
if __name__ == '__main__':
    unittest.main()