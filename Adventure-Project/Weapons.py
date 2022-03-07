"""
Weapons.py
By Matthew Graber
Last Edit: 3/26/2021
"""


import abc, random, time

import GlobalVariables

class Weapon(abc.ABC):

   def __init__(self):
      self.name = ''
      self.damage = 5
      self.hands = 1
      self.weight = 2
      self.block = 5
      self.ranged = False
      self.loading = False
      self.goodType = 'weapon'
      self.loaded = True
      self.cost = 20

      # Special tags for unarmed and other specials
      self.mutable = True
      self.sellable = True
      
      # Chance of something happening
      # All but hit are only relevant with characters with Precise Strike
      # Range 0 to 100
      self.hit = 75
      self.trip = 20
      self.disarm = 20
      self.shove = 20
      self.counter = 20

   # a is the number of actions used
   def attack(self, a):
      hit = False
      GlobalVariables.PC.changeStamina(-self.weight*a)

      # If you have a loading weapon, loading it takes one action
      if self.loading and not self.loaded:
         self.loaded = True
         a -= 1

      if a != 0:
         # Determines your hit modifier
         modifier = self.hit + GlobalVariables.PC.tempHitBuff.get() - GlobalVariables.Enemy.armor
         if GlobalVariables.Enemy.flying and not self.ranged:
            modifier -= 25
         
         
         miss = ((100-modifier)/100)**a # You effectively gain one additionall chance to hit for each action you spend, but can only hit once
         roll = random.randint(1, 100)

         if miss*100 <= roll:
            # print("Hit with", self.name)
            damage = self.damage + GlobalVariables.PC.tempDamageBuff.get()
            GlobalVariables.GUI.typeOutDelay("Hit with " + self.name + " for " + str(damage) + " damage!")

            GlobalVariables.Enemy.takeDamage(damage)
            hit = True
         else:
            GlobalVariables.GUI.typeOutDelay("Missed with " + self.name + "!")
         if self.loading:
            self.loaded = False
         
      else:
         GlobalVariables.GUI.typeOutDelay("Loaded " + self.name)
      
      return hit
   
   def tripAttack(self):
      pass

   def disarmAttack(self):
      pass
   
   def isWeapon(self):
      return True
   
   def getStats(self):
      stats = ''
      stats += 'Damage: ' + str(self.damage)
      stats += '\nHit chance: ' + str(self.hit)
      stats += '\nHands: ' + str(self.hands)
      stats += '\nWeight: ' + str(self.weight)
      stats += '\nRanged: ' + str(self.ranged)
      if self.loading:
         stats += '\nLoaded: ' + str(self.loaded)
      # stats += '\nTrip chance: ' + str(self.trip)
      # stats += '\nDisarm chance: ' + str(self.disarm)
      # stats += '\nShove chance: ' + str(self.shove)
      # stats += '\nCounter chance: ' + str(self.counter)

      return stats


#Different weapons
class Unarmed(Weapon):
   def __init__(self):
      super().__init__()
      self.hit = 50
      self.damage = 2
      self.weight = 0
      self.name = "Unarmed strike"
      self.mutable = False
      self.sellable = False

# class BusterSword(Weapon):
#    def __init__(self):
#       super().__init__()
#       self.hit = 1000
#       self.damage = 999
#       self.ranged = True
#       self.name = "Buster Sword"

class Battleaxe(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Battleaxe'
      self.hands = 2
      self.weight = 2
      self.hit = 70
      self.damage = 8
      self.cost = 10

class Dagger(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Dagger'
      self.weight = 0
      self.hit = 80
      self.damage = 3
      self.cost = 5

class Flail(Weapon):       
   def __init__(self):     
      super().__init__()
      self.name = 'Flail'
      self.hit = 70
      self.damage = 6
      self.weight = 2
      self.cost = 10

class Glaive(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Glaive'
      self.hands = 2
      self.hit = 75
      self.damage = 9
      self.weight = 3
      self.cost = 20

class GreatAxe(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Greateaxe'
      self.hands = 2
      self.damage = 15
      self.hit = 50
      self.weight = 3
      self.cost = 30

class Greatsword(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Greatsword'
      self.hands = 2
      self.damage = 12
      self.hit = 60
      self.weight = 3
      self.cost = 30

class Halberd(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Halberd'
      self.hands = 2
      self.hit = 65
      self.damage = 11
      self.weight = 3
      self.cost = 20

class Lance(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Lance'
      self.hands = 2
      self.cost = 10

class Longsword(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Longsword'
      self.hands = 2
      self.hit = 85
      self.damage = 8
      self.weight = 2
      self.cost = 15

class Maul(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Maul'
      self.hands = 2
      self.hit = 55
      self.damage = 18
      self.weight = 4
      self.cost = 50

class Morningstar(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Morningstar'
      self.cost = 15

class Pike(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Pike'
      self.cost = 15

class Rapier(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Rapier'
      self.weight = 1
      self.hit = 100
      self.damage = 5
      self.cost = 25

class Scimitar(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Scimitar'
      self.hit = 95
      self.weight = 2
      self.damage = 7
      self.cost = 25

class Shortsword(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Shortsword'
      self.weight = 1
      self.hit = 90
      self.damage = 5
      self.cost = 10

class Trident(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Trident'
      self.cost = 5

class WarPick(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'War pick'
      self.cost = 5

class Warhammer(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Warhammer'
      self.damage = 10
      self.hands = 2
      self.weight = 2
      self.hit = 70
      self.cost = 15

class Whip(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Whip'
      self.cost = 5

class Longbow(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Longbow'
      self.ranged = True
      self.damage = 6
      self.hands = 2
      self.hit = 85
      self.cost = 40

class Shortbow(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Shortbow'
      self.ranged = True
      self.hit = 100
      self.damage = 4
      self.hands = 2
      self.weight = 1
      self.cost = 25
   
class HandCrossbow(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Hand Crossbow'
      self.ranged = True
      self.hit = 100
      self.damage = 6
      self.weight = 1
      self.hands = 2
      self.loading = True
      self.loaded = True
      self.cost = 60

class LightCrossbow(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Light Crossbow'
      self.ranged = True
      self.hands = 2
      self.hit = 100
      self.damage = 7
      self.loading = True
      self.loaded = True
      self.cost = 25

class HeavyCrossbow(Weapon):
   def __init__(self):
      super().__init__()
      self.name = 'Heavy Crossbow'
      self.ranged = True
      self.hands = 2
      self.damage = 10
      self.hit = 85
      self.weight = 3
      self.loading = True
      self.loaded = True
      self.cost = 50

