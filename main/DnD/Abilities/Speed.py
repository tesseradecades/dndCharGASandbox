from .Abilities import Ability
from ..Character import Character

class Speed(Ability):
    speed = 0
    def __init__(self, speed:int):
        super(Speed,self).__init__()
        self.speed=speed
    def concreteEffect(self,character:Character):
        character.speed=self.speed
    def __str__(self)->str:
        return f"Speed of {self.speed}"