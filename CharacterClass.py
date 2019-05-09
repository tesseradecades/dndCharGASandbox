class CharacterClass:

    armorProficiencies = set()
    weaponProficiencies = set()
    toolProficiencies = set()
    savingThrowProficiencies = set()
    skillProficiencies = set()
    classAbilities = set()
    
    def __init__(self):
        pass

    """
    def setStats(self):
        self.setHitPoints()
        self.setArmorProficiencies()
        self.setWeaponProficiencies()
        self.setToolProficiencies()
        self.setSavingThrowProficiencies()
        self.setSkillProficiencies()
        self.setAbilities()


    def setHitPoints(self):
        self.phenotype.hitPoints = 4

    def setArmorProficiencies(self):
        p = self.phenotype.armorProficiencies
        for prof in self.armorProficiencies:
            if(prof not in p):
                p.add(prof)
    
    def setWeaponProficiencies(self):
        p = self.phenotype.weaponProficiencies
        for prof in self.weaponProficiencies:
            if(prof not in p):
                p.add(prof)
    
    def setToolProficiencies(self):
        p = self.phenotype.toolProficiencies
        for prof in self.toolProficiencies:
            if(prof not in p):
                p.add(prof)

    def setSavingThrowProficiencies(self):
        p = self.phenotype.savingThrowProficiencies
        for prof in self.savingThrowProficiencies:
            if(prof not in p):
                p.add(prof)

    def setSkillProficiencies(self):
        p = self.phenotype.skillProficiencies
        for prof in self.skillProficiencies:
            if(prof not in p):
                p.add(prof)

    def setAbilities(self):
        p = self.phenotype.abilities
        for ability in self.classAbilities:
            if(ability not in p):
                p.add(prof)   
    """
    def __str__(self) -> str:
        return "None"

def main(): 
    #print(ClassStrategy(Phenotype.Phenotype(array('b',[0]*188))))
    pass


if __name__ == "__main__":
    main()