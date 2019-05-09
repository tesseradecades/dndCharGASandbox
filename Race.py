import Abilities

class Race:

    scoreIncreases = {
        Abilities.STRENGTH:0,
        Abilities.DEXTERITY:0,
        Abilities.CONSTITUTION:0,
        Abilities.INTELLIGENCE:0,
        Abilities.WISDOM:0,
        Abilities.CHARISMA:0
        }
    speed = 0
    raceAbilities = set()
    weaponProficiencies = set()
    toolProficiencies = set()
    def __init__(self):
        pass
    
    def __str__(self) -> str:
        return "None"
    
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