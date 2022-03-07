"""
Inventory.py
By Matthew Graber
"""

# Temp imports for testing
import Weapons, Armor

import tkinter

class Inventory:

    def __init__(self, startingArmor, startingWeapons, startingSpells):
        # Complete inventory
        # Should be an array
        self.__allArmor = startingArmor
        self.__allWeapons = startingWeapons
        self.__allSpells = startingSpells

        #Currently equipped items
        self.__currentArmor = startingArmor[0]
        self.__currentWeapon = startingWeapons[0]
        for i in range(1, len(startingWeapons)):
            if startingWeapons[i].hands == 1:
                self.__currentSideWeapon = startingWeapons[i]
        
        # For unequiping items
        self.unarmored = Armor.Unarmored()
        self.unarmed = Weapons.Unarmed()
        self.__allWeapons.append(self.unarmed)
        self.__allArmor.append(self.unarmored)

    # Returns current equipment
    def getMainWeapon(self):
        return self.__currentWeapon

    def getOffWeapon(self):
        return self.__currentSideWeapon

    def getArmor(self):
        return self.__currentArmor

    # Returns lists of all items
    def getAllWeapons(self):
        return self.__allWeapons
    
    def getAllSideWeapons(self):
        sideWeapons = []
        for i in self.__allWeapons:
            if i.hands == 1:
                sideWeapons.append(i)
        return sideWeapons

    def getAllArmor(self):
        return self.__allArmor

    def getAllSpells(self):
        return self.__allSpells

    # Changes current equipment
    def setMainWeapon(self, num):
        # Ensures that you don't equip the same weapon twice
        if self.__currentSideWeapon == self.__allWeapons[num]:
            if self.__currentWeapon.hands == 1:
                self.__currentSideWeapon = self.__currentWeapon
            elif self.__currentWeapon.name != "Unarmed strike":
                self.__currentSideWeapon = Weapons.Unarmed()
        self.__currentWeapon = self.__allWeapons[num]

    def setOffWeapon(self, num):
        # Ensures that you don't equip the same weapon twice
        if self.__currentWeapon == self.getAllSideWeapons()[num]:
            if self.__currentSideWeapon.hands == 1:
                self.__currentWeapon = self.__currentSideWeapon
            elif self.__currentSideWeapon.name != "Unarmed strike":
                self.__currentWeapon = Weapons.Unarmed()
        self.__currentSideWeapon = self.getAllSideWeapons()[num]
    
    def setArmor(self, num):
        self.__currentArmor = self.__allArmor[num]
    
    # Adders
    def addSpell(self, spell):
        if spell not in self.__allSpells:
            self.__allSpells.append(spell)
    
    def addArmor(self, armor):
        self.__allArmor.append(armor)
    
    def addWeapon(self, weapon):
        self.__allWeapons.append(weapon)

def main():
    pass

if (__name__ == "__main__"):
    main()