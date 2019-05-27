try:
    from Dnd.Abilities.Ability import Ability
    from DnD.Character import Character
except ModuleNotFoundError:
    from main.DnD.Abilities.Ability import Ability
    from main.DnD.Character import Character

class Darkvision(Ability):
    def __init__(self):
        super(Darkvision,self).__init__()
        self.distance = 60
    def executeConcreteAbility(self, character:Character):
        character.senses["Darkvision"]=self.distance
    def __str__(self)->str:
        return f"Darkvision out to {self.speed} ft"
class SuperiorDarkvision(Darkvision):
    def __init__(self):
        super(SuperiorDarkvision,self).__init__()
        self.distance=120
