import unittest
from array import array
import main.GeneticAlgorithm as GeneticAlgorithm

class TestInitialPopulationMethod(unittest.TestCase):
    def test_initial_population_genome_length(self):
        #Arrange
        genomeLength = 199
        #Act
        initialPopulation = GeneticAlgorithm.generateInitialPopulation(genomeLength)
        #Assert
        actual =len(initialPopulation[0])
        self.assertEqual(genomeLength,actual)
    def test_initial_population_size_is_four(self):
        #Arrange
        genomeLength = 199
        #Act
        initialPopulation = GeneticAlgorithm.generateInitialPopulation(genomeLength)
        #Assert
        actual = len(initialPopulation)
        self.assertEqual(4,actual)
    def test_initial_population_has_same_size_genomes(self):
        #Arrange
        genomeLength = 199
        #Act
        initialPopulation = GeneticAlgorithm.generateInitialPopulation(genomeLength)
        #Assert
        self.assertGreater(len(initialPopulation),0)
        for individual in initialPopulation:
            actual =len(individual)
            self.assertEqual(genomeLength,actual)

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
        fittestTwo = GeneticAlgorithm.selection(population, fitnessFunction)
        #Assert
        self.assertSequenceEqual((fittest,secondFittest),fittestTwo)

class TestCrossoverMethod(unittest.TestCase):
    def test_genes_exchanged_up_to_crossover_point(self):
        #Arrange
        genomeLength = 199
        parent1 = array('b',[0]*genomeLength)
        parent2 = array('b',[1]*genomeLength)
        crossoverPoint = genomeLength // 2
        #Act
        children = GeneticAlgorithm.crossover(parent1,parent2, crossoverPoint)
        #Assert
        child1 = children[0]
        child2 = children[1]
        for gene in range(crossoverPoint):
            self.assertEqual(parent1[gene],child1[gene])
            self.assertEqual(parent2[gene],child2[gene])
        for gene in range(crossoverPoint,genomeLength):
            self.assertEqual(parent1[gene],child2[gene])
            self.assertEqual(parent2[gene],child1[gene])

class TestCrossoverMethod(unittest.TestCase):
    def test_mutation_switches_only_desired_gene(self):
        #Arrange
        individual = array('b',[0]*10)
        mutationPoint = 5
        #Act
        GeneticAlgorithm.mutation(individual,mutationPoint)
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
        GeneticAlgorithm.mutation(individual,mutationPoint)
        #Assert
        self.assertEqual(1,individual[mutationPoint])
    def test_mutation_switches_from_one_to_zero(self):
        #Arrange
        individual = array('b',[1])
        mutationPoint = 0
        #Act
        GeneticAlgorithm.mutation(individual,mutationPoint)
        #Assert
        self.assertEqual(0,individual[mutationPoint])
class TestConvergedMethod(unittest.TestCase):
    def test_returns_true_when_converged(self):
        #Arrange
        parents = (array('b',[0]*2),array('b',[0]*2))
        children = (array('b',[0]*2),array('b',[0]*2))
        #Act
        converged = GeneticAlgorithm.converged(parents,children)
        #Assert
        self.assertTrue(converged)
    def test_returns_false_when_not_converged(self):
        #Arrange
        parents = (array('b',[0]*2),array('b',[0]*2))
        children = (array('b',[1]*2),array('b',[1]*2))
        #Act
        converged = GeneticAlgorithm.converged(parents,children)
        #Assert
        self.assertFalse(converged)
class TestHammingDistanceComputation(unittest.TestCase):
    def test_returns_zero_on_same_arrays(self):
        #Arrange
        array1 = array('b',[0])
        array2 = array('b',[0])
        #Act
        hammingDistance = GeneticAlgorithm.computeHammingDistance(array1,array2)
        #Assert
        self.assertEqual(hammingDistance,0)
    def test_returns_n_on_opposite_arrays(self):
        #Arrange
        array1 = array('b',[0])
        array2 = array('b',[1])
        #Act
        hammingDistance = GeneticAlgorithm.computeHammingDistance(array1,array2)
        #Assert
        self.assertEqual(hammingDistance,1)
    def test_returns_one_on_near_same_arrays(self):
        #Arrange
        array1 = array('b',[0]*10)
        array2 = array('b',[0]*10)
        array2[0]=1
        #Act
        hammingDistance = GeneticAlgorithm.computeHammingDistance(array1,array2)
        #Assert
        self.assertEqual(hammingDistance,1)
if __name__ == '__main__':
    unittest.main()