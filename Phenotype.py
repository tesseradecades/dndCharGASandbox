from array import array

class Phenotype:
    genes = None

    #Ability Scores
    strengthScore = None
    dexterityScore = None
    constitutionScore = None
    intelligenceScore = None
    wisdomScore = None
    charismaScore = None

    #Ability Score Modifiers
    strengthModifier = None
    dexterityModifier = None
    constitutionModifier = None
    intelligenceModifier = None
    wisdomModifier = None
    charismaModifier = None

    def __init__(self, genes: array, points: int, raceChromosomeLength: int, classChromosomeLength: int):
        self.genes = genes
        self.setAbilityScores(genes,points)
        self.setRace(genes,raceChromosomeLength)
        self.setAbilityScoreModifiers()
    
    def getPointChromosome(self,point: int, genes: array) -> array:
        stop = point * 5
        start = stop - 5
        return genes[start:stop]
        
    def setAbilityScores(self, genes: array, points: int):
        pointMap = {0:0, 1:0, 2:0,3:0,4:0,5:0}
        for point in range(1,points+1):
            chromosome = self.getPointChromosome(point,genes)
            assignment = self.getPointAssignment(chromosome)
            pointMap[assignment]+=1
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
    def setRace(self,genes: array, raceChromosomeLength: int):
        pass
    """def getRaceChromosome(self) -> array:
        start = 5*POINTS
        return self.genes[start:start+RACE_CHROMOSOME_LENGTH]
    def getClassChromosome(self) -> array:
        start = (5*POINTS)+RACE_CHROMOSOME_LENGTH
        return self.genes[start:start+CLASS_CHROMOSOME_LENGTH]"""
    def setAbilityScoreModifiers(self):
        self.strengthModifier = self.getModifier(self.strengthScore)
        self.dexterityModifier = self.getModifier(self.dexterityScore)
        self.constitutionModifier = self.getModifier(self.constitutionScore)
        self.intelligenceModifier = self.getModifier(self.intelligenceScore)
        self.wisdomModifier = self.getModifier(self.wisdomScore)
        self.charismaModifier = self.getModifier(self.charismaScore)
    
    def getModifier(self, score: int)->int:
        return (score - 10)/2
    
    def __str__(self) -> str:
        ret = f"Strength Score:\t{self.strengthScore}\t{self.strengthModifier}\
            \nDexterity Score:\t{self.dexterityScore}\t{self.dexterityModifier}\
            \nConstitution Score:\t{self.constitutionScore}\t{self.constitutionModifier}\
            \nIntelligence Score:\t{self.intelligenceScore}\t{self.intelligenceModifier}\
            \nWisdom Score:\t{self.wisdomScore}\t{self.wisdomModifier}\
            \nCharisma Score:\t{self.charismaScore}\t{self.charismaModifier}"
        return ret

def main():
    phenotype = Phenotype(array('b',[1]*188),27,13,40)
    print(phenotype)


if __name__ == "__main__":
    main()