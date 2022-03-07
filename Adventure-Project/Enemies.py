import abc, random
import GlobalVariables

class Enemy(abc.ABC):
    
    def __init__(self):
        self.name = 'Generic enemy name'
        self.hp = 1 # Hit points
        self.armor = 20
        self.ap = [0, 1] # Attack power (range)
        self.tier = "weak" # Can be weak, average, or strong
        self.alive = True
        self.flying = False
        self.hasHit = False # Should be true if it hit on its last turn
        self.gemStones = random.randint(1, 35)
        self.turn = 0 # Tracks the round for the purpose of the attack pattern
        self.displayMessage = "Enemy intends to attack!"

    # Getters
    def getHp(self):
        return self.hp
    def getArmor(self):
        return self.armor
    def getTier(self):
        return self.tier
    def getAlive(self):
        return self.alive
    def getFlying(self):
        return self.flying
    
    # Setterss
    def takeDamage(self, damage):
        self.hp -= damage
        if (self.hp <= 0):
            self.alive = False    
    def heal(self, healing):
        self.hp += healing
    
    # Attacks
    def genericAttack(self, attackRange, pcArmor, message):
        roll = random.randint(1,100)

        self.sendMessage(message)
        # GlobalVariables.GUI.typeOutDelay("Requires " + str(pcArmor) + " to hit.")
        if roll >= pcArmor:
            damage = random.randint(attackRange[0], attackRange[1])
            GlobalVariables.PC.takeDamage(damage)
            self.sendMessage(str(roll) + " to hit! You take " + str(damage) + " damage!")
            self.hasHit = True
        else:
            self.sendMessage(str(roll) + " to hit! Miss!")
            self.hasHit = False
    
    def basicAttack(self, attackRange, message=" attacking..."):
        self.genericAttack(attackRange, GlobalVariables.PC.getDefense(), message)
    
    def touchAttack(self, attackRange, message= " attacking..."):
        self.genericAttack(attackRange, GlobalVariables.PC.getTouch(), message)

    def flatFootedAttack(self, attackRange, message=" attacking..."):
        self.genericAttack(attackRange, GlobalVariables.PC.getFlatFooted(), message)

    def mainAttack(self, message=" attacking..."):
        self.basicAttack(self.ap, message)
    
    # Sets the pattern of the attacks
    def attackPattern(self):
        self.mainAttack()

    # Runs the attacks
    def attackCycle(self):
        self.attackPattern()
        GlobalVariables.GUI.updateStats()
        self.turn += 1
    
    def sendMessage(self, message):
        self.displayMessage = message
        GlobalVariables.Combat.setDisplay()

    def display(self):
        message = ''
        # message += self.name + " HP: " + str(self.getHp())
        message += self.displayMessage
        return message


class EnemyAbility:
    class PlayerStatusEffect(abc.ABC):
        pass

    class GlobalStatusEffect(abc.ABC):
        pass

    class SelfStatusEffect(abc.ABC):
        pass

    class DamageInfliction(abc.ABC):
        pass

class Slime(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Slime'
        self.hp = 4
        self.ap = [1, 1]

class Bilgesnipe(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Bilgesnipe'
        self.hp = 18
        self.ap = [5, 7]

# class BountyHunter(Enemy):
#     def __init__(self):
#         self.hp = 25
#         self.ap = [8, 12]
    
class Mage(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Posessed Mage'
        self.hp = 20
        self.ap = [3,9]

class Boblin(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Boblin: The Goblin'
        self.hp = 20
        self.ap = [17, 20]

class Mythergius(Enemy):
    def __init__(self):
        super().__init__()
        self.name = 'Mythergius: The Eternal Sorcerer'
        self.hp = 20
        self.ap = [15, 24]

class Annith(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 30
        self.ap = [3, 6]
        self.armor = 30
        self.name = "Annith Mech Warrior"
        self.displayMessage = "The Annith intends to LAUNCH A BARRAGE and then ASSIMILATE!"
        self.tier = 'strong'
    
    def assimilate(self):
        GlobalVariables.GUI.typeOutDelay("The Annith is ASSIMILATING! It heals 2, increases armor by 3 and damage by 1!")
        self.hp += 2
        self.ap[0] += 1
        self.ap[1] += 1
        self.armor += 3
    
    def attackPattern(self):
        self.flatFootedAttack(self.ap, message="Annith is LAUNCHING A BARRAGE...")
        self.assimilate()
        self.displayMessage = "The Annith intends to LAUNCH A BARRAGE and then ASSIMILATE!"


class BlackPudding(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 15
        self.ap = [3,6]
        self.name = "Black Pudding"
        self.tier = "middle"
        self.displayMessage = "The Black Pudding intends to CORRODE!"
    
    def corrode(self):
        self.basicAttack(self.ap, message="Gloop glop...")
        armor = GlobalVariables.PC.inventory.getArmor()
        if self.hasHit and armor.mutable:
            GlobalVariables.GUI.typeOutDelay("Your armor is being CORRODED! Permanent -5 to it's armor value!")
            armor.armorValue -= 5
        elif self.hasHit and armor.name == "Unarmored":
            GlobalVariables.GUI.typeOutDelay("Without any armor to protect you, the ooze burns \nyour skin like acid! You take an additional 3 damage!")
            GlobalVariables.PC.takeDamage(3)
    
    def corrodeWeapon(self, weapon, hitWithWeapon):
        if hitWithWeapon and not weapon.ranged and weapon.mutable:
            GlobalVariables.GUI.typeOutDelay("As your " + weapon.name + " connects with the ooze, \nit begins to corrode! Permanent -5 penalty to hit and -1 penalty to damage!")
            weapon.hit -= 5
            weapon.damage -= 1
        elif hitWithWeapon and weapon.name == "Unarmed strike":
            GlobalVariables.GUI.typeOutDelay("You strike the gelatinous sludge with your bare hand, \nand it melts your skin like butter! You take 3 damage!")
            GlobalVariables.PC.takeDamage(3)

    def attackPattern(self):
        mainWeapon = GlobalVariables.PC.inventory.getMainWeapon()
        offWeapon = GlobalVariables.PC.inventory.getOffWeapon()
        self.corrodeWeapon(mainWeapon, GlobalVariables.PC.hitMain)
        self.corrodeWeapon(offWeapon, GlobalVariables.PC.hitOff)
        
        self.corrode()
        self.displayMessage = "The Black Pudding intends to CORRODE!"
            

class Chimera(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 20
        self.name = "Chimera"
        self.flying = True
        self.tier = "strong"
        self.ap = [2, 4]
        self.displayMessage = "The Chimera intends to use FIRE BREATH!"
    
    def fireBreath(self):
        self.touchAttack([3, 6], message="Chimera is BREATHING FIRE!")
        if self.hasHit:
            GlobalVariables.GUI.typeOutDelay("You are on fire!")
            GlobalVariables.PC.persistentDamage.addBuff("Fire", 2, 3)
        pass

    def attackPattern(self):
        if self.turn % 3 == 0:
            self.fireBreath()
            self.displayMessage = "The Chimera intends to BITE and CLAW!"
        elif self.turn % 3 == 1:
            self.basicAttack(self.ap, message="Chimera biting...")
            self.basicAttack(self.ap, message="Chimera clawing...")
            self.flying = False
            self.displayMessage = "The Chimera intends to FLY!"
        else:
            self.hasHit = False
            self.flying = True
            GlobalVariables.GUI.typeOutDelay("The Chimera is FLYING!")
            self.displayMessage = "The Chimera intends to use FIRE BREATH!"


class GiantSpider(Enemy):
    def __init__(self):
        super().__init__()
        self.hp = 15
        self.name = "Giant Spider"
        self.tier = "middle"
        self.ap = [1,2]
        self.displayMessage = "The Giant Spider intends to SHOOT WEBS!"

    def shootWebs(self):
        pcArmor = GlobalVariables.PC.getDefense()
        roll = random.randint(1,100)

        self.sendMessage("The Giant Spider is SHOOTING WEBS!")
        if roll >= pcArmor:
            self.sendMessage(str(roll) + " to hit! You are restrained by webs! -20 to dodge and attack rolls!")
            GlobalVariables.PC.tempDodge.addBuff("Webs", -20, 3)
            GlobalVariables.PC.tempHitBuff.addBuff("Webs", -20, 3)
            self.hasHit = True
        else:
            self.sendMessage(str(roll) + " to hit! Miss!")
            self.hasHit = False
    
    def bite(self):
        self.basicAttack(self.ap, message="Biting...")
        if self.hasHit:
            GlobalVariables.PC.persistentDamage.addBuff("Poison", 2, 3, stacks=True)
            self.sendMessage("You have been poisoned!")

    def attackPattern(self):
        if self.turn % 2 == 1:
            self.bite()
            self.displayMessage = "The Giant Spider intends to SHOOT WEBS!"
        else:
            self.shootWebs()
            self.displayMessage = "The Giant Spider intends to BITE!"


class Reaper(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "REAPER"
        self.armor = 15
        self.hp = 30
        self.ap = [10, 20]
        self.intagible = False
        self.displayMessage = "The REAPER intends to DRAIN YOUR SOUL!"
        self.tier = "strong"
    
    def takeDamage(self, damage):
        if self.intagible:
            GlobalVariables.GUI.typeOutDelay("The REAPER is INTANGIBLE and takes no damage!")
        else:
            super().takeDamage(damage)

    def wraithForm(self):
        self.intagible = True

    def soulDrain(self):
        GlobalVariables.GUI.typeOutDelay("REAPER is DRAINING YOUR SOUL! Cumulative -1 to everything and 1 damage to HP, Stamina, and Magicka each round!")
        GlobalVariables.PC.tempArmor.addBuff("Soul Drain", -1, "Encounter", stacks=True)
        GlobalVariables.PC.tempDodge.addBuff("Soul Drain", -1, "Encounter", stacks=True)
        GlobalVariables.PC.tempHitBuff.addBuff("Soul Drain", -1, "Encounter", stacks=True)
        GlobalVariables.PC.tempDamageBuff.addBuff("Soul Drain", -1, "Encounter", stacks=True)
        GlobalVariables.PC.persistentDamage.addBuff("Soul Drain", 1, "Encounter", stacks=True)
        GlobalVariables.PC.persistentStaminaDrain.addBuff("Soul Drain", 1, "Encounter", stacks=True)
        GlobalVariables.PC.persistentMagickaDrain.addBuff("Soul Drain", 1, "Encounter", stacks=True)
    
    def harvest(self):
        self.basicAttack(self.ap, message="The REAPER swings it's scythe towards you...")
    
    def attackPattern(self):
        if self.turn % 3 == 0:
            self.soulDrain()
            self.displayMessage = "The REAPER will enter WRAITH FORM to become INTANGIBLE!"
        elif self.turn % 3 == 1:
            self.wraithForm()
            self.displayMessage = "The REAPER intends to HARVEST!"
        else:
            self.harvest()
            GlobalVariables.GUI.typeOutDelay("The REAPER is no longer INTAGIBLE")
            self.intagible = False
            self.displayMessage = "The REAPER intends to DRAIN YOUR SOUL!"


def main():
    # chim = Chimera()
    # print(chim.getHp())
    # chim.takeDamage(5)
    # print(chim.getHp())
    # print("Current HP:", GlobalVariables.PC.currentHP())
    # for i in range(0, 5):
    #     chim.attackCycle()
    # print("Current HP:", GlobalVariables.PC.currentHP())
    pass

if (__name__ == "__main__"):
    main()