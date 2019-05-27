from array import array
from enum import Enum
try:
    from Character import Character
except ModuleNotFoundError:#So that unittests can use this module
    from main.DnD.Character import Character

class Phenotype:

    def __init__(self,genes:array):
        self.startingStats = self.getStats(genes)
        self.race = self.getRace(genes)
        self.background = self.getBackground(genes)
        self.characterClass = self.getClass(genes)
        self.abilities = set()
        self.feats = set()
        pass
    
    def createCharacter(self,genes:array)-> Character:
        pass
    def getStats(self,statGenes:array)->dict:
        return {
            AbilityScores.STRENGTH:8,
            AbilityScores.DEXTERITY:8,
            AbilityScores.CONSTITUTION:8,
            AbilityScores.INTELLIGENCE:8,
            AbilityScores.WISDOM:8,
            AbilityScores.CHARISMA:8
        }
    def getRace(self,raceGenes:array):
        return "Human"
    def getBackground(self,backgroundGenes:array):
        return "Acolyte"
    def getClass(self,classGenes:array):
        return "Path of the Berserker Barbarian"
    def getFeats(self,featGenes:array)->set:
        return set()

    def __str__(self)->str:
        toString = f"Race:\t\t{self.race}\
            \nBackground:\t{self.background}\
            \nClass:\t\t{self.characterClass}\
            \nStarting Stats:\t{self.startingStats}\
            \nAbilities:\t{self.abilities}\
            \nFeats:\t\t{self.feats}"
        return toString

class AbilityScores(Enum):
    STRENGTH = 0,
    DEXTERITY = 1,
    CONSTITUTION = 2,
    INTELLIGENCE = 3,
    WISDOM = 4,
    CHARISMA = 5
ABILITY_SCORE_GENOME_LENGTH = ((len(AbilityScores)-1)*27)
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

GENOME_LENGTH = ABILITY_SCORE_GENOME_LENGTH+RACES_GENOME_LENGTH+BACKGROUNDS_GENOME_LENGTH+CLASSES_GENOME_LENGTH

def main():
    print(GENOME_LENGTH)
    print(Phenotype([0]*GENOME_LENGTH))

if(__name__ == "__main__"):
    main()