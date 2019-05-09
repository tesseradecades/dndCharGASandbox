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
CLASS_MAP = {
    0:"Berserker Barbarian", 1: "Totem Barbarian",
    2:"Lore Bard", 3:"Valor Bard",
    4:"Knowledge Cleric", 5:"Life Cleric", 6:"Light Cleric", 7:"Nature Cleric",8:"Tempest Cleric",9:"Trickery Cleric",10:"War Cleric",
    11:"Land Druid", 12:"Moon Druid",
    13:"Champion Fighter", 14:"Battlemaster Fighter",15:"Eldritch Knight Fighter",
    16:"Open Hand Monk",17:"Shadow Monk",18:"Four Elements Monk",
    19:"Devotion Paladin",20:"Ancients Paladin",21:"Vengeance Paladin",
    22:"Hunter Ranger",23:"Beast Master Ranger",
    24:"Thief Rogue",25:"Assassin Rogue",26:"Arcane Trickster Rogue",
    27:"Draconic Sorcerer",28:"Wild Magic Sorcerer",
    29:"Fiend Warlock",30:"Archfey Warlock", 31:"Great Old One Warlock",
    32:"Abjuration Wizard",33:"Conjuration Wizard",34:"Divination Wizard",35:"Enchantment Wizard",36:"Evocation Wizard",37:"Illusion Wizard",38:"Necromancy Wizard",39:"Transmutation Wizard"
}
def main(): 
    #print(ClassStrategy(Phenotype.Phenotype(array('b',[0]*188))))
    pass


if __name__ == "__main__":
    main()