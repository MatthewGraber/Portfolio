"""
Actions.py
By Matthew Graber
Created 3/23/2021
"""

import Weapons
import abc
import GlobalVariables

#Basic action class that all other classes are derived from
#By making it an abstract class
class Action(abc.ABC):
    name = 'Generic action name'
    description = 'Generic action description'
    staminaCost = 0
    magickaCost = 0

    #The function that contains this action's behavior
    def act(self, n):
        pass
    #The function we call to execute this action
    #Will contain the functions to reduce magicka and stamina, plus
    #any other functions that run with any action
    def execute(self, n):
        self.act(n)
        GlobalVariables.PC.changeMagicka(-n*self.magickaCost)
        GlobalVariables.PC.changeStamina(-n*self.staminaCost)

        GlobalVariables.Combat.nextAction()
    
    def canTakeAction(self, currentStaminaCost):
        requiredStamina = GlobalVariables.PC.getStamina() - currentStaminaCost
        if self.staminaCost <= requiredStamina:
            return True
        else:
            return False


"""
All basic actions
"""
class Strike(Action):
    name = 'Strike'
    staminaCost = 0

    def act(self, n):

        mainWeapon = GlobalVariables.PC.inventory.getMainWeapon()
        offWeapon = GlobalVariables.PC.inventory.getOffWeapon()
        if (mainWeapon.hands == 2) or not offWeapon.isWeapon() or n == 1:
            GlobalVariables.PC.hitMain = mainWeapon.attack(n)
            GlobalVariables.PC.hitOff = False
        else:
            GlobalVariables.PC.hitMain = mainWeapon.attack(n-1)
            GlobalVariables.PC.hitOff = offWeapon.attack(1)


class Cast(Action):
    name = 'Cast'
    spell = None

    def execute(self, n):
        self.act(n)

    def act(self, n):
        self.actionsUsed = n
        GlobalVariables.GUI.selectSpellGui([GlobalVariables.GUI.combatFrame])
    
    def castChosenSpell(self, spell, n):
        self.spell = GlobalVariables.PC.inventory.getAllSpells()[spell]
        self.spell.effect(n)
        GlobalVariables.PC.changeMagicka(-n*self.spell.level)
        GlobalVariables.PC.changeStamina(-n*self.staminaCost)
        GlobalVariables.Combat.nextAction()

    # def chooseSpell(self):
    #     # Prompts the player to choose a spell
    #     self.spell = GlobalVariables.PC.inventory.getAllSpells()[0]
    #     # GlobalVariables.GUI.SelectSpell()

class SwapEquipment(Action):
    name = "Swap Equipment"

    def act(self, n):


        GlobalVariables.GUI.swapItemGui([GlobalVariables.GUI.combatFrame])
        # GlobalVariables.Combat.root.destroy()
        # GlobalVariables.PC.inventory.swapItems()
        # GlobalVariables.Combat.battleGui()
    
    def execute(self, n):
        self.act(n)
        GlobalVariables.PC.changeMagicka(-n*self.magickaCost)
        GlobalVariables.PC.changeStamina(-n*self.staminaCost)
    
    def exitInventory(self):
        GlobalVariables.GUI.battleGui([GlobalVariables.GUI.currentItemLabel, GlobalVariables.GUI.buttonFrame])
        GlobalVariables.Combat.nextAction()

class Dodge(Action):
    name = 'Dodge'
    staminaCost = 1

    def act(self, n):
        dodge = GlobalVariables.PC.inventory.getArmor().dodgeValue
        GlobalVariables.PC.tempDodge.addBuff("Dodge action", dodge*(n+1), 1)
        GlobalVariables.GUI.typeOutDelay("Dodging! +" + str(dodge*(n+1)) + " armor this round!")

class Rest(Action):
    name = 'Rest'
    staminaCost = -2
    
    def act(self, n):
        GlobalVariables.GUI.typeOutDelay("Resting. Recovered " + str(n*2) + " stamina.")

class Channel(Action):
    name = 'Channel'
    description = 'Regain magicka equal to the number of actions spent.'
    magickaCost = -1

    def act(self, n):
        GlobalVariables.GUI.typeOutDelay("Channeling. Recovered " + str(n) + " magicka.")


"""
All Archetype-specific Actions
"""
class PresiceStrike(Action):
    name = 'Strike'
    staminaCost = 2

    def act(self, n):
        mainWeapon = GlobalVariables.PC.inventory.getMainWeapon()
        offWeapon = GlobalVariables.PC.inventory.getOffWeapon()
        
        # Temporarily buffs the main weapon's hit chance
        mainWeapon.hit += 15
        offWeapon.hit += 15

        if (mainWeapon.hands == 2) or not offWeapon.isWeapon() or n == 1:
            mainWeapon.attack(n)
        else:
            mainWeapon.attack(n-1)
            offWeapon.attack(1)
        
        mainWeapon.hit -= 15
        offWeapon.hit -= 15

class SwiftDodge(Dodge):
    def __init__(self):
        self.staminaCost = 0

class SuperiorCast(Action):
    name = 'Cast'
    spell = None

    def execute(self, n):
        self.act(n+1)

    def act(self, n):
        self.actionsUsed = n
        GlobalVariables.GUI.selectSpellGui([GlobalVariables.GUI.combatFrame])
    
    def castChosenSpell(self, spell, n):
        self.spell = GlobalVariables.PC.inventory.getAllSpells()[spell]
        self.spell.effect(n)
        GlobalVariables.PC.changeMagicka(-(n-1)*self.spell.level)
        GlobalVariables.PC.changeStamina(-n*self.staminaCost)
        GlobalVariables.Combat.nextAction()


#Main function for testing
def main():
    strike = Strike()
    print("Stamina cost:", strike.staminaCost)
    print("Magicka cost:", strike.magickaCost)
    strike.execute(2)
    print(GlobalVariables.Enemy.getHp())

if (__name__ == "__main__"):
    main()