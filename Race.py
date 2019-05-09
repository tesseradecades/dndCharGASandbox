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
    
