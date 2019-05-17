import operator
import random
from array import array

#Initial Population
def generateInitialPopulation(genomeLength:int)->list:
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