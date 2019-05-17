import operator
import random
from array import array

#Initial Population
def generateInitialPopulation(genomeLength:int)->list:
    if(genomeLength < 2):
        raise Exception("Genome too short")
    initialPopulation = []
    for i in range(4):
        initialPopulation.append(array('b',[0]*genomeLength))
    return initialPopulation
#Fitness Function
#Selection
def selection(population:list, fitnessFunction)->tuple:
    fitnessDict = {}
    for individual in range(len(population)):
        fitnessDict[individual] = fitnessFunction(population[individual])
    fittest = getKeyOfMaxValue(fitnessDict)
    fitnessDict.pop(fittest)
    secondFittest = getKeyOfMaxValue(fitnessDict)
    fitnessDict.pop(secondFittest)
    return (population[fittest],population[secondFittest])
def getKeyOfMaxValue(d:dict)->object:
    return max(d.items(), key=operator.itemgetter(1))[0]
#Crossover
def crossover(parent1:array, parent2:array)->tuple:
    return crossover(parent1,parent2,random.randint(len(parent1)))

def crossover(parent1:array, parent2:array, crossoverPoint: int)->tuple:
    return (parent1[:crossoverPoint]+parent2[crossoverPoint:],parent2[:crossoverPoint]+parent1[crossoverPoint:])
#Mutation
def mutation(individual:array):
    mutation(individual, random.randint(len(individual)))
def mutation(individual:array, mutationPoint:int):
    if(individual[mutationPoint]==0):
        individual[mutationPoint]=1
    else:
        individual[mutationPoint]=0

def converged(parents:tuple,children:tuple)->bool:
    if(len(parents[0]) < 2):
        raise Exception("Genome too short")
    return computeHammingDistance(parents[0]+parents[1],children[0]+children[1]) <=2

def computeHammingDistance(array1:array,array2:array)->int:    
    hammingDistance=0
    for item in range(len(array1)):
        if(array1[item] != array2[item]):
            hammingDistance+=1
    return hammingDistance

def run(genomeLength:int,fitnessFunction)->array:
    population = generateInitialPopulation(genomeLength)
