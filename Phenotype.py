from array import array

class Phenotype:
    genes = None

    strengthScore = None
    dexterityScore = None
    constitutionScore = None
    intelligenceScore = None
    wisdomScore = None
    charismaScore = None

    def __init__(self, genes: array, points: int, raceChromosomeLength: int, classChromosomeLength: int):
        self.genes = genes
        self.setAbilityScores(genes,points)
    
    def getPointChromosome(self,point: int, genes: array) -> array:
        stop = point * 5
        start = stop - 5
        return genes[start:stop]
    
    """def getRaceChromosome(self) -> array:
        start = 5*POINTS
        return self.genes[start:start+RACE_CHROMOSOME_LENGTH]
    def getClassChromosome(self) -> array:
        start = (5*POINTS)+RACE_CHROMOSOME_LENGTH
        return self.genes[start:start+CLASS_CHROMOSOME_LENGTH]"""
    
    def setAbilityScores(self, genes: array, points: int):
        pointMap = {0:0, 1:0, 2:0,3:0,4:0,5:0}
        for point in range(1,points+1):
            chromosome = self.getPointChromosome(point,genes)
            assignment = self.getPointAssignment(chromosome)
            pointMap[assignment]+=1
        #print("pointMap:",pointMap)
        self.strengthScore = self.renderScore(pointMap[0])
        self.dexterityScore = self.renderScore(pointMap[1])
        self.constitutionScore = self.renderScore(pointMap[2])
        self.intelligenceScore = self.renderScore(pointMap[3])
        self.wisdomScore = self.renderScore(pointMap[4])
        self.charismaScore = self.renderScore(pointMap[5])

    def getPointAssignment(self,chromosome: array) -> str:
        total = 0
        for bit in chromosome:
            if(bit > 0):
                total+=1
        return total
    def renderScore(self, points: int)-> int:
        if(points == 0):
            return 8
        if(points <= 5):
            return 8+points
        if(points == 6):
            return 13
        if(points <= 8):
            return 14
        if(points <= 11):
            return 15
        if(points <=14):
            return 16
        if(points <=18):
            return 17
        if(points > 18):
            return 18
        else:
            return 8
    def __str__(self) -> str:
        ret = f"Strength Score:\t{self.strengthScore}\nDexterity Score:\t{self.dexterityScore}\nConstitution Score:\t{self.constitutionScore}\nIntelligence Score:\t{self.intelligenceScore}\nWisdom Score:\t{self.wisdomScore}\nCharisma Score:\t{self.charismaScore}"
        return ret

def main():
    phenotype = Phenotype(array('b',[1]*188),27,13,40)
    print(phenotype)


if __name__ == "__main__":
    main()