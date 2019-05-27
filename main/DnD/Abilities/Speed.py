try:
    from Dnd.Abilities.Ability import Ability
    from DnD.Character import Character
except ModuleNotFoundError:
    from main.DnD.Abilities.Ability import Ability
    from main.DnD.Character import Character

class Speed(Ability):
    def __init__(self,speed:int):
        super(Speed,self).__init__()
        self.speed = speed

    def executeConcreteAbility(self,character:Character):
        character.speed = self.speed
    def __str__(self)->str:
        return f"{self.speed} ft"
class FlightSpeed(Speed):
    def __init__(self,speed:int):
        super(FlightSpeed,self).__init__(speed)
    def executeAbstractAbility(self,character:Character):
        character.armorClass+=2
    def executeConcreteAbility(self,character:Character):
        character.flightSpeed=self.speed
    def __str__(self)->str:
        return f"{self.speed} ft flight"