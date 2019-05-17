from array import array
from GeneticAlgorithm import GeneticAlgorithm
"""
This version of the Genetic Algorithm defines "convergence" as "reaching the
specified number of generations without a change in the maximum observed
fitness"
"""
class FitnessChange(GeneticAlgorithm):

    def __init__(self):
        super(FitnessChange,self).__init__()

    def selection(self,population:list, fitnessFunction)->tuple:
        fitnessDict = {}
        for individual in range(len(population)):
            fitnessDict[individual] = fitnessFunction(population[individual])
        fittest = self.getKeyOfMaxValue(fitnessDict)
        fittestScore = fitnessDict[fittest]
        fitnessDict.pop(fittest)
        secondFittest = self.getKeyOfMaxValue(fitnessDict)
        fitnessDict.pop(secondFittest)
        return (population[fittest],population[secondFittest], fittestScore)

    def run(self,genomeLength:int,targetGenerations:int,fitnessFunction)->array:
        generationsWithoutChange = 0
        population = self.generateInitialPopulation(genomeLength)
        parent1, parent2,fittestScore = self.selection(population, fitnessFunction)
        child1,child2 = self.crossoverHelper(parent1,parent2)
        self.mutationHelper(child1)
        self.mutationHelper(child2)
        population = [parent1,parent2,child1,child2]
        while(generationsWithoutChange < targetGenerations):
            print(f"Fitness:\t{fittestScore}")
            parent1, parent2, newFittestScore = self.selection(population, fitnessFunction)

            if(newFittestScore <= fittestScore):
                generationsWithoutChange+=1
            else:
                generationsWithoutChange = 0
            fittestScore = newFittestScore

            child1,child2 = self.crossoverHelper(parent1,parent2)
            self.mutationHelper(child1)
            self.mutationHelper(child2)
            population = [parent1,parent2,child1,child2]
        return parent1
def fitnessFunction(genome: array)-> float:
            f = 0
            for gene in genome:
                if(gene == 1):
                    f+=1
            return f
def main():
    genomeLength = 10
    ga = FitnessChange()
    best = ga.run(genomeLength,genomeLength*genomeLength,fitnessFunction)
    print(best)
if __name__ == '__main__':
    main()