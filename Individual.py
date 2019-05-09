from array import array
import Phenotype

class Individual:
    fitness = None

    genes = None

    phenotype = None

    def __init__(self, genes: array):
        self.genes = genes
    
    def getPhenotype(self):
        if(self.phenotype != None):
            return self.phenotype
        else:
            self.phenotype = Phenotype.Phenotype(self.genes)
            return self.phenotype
    def getFitness(self) -> int:
        if(self.fitness != None):
            return fitness
        else:
            return calculateFitness(self.getPhenotype())
    
    def calculateFitness(self,phenotype) -> int:
        return (getDefensiveChallengeRating(phenotype) + getOffensiveChallengeRating(phenotype))/2
    
    def getDefensiveChallengeRating(self,phenotype)-> int:
        return 0
    
    def getOffensiveChallengeRating(self,phenotype) -> int:
        return 0
        
    def flipBit(self,bit: int):
        ix = bit-1
        if(self.genes[ix] == 0):
            self.genes[ix] = 1
        else:
            self.genes[ix] = 0

    def __str__(self) -> str:
        import Race
        ret = f"Phenotype:\n{self.getPhenotype()}\
            \nGenes:\n{self.genes}"
        return ret
def makeMountainDwarf(individual):
    individual.flipBit(148)

def makeHighElf(individual):
    makeMountainDwarf(individual)
    individual.flipBit(149)

def makeWoodElf(individual):
    makeHighElf(individual)
    individual.flipBit(150)
def makeDarkElf(individual):
    makeWoodElf(individual)
    individual.flipBit(151)
def makeLightfoot(individual):
    makeDarkElf(individual)
    individual.flipBit(152)
def makeStout(individual):
    makeLightfoot(individual)
    individual.flipBit(153)
def makeHuman(individual):
    makeStout(individual)
    individual.flipBit(154)
def makeDragonborn(individual):
    makeHuman(individual)
    individual.flipBit(155)
def makeForestGnome(individual):
    makeDragonborn(individual)
    individual.flipBit(156)
def makeRockGnome(individual):
    makeForestGnome(individual)
    individual.flipBit(157)
def makeHalfElf(individual):
    makeRockGnome(individual)
    individual.flipBit(158)
def makeHalfOrc(individual):
    makeHalfElf(individual)
    individual.flipBit(159)
def makeTiefling(individual):
    makeHalfOrc(individual)
    individual.flipBit(160)

def main():
    individual = Individual(array('b',[0]*Phenotype.GENOME_LENGTH))
    print(Phenotype.GENOME_LENGTH)
    makeTiefling(individual)
    print(individual)
    

if __name__ == "__main__":
    main()