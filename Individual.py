from array import array
from Background import BACKGROUND_MAP
import Phenotype


GENOME_LENGTH = (5*Phenotype.POINTS)+(len(BACKGROUND_MAP)-1)+(len(Phenotype.RACE_MAP)-1)+(len(Phenotype.CLASS_MAP)-1)

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
        self.phenotype = Phenotype.Phenotype(self.genes)
    def __str__(self) -> str:
        ret = f"Phenotype:\n{self.getPhenotype()}\
            \nGenes:\n{self.genes}"
        return ret
    


def main():
    individual = Individual(array('b',[0]*GENOME_LENGTH))
    print(GENOME_LENGTH)
    print(individual)
    print()
    individual.flipBit(1)
    print(individual)

if __name__ == "__main__":
    main()