class Dwarf():
    def getAbilities(self)->set:
        return set()
class HillDwarf(Dwarf):
    def __init__(self):
        super(HillDwarf,self).__init__()
    def __str__(self)->str:
        return "Hill Dwarf"