from array import array
from GeneticAlgorithm import GeneticAlgorithm
"""
This version of the Genetic Algorithm defines "convergence" as "reaching the
specified count of generations"
"""
class TargetGenerations(GeneticAlgorithm):
    def __init__(self):
        super(TargetGenerations,self).__init__()
    def run(self,genomeLength:int,targetGenerations:int,fitnessFunction)->array:
        generation = 1
        population = self.generateInitialPopulation(genomeLength)
        parent1, parent2 = self.selection(population, fitnessFunction)
        child1,child2 = self.crossoverHelper(parent1,parent2)
        self.mutationHelper(child1)
        self.mutationHelper(child2)
        population = [parent1,parent2,child1,child2]
        while(generation < targetGenerations):
            #print(f"Generation:\t{generation}")
            generation+=1
            parent1, parent2 = self.selection(population, fitnessFunction)
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
    ga = TargetGenerations()
    best = ga.run(10,35,fitnessFunction)
    print(best)
if __name__ == '__main__':
    main()