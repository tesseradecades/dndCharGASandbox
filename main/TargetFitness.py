from array import array
from GeneticAlgorithm import GeneticAlgorithm
"""
This version of the Genetic Algorithm defines "convergence" as "reaching the
specified level of fitness"
"""
class TargetFitness(GeneticAlgorithm):

    def __init__(self):
        super(TargetFitness,self).__init__()

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

    def run(self,genomeLength:int,targetFitness:float,fitnessFunction)->array:
        generation = 1
        population = self.generateInitialPopulation(genomeLength)
        parent1, parent2,fittestScore = self.selection(population, fitnessFunction)
        child1,child2 = self.crossoverHelper(parent1,parent2)
        self.mutationHelper(child1)
        self.mutationHelper(child2)
        population = [parent1,parent2,child1,child2]
        while(fittestScore < targetFitness):
            print(f"Fitness:\t{fittestScore}")
            generation+=1
            parent1, parent2, fittestScore = self.selection(population, fitnessFunction)
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
    ga = TargetFitness()
    best = ga.run(10,10,fitnessFunction)
    print(best)
if __name__ == '__main__':
    main()