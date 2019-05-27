from array import array
from enum import IntEnum
try:
    from Character import Character
except ModuleNotFoundError:#So that unittests can use this module
    from main.DnD.Character import Character

class Phenotype:

    def __init__(self,genes:array,level:int):
        start = 0
        end = ABILITY_SCORE_GENOME_LENGTH+1
        self.startingStats = self.getStats(genes[start:end])
        start = end
        end = start+RACES_GENOME_LENGTH
        self.race = self.getRace(genes[start:end])
        start = end
        end = start+BACKGROUNDS_GENOME_LENGTH
        self.background = self.getBackground(genes[start:end])
        start = end
        end = start+CLASSES_GENOME_LENGTH
        self.characterClass = self.getClass(genes[start:end])
        numFeats = 0
        if(level >=4):
            numFeats+=1
        if(level >= 8):
            numFeats+=1
        if(level >= 12):
            numFeats+=1
        if(level >= 16):
            numFeats+=1
        if(level >= 19):
            numFeats+=1
        start = end
        end = start+FEATS_GENOME_LENGTH
        self.feats = self.getFeats(numFeats,genes[start:end])
        self.abilities = set()
        
    
    def createCharacter(self,genes:array)-> Character:
        pass
    def getStats(self,statGenes:array)->dict:
        points = self.getPoints(statGenes)
        stats = {
            AbilityScores.STRENGTH:0,
            AbilityScores.DEXTERITY:0,
            AbilityScores.CONSTITUTION:0,
            AbilityScores.INTELLIGENCE:0,
            AbilityScores.WISDOM:0,
            AbilityScores.CHARISMA:0
        }
        for score in points.keys():
            stats[score] = self.renderScore(points[score])
        return stats
    def getPoints(self,statGenes:array)->dict:
        pointsDict = {
            AbilityScores.STRENGTH:0,
            AbilityScores.DEXTERITY:0,
            AbilityScores.CONSTITUTION:0,
            AbilityScores.INTELLIGENCE:0,
            AbilityScores.WISDOM:0,
            AbilityScores.CHARISMA:0
        }
        for point in range(POINTS):
            end = (point+1)*5
            start = end-5
            value = self.getChromosomeValue(statGenes[start:end])
            pointsDict[value]+=1
        return pointsDict
    def getChromosomeValue(self,chromosome:array)->int:
        value = 0
        for gene in chromosome:
            value+=gene
        return value
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

    def getRace(self,raceGenes:array):
        return RACES[self.getChromosomeValue(raceGenes)]
    def getBackground(self,backgroundGenes:array):
        return BACKGROUNDS[self.getChromosomeValue(backgroundGenes)]
    def getClass(self,classGenes:array):
        return CLASSES[self.getChromosomeValue(classGenes)]
    def getFeats(self,numFeats:int,featGenes:array)->set:
        chosenFeats = set()
        for f in range(numFeats):
            start = (f+1)*FEATS_GENOME_LENGTH
            end = start - FEATS_GENOME_LENGTH
            chosenFeats.add(FEATS[self.getChromosomeValue(featGenes[start:end])])
        return chosenFeats

    def __str__(self)->str:
        toString = f"Race:\t\t{self.race}\
            \nBackground:\t{self.background}\
            \nClass:\t\t{self.characterClass}\
            \nStarting Stats:\t{self.startingStats}\
            \nFeats:\t\t{self.feats}"
        return toString

POINTS = 27
class AbilityScores(IntEnum):
    STRENGTH = 0,
    DEXTERITY = 1,
    CONSTITUTION = 2,
    INTELLIGENCE = 3,
    WISDOM = 4,
    CHARISMA = 5
ABILITY_SCORE_GENOME_LENGTH = ((len(AbilityScores)-1)*POINTS)

RACES = {
    0:"Hill Dwarf",
    1:"Mountain Dwarf",
    2:"High Elf",
    3:"Wood Elf",
    4:"Dark Elf",
    5:"Lightfoot Halfling",
    6:"Stout Halfling",
    7:"Human",
    8:"Black Dragonborn",
    9:"Blue Dragonborn",
    10:"Brass Dragonborn",
    11:"Bronze Dragonborn",
    12:"Copper Dragonborn",
    13:"Gold Dragonborn",
    14:"Green Dragonborn",
    15:"Red Dragonborn",
    16:"Silver Dragonborn",
    17:"White Dragonborn",
    18:"Forest Gnome",
    19:"Rock Gnome",
    20:"Half-Elf",
    21:"Half-Orc",
    22:"Tiefling"
}
RACES_GENOME_LENGTH = len(RACES)-1

BACKGROUNDS = {
    0:"Acolyte",
    1:"Charlatan",
    2:"Criminal",
    3:"Entertainer",
    4:"Folk Hero",
    5:"Guild Artisan",
    6:"Hermit",
    7:"Noble",
    8:"Outlander",
    9:"Sage",
    10:"Sailor",
    11:"Soldier",
    12:"Urchin"
}
BACKGROUNDS_GENOME_LENGTH = len(BACKGROUNDS)-1

CLASSES = {
    0:"Path of the Berserker Barbarian",
    1:"Path of the Totem Warrior Barbarian",
    2:"College of Lore Bard",
    3:"College of Valor Bard",
    4:"Knowledge Domain Cleric",
    5:"Life Domain Cleric",
    6:"Light Domain Cleric",
    7:"Nature Domain Cleric",
    8:"Tempest Domain Cleric",
    9:"Trickery Domain Cleric",
    10:"War Domain Cleric",
    11:"Circle of the Land Druid",
    12:"Circle of the Moon Druid",
    13:"Champion Fighter",
    14:"Battle Master Fighter",
    15:"Eldritch Knight Fighter",
    16:"Way of the Open Hand Monk",
    17:"Way of Shadow Monk",
    18:"Way of the Four Elements Monk",
    19:"Oath of Devotion Paladin",
    20:"Oath of the Ancients Paladin",
    21:"Oath of Vengeance Paladin",
    22:"Hunter Ranger",
    23:"Beast Master Ranger",
    24:"Thief Rogue",
    25:"Assassin Rogue",
    26:"Arcane Trickster Rogue",
    27:"Draconic Bloodline Sorcerer",
    28:"Wild Magic Sorcerer",
    29:"Archfey Warlock",
    30:"Fiend Warlock",
    31:"Great Old One Warlock",
    32:"Abjuration Wizard",
    33:"Conjuration Wizard",
    34:"Divination Wizard",
    35:"Enchantment Wizard",
    36:"Evocation Wizard",
    37:"Illusion Wizard",
    38:"Necromancy Wizard",
    39:"Transmutation Wizard"
}
CLASSES_GENOME_LENGTH = len(CLASSES)-1

FEATS = {
    0:"Alert",
    1:"Athlete",
    2:"Actor",
    3:"Charger",
    4:"Crossbow Expert",
    5:"Defensive Duelist",
    6:"Dual Wielder",
    7:"Dungeon Delver",
    8:"Durable",
    9:"Elemental Adept",
    10:"Grappler",
    11:"Great Weapon Master",
    12:"Healer",
    13:"Heavily Armored",
    14:"Heavy Armor Master",
    15:"Inspiring Leader",
    16:"Keen Mind",
    17:"Lightly Armored",
    18:"Linguist",
    19:"Lucky",
    20:"Mage Slayer",
    21:"Magic Initiate",
    22:"Martial Adept",
    23:"Medium Armor Master",
    24:"Mobile",
    25:"Moderately Armored",
    26:"Mounted Combatant",
    27:"Observant",
    28:"Polearm Master",
    29:"Resilient",
    30:"Ritual Caster",
    31:"Savage Attacker",
    32:"Sentinel",
    33:"Sharpshooter",
    34:"Shield Master",
    35:"Skilled",
    36:"Skulker",
    37:"Spell Sniper",
    38:"Tavern Brawler",
    39:"Tough",
    40:"War Caster",
    41:"Weapon Master"
}
FEATS_GENOME_LENGTH = len(FEATS)-1

GENOME_LENGTH = ABILITY_SCORE_GENOME_LENGTH+RACES_GENOME_LENGTH+BACKGROUNDS_GENOME_LENGTH+CLASSES_GENOME_LENGTH+FEATS_GENOME_LENGTH

def main():
    print(GENOME_LENGTH)
    print(Phenotype([0]*GENOME_LENGTH,20))

if(__name__ == "__main__"):
    main()