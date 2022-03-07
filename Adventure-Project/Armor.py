"""
Armor.py
Matthew Graber
"""

import abc

class Armor(abc.ABC):
    def __init__(self):
        self.armorValue = 30
        self.dodgeValue = 10
        self.isLoud = True
        self.name = 'Generic Armor'
        self.goodType = 'armor'

        self.mutable = True
        self.sellable = True

        self.cost = 30

    def getValue(self):
        return self.armorValue
    
    def getStats(self):
        stats = ''
        stats += "Armor Value: " + str(self.armorValue)
        stats += "\nDodge Vaule: " + str(self.dodgeValue)
        stats += "\nLoud: " + str(self.isLoud)
        return stats

class Unarmored(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Unarmored"
        self.armorValue = 10
        self.dodgeValue = 15
        self.isLoud = False
        self.mutable = False
        self.sellable = False

# Light armor
class Leather(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Leather"
        self.armorValue = 20
        self.dodgeValue = 15
        self.isLoud = False
        self.cost = 10

class StuddedLeather(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Studded Leather"
        self.armorValue = 25
        self.dodgeValue = 15
        self.isLoud = False
        self.cost = 30


# Medium armor
class ChainShirt(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Chain Shirt"
        self.armorValue = 30
        self.dodgeValue = 10
        self.isLoud = False
        self.cost = 20

class ScaleMail(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Scale Mail"
        self.armorValue = 35
        self.dodgeValue = 9
        self.isLoud = True
        self.cost = 30

class Breastplate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Breastplate"
        self.armorValue = 35
        self.dodgeValue = 10
        self.isLoud = False
        self.cost = 50

class HalfPlate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Half Plate"
        self.armorValue = 45
        self.dodgeValue = 8
        self.isLoud = True
        self.cost = 75

# Heavy armor
class ChainMail(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Chain Mail"
        self.armorValue = 50
        self.dodgeValue = 4
        self.isLoud = True
        self.cost = 30

class Splint(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Splint"
        self.armorValue = 65
        self.dodgeValue = 3
        self.isLoud = True
        self.cost = 50

class Plate(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Plate"
        self.armorValue = 75
        self.dodgeValue = 2
        self.isLoud = True
        self.cost = 100

# Special armor
class MithralChain(Armor):
    def __init__(self):
        super().__init__()
        self.name = "Mithral Chain"
        self.armorValue = 45
        self.dodgeValue = 12
        self.isLoud = False
        self.cost = 150