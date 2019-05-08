from array import array

POINTS = 27

RACE_MAP = {
    0:"Hill Dwarf",1:"Mountain Dwarf",
    2:"High Elf", 3: "Wood Elf", 4: "Dark Elf",
    5:"Lightfoot Halfling", 6:"Stout Halfling",
    7: "Human",
    8:"Dragonborn",
    9:"Forest Gnome", 10: "Rock Gnome",
    11:"Half-Elf",
    12:"Half-Orc",
    13:"Tiefling"
    }

CLASS_MAP = {
    0:"Berserker Barbarian", 1: "Totem Barbarian",
    2:"Lore Bard", 3:"Valor Bard",
    4:"Knowledge Cleric", 5:"Life Cleric", 6:"Light Cleric", 7:"Nature Cleric",8:"Tempest Cleric",9:"Trickery Cleric",10:"War Cleric",
    11:"Land Druid", 12:"Moon Druid",
    13:"Champion Fighter", 14:"Battlemaster Fighter",15:"Eldritch Knight Fighter",
    16:"Open Hand Monk",17:"Shadow Monk",18:"Four Elements Monk",
    19:"Devotion Paladin",20:"Ancients Paladin",21:"Vengeance Paladin",
    22:"Hunter Ranger",23:"Beast Master Ranger",
    24:"Thief Rogue",25:"Assassin Rogue",26:"Arcane Trickster Rogue",
    27:"Draconic Sorcerer",28:"Wild Magic Sorcerer",
    29:"Fiend Warlock",30:"Archfey Warlock", 31:"Great Old One Warlock",
    32:"Abjuration Wizard",33:"Conjuration Wizard",34:"Divination Wizard",35:"Enchantment Wizard",36:"Evocation Wizard",37:"Illusion Wizard",38:"Necromancy Wizard",39:"Transmutation Wizard"
}

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

    #Race
    race = None

    #Class
    characterClass = None

    def __init__(self, genes: array):
        self.genes = genes
        self.setAbilityScores(genes)
        raceStart = 5*POINTS
        raceEnd = raceStart+len(RACE_MAP)-1
        self.setRace(genes, raceStart,raceEnd)
        self.setAbilityScoreModifiers()
        classStart = raceEnd
        classEnd = classStart+len(CLASS_MAP)-1
        self.setClass(genes,classStart,classEnd)
    
    def getPointChromosome(self,point: int, genes: array) -> array:
        stop = point * 5
        start = stop - 5
        return genes[start:stop]
        
    def setAbilityScores(self, genes: array):
        pointMap = {0:0, 1:0, 2:0,3:0,4:0,5:0}
        for point in range(1,POINTS+1):
            chromosome = self.getPointChromosome(point,genes)
            assignment = self.getAssignment(chromosome)
            pointMap[assignment]+=1
        self.strengthScore = self.renderScore(pointMap[0])
        self.dexterityScore = self.renderScore(pointMap[1])
        self.constitutionScore = self.renderScore(pointMap[2])
        self.intelligenceScore = self.renderScore(pointMap[3])
        self.wisdomScore = self.renderScore(pointMap[4])
        self.charismaScore = self.renderScore(pointMap[5])

    def getAssignment(self,chromosome: array) -> int:
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
    def setRace(self,genes: array, start: int,end:int):
        chromosome = self.genes[start:end]
        self.race = RACE_MAP[self.getAssignment(chromosome)]

    def setClass(self,genes:array,start:int,end:int):
        chromosome = self.genes[start:end]
        self.characterClass = CLASS_MAP[self.getAssignment(chromosome)]

    def setAbilityScoreModifiers(self):
        self.strengthModifier = self.getModifier(self.strengthScore)
        self.dexterityModifier = self.getModifier(self.dexterityScore)
        self.constitutionModifier = self.getModifier(self.constitutionScore)
        self.intelligenceModifier = self.getModifier(self.intelligenceScore)
        self.wisdomModifier = self.getModifier(self.wisdomScore)
        self.charismaModifier = self.getModifier(self.charismaScore)
    
    def getModifier(self, score: int)->int:
        return (score - 10)//2
    
    def __str__(self) -> str:
        ret = f"Race:\t{self.race}\
            \nClass:\t{self.characterClass}\
            \nStrength Score:\t{self.strengthScore}\t{self.strengthModifier}\
            \nDexterity Score:\t{self.dexterityScore}\t{self.dexterityModifier}\
            \nConstitution Score:\t{self.constitutionScore}\t{self.constitutionModifier}\
            \nIntelligence Score:\t{self.intelligenceScore}\t{self.intelligenceModifier}\
            \nWisdom Score:\t{self.wisdomScore}\t{self.wisdomModifier}\
            \nCharisma Score:\t{self.charismaScore}\t{self.charismaModifier}"
        return ret

def main(): 
    print(Phenotype(array('b',[0]*188)))
    print()
    print(Phenotype(array('b',[1]*188)))


if __name__ == "__main__":
    main()