import abc
import Enemies
from Weapons import *
from Armor import *
from Spells import *

class Npc:
    def __init__(self, name = ''):
        self.name = name
        self.__hasSpoken = False
        self.__firstGreeting = 'Hello there!'
        self.__greetings = ['']
        self.__locations = ['']
        self.__questions = ['']
        self.__associatedEnemyObject = None
        self.__associatedPNG = ''
        self.__alternativePNG = ''
        
    def setGreetings(self, greetings):
        self.__greetings = greetings
    
    def getGreetings(self):
        return self.__greetings

    def hasSpoken(self, spoken = None):
        if spoken == None:
            return self.__hasSpoken
        else: self.__hasSpoken = spoken

    def setLocations(self, locations):
        self.__locations = locations

    def getLocations(self):
        return self.__locations

    def setAssociatedEnemyObject(self, enemyObject):
        self.__associatedEnemyObject = enemyObject

    def getAssociatedEnemyObject(self):
        return self.__associatedEnemyObject

    def setFirstGreeting(self, firstGreeting):
        self.__firstGreeting = firstGreeting

    def getFirstGreeting(self):
        return self.__firstGreeting

    def setAssociatedPNG(self, png):
        self.__associatedPNG = png

    def getAssociatedPNG(self):
        return self.__associatedPNG

    def setAlternativePNG(self, png):
        self.__alternativePNG = png

    def getAlternativePNG(self):
        return self.__alternativePNG

class Merchant(Npc):
    def __init__(self, name = ''):
        Npc.__init__(self, name)
        self.__goods = []
        self.__salesPrompt = 'What would you like to buy?'
        self.__saleReaction = ['Thank you for buying my goods.']
    
    def setGoods(self, goods):
        self.__goods = goods

    def getGoods(self):
        return self.__goods

    def setSalesPrompt(self, prompt):
        self.__salesPrompt = prompt
        
    def getSalesPrompt(self):
        return self.__salesPrompt

    def setSaleReaction(self, reaction):
        self.__saleReaction = reaction

    def getSaleReaction(self):
        return self.__saleReaction

class Characters:
    def __init__(self):
        self.Boblin = Merchant('Boblin: The Goblin') # Race = Goblin
        self.Boblin.setFirstGreeting("Hee har! I'm Boblin, the Goblin!")
        self.Boblin.setGreetings(["Hee har!", "Heee har, I want to be just like you. Har har har!", "Didja miss me? Har har har!", "Hee har. You're a good person, yes? Har har har!"])
        self.Boblin.setLocations(['City', 'Mountains'])
        self.Boblin.setSalesPrompt('What would yer like to buy?')
        self.Boblin.setSaleReaction(['YEEEEE HOW! Thank yer, my hero. I want ter be yer best friend! Hee har!', 'Tank yer very much, good person!', 'YEEEEE.', 'YAAAAAAAAAAAAAAAAA HOW!'])
        self.Boblin.setAssociatedPNG('boblin.png')
        self.Boblin.setAlternativePNG('evilBoblin.png')
        self.Boblin.setGoods([Shortsword(), WarPick(), Whip(), Longbow(), HeavyCrossbow()])
        self.Boblin.setAssociatedEnemyObject(Enemies.Boblin())

        self.Harold = Merchant('Harold: The Bargainer') #  Race = Dwarf
        self.Harold.setFirstGreeting("My naaaame is Harold. I'm just another old dwaaaaarf; nothing special about me, reeeeally. I have weapons for saaaale if you\'re loooooking to buy.")
        self.Harold.setGreetings(["Hiiiii there! I hope your evening is going well. It's been days since I've dranken—er, I mean—nevermiiind.", "Hey! I would have more for you here, but resources are lacking due to the... unfortunate circumstances.", "Ow! You ran into me! You shall pay with your blood! Ha! I kid, my friend. I have no need for blood. Mmmmmmmmmmmmmm."])
        self.Harold.setSaleReaction(['Yes! That transaction was quite the steal! Well, for me, anyway.', 'Thfhfhranks.', 'Exccccelllent.', 'My faaaavorite customer.', 'Perfect!'])
        self.Harold.setSalesPrompt('Anything catch your eye?')
        self.Harold.setLocations(['Swamp', 'Forest', 'Mountains'])
        self.Harold.setGoods([Pike(), Scimitar(), Flail(), Glaive(), HeavyCrossbow(), Trident()])
        self.Harold.setAssociatedPNG('harold.png')

        self.Merlina = Npc('Merlina: The Mage of Power') #  Race = Magelike
        self.Merlina.setFirstGreeting('Hmmm... I am Merlina... I am one of the Magelike.')
        self.Merlina.setGreetings(['Well... hello there.', 'Hello... again.', 'Hello...', '...', 'Yes, hi...', 'Ummm, hi there...', 'Hmmmm. Yes. Let\'s see.'])
        self.Merlina.setAssociatedPNG('merlina.png')

        self.Merlishnes = Npc('Merlishnes: The Mage of Wisdom') #  Race = Magelike
        self.Merlishnes.setFirstGreeting('I am Merlishnes. And you... you are insignificant.')
        self.Merlishnes.setGreetings(['What are you doing here? I need to be alone right now. Just leave me here.', 'You again. Something seems... off. Do you feel it? Something in the air...'])
        self.Merlishnes.setAssociatedPNG('merlishnes.png')

        self.Donrak = Npc('Donrak: The Purveyor of Good News')
        self.Donrak.setFirstGreeting('Tis I! Donrak: Purveyor of Good News!')
        self.Donrak.setGreetings(['Hello there, you magnificent being!', 'Why, hello there. What a pleasure it is to see you again.', 'Hi there! Once again, tis I—Donrak: Purveyor of Good News!', 'Hey you, remember me? Ha ha! Of course you do! I am the Purveyor of Good News, after all.'])
        self.Donrak.setLocations(['City', 'Mountains', 'Forest', 'Fortress'])
        self.Donrak.setAssociatedPNG('donrak.png')

        self.Matilda = Npc('Matilda: The Warrior') #  Race = Android
        self.Matilda.setFirstGreeting('Haven\'t see you around here before. Name\'s Matilda.')
        self.Matilda.setGreetings(["Why, hello there Fragile Soul.", "I'm a very busy person, Fragile Soul.", "We meet again, Fragile Soul. I'd accompany you on your journey, but... well, I am much older than I used to be. Back in the day, no one would need to accompany me on me journeys. That still makes me sad."])
        self.Matilda.setLocations(['City', 'Swamp'])
        self.Matilda.setAssociatedPNG('matilda.png')

        self.Altaïr = Merchant('Altaïr: The Sorcerer') #  Race = Reaper
        self.Altaïr.setFirstGreeting('My name Altaïr. I am one of the few sorcerers in this world who is not a Magelike. I am a Reaper. I think we\'ll get along well.')
        self.Altaïr.setGreetings(['Oh, hello there. Nice to see you passing by.'])
        self.Altaïr.setLocations(['Swamp', 'Fortress'])
        self.Altaïr.setGoods([HalfPlate(), MithralChain(), Shield(), MagicMissile(), CureWounds(), BoomingBlade(), Morningstar()])
        self.Altaïr.setSalesPrompt('I\'m selling gear and spellbooks. Interested in anything?')
        self.Altaïr.setSaleReaction(['Thank you for your purchase.', 'Ah, yes. That\'s a good one.', 'A wise decision.', 'I thought I saw you eyeing that one. Enjoy.', 'Take it. Just get yourself killed.'])
        self.Altaïr.setAssociatedPNG('altaïr.png')

        self.Ysmay = Npc('Ysmay: The Prophet') #  Race = Magelike
        self.Ysmay.setFirstGreeting('Young one... over here. I sense a great darkness lingering ahead of us.')
        self.Ysmay.setGreetings(['Ah, yes, I have foreseen your arrival.', 'Welcome, Forgotten One.', 'I can see many paths ahead of us. Ultimately, everything comes down to choices.'])
        self.Ysmay.setLocations(['Mountains', 'Swamp', 'Forest', 'City'])
        self.Ysmay.setAssociatedPNG('ysmay.png')

        self.Ryia = Merchant('Ryia: The Elf') #  Race = Elf
        self.Ryia.setLocations(['Swamp', 'Fortress'])
        self.Ryia.setFirstGreeting("You there! I haven't seen your face before.... My name is Ryia. I am a wandering merchant.")
        self.Ryia.setGreetings(["Hello again. You shouldn't have come here. It's dangerous.", "Hi! It's dangerous in these parts. I'd be careful if I were you.", 'As much as I love to have the opportunity of selling you things, try to stay inside more often. It\'s very dangerous outside.'])
        self.Ryia.setSalesPrompt("Interested? Take a look at what I have. Don't try to steal anything, though. I see everything... mostly.")
        self.Ryia.setSaleReaction(['Good deal!', 'Thank you very much!', 'Much appreciated!', 'Thanks for buying my stuff, mate.', 'Nice choice!', 'Oh, that one... okay, then.'])
        self.Ryia.setGoods([StuddedLeather(), ChainShirt(), HalfPlate(), Splint(), Longbow(), Warhammer()])
        self.Ryia.setAssociatedPNG('ryia.png')

        self.Mythergius = Npc('Mythergius: The Eternal Sorcerer')
        self.Mythergius.setLocations(['Mountains', 'Swamp', 'Forest', 'City', 'Fortress'])
        self.Mythergius.setFirstGreeting('I am Mythergius. I am the Wielder of Death itself, yet I am cursed enough to never claim Death\'s rewards.')
        self.Mythergius.setGreetings([''])

        self.completeCharacterList = [self.Boblin, self.Harold, self.Donrak, self.Matilda, self.Altaïr, self.Ysmay, self.Ryia, self.Mythergius]
        self.merchantCharacterList = [self.Ryia, self.Harold, self.Boblin, self.Altaïr]
        self.mountainsCharacters = []
        self.swampCharacters = []
        self.forestCharacters = []
        self.cityCharacters = []
        self.fortressCharacters = []

        for character in self.completeCharacterList:
            if 'Mountains' in character.getLocations():
                self.mountainsCharacters.append(character)

        for character in self.completeCharacterList:
            if 'Swamp' in character.getLocations():
                self.swampCharacters.append(character)

        for character in self.completeCharacterList:
            if 'Forest' in character.getLocations():
                self.forestCharacters.append(character)

        for character in self.completeCharacterList:
            if 'City' in character.getLocations():
                self.cityCharacters.append(character)

        for character in self.completeCharacterList:
            if 'Fortress' in character.getLocations():
                self.fortressCharacters.append(character)






# class Boblin(NPC):
#     name = "Boblin the Goblin"
#     greetings = ["Hee har! I'm Boblin the Goblin!", "Hee har!", "Heee har, I want to be just like you. Har har har!" "Hee har. You're a good person, yes? Har har har!"]
#     sellsGoods = True

# class Altaïr(NPC):
#     name = 'Altaïr'
#     greetings = ['Ahoy!']