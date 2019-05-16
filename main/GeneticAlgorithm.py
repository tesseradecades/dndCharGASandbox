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
    return ()
#Crossover
#Mutation