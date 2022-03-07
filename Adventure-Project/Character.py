"""
Character.py
By Matthew Graber
Created 3/23/2021
"""

import Spells
import Actions, Weapons, Inventory, Armor, GlobalVariables, Enemies, StatusEffects
import abc

class Character():

    archetype = ''
    maxHP = 80
    maxStamina = 10
    maxMagicka = 5
    energy = 3
    startingItems = [[],[]]
    startingSpells = []
    inventory = None

    # Conditions
    alive = True
    hitMain = False
    hitOff = False

    # Temporary boosts go here
    # Boosts should be added as [source, value, duration]
    tempArmor = StatusEffects.TempBuff()
    tempDodge = StatusEffects.TempBuff()
    tempDamageBuff = StatusEffects.TempBuff()
    tempHitBuff = StatusEffects.TempBuff()
    tempActionBuff = StatusEffects.TempBuff()

    # Persistent end of round effects go here
    persistentDamage = StatusEffects.TempBuff()
    persistentStaminaDrain = StatusEffects.TempBuff()
    persistentMagickaDrain = StatusEffects.TempBuff()

    #Actions
    strike = Actions.Strike()
    cast = Actions.Cast()
    dodge = Actions.Dodge()
    swapEquipment = Actions.SwapEquipment()
    rest = Actions.Rest()
    channel = Actions.Channel()
    actions = []

    #A method that runs at the end of the Archetype's __init__ function
    def startUp(self):
        self.__hp = self.maxHP
        self.__stamina = self.maxStamina
        self.__magicka = self.maxMagicka
        self.inventory = Inventory.Inventory(self.startingItems[0], self.startingItems[1], self.startingSpells)
        self.actions.append(self.strike) #All basic actions
        self.actions.append(self.cast)
        self.actions.append(self.dodge)
        self.actions.append(self.swapEquipment)
        self.actions.append(self.rest)
        self.actions.append(self.channel)

        # Cheats
        # self.inventory.addWeapon(Weapons.BusterSword())

    def increaseMaxHP(self, increase):
        self.maxHP += increase

    def takeDamage(self, damage):
        self.__hp -= damage
        if self.__hp <= 0:
            self.alive = False

    def heal(self, heal):
        self.__hp += heal
        if self.__hp > self.maxHP:
            self.__hp = self.maxHP

    def changeStamina(self, change):
        self.__stamina += change
        if self.__stamina > self.maxStamina:
            self.__stamina = self.maxStamina
        # If the player for some reason loses more stamina than they have, they take damage equal to the excess
        elif self.__stamina < 0:
            GlobalVariables.GUI.typeOutDelay("You overexert yourself and take " + str(-self.__stamina*2) + " damage!")
            self.takeDamage(-self.__stamina*2)
            self.__stamina = 0
    
    def changeMagicka(self, change):
        self.__magicka += change
        if self.__magicka > self.maxMagicka:
            self.__magicka = self.maxMagicka
        elif self.__magicka < 0:
            GlobalVariables.GUI.typeOutDelay("You pull too much magicka from the weave and take " + str(-self.__magicka*3) + " damage!")
            self.takeDamage(-self.__magicka*3)
            self.__magicka = 0

    #Getters
    def getActions(self):
        return self.actions
    
    def getArchetype(self):
        return self.archetype
    
    def getHp(self):
        return self.__hp

    def getStamina(self):
        return self.__stamina

    def getMagicka(self):
        return self.__magicka

    # Return defense values
    def getDefense(self):
        return self.getFlatFooted() + self.getTouch()
    # For attacks that cannot be avoided
    def getFlatFooted(self):
        block = self.inventory.getArmor().armorValue + self.tempArmor.get()
        if block > 0:
            return block
        return 0
    # For attacks that cannot be blocked
    def getTouch(self):
        dodge = 10 + self.inventory.getArmor().dodgeValue + self.tempDodge.get()
        if dodge > 0:
            return dodge
        return 0
    
    # def display(self):
    #     message = ''
    #     message += 'HP: ' + str(self.getHp())
    #     message += '   Stamina: ' + str(self.getStamina())
    #     message += '   Magicka: ' + str(self.getMagicka())
    #     return message

    # Other methods
    def endOfRound(self):
        # Reduces temporary buffs
        self.tempArmor.reduceAll()
        self.tempDodge.reduceAll()
        self.tempDamageBuff.reduceAll()
        self.tempHitBuff.reduceAll()
        self.tempActionBuff.reduceAll()

        for i in self.persistentDamage.buff:
            self.takeDamage(i[1])
            GlobalVariables.GUI.typeOutDelay("You take " + str(i[1]) + " damage from " + i[0] + "!")
        self.persistentDamage.reduceAll()

        for i in self.persistentStaminaDrain.buff:
            self.changeStamina(-i[1])
            GlobalVariables.GUI.typeOutDelay("You take " + str(i[1]) + " stamina damage from " + i[0] + "!")
        self.persistentStaminaDrain.reduceAll()

        for i in self.persistentMagickaDrain.buff:
            self.changeMagicka(-i[1])
            GlobalVariables.GUI.typeOutDelay("You take " + str(i[1]) + " magicka damage from " + i[0] + "!")
        self.persistentMagickaDrain.reduceAll()

        # Updates various statuses
        self.hitMain = False
        self.hitOff = False
        self.changeStamina(2)
        GlobalVariables.GUI.updateStats()
        GlobalVariables.GUI.typeOutDelay("Recovering 2 stamina.")
        self.energy = 3
    
    def endOfCombat(self):
        self.tempActionBuff.endSingleCombatEffects()
        self.tempArmor.endSingleCombatEffects()
        self.tempDamageBuff.endSingleCombatEffects()
        self.tempDodge.endSingleCombatEffects()
        self.tempHitBuff.endSingleCombatEffects()

        self.persistentDamage.endSingleCombatEffects()
        self.persistentStaminaDrain.endSingleCombatEffects()
        self.persistentMagickaDrain.endSingleCombatEffects()

        self.endOfRound()

class Fighter(Character):
    def __init__(self):
        # self.defaultValues()
        self.archetype = 'Fighter'
        self.maxHP = 90 #Placeholder value for __hp
        self.maxStamina = 15 #Placeholder value for __stamina
        # self.strike = Actions.PresiceStrike()
        self.startingItems = [[Armor.ScaleMail()], [Weapons.Greatsword(), Weapons.Shortsword(), Weapons.Longbow(), Weapons.HeavyCrossbow()]]
        self.startingSpells = [Spells.MageArmor()]
        self.tempHitBuff.addBuff("Fighter", 20, "Permanent")
        self.startUp()


class Rogue(Character):
    def __init__(self):
        self.archetype = 'Rogue'
        self.dodge = Actions.SwiftDodge()
        self.startingItems = [[Armor.Leather()], [Weapons.Shortsword(), Weapons.Shortsword(), Weapons.Shortbow(), Weapons.LightCrossbow()]]
        self.startingSpells = [Spells.MageArmor()]
        self.startUp()

class Wizard(Character):
    def __init__(self):
        self.archetype = 'Wizard'
        self.maxHP = 70
        self.maxStamina = 5 #Placeholder value for __stamina
        self.maxMagicka = 10 #Placeholder value for __magicka
        self.cast = Actions.SuperiorCast()
        self.startingItems = [[Armor.Leather()], [Weapons.Greatsword(), Weapons.Shortsword(), Weapons.Shortbow()]]
        self.startingSpells = [Spells.MageArmor(), Spells.MagicMissile(), Spells.HuntersMark(), Spells.CureWounds(), Spells.BoomingBlade(), Spells.Shield()]
        self.startUp()

# Testing function
def main():
    pass

    
    

if (__name__ == "__main__"):
    main()