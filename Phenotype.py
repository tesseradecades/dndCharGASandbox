from array import array
import Abilities
import CharacterClass
import Race
import Skills

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

    proficiency = 6

    race = None
    characterClass = None

    #Ability Scores
    abilityScores = {
        Abilities.STRENGTH:0,
        Abilities.DEXTERITY:0,
        Abilities.CONSTITUTION:0,
        Abilities.INTELLIGENCE:0,
        Abilities.WISDOM:0,
        Abilities.CHARISMA:0
    }

    #Ability Score Modifiers
    abilityScoreModifiers = {
        Abilities.STRENGTH:0,
        Abilities.DEXTERITY:0,
        Abilities.CONSTITUTION:0,
        Abilities.INTELLIGENCE:0,
        Abilities.WISDOM:0,
        Abilities.CHARISMA:0
    }
    savingThrows = {
        Abilities.STRENGTH:0,
        Abilities.DEXTERITY:0,
        Abilities.CONSTITUTION:0,
        Abilities.INTELLIGENCE:0,
        Abilities.WISDOM:0,
        Abilities.CHARISMA:0
    }
    #Skill Modifiers
    skillModifiers = {
        Skills.ACROBATICS:0,
        Skills.ANIMAL_HANDLING:0,
        Skills.ATHLETICS:0,
        Skills.ARCANA:0,
        Skills.DECEPTION:0,
        Skills.HISTORY:0,
        Skills.INITIATIVE:0,
        Skills.INSIGHT:0,
        Skills.INTIMIDATION:0,
        Skills.INVESTIGATION:0,
        Skills.MEDICINE:0,
        Skills.NATURE:0,
        Skills.PERCEPTION:0,
        Skills.PERFORMANCE:0,
        Skills.PERSUASION:0,
        Skills.RELIGION:0,
        Skills.SLEIGHT_OF_HAND:0,
        Skills.STEALTH:0,
        Skills.SURVIVAL:0
    }

    #Derives Stats
    armorClass = 0
    hitPoints = 0
    movement = 0

    #Proficiencies
    armorProficiencies = set()
    weaponProficiencies = set()
    toolProficiencies = set()
    savingThrowProficiencies = set()
    skillProficiencies = set()

    abilities = set()

    def __init__(self, genes: array):
        #Get Point Chromosomes
        pointChromosomes = []
        for point in range(1,POINTS+1):
            stop = point * 5
            start = stop - 5
            pointChromosomes.append(self.getChromosome(genes,start,stop))
        
        #Get Race Chromosome
        raceStart = 5*POINTS
        raceEnd = raceStart+len(RACE_MAP)-1
        raceChromosome = self.getChromosome(genes,raceStart,raceEnd)
        #Get Class Chromosome
        classStart = raceEnd
        classEnd = classStart+len(CLASS_MAP)-1
        classChromosome = self.getChromosome(genes,classStart,classEnd)

        #Derive Stats from Point Chromosomes
        pointMap = {0:0, 1:0, 2:0,3:0,4:0,5:0}
        for chromosome in pointChromosomes:
            pointMap[sumArray(chromosome)]+=1
        self.renderScoresFromPoints(pointMap)
        #Adjust Stats by Race
        self.race = Race.Race()#RACE_MAP[sumArray(raceChromosome)]
        #Adjust Stats by Class
        self.characterClass = CharacterClass.CharacterClass()#CLASS_MAP[sumArray(classChromosome)]
        self.renderDerivedStats()

    def __str__(self) -> str:
        ret = f"Race:\t{self.race}\
            \nClass:\t{self.characterClass}\
            \nHit Points:\t{self.hitPoints}\
            \nArmor Class:\t{self.armorClass}\
            \nMovement:\t{self.movement}\
            \nScores:\t{self.abilityScores}\
            \nModifiers:\t{self.abilityScoreModifiers}\
            \nSaving Throws:\t{self.savingThrows}\
            \nSkills:\t{self.skillModifiers}"
        return ret

    def getChromosome(self, genes: array, start: int, stop: int)->array:
        return genes[start:stop]

    def renderScoresFromPoints(self, pointMap:dict):
        scores = self.abilityScores
        renderScore = self.renderScore
        scores[Abilities.STRENGTH] = renderScore(pointMap[0])
        scores[Abilities.DEXTERITY] = renderScore(pointMap[1])
        scores[Abilities.CONSTITUTION] = renderScore(pointMap[2])
        scores[Abilities.INTELLIGENCE] = renderScore(pointMap[3])
        scores[Abilities.WISDOM] = renderScore(pointMap[4])
        scores[Abilities.CHARISMA] = renderScore(pointMap[5])

    def renderScore(self, points: int)-> int:
        score = 8
        if(points <= 5):
            score+points
        elif(points == 6):
            score+=5
        elif(points <= 8):
            score+=6
        elif(points <= 11):
            score+=7
        elif(points <=14):
            score+=8
        elif(points <=18):
            score+=9
        elif(points > 18):
            score+=10
        return score

    def renderDerivedStats(self):
        #Modifiers
        for score in self.abilityScores.keys():
            self.abilityScoreModifiers[score] = getModifier(self.abilityScores[score])
        #Saving Throws
        for modifier in self.abilityScoreModifiers.keys():
            mod = self.abilityScoreModifiers[modifier]
            if(modifier in self.savingThrowProficiencies):
                mod+=self.proficiency
            self.savingThrows[modifier] = mod
        #Skills
        for skill in Skills.STR_SKILLS:
            mod = self.abilityScoreModifiers[Abilities.STRENGTH]
            if(skill in self.skillProficiencies):
                mod+=self.proficiency
            self.skillModifiers[skill] = mod
        for skill in Skills.DEX_SKILLS:
            mod = self.abilityScoreModifiers[Abilities.DEXTERITY]
            if(skill in self.skillProficiencies):
                mod+=self.proficiency
            self.skillModifiers[skill] = mod
        for skill in Skills.INT_SKILLS:
            mod = self.abilityScoreModifiers[Abilities.INTELLIGENCE]
            if(skill in self.skillProficiencies):
                mod+=self.proficiency
            self.skillModifiers[skill] = mod
        for skill in Skills.WIS_SKILLS:
            mod = self.abilityScoreModifiers[Abilities.WISDOM]
            if(skill in self.skillProficiencies):
                mod+=self.proficiency
            self.skillModifiers[skill] = mod
        for skill in Skills.CHA_SKILLS:
            mod = self.abilityScoreModifiers[Abilities.CHARISMA]
            if(skill in self.skillProficiencies):
                mod+=self.proficiency
            self.skillModifiers[skill] = mod
        self.armorClass = 10+self.abilityScoreModifiers[Abilities.DEXTERITY]
        self.hitPoints = 4+self.abilityScoreModifiers[Abilities.CONSTITUTION]

def sumArray(a:array)->int:
    total = 0
    for i in a:
        total+=i
    return total

def getModifier(score:int)->int:
    return (score-10)//2

def main(): 
    print(Phenotype(array('b',[0]*188)))


if __name__ == "__main__":
    main()