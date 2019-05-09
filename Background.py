import Skills
class Background:

    skillProficiencies = set()
    
    def __str__(self) -> str:
        return "None"

class Acolyte(Background):
    skillProficiencies = {
        Skills.INSIGHT,
        Skills.RELIGION
        }
    def __str__(self) -> str:
        return "Acolyte"
class Charlatan(Background):
    skillProficiencies = {
        Skills.DECEPTION,
        Skills.SLEIGHT_OF_HAND
        }
    def __str__(self) -> str:
        return "Charlatan"
class Criminal(Background):
    skillProficiencies = {
        Skills.DECEPTION,
        Skills.STEALTH
        }
    def __str__(self) -> str:
        return "Criminal"
class Entertainer(Background):
    skillProficiencies = {
        Skills.ACROBATICS,
        Skills.PERFORMANCE
        }
    def __str__(self) -> str:
        return "Entertainer"
class FolkHero(Background):
    skillProficiencies = {
        Skills.ANIMAL_HANDLING,
        Skills.SURVIVAL
        }
    def __str__(self) -> str:
        return "Folk Hero"
class GuildArtisan(Background):
    skillProficiencies = {
        Skills.INSIGHT,
        Skills.PERSUASION
        }
    def __str__(self) -> str:
        return "Guild Artisan"
class Hermit(Background):
    skillProficiencies = {
        Skills.MEDICINE,
        Skills.RELIGION
        }
    def __str__(self) -> str:
        return "Hermit"
class Noble(Background):
    skillProficiencies = {
        Skills.HISTORY,
        Skills.PERSUASION
        }
    def __str__(self) -> str:
        return "Noble"
class Outlander(Background):
    skillProficiencies = {
        Skills.ATHLETICS,
        Skills.PERCEPTION
        }
    def __str__(self) -> str:
        return "Outlander"
class Sage(Background):
    skillProficiencies = {
        Skills.ARCANA,
        Skills.HISTORY
        }
    def __str__(self) -> str:
        return "Sage"
class Sailor(Background):
    skillProficiencies = {
        Skills.ATHLETICS,
        Skills.PERCEPTION
        }
    def __str__(self) -> str:
        return "Sailor"
class Soldier(Background):
    skillProficiencies = {
        Skills.ATHLETICS,
        Skills.INTIMIDATION
        }
    def __str__(self) -> str:
        return "Soldier"
class Urchin(Background):
    skillProficiencies = {
        Skills.SLEIGHT_OF_HAND,
        Skills.STEALTH
        }
    def __str__(self) -> str:
        return "URCHIN"
BACKGROUND_MAP = {
    0:Acolyte,
    1:Charlatan,
    2:Criminal,
    3:Entertainer,
    4:FolkHero,
    5:GuildArtisan,
    6:Hermit,
    7:Noble,
    8:Outlander,
    9:Sage,
    10:Sailor,
    11:Soldier,
    12:Urchin
}