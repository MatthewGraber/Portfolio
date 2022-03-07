import abc
import random, tkinter
import Enemies
import Conditions
import NPCs
import Events
import GlobalVariables, Main

class BattleScenario(abc.ABC):

    def __init__(self):
        self.chanceAppearance = 0
        self.id = 0
        self.part = 0
        self.enemies = []
        self.messages = []
        # def __init__(self, destroyables):
        #     self.destroyables = destroyables

    def begin(self):
        self.nextBattle([])

    def nextBattle(self, destroyables):
        if len(self.enemies) > self.part:
            if len(self.messages) > self.part:
                if self.messages[self.part] != None:
                    GlobalVariables.GUI.typeOutDelay(self.messages[self.part])
            GlobalVariables.GUI.runCombat(self.enemies[self.part], destroyables)
            self.part += 1
        else:
            GlobalVariables.GUI.destroyEverything([self.frame])
            runNextEncounter()

    def victoryGui(self, destroyables):
        GlobalVariables.GUI.destroyEverything([GlobalVariables.GUI.combatFrame])
        gemsEarned = random.randint(10, 55)
        GlobalVariables.GUI.setGems(GlobalVariables.currentGems + gemsEarned)
        GlobalVariables.GUI.typeOutDelay("You have defeated the " + self.enemies[self.part-1].name + "!")
        GlobalVariables.GUI.typeOut("You earned " + str(gemsEarned) + " gems!")
        self.frame = tkinter.Frame(GlobalVariables.GUI.frameMiddle)
        self.newGameButton = tkinter.Button(self.frame, text="Continue", command=lambda: self.nextBattle([self.frame]))
        self.quit = tkinter.Button(self.frame, text="Exit game", command=GlobalVariables.GUI.quit)
        self.newGameButton.pack()
        #self.quit.pack()
        self.frame.pack()

    def defeatGui(self, destroyables):
        GlobalVariables.GUI.destroyEverything(destroyables)
        GlobalVariables.GUI.typeOutDelay("You have been defeated.")
        GlobalVariables.GUI.typeOut("New game?")        
        self.frame = tkinter.Frame(GlobalVariables.GUI.frameMiddle)
        self.newGameButton = tkinter.Button(self.frame, text="Yes", command=Main.restartGame)
        self.quit = tkinter.Button(self.frame, text="No", command=GlobalVariables.GUI.quit)
        self.newGameButton.pack()
        self.quit.pack()
        self.frame.pack()

# A generic class for battles with single enemies
class GenericBattle(BattleScenario):
    def __init__(self, enemy, introText):
        super().__init__()
        self.enemies.append(enemy)
        self.messages.append(introText)

class LoneChimera(BattleScenario):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemies.Chimera())
        self.messages.append("A Chimera swoops down from the sky towards you!")

class DualChimeras(BattleScenario):
    def __init__(self):
        super().__init__()
        self.enemies.append(Enemies.Chimera())
        self.enemies.append(Enemies.Chimera())
        self.messages.append("A Chimera swoops down from the sky towards you!")
        self.messages.append("Now there are two of them? This is getting out of hand!")

class Event:
    def __init__(self):
        self.encounter = None

    def runEvent(self, event):
        for condition in GlobalVariables.conditionsList:
            if condition.name == event.conditionName:
                if condition.met:
                    if event.Decision != None:
                        GlobalVariables.GUI.startNarration(event.story, lambda: GlobalVariables.GUI._gui__createDecision(event.Decision.choices, event.Decision.consequences, event.Decision.consequenceChances))
                    else:
                        GlobalVariables.GUI.startNarration(event.story, runNextEncounter)
                else:
                    runNextEncounter()
    
    def begin(self):
        self.runEvent(self.encounter)

class WanderingMerchant:
    def __init__(self):
        self.merchant = None

    def begin(self):
        self.merchant = random.choice(GlobalVariables.GUI.npcs.merchantCharacterList)
        GlobalVariables.GUI.sellGoods(self.merchant, runNextEncounter)

class RandomEncounter:
    def __init__(self):
        pass

    def begin(self):
        for condition in GlobalVariables.conditionsList:
            if condition.name == 'FoundYsmay':
                if condition.met:
                    GlobalVariables.GUI.startNarration(['You are temporary pulled into the Realm of Thoughts.', 'You walk over to Ysmay\'s desk.'], lambda: GlobalVariables.GUI.NPCGreet(GlobalVariables.GUI.npcs.Ysmay, self.__contin))
                else:
                    try:
                        randomEncounter = RandomEnemyEncounter()    
                    except:
                        pass
                    runNextEncounter()               

    def __contin(self):
        try:
            randomEncounter = RandomEnemyEncounter()
            
            GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Ysmay, ['Hello. I shall try to make you wary of the dangers that await in your near future.', 'I sense there is a {} that will attempt to take your life in the near future.'.format(randomEncounter.enemies[0].name)], runNextEncounter)
        except:
            GlobalVariables.GUI.NPCChat(GlobalVariables.GUI.npcs.Ysmay, ['Hello. I shall try to make you wary of the dangers that await in your near future.', 'What? I can\'t... see anything. There\'s too much darkness ahead.', 'I think... I think you\'re on your own, now. Good luck.'], runNextEncounter)

class EncounterInTheFog(Event):
    def __init__(self):
        Event.__init__(self)
        encounterInTheFog = Events.EncounterInTheFog()

        self.encounter = encounterInTheFog
    
class ChasedByChimeras(Event):
    def __init__(self):
        Event.__init__(self)
        chasedByChimeras = Events.ChasedByChimeras()
        self.encounter = chasedByChimeras

class LookASign(Event):
    def __init__(self):
        Event.__init__(self)
        lookASign = Events.LookASign()
        self.encounter = lookASign

class ExploreYsmayArea(Event):
    def __init__(self):
        Event.__init__(self)
        exploreYsmayArea = Events.ExploreYsmayArea()
        self.encounter = exploreYsmayArea

class SearchingForFriends(Event):
    def __init__(self):
        Event.__init__(self)
        searchingForFriends = Events.SearchingForFriends()
        self.encounter = searchingForFriends

class BoblinLovesYou(Event):
    def __init__(self):
        Event.__init__(self)
        boblinLovesYou = Events.BoblinLovesYou()
        self.encounter = boblinLovesYou

class SearchingForAliveFriends(Event):
    def __init__(self):
        Event.__init__(self)
        searchingForAliveFriends = Events.SearchingForAliveFriends()
        self.encounter = searchingForAliveFriends

def RandomEnemyEncounter():
    randomEncounter = random.choice([GenericBattle(Enemies.Bilgesnipe(), 'A Bilgesnipe approaches with its huge, scaly antlers!'), GenericBattle(Enemies.BlackPudding(), 'A black pudding oozes its way toward you!'), GenericBattle(Enemies.GiantSpider(), 'A creepy crawly giant spider scuttles in your direction!'), GenericBattle(Enemies.Slime(), 'A slime flops around on the ground!')])
    posDeterminer = random.randint(2, 4)
    GlobalVariables.FixedEncounters.insert(GlobalVariables.CurrentEncounterNumber + posDeterminer, randomEncounter)
    return randomEncounter
# class Mountains:
#     # All USED percentage values must add up to 100%
#     class Scenario1(BattleScenario):
#         chanceAppearance = 1
#         id = 1
#         # Enemies
#         slime1 = Enemies.Slime()
#         slime2 = Enemies.Slime()
#         enemies = [slime1, slime2]
#     class Scenario2(BattleScenario):
#         chanceAppearance = 1
#         id = 1
#         # Enemies
#         slime1 = Enemies.Slime()
#         slime2 = Enemies.Slime()
#         enemies = [slime1, slime2]

#     allScenarios = [Scenario1, Scenario2]

# class Swamp:
#     pass

# class City:
#     pass

# class Forest:
#     pass

# class Fortress:
#     pass

def runNextEncounter():
    if GlobalVariables.Encounter != GlobalVariables.FixedEncounters[len(GlobalVariables.FixedEncounters) - 1]:
        GlobalVariables.CurrentEncounterNumber += 1
        # if GlobalVariables.CurrentEncounterNumber % 2 == 0:
        GlobalVariables.Encounter = GlobalVariables.FixedEncounters[GlobalVariables.CurrentEncounterNumber]
        GlobalVariables.Encounter.begin()
    # else:
    #     GlobalVariables.Encounter = GlobalVariables.RandomEncounters[int(GlobalVariables.CurrentEncounterNumber / 2)]
    #     GlobalVariables.Encounter.begin()
    #     pass
