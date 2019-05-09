import Abilities
import Armors
import Skills
import Weapons
class Race:
    """def __init__(self):
        pass
    """
    def __str__(self) -> str:
        return "None"
    
    def getScoreIncreases(self)->dict:
        return dict()
    def getSpeed(self)->int:
        return 0
    def getRaceAbilities(self)->set:
        return set()
    def getWeaponProficiencies(self)->set:
        return set()
    def getArmorProficiencies(self)->set:
        return set()
    def getSkillProficiencies(self)->set:
        return set()
class Dwarf(Race):

    def getScoreIncreases(self)->dict:
        return {Abilities.CONSTITUTION:2}
    def getSpeed(self)->int:
        return 25
    def getWeaponProficiencies(self)->set:
        return Weapons.DWARVEN_COMBAT_TRAINING
    def getRaceAbilities(self)->set:
        return {"Darkvision","Dwarven Resilience","Tool Proficiency","Stonecunning"}

class HillDwarf(Dwarf):

    def getScoreIncreases(self)->dict:
        scoreIncreases = super(HillDwarf,self).getScoreIncreases()
        scoreIncreases[Abilities.WISDOM]=1
        return scoreIncreases

    def getRaceAbilities(self)->set:
        raceAbilities = super(HillDwarf,self).getRaceAbilities()
        raceAbilities.add("Dwarven Toughness")
        return raceAbilities

    def __str__(self)->str:
        return "Hill Dwarf"
class MountainDwarf(Dwarf):

    def getScoreIncreases(self) -> dict:
        scoreIncreases = super(MountainDwarf,self).getScoreIncreases()
        scoreIncreases[Abilities.STRENGTH]=2
        return scoreIncreases

    def getArmorProficiencies(self)->set:
        armorProficiencies = super(MountainDwarf,self).getArmorProficiencies()
        armorProficiencies.update(Armors.DWARVEN_ARMOR_TRAINING)
        return armorProficiencies

    def __str__(self)->str:
        return "Mountain Dwarf"

class Elf(Race):
    def getScoreIncreases(self)-> dict:
        return {Abilities.DEXTERITY:2}
    def getSpeed(self)->int:
        return 30
    def getRaceAbilities(self)->set:
        return {"Darkvision","Fey Ancestry","Trance"}
    def getSkillProficiencies(self)->set:
        return {Skills.PERCEPTION}
class HighElf(Elf):
    def getScoreIncreases(self)->dict:
        scoreIncreases = super(HighElf,self).getScoreIncreases()
        scoreIncreases[Abilities.INTELLIGENCE]=1
        return scoreIncreases
    def getWeaponProficiencies(self)->set:
        return Weapons.ELF_WEAPON_TRAINING
    def getRaceAbilities(self)->set:
        raceAbilities = super(HighElf,self).getRaceAbilities()
        raceAbilities.update("Cantrip")
        return raceAbilities

    def __str__(self) -> str:
        return "High Elf"
class WoodElf(Elf):
    def getScoreIncreases(self)->dict:
        scoreIncreases = super(WoodElf,self).getScoreIncreases()
        scoreIncreases[Abilities.WISDOM]=1
        return scoreIncreases
    def getWeaponProficiencies(self)->set:
        return Weapons.ELF_WEAPON_TRAINING
    def getSpeed(self)->int:
        return 35
    def getRaceAbilities(self)->set:
        raceAbilities = super(WoodElf,self).getRaceAbilities()
        raceAbilities.update("Mask of the Wild")
        return raceAbilities
    def __str__(self) -> str:
        return "Wood Elf"
RACE_MAP = {
    0:HillDwarf(),1:MountainDwarf(),
    2:HighElf(), 3:WoodElf(), 4: "Dark Elf",
    5:"Lightfoot Halfling", 6:"Stout Halfling",
    7: "Human",
    8:"Dragonborn",
    9:"Forest Gnome", 10: "Rock Gnome",
    11:"Half-Elf",
    12:"Half-Orc",
    13:"Tiefling"
    }