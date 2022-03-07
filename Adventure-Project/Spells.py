import abc
import GlobalVariables

# class Spells:
#     class Fire:
#         chanceBurn = .2
#         range = [3, 8]

class Spell(abc.ABC):

    def __init__(self):
        self.level = 1
        self.goodType = 'spell'
        self.name = ""
        self.description = "Generic spell description"
        self.target = GlobalVariables.Enemy
        self.actionMessage = "Generic spell message"
        self.cost = 40

    # Getters
    def getName(self):
        return self.name

    def getLevel(self):
        return self.level

    # Effects
    def effect(self, n):
        pass

class BoomingBlade(Spell):
    def __init__(self):
        super().__init__()
        self.name = 'Booming Blade'
        self.cost = 30
        self.description = "Make attacks as if you used the strike action, \nbut buff your weapon's hit by 10 and its damage by 3."
    
    def effect(self, n):
        # Buffs weapons
        GlobalVariables.PC.inventory.getMainWeapon().hit += 10
        GlobalVariables.PC.inventory.getOffWeapon().hit += 10
        GlobalVariables.PC.inventory.getMainWeapon().damage += 3
        GlobalVariables.PC.inventory.getOffWeapon().damage += 3
        
        self.actionMessage = "Now for my special blue attack!"
        GlobalVariables.GUI.typeOutDelay(self.actionMessage)
        GlobalVariables.PC.actions[0].act(n)

        # Reseting weapon values
        GlobalVariables.PC.inventory.getMainWeapon().hit -= 10
        GlobalVariables.PC.inventory.getOffWeapon().hit -= 10
        GlobalVariables.PC.inventory.getMainWeapon().damage -= 3
        GlobalVariables.PC.inventory.getOffWeapon().damage -= 3

class Shield(Spell):
    def __init__(self):
        super().__init__()
        self.name = 'Shield'
        self.cost = 30
        self.description = "Increases your armor by 20, plus an additional \n20 for each action spent. Lasts 1 round."
        self.target = GlobalVariables.PC

    def effect(self, n):
        buff = 20 + 20*n
        GlobalVariables.PC.tempArmor.addBuff(self.name, buff, 1)
        self.actionMessage = "+" + str(buff) + " armor for this round!"
        GlobalVariables.GUI.typeOutDelay(self.actionMessage)

class HuntersMark(Spell):
    def __init__(self):
        super().__init__()
        self.name = "Hunter's Mark"
        self.cost = 40
        self.description = "Increases your damage per hit by the 3. \nLasts 2 rounds plus an extra 2 for each action spent."

    def effect(self, n):
        GlobalVariables.PC.tempDamageBuff.addBuff(self.name, 3, 2*(n+1))
        self.actionMessage = "+3 damage to all attacks for the next " + str(2*(n+1)) + " rounds!"
        GlobalVariables.GUI.typeOutDelay(self.actionMessage)

class CureWounds(Spell):
    def __init__(self):
        super().__init__()
        self.cost = 50
        self.name = "Cure Wounds"
        self.description = "Heals you for 2 points of damage, \nplus an additional 2 for each action spent."
    
    def effect(self, n):
        heal = n*2 + 2
        self.actionMessage = "Healing " + str(heal) + " HP!"
        GlobalVariables.PC.heal(heal)
        GlobalVariables.GUI.typeOutDelay(self.actionMessage)

class MagicMissile(Spell):
    def __init__(self):
        super().__init__()
        self.name = "Magic Missile"
        self.cost = 50
        self.description = "Sends unerring missiles of magical energy. \nThe spell fires one missile plus an \naddition one for each action you spend on it, \nand each missile deals 2 points of damage."
    
    def effect(self, n):
        damage = n*2 + 2
        self.actionMessage = "Firing " + str(n+1) + " darts! " + GlobalVariables.Enemy.name + " takes " + str(damage) + " damage!"
        GlobalVariables.Enemy.takeDamage(damage)
        GlobalVariables.GUI.typeOutDelay(self.actionMessage)

class MageArmor(Spell):
    def __init__(self):
        super().__init__()
        self.name = 'Mage Armor'
        self.cost = 40
        self.description = "Increases your armor by 10 for 2 rounds, \nplus an additional 2 for each action spent"
        self.target = GlobalVariables.PC

    def effect(self, n):
        GlobalVariables.PC.tempArmor.addBuff(self.name, 10, 2*(n+1))
        self.actionMessage = "+10 armor for the next " + str(2*(n+1)) + " rounds!"
        GlobalVariables.GUI.typeOutDelay(self.actionMessage)

# class BurningHands(Spell):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Burning Hands'

# class Thunderwave(Spell):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Thunderwave'

# class Web(Spell):
#     def __init__(self):
#         super().__init__()
#         self.name = 'Web'
#         self.level = 2