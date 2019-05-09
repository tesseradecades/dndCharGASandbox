import Abilities
import Armors
import Skills
import Weapons
class Race:
    def __str__(self) -> str:
        return "None"
    def getScoreIncreases(self)->dict:
        return dict()
    def getSpeed(self)->int:
        return 30
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
        raceAbilities.update({"Dwarven Toughness"})
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
        raceAbilities.update({"Cantrip"})
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
        raceAbilities.update({"Mask of the Wild"})
        return raceAbilities
    def __str__(self) -> str:
        return "Wood Elf"
class DarkElf(Elf):
    def getScoreIncreases(self)->dict:
        scoreIncreases = super(DarkElf,self).getScoreIncreases()
        scoreIncreases[Abilities.CHARISMA]=1
        return scoreIncreases
    def getRaceAbilities(self)->set:
        raceAbilities = super(DarkElf,self).getRaceAbilities()
        raceAbilities.update({"Superior Darkvision","Drow Magic"})
        return raceAbilities
    def getWeaponProficiencies(self)->set:
        return Weapons.DROW_WEAPON_TRAINING
    def __str__(self) -> str:
        return "Dark Elf"
class Halfling(Race):
    def getScoreIncreases(self)->dict:
        return {Abilities.DEXTERITY:2}
    def getSpeed(self)->int:
        return 25
    def getRaceAbilities(self)->set:
        return {"Lucky","Halfling Nimbleness", "Brave"}     
class LightfootHalfling(Halfling):
    def getScoreIncreases(self)->dict:
        scoreIncreases = super(LightfootHalfling,self).getScoreIncreases()
        scoreIncreases[Abilities.CHARISMA]=1
        return scoreIncreases
    def getRaceAbilities(self)->set:
        raceAbilities = super(LightfootHalfling,self).getRaceAbilities()
        raceAbilities.update({"NaturallyStealthy"})
        return raceAbilities
    def __str__(self) -> str:
        return "Lightfoot Halfling"
class StoutHalfling(Halfling):
    def getScoreIncreases(self)->dict:
        scoreIncreases = super(StoutHalfling,self).getScoreIncreases()
        scoreIncreases[Abilities.CONSTITUTION]=1
        return scoreIncreases
    def getRaceAbilities(self)->set:
        raceAbilities = super(StoutHalfling,self).getRaceAbilities()
        raceAbilities.update({"Stout Resilience"})
        return raceAbilities
    def __str__(self) -> str:
        return "Stout Halfling"
class Human(Race):
    def getScoreIncreases(self)->dict:
        return {
            Abilities.CONSTITUTION:1,
            Abilities.STRENGTH:1,
            Abilities.DEXTERITY:1,
            Abilities.INTELLIGENCE:1,
            Abilities.WISDOM:1,
            Abilities.CHARISMA:1
            }
    def __str__(self) -> str:
        return "Human"
class Dragonborn(Race):
    def getScoreIncreases(self)->dict:
        return {Abilities.STRENGTH:2, Abilities.CHARISMA:1}
    def getRaceAbilities(self)->set:
        return{"Draconic Ancestry","Breath Weapon","Damage Resistance"}
    def __str__(self)->str:
        return "Dragonborn"
class Gnome(Race):
    def getScoreIncreases(self)->dict:
        return {Abilities.INTELLIGENCE:2}
    def getSpeed(self)->int:
        return 25
    def getRaceAbilities(self)->set:
        return {"Darkvision","Gnome Cunning"}
class ForestGnome(Gnome):
    def getScoreIncreases(self)->dict:
        scoreIncreases = super(ForestGnome,self).getScoreIncreases()
        scoreIncreases[Abilities.DEXTERITY]=1
        return scoreIncreases
    def getRaceAbilities(self)->set:
        abilities = super(ForestGnome,self).getRaceAbilities()
        abilities.update({"Natural Illusionist","Speak With Small Beasts"})
        return abilities
    def __str__(self)->str:
        return "Forest Gnome"
class RockGnome(Gnome):
    def getScoreIncreases(self)->dict:
        scoreIncreases = super(RockGnome,self).getScoreIncreases()
        scoreIncreases[Abilities.CONSTITUTION]=1
        return scoreIncreases
    def getRaceAbilities(self)->set:
        abilities = super(RockGnome,self).getRaceAbilities()
        abilities.update({"Artificer's Lore","Tinker"})
        return abilities
    def __str__(self)->str:
        return "Rock Gnome"

RACE_MAP = {
    0:HillDwarf,1:MountainDwarf,
    2:HighElf, 3:WoodElf, 4:DarkElf,
    5:LightfootHalfling, 6:StoutHalfling,
    7: Human,
    8:Dragonborn,
    9:ForestGnome, 10:RockGnome,
    11:"Half-Elf",
    12:"Half-Orc",
    13:"Tiefling"
    }