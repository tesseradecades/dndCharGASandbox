from .Background import Background
from ..Skills import Skills
class Acolyte(Background):
    def __init__(self):
        super(Acolyte,self).__init__()
    def getSkillProficiencies(self)->set:
        return {Skills.Insight,Skills.Religion}