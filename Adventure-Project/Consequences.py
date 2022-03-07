import Conditions
import tkinter
import Inventory
import GlobalVariables
import Encounters

class allConsequences:
    def __init__(self):
        pass

    def IrritateBoblin(self):
        self.__destroyDecision()
        Conditions.SetCondition('MetBob', True)
        for condition in GlobalVariables.conditionsList:
            if condition.name == 'BoblinPathInstantiated':
                condition.counter += 1
                if condition.counter >= 3:
                    condition.met = True
        
        GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Boblin, ['Ahoo! Yer hit me!', 'Thatta really hurted!', 'Oh, please don\'t do that again!'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Boblin, lambda: GlobalVariables.GUI.startNarration(['You aren\'t sure what that was about, but apparently the goblin didn\'t mean you any harm.', 'The Magelike are expecting you. You continue to make your way across the rocky landscape.'], Encounters.runNextEncounter)))

    def StartleBoblin(self):
        self.__destroyDecision()
        Conditions.SetCondition('MetBob', True)
        GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Boblin, ['Awow there! Yeez nearly hit me with that thing!', 'Yee\'d better watch what yer doin\'!'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Boblin, Encounters.runNextEncounter))

    def EscapeBoblin(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You sprint in whichever direction you think the noises aren\'t coming from.', 'You manage to get away.', 'You continue to traverse the through the mountains.'], Encounters.runNextEncounter)
        Conditions.SetCondition('RanFromBoblin', True)

    def FallOffCliff(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You sprint in whichever direction you think the noises aren\'t coming from.', 'You fall off of the mountainside and land on a giant rock.', 'Ouch.', '3 damage taken.', 'Whatever seemed to have been following you, it definitely isn\'t here anymore.'], self.__cliffExtended)
        
    def __cliffExtended(self):
        GlobalVariables.GUI.PC.takeDamage(3)
        GlobalVariables.GUI.setHP(GlobalVariables.GUI.PC.getHp())
        Conditions.SetCondition('RanFromBoblin', True)
        Encounters.runNextEncounter()

    def BoblinSurprise(self):
        self.__destroyDecision()
        Conditions.SetCondition('MetBob', True)
        GlobalVariables.GUI.startNarration(['You sprint in whichever direction you think the noises aren\'t coming from.', 'You tremble and nearly fall off of a ledge.', 'Luckily, you\'re able to regain your footing and keep on the move for a while.', 'The noises seem to have passed, and the air is clear now.', 'You look behind you. No one appears to have followed.', 'Relieved, you stretch and turn back around again... oh no.', '\"HEEEEEEEEEEEEE HOW!\"'], lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Boblin, ['You! Er, hey! What\'s the matter!'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Boblin, Encounters.runNextEncounter)))
        
    def getBittenByChimera(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You see plenty of good hiding spots, so you might as well take what\'s guaranteed.', 'You squeeze between the cracks of a very large pile of boulders.', 'Ouch!', 'It\'s a... it\'s...', 'A baby chimera!', 'You\'ve ended up in a chimera\'s crib!', 'The adrenaline from the bite lets you use an insane amount of strength to push back through the boulders before any of the other babies realize you\'re there.', 'You run away from the nest, faster than ever, without looking back.', 'You lose 1 stamina.'], self.__chimeraBiteExtended)
    
    def __chimeraBiteExtended(self):
        GlobalVariables.GUI.PC.changeStamina(-1)
        GlobalVariables.GUI.setStamina(GlobalVariables.GUI.PC.getStamina())
        Encounters.runNextEncounter()

    def findHidingSpot(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You see plenty of good hiding spots, so you might as well take what\'s guaranteed.', 'You find a spot underneath a wide log, and you pray to the gods they won\'t be able to follow your scent.', 'You stay there until you\'re sure nothing is coming.', 'Relieved, you venture forth.'], Encounters.runNextEncounter)

    def catchingUpToYou(self):
        self.__destroyDecision()
        try:
            GlobalVariables.FixedEncounters.insert(GlobalVariables.CurrentEncounterNumber + 2, Encounters.LoneChimera())
        except:
            pass
        try:
            GlobalVariables.FixedEncounters.insert(GlobalVariables.CurrentEncounterNumber + 5, Encounters.LoneChimera())
        except:
            pass
        try:
            GlobalVariables.FixedEncounters.insert(GlobalVariables.CurrentEncounterNumber + 14, Encounters.DualChimeras())
        except:
            pass
        GlobalVariables.GUI.startNarration(['Running is definitely a good idea. They\'ve already seen you, after all.', 'You take off accross the rocky terrain, only to discover that you are more exposed than before.', 'You are terrified to note that the chimeras have followed you, and they seem to be in the mood for lunch.', 'You keep running, but the chimeras will catch up to you soon enough.', 'You finally arrive at an abandoned chamber around the side of a cliff anad just manage to slam a solid, semi-mechanical door and it snaps shut behind you.', 'You know you are safe here for now, but the chimeras know what you smell like.', 'They have chosen you as food, and they will no doubt be searching for you in the future.', 'The next morning, they are gone. You continue your journey through the mountains.'], Encounters.runNextEncounter)

    def enterSecretLair(self):
        self.__destroyDecision()
        Conditions.SetCondition('FoundYsmay', True)
        GlobalVariables.GUI.startNarration(['Running is definitely a good idea. They\'ve already seen you, after all.', 'You\'re faster than the chimeras, and you no longer feel as though they are close behind.', 'You decide that now is a good time to search for a good hiding spot.', 'You see a sort of glowing tree in the distance.', 'You approach the tree and discover traces of purpley light coming from behind a doorframe shape which appears to have been etched into the bark.', 'You push on the bark and discover that it is an actual door!', 'You walk through the portal.'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Ysmay, lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Ysmay, ['From now on, whenever I sense that you need some insight on your journey, I will be there for you.', 'You will understand soon enough.'], Encounters.runNextEncounter)))

    def findYsmayByFollowingSign(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You walk up the trail toward this "Ysmay\'s" hut, in hopes of finding someone who can aid you.', 'You arrive at the end of the trail.', 'Unfortunately, there\'s nothing here. For all you know, this Ysmay person hasn\'t been here for a few decades.'], self.__findYsmayByFollowingSignExtended)

    def __findYsmayByFollowingSignExtended(self):
        self.__destroyDecision()
        Conditions.SetCondition('NearYsmay', True)
        # try:
        #     GlobalVariables.FixedEncounters.insert(int(GlobalVariables.CurrentEncounterNumber) + 2, Encounters.ExploreYsmayArea)
        # except:
        #     pass
        Conditions.SetCondition('FriendsAreKilled', True)
        Conditions.SetCondition('FriendsAreNotKilled', False)
        Encounters.runNextEncounter()
        # GlobalVariables.GUI.startNarration(['You head back down the trail toward the swamp.'], Encounters.runNextEncounter)

    def getLostFromSign(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You\'re almost out to the swampland, so you hope that you will be able to find someone once you\'re there.', 'The dark of night falls.', 'You can no longer see the swampland. You are lost and afraid.', 'You are very cold. Use 2 magicka to warm yourself up until morning.'], Encounters.runNextEncounter)
    
    def makeItToSwamp(self): # After sign choice
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You\'re almost out to the swampland, so you hope that you will be able to find someone once you\'re there.', 'You make it to the swamp.'], Encounters.runNextEncounter)

    def welcomeToTheSwamp(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You start heading down the path toward the swamp.'], Encounters.runNextEncounter)

    def hiYsmay(self):
        self.__destroyDecision()
        Conditions.SetCondition('FoundYsmay', True)
        GlobalVariables.GUI.startNarration(['For some reason you just really want to see if this Ysmay person is still around here somewhere.', 'Okay, so it\'s been a little over two hours. Just when you start to give up, something catches your eye.', 'You see a sort of glowing tree in the distance.', 'You approach the tree and discover traces of purpley light coming from behind a doorframe shape which appears to have been etched into the bark.', 'You push on the bark and discover that it is an actual door!', 'You walk through the portal.'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Ysmay, lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Ysmay, ['From now on, whenever I sense that you need some insight on your journey, I will be there for you.', 'You will understand soon enough.'], Encounters.runNextEncounter)))
    
    def kidnapped(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['For some reason you just really want to see if this Ysmay person is still around here somewhere.', 'Okay, so it\'s been a little over two hours. Just when you start to give up, something catches your eye.', 'You see a sort of glowing tree in the distance.', 'You out call her name. "Ysmay?"', 'You feel a hard object bash onto yuofrbo gvregv g ....', 'You wake up.', '"Har har har..."', 'The room is pitch black.', '"Heeeee hee hee!"', 'You hear someone in front of you let out a loud shriek.', 'You hear them let out their final breath.', '"Gotcha! Har har har!"'], lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Boblin, ['Har har! I saved you from your kidnapper, good sir!'], lambda: GlobalVariables.GUI.startNarration(['The goblin opens up a large door in front of you. Light shines in. Is it morning already?'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Boblin, Encounters.runNextEncounter))))

    def assassinateMatilda(self):
        self.__destroyDecision()
        Conditions.SetCondition('KilledMatilda', True)
        GlobalVariables.GUI.startNarration(['You equip your main weapon, surprising the Annith.', 'You use it to kill the Annith.'], lambda: GlobalVariables.GUI.NPCChat(['Why... it wasn\'t... me....'], lambda: GlobalVariables.GUI.startNarration(['The Annith was innocent. You should have asked what happened.'], lambda: GlobalVariables.GUI.NPCChat(['Find Mythergius. It was him.'], lambda: GlobalVariables.GUI.startNarration(['The Annith dies, using her last movement to point a finger in a direction.', 'You run in that direction, abandoning all of the bodies.', 'You don\'t stop running for a while.'], Encounters.runNextEncounter)))))

    def failAssassinateMatilda(self):
        self.__destroyDecision()
        GlobalVariables.GUI.startNarration(['You equip your main weapon, surprising the Annith.', 'You can\'t seem to work up the courage to kill her, and she appears to feel sympathy for you. You didn\'t think the Annith had feelings.', '"What... happened?", you ask.'], lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Matilda, ['I arrived here shortly before you did. I was here in time to see it happen.'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Matilda, Encounters.runNextEncounter)))

    def demandInfoFromMatilda(self):
        self.__destroyDecision()
        GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Matilda, ['Wha—look. It wasn\'t me. I didn\'t do this. I can see that you\'re angry. Just let me explain, okay?'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Matilda, lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Matilda, ['INSERT EXPLANATION HERE'], Encounters.runNextEncounter)))
    
    def comeWme(self):
        self.__destroyDecision()
        GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Matilda, ['You need help.', 'I know somewhere safe that we can go.', 'It\'s a city.'], self.findOutWhoSheIs)

    def findOutWhoSheIs(self):
        self.__destroyDecision()
        GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Matilda, lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Matilda, ['Now, listen. You need to come with me.'], lambda: GlobalVariables.GUI.startNarration(['You and Matilda set off for the city.', 'You\'ve been walking for a while.'], Encounters.runNextEncounter)))   
    
    def BoblinPathInstantiated(self):
        self.__destroyDecision()
        Conditions.SetCondition('BoblinPathInstantiated', True)
        GlobalVariables.GUI.npcs.merchantCharacterList.pop(2)
        GlobalVariables.GUI.startNarration(['You watch as Boblin falls to his doom.'], lambda: GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Boblin, ['WHYYYYYYYYYYYYYYYYYYYYYYY'], lambda: GlobalVariables.GUI.startNarration(['Matilda looks at you silently.', 'You both start heading to the city together, without saying a word.'], Encounters.runNextEncounter)))

    def MatildaFightsBack(self):
        self.__destroyDecision()
        Encounters.runNextEncounter()

    def MatildaFalls(self):
        self.__destroyDecision()
        Encounters.runNextEncounter()

    def JumpedOffCliff(self):
        self.__destroyDecision()
        Encounters.runNextEncounter()
    
    
    
    
    
    
    
    
    
    
    
    
    def __destroyDecision(self):
        for button in GlobalVariables.GUI.choiceButtons:
            button.destroy()
