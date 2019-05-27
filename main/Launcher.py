from GeneticAlgorithm.FitnessChange import FitnessChange
from DnD.Phenotype import *
def fitnessFunction(individual:array)->float:
    fitness = 0
    phenotype = Phenotype(individual,1)
    c = phenotype.characterClass
    r = phenotype.race
    b = phenotype.background
    racePoints = 0
    for key in RACES:
        if(RACES[key] == r):
            fitness+=key
            break
    for key in BACKGROUNDS:
        if(BACKGROUNDS[key] == b):
            fitness+=key
            break
    for key in CLASSES:
        if(CLASSES[key] == c):
            fitness+=key
            break
    return fitness

def main():
    print(Phenotype(FitnessChange().run(GENOME_LENGTH,GENOME_LENGTH,fitnessFunction),20))
if(__name__ == "__main__"):
    main()