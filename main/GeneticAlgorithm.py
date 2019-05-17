import operator
import random
from array import array
from copy import deepcopy

class GeneticAlgorithm():
    #Initial Population
    def generateInitialPopulation(self,genomeLength:int)->list:
        if(genomeLength < 2):
            raise Exception("Genome too short")
        initialPopulation = []
        for i in range(4):
            initialPopulation.append(array('b',[0]*genomeLength))
        return initialPopulation
    #Selection
    def selection(self,population:list, fitnessFunction)->tuple:
        fitnessDict = {}
        for individual in range(len(population)):
            fitnessDict[individual] = fitnessFunction(population[individual])
        fittest = self.getKeyOfMaxValue(fitnessDict)
        fitnessDict.pop(fittest)
        secondFittest = self.getKeyOfMaxValue(fitnessDict)
        fitnessDict.pop(secondFittest)
        return (population[fittest],population[secondFittest])

    def getKeyOfMaxValue(self,d:dict)->object:
        return max(d.items(), key=operator.itemgetter(1))[0]
    #Crossover
    def crossoverHelper(self,parent1:array, parent2:array)->tuple:
        return self.crossover(parent1,parent2,random.randint(0,len(parent1)-1))

    def crossover(self,parent1:array, parent2:array, crossoverPoint: int)->tuple:
        return (parent1[:crossoverPoint]+parent2[crossoverPoint:],parent2[:crossoverPoint]+parent1[crossoverPoint:])
    #Mutation
    def mutationHelper(self,individual:array):
        self.mutation(individual, random.randint(0,len(individual)-1))
    def mutation(self,individual:array, mutationPoint:int):
        if(individual[mutationPoint]==0):
            individual[mutationPoint]=1
        else:
            individual[mutationPoint]=0

    def converged(self,parents:tuple,children:tuple)->bool:
        if(len(parents[0]) < 2):
            raise Exception("Genome too short")
        return self.computeHammingDistance(parents[0]+parents[1],children[0]+children[1]) <=2

    def computeHammingDistance(self,array1:array,array2:array)->int:    
        hammingDistance=0
        for item in range(len(array1)):
            if(array1[item] != array2[item]):
                hammingDistance+=1
        return hammingDistance
    """
    def run(self,genomeLength:int,fitnessFunction)->array:
        population = generateInitialPopulation(genomeLength)
        snapshot = deepcopy(population)
        parent1, parent2 = selection(population, fitnessFunction)
        child1,child2 = crossoverHelper(parent1,parent2)
        mutationHelper(child1)
        mutationHelper(child2)
        population = [parent1,parent2,child1,child2]
        first = True
        while((first) or (not converged(snapshot,population))):
            first=False
            print("generation")
            snapshot = deepcopy(population)
            parent1, parent2 = selection(population, fitnessFunction)
            child1,child2 = crossoverHelper(parent1,parent2)
            mutationHelper(child1)
            mutationHelper(child2)
            population = [parent1,parent2,child1,child2]
        return parent1"""