"""
from enum import Enum
class Race(Enum):
    HILL_DWARF = 0,
    MOUNTAIN_DWARF = 1,
    HIGH_ELF = 2,
    WOOD_ELF = 3,
    DARK_ELF = 4,
    LIGHTFOOT_HALFLING = 5,
    STOUT_HALFLING = 6,
    HUMAN = 7,
    BLACK_DRAGONBORN = 8,
    BLUE_DRAGONBORN = 9,
    BRASS_DRAGONBORN = 10,
    BRONZE_DRAGONBORN = 11,
    COPPER_DRAGONBORN = 12,
    GOLD_DRAGONBORN = 13,
    GREEN_DRAGONBORN = 14,
    RED_DRAGONBORN = 15,
    SILVER_DRAGONBORN = 16,
    WHITE_DRAGONBORN = 17,
    FOREST_GNOME = 18,
    ROCK_GNOME = 19,
    HALF_ELF = 20,
    HALF_ORC = 21,
    TIEFLING = 22
"""

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

class Race():
    def getAbilities(self)->set:
        return set()