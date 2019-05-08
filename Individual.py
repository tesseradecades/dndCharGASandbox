from array import array

CLASS_CHROMOSOME_LENGTH = 40
POINTS = 27
RACE_CHROMOSOME_LENGTH = 13

GENOME_LENGTH = (5*POINTS)+(RACE_CHROMOSOME_LENGTH)+(CLASS_CHROMOSOME_LENGTH)

class Individual:
    fitness = None

    genes = None#[0]*GENOME_LENGTH

    phenotype = None

    def __init__(self, genes: array):
        self.genes = genes
    
    def getPhenotype(self):
        if(self.phenotype != None):
            return phenotype
        else:
            return None
    def getFitness(self) -> int:
        if(self.fitness != None):
            return fitness
        else:
            return calculateFitness(self.getPhenotype())
    
    def calculateFitness(self,phenotype) -> int:
        return (getDefensiveChallengeRating(phenotype) + getOffensiveChallengeRating(phenotype))//2
    
    def getDefensiveChallengeRating(self,phenotype)-> int:
        return 0
    
    def getOffensiveChallengeRating(self,phenotype) -> int:
        return 0
    
    def getPointChromosome(self,point: int) -> array:
        stop = point * 5
        start = stop - 5
        return self.genes[start:stop]
    
    def getRaceChromosome(self) -> array:
        start = 5*POINTS
        return self.genes[start:start+RACE_CHROMOSOME_LENGTH]
    def getClassChromosome(self) -> array:
        start = (5*POINTS)+RACE_CHROMOSOME_LENGTH
        return self.genes[start:start+CLASS_CHROMOSOME_LENGTH]
    
    def flipBit(self,bit: int):
        ix = bit-1
        if(self.genes[ix] == 0):
            self.genes[ix] = 1
        else:
            self.genes[ix] = 0

    


def main():
    individual = Individual(array('b',[0]*GENOME_LENGTH))
    print(individual.genes)
    print(len(individual.genes))
    individual.genes[5]=1
    individual.genes[9]=1
    print(individual.getPointChromosome(1))
    print(len(individual.getRaceChromosome()))
    print(len(individual.getClassChromosome()))
    print(individual.genes)
    individual.flipBit(1)
    print(individual.genes)

if __name__ == "__main__":
    main()