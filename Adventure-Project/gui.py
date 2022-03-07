import tkinter
import tkinter.messagebox
import time
import abc
from functools import partial
import NPCs
import random
import Narration
import Character, GlobalVariables, Enemies, CombatInterface, Encounters
import Decisions
import Events
import Conditions

'''
GENERAL NOTES FOR MATT BY CABEL:

I made two "events" so far: being chased by chimeras and an encounter with someone special. Which event occurs in the beginning depends on whether it's foggy or not.
Run the code to see what I did!

'''

'''
GENERAL NOTES FOR CABEL BY MATT:



'''

class gui:
    def __init__(self):
        self.__initMainWindow()
        self.__initFrames()
        
        self.__needsUpdate = True
        # Is true when you can press buttons
        self.canTakeActions = False

        # Game stuff that needs to happen on GUI instantiation

        if random.randint(1, 2) == 2:
            for condition in GlobalVariables.conditionsList:
                if condition.name == 'Foggy':
                    condition.met = True
        else:
            for condition in GlobalVariables.conditionsList:
                if condition.name == 'Clear':
                    condition.met = True

        self.npcs = NPCs.Characters()
      
        self.__mainText = tkinter.StringVar()
        self.__main = tkinter.Label(self.frameTop, textvariable = self.__mainText, wraplength = 700, justify = tkinter.CENTER, font = 'Times 15')

        self.__lTextnpcSlot = tkinter.StringVar()
        self.__labelnpcSlot = tkinter.Label(self.frameTop, textvariable = self.__lTextnpcSlot, wraplength = 700, justify = tkinter.CENTER, font = 'Constantia 18')

        self.__photo = tkinter.PhotoImage(file = 'AyleeGoblinPixelArt.png').zoom(5, 5)

        self.__img = tkinter.Label(self.frameMiddle, image = self.__photo)
        self.__img.image = self.__photo
        self.__img.pack(expand = 1, side = 'top')

        # self.__imgCanvas = tkinter.Canvas(self.__frameTop, width = 500, height = 500)
        # self.__imgCanvas.create_image(self.__imgCanvas.winfo_width() / 2, self.__imgCanvas.winfo_height() / 2, ImageTk.PhotoImage(Image.open(r'AyleeGoblinPixelArt.png')))
        # self.__imgCanvas.pack(expand = 1)

        self.__button = tkinter.Button(self.frameMiddle, text = 'Begin Game', command = self.__begin)

        self.__main.pack(expand = True, side = 'bottom')
        self.__labelnpcSlot.pack(expand = 1, side = 'bottom')
        
        self.__button.pack(expand = True)

        

    def startGUI(self):
        self.__mainWindow.mainloop()

    def __initMainWindow(self):
        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title('The Origin of Myths')
        self.__mainWindow.geometry('1440x700')
        self.__mainWindow.resizable(0, 0)
        self.__mainWindow.option_add('*Label.Foreground', 'white')
        self.__mainWindow.option_add('*Label.Background', 'black')
        self.__mainWindow.option_add('*Label.Font', 'Times 12')
        self.__mainWindow.option_add('*Button.font', 'Elephant 15')
        self.__mainWindow.iconphoto(0, tkinter.PhotoImage(file = 'AyleeGoblinPixelArt.png'))

    def __initFrames(self):
        # self.__frameExtraTop = tkinter.Frame(bg = 'black')
        self.frameTop = tkinter.Frame(bg = 'black')
        #self.__frameSecret = tkinter.Frame(bg = 'black')
        self.frameMiddle = tkinter.Frame(bg = 'black')
        self.frameBottom = tkinter.Frame(bg = 'black')

        # self.__frameExtraTop.pack_propagate(0)
        self.frameTop.pack_propagate(0)
        #self.__frameSecret.pack_propagate(0)
        self.frameMiddle.pack_propagate(0)
        self.frameBottom.pack_propagate(0)

        # self.__frameExtraTop.pack(fill = tkinter.BOTH, expand = 1)
        self.frameTop.pack(fill = tkinter.BOTH, expand = 1)
        #self.__frameSecret.pack(fill = tkinter.BOTH, expand = 1)
        self.frameMiddle.pack(fill = tkinter.BOTH, expand = 1)
        self.frameBottom.pack(fill = tkinter.BOTH, expand = 1)


    def __begin(self):
        self.__img.destroy()
        self.NPCGreet(self.npcs.Donrak, lambda: self.NPCChat(self.npcs.Donrak, ['I understand that you may not fully remember the events of the past. \'Tis why I\'m here, of course!', 'You and I, Oh Simple Spirit, we are known as the Magelike.', 'Us Magelike are capable of wielding magic, but we can survive in other ways as well.', 'We sort of have a bad reputation in this world. You have Mythergius to thank for that.', 'Mythergius is a ruthless killer, AND he is supposedly immortal. He\'ll use his powers to destroy anyone, and he doesn\'t die.', 'At least... we haven\'t figured out how to kill him yet.', 'I am fading away, Oh Simple Spirit, but please...', 'Just know...', 'A wonderful journey awaits you.', 'Also....', 'Don\'t die.'], self.__screenCharacterChoice))

    def typeOut(self, phrase, doAfter = None):
        self.canTakeActions = False
        self.__mainText.set('')
        self.__mainWindow.update()
        aPhrase = ''
        self.__button.destroy()
        for character in phrase:
            time.sleep(.02)
            aPhrase += character
            self.__mainText.set(aPhrase)
            self.__mainWindow.update()
        self.canTakeActions = True
        if doAfter != None:
            doAfter()

    def typeOutDelay(self, phrase):
        self.typeOut(phrase)
        self.canTakeActions = False
        time.sleep(1)
        self.canTakeActions = True


    def __screenCharacterChoice(self):

        self.typeOut('Which character will you play as?')

        buttonFont = 'Elephant 15'

        self.__buttonFighter = tkinter.Button(self.frameMiddle, text = 'Fighter', bg = 'red', fg = 'white', font = buttonFont, command = lambda: self.__areYouSure([self.__buttonFighter, self.__buttonWizard, self.__buttonRogue], 'Fighter'))
        self.__buttonWizard = tkinter.Button(self.frameMiddle, text = 'Wizard', bg = 'blue', fg = 'white', font = buttonFont, command = lambda: self.__areYouSure([self.__buttonFighter, self.__buttonWizard, self.__buttonRogue], 'Wizard'))
        self.__buttonRogue = tkinter.Button(self.frameMiddle, text = 'Rogue', bg = 'green', fg = 'white', font = buttonFont, command = lambda: self.__areYouSure([self.__buttonFighter, self.__buttonWizard, self.__buttonRogue], 'Rogue'))
        self.__buttonFighter.pack(expand = 1, side = 'left', fill = tkinter.BOTH)
        self.__buttonWizard.pack(expand = 1, side = 'left', fill = tkinter.BOTH)
        self.__buttonRogue.pack(expand = 1, side = 'left', fill = tkinter.BOTH)
    
    def battleGui(self, destroyables):
        self.destroyEverything(destroyables)

        self.__combat = GlobalVariables.Combat

        self.combatFrame = tkinter.Frame(self.frameMiddle, bg = 'black')
        # if len(self.__combat.actionsChosen) >= 3:
        #     self.__combat.PCacting = False
        #     self.__combat.round()

        self.informationVar = tkinter.StringVar()
        self.informationLabel = tkinter.Label(self.combatFrame, textvariable=self.informationVar)
        self.informationLabel.pack()

        # PC information
        self.selectedActionVar = tkinter.StringVar()
        self.selectedActionVar.set("")
        self.selectedActionLabel = tkinter.Label(self.combatFrame, textvariable=self.selectedActionVar)
        self.selectedActionLabel.pack()

        # Action buttons
        self.actionButton = []

        self.actionTopFrame = tkinter.Frame(self.combatFrame)
        self.actionButton.append(tkinter.Button(self.actionTopFrame, text=self.PC.actions[0].name, command=lambda: self.__combat.chooseAction(0)))
        self.actionButton.append(tkinter.Button(self.actionTopFrame, text=self.PC.actions[2].name, command=lambda: self.__combat.chooseAction(2)))
        self.actionButton.append(tkinter.Button(self.actionTopFrame, text=self.PC.actions[4].name, command=lambda: self.__combat.chooseAction(4)))

        self.actionBottomFrame = tkinter.Frame(self.combatFrame)
        self.actionButton.append(tkinter.Button(self.actionBottomFrame, text=self.PC.actions[1].name, command=lambda: self.__combat.chooseAction(1)))
        self.actionButton.append(tkinter.Button(self.actionBottomFrame, text=self.PC.actions[3].name, command=lambda: self.__combat.chooseAction(3)))
        self.actionButton.append(tkinter.Button(self.actionBottomFrame, text=self.PC.actions[5].name, command=lambda: self.__combat.chooseAction(5)))

        for i in range(0, len(self.PC.actions)):            
            self.actionButton[i].pack(expand = True, side='left')
        
        self.actionTopFrame.pack()
        self.actionBottomFrame.pack()
        self.combatFrame.pack()
    
    def swapItemGui(self, destroyables):
        self.destroyEverything(destroyables)
        self.typeOut("Which items do you want to swap?")

        self.currentItems = tkinter.StringVar()
        self.currentItems.set("Main weapon: " + self.PC.inventory.getMainWeapon().name + "\nSide weapon: " + self.PC.inventory.getOffWeapon().name + "\nArmor: " + self.PC.inventory.getArmor().name)
        self.currentItemLabel = tkinter.Label(self.frameMiddle, textvariable=self.currentItems, bg = 'black')
        self.currentItemLabel.pack()

        self.buttonFrame = tkinter.Frame(self.frameMiddle, bg = 'black')

        self.mainWeaponGui = SwapMainWeapon("Which weapon do you want to equip?")
        self.sideWeaponGui = SwapSideWeapon("Which side weapon do you want to equip?")
        self.armorGui = SwapArmor("Which armor do you want to equip?")

        self.mainWeaponButton = tkinter.Button(self.buttonFrame, text="Main weapon", command=lambda: self.mainWeaponGui.build([self.currentItemLabel, self.buttonFrame]))
        self.sidWeaponButton = tkinter.Button(self.buttonFrame, text="Side weapon", command=lambda: self.sideWeaponGui.build([self.currentItemLabel, self.buttonFrame]))
        self.armorButton = tkinter.Button(self.buttonFrame, text="Armor", command=lambda: self.armorGui.build([self.currentItemLabel, self.buttonFrame]))
        self.confirmButton = tkinter.Button(self.buttonFrame, text="Done", command=self.PC.actions[3].exitInventory)
        self.mainWeaponButton.pack(side='left')
        self.sidWeaponButton.pack(side='left')
        self.armorButton.pack(side="left")
        self.confirmButton.pack(side='left')

        self.buttonFrame.pack()
        self.__mainWindow.update()
    
    def selectSpellGui(self, destroyables):
        self.destroyEverything(destroyables)
        self.spellMenu = SelectSpell("Choose a spell to cast.\nIf you can't cast any spells, select 'channel' instead to regain magicka.")
        self.spellMenu.build([])
    
    # def victoryGui(self, destroyables):
    #     self.destroyEverything(destroyables)
    #     self.typeOut("You defeated ")

    def __areYouSure(self, destroyables = [], selection = ''):
        self.destroyEverything(destroyables)

        self.typeOut('You have selected \"{}.\" Are you sure that you want to continue?'.format(selection))

        self.__iAmSure = tkinter.Button(self.frameMiddle, text = 'Yes, I am sure.', command = lambda: self.__selectArchetype([self.__iAmSure, self.__iAmNotSure], selection))
        self.__iAmNotSure = tkinter.Button(self.frameMiddle, text = 'No, I am not sure.', command = lambda: self.__unoReverse([self.__iAmSure, self.__iAmNotSure]))

        self.__iAmNotSure.pack(expand = 1, side = 'left')
        self.__iAmSure.pack(expand = 1, side = 'left')

    def destroyEverything(self, something):
        'Delete, delete, delete?'
        for anything in something:
            anything.destroy()

    def __selectArchetype(self, destroyables, character):
        self.destroyEverything(destroyables)

        if character == 'Fighter':
            GlobalVariables.PC = Character.Fighter()
        elif character == 'Wizard':
            GlobalVariables.PC = Character.Wizard()
        elif character == 'Rogue':
            GlobalVariables.PC = Character.Rogue()
        self.PC = GlobalVariables.PC
        self.__startingConfig()

    def __unoReverse(self, destroyables):
        self.destroyEverything(destroyables)
        self.__screenCharacterChoice()

    def __startingConfig(self):
        self.__gemsBOX = tkinter.LabelFrame(self.frameBottom, bg = 'yellow', height = .5)
        self.__hpBOX = tkinter.LabelFrame(self.frameBottom, bg = 'red', height = .5)
        self.__staminaBOX = tkinter.LabelFrame(self.frameBottom, bg = 'green', height = .5)
        self.__magickaBOX = tkinter.LabelFrame(self.frameBottom, bg = 'blue', height = .5)
        self.__armorBOX = tkinter.LabelFrame(self.frameBottom, bg = 'grey', height = .5)

        self.__hpStatusText = tkinter.StringVar()
        self.setHP(self.PC.getHp())
        self.__hpStatus = tkinter.Label(self.__hpBOX, textvariable = self.__hpStatusText)

        self.__staminaStatusText = tkinter.StringVar()
        self.setStamina(self.PC.getStamina())
        self.__staminaStatus = tkinter.Label(self.__staminaBOX, textvariable = self.__staminaStatusText)
        
        self.__magickaStatusText = tkinter.StringVar()
        self.__setMagicka(self.PC.getMagicka())
        self.__magickaStatus = tkinter.Label(self.__magickaBOX, textvariable = self.__magickaStatusText)

        self.__gemsStatusText = tkinter.StringVar()
        self.setGems(GlobalVariables.currentGems)
        self.__gemsStatus = tkinter.Label(self.__gemsBOX, textvariable = self.__gemsStatusText)

        self.__armorStatusText = tkinter.StringVar()
        # self.__setMagicka(self.PC.getMagicka())
        self.__armorStatus = tkinter.Label(self.__armorBOX, textvariable = self.__armorStatusText)

        self.__enemyNameText = tkinter.StringVar()

        self.__enemyHPStatusText = tkinter.StringVar()

        self.__createEnemyBoxes()

        self.__gemsBOX.pack(expand = 1, side = 'left', anchor = tkinter.S, fill = tkinter.X)
        self.__hpBOX.pack(expand = 1, side = 'left', anchor = tkinter.S, fill = tkinter.X)
        self.__staminaBOX.pack(expand = 1, side = 'left', anchor = tkinter.S, fill = tkinter.X)
        self.__magickaBOX.pack(expand = 1, side = 'left', anchor = tkinter.S, fill = tkinter.X)
        self.__armorBOX.pack(expand = 1, side = 'left', anchor = tkinter.S, fill = tkinter.X)

        self.__hpStatus.pack(expand = 1)
        self.__gemsStatus.pack(expand = 1)
        self.__staminaStatus.pack(expand = 1)
        self.__magickaStatus.pack(expand = 1)
        self.__armorStatus.pack(expand = 1)

        self.__enemyHP.pack(expand = 1)
        self.__enemyName.pack(expand = 1)

        self.updateStats()

        # self.__portraitBoblin = tkinter.PhotoImage(file = NPCs.Characters.Boblin.getAssociatedPNG()).zoom(2, 2)
        # self.__imageBoblin = tkinter.Label(self.__frameBottom, image = self.__portraitBoblin)
        # self.__imageBoblin.image = self.__portraitBoblin

        # GlobalVariables.Enemy = Enemies.Chimera()
        # GlobalVariables.Combat = CombatInterface.Combat()
        # self.runCombat(Enemies.Chimera(), [])

        #Encounters.runNextEncounter()
        # ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
        
        # self.__NPCGreet(npcs.Donrak, lambda: self.__startNarration(Narration.lines.intro, lambda: GlobalVariables.Encounter.nextBattle([])))
        # self.__startNarration(Narration.lines.intro, lambda: self.__NPCGreet(npcs.Donrak, lambda: GlobalVariables.Encounter.nextBattle([])))


        Encounters.runNextEncounter()
        # self.sellGoods(self.npcs.Boblin) # ADD GREET TO MERCHANTS

        # Depends on Fog condition which one is actually ran

        
        # self.NPCGreet(self.npcs.Matilda, lambda: GlobalVariables.Encounter.nextBattle([]))


        # Can be moved to separate location such as enounters, I just wanted to do this fast
        
        # self.listDecisions = []
        # self.listDecisions.append(lambda: self.__createDecision(self.foggyboblinEncounter.choices, self.foggyboblinEncounter.consequences, self.foggyboblinEncounter.consequenceChances))
        
        # self.listDecisions[0]()

        #self.next(lambda: GlobalVariables.Encounter.nextBattle([])


    def __createEnemyBoxes(self):
        self.__enemyNameBox = tkinter.LabelFrame(self.frameTop, bg = 'blue', height = .5)
        self.__enemyHPBox = tkinter.LabelFrame(self.frameTop, bg = 'red', height = .5)

        self.__enemyNameText.set("None")
        self.__enemyName = tkinter.Label(self.__enemyNameBox, textvariable = self.__enemyNameText)

        self.__enemyHPStatusText.set("HP: 0")
        self.__enemyHP = tkinter.Label(self.__enemyHPBox, textvariable = self.__enemyHPStatusText)

        self.__enemyNameBox.pack(expand = 1, side = 'left', anchor = tkinter.N, fill = tkinter.X)
        self.__enemyHPBox.pack(expand = 1, side = 'left', anchor = tkinter.N, fill = tkinter.X)

    def startNarration(self, phrases, continueCommand = None, destroyables = None, typer = None):
        if destroyables != None:
            self.destroyEverything(destroyables)
        
        self.__narrationInc = 0
        self.__buttonMoveOn = tkinter.Button(self.frameMiddle, text = 'Continue', command = lambda: self.__continueNarration(phrases, continueCommand, typer))
        self.__buttonMoveOn.pack(expand = 1)

        self.__continueNarration(phrases, continueCommand, typer)

    def __continueNarration(self, phrases, continueCommand, typer = None):
        self.__buttonMoveOn.pack_forget()
        if self.__narrationInc == -1:
            self.__buttonMoveOn.destroy()
            if typer != 'sale':
                self.__lTextnpcSlot.set('')
                try:
                    self.__imageNPC.destroy()
                except:
                    pass
            try:
                continueCommand()
            except:
                pass
        else:
            self.__narrate(phrases, typer)

    def __narrate(self, narrationElements, typer = None):
        if len(narrationElements) - 1 > self.__narrationInc:
            self.typeOut(narrationElements[self.__narrationInc])
            self.__narrationInc += 1
        elif len(narrationElements) - 1 == self.__narrationInc:
            self.typeOut(narrationElements[self.__narrationInc])
            self.__narrationInc = -1

        self.__buttonMoveOn.pack(expand = 1)

    def setHP(self, hpVal):
        self.__hpStatusText.set('HP  {0}'.format(hpVal))

    def setGems(self, gemsVal):
        self.__gemsStatusText.set('Gemstones  {0}'.format(gemsVal))
        GlobalVariables.currentGems = gemsVal

    def setStamina(self, hpVal):
        self.__staminaStatusText.set('Stamina  {0}'.format(hpVal))

    def __setMagicka(self, hpVal):
        self.__magickaStatusText.set('Magicka  {0}'.format(hpVal))
    
    def __setArmor(self, totalArmorVal, flatFootedVal, touchVal):
        self.__armorStatusText.set("Total Armor  {0}  ".format(totalArmorVal) + "—  Flat footed  {0}  ".format(flatFootedVal) + "—  Touch  {0}".format(touchVal))
    
    def updateStats(self):
        self.setHP(self.PC.getHp())
        self.setStamina(self.PC.getStamina())
        self.__setMagicka(self.PC.getMagicka())
        self.__setArmor(self.PC.getDefense(), self.PC.getFlatFooted(), self.PC.getTouch())

        if GlobalVariables.Enemy != None:
            if GlobalVariables.Enemy.alive:
                self.__enemyHPStatusText.set("HP: " + str(GlobalVariables.Enemy.getHp()))
                self.__enemyNameText.set(GlobalVariables.Enemy.name)
            else:
                self.__enemyHPStatusText.set("HP: 0")
                self.__enemyNameText.set("None")
        else:
            self.__enemyHPStatusText.set("HP: 0")
            self.__enemyNameText.set("None")

    def __changeText(self, newText = ''):
        print(self.__mainText.get())

    def __createDecision(self, choices, consequences, consequenceChances, destroyables = None):
        if destroyables != None:
            self.destroyEverything(destroyables)

        self.choiceButtons = []

        # finalConsequences = []

        for i in range(0, len(choices), 1):
            __currentConsquences = []
            __currentConsquenceChances = []

            for consequence in consequences[i]:
                __currentConsquences.append(consequence)

            for consequenceChance in consequenceChances[i]:
                __currentConsquenceChances.append(consequenceChance)

            determinedConsequence = random.choices(__currentConsquences, weights = __currentConsquenceChances, k = 1)[0]

            self.choiceButtons.append(tkinter.Button(self.frameMiddle, text = choices[i], command = determinedConsequence))

        for button in self.choiceButtons:
            button.pack(expand = 1, side = 'top')

    def __destroyDecision(self, consequence):
        for button in self.choiceButtons:
            button.destroy()
        
        consequence()

    def sellGoods(self, npc, doAfter = None, destroyables = None):
        self.NPCGreet(npc, lambda: self.__sellGoods(npc, doAfter, destroyables))
        if npc.name == 'Boblin: The Goblin':
            Conditions.SetCondition('MetBob', True)

    def __sellGoods(self, npc, doAfter = None, destroyables = None):

        if destroyables != None:
            self.destroyEverything(destroyables)

        self.__portraitNPC = tkinter.PhotoImage(file = npc.getAssociatedPNG()).zoom(3, 3)
        self.__imageNPC = tkinter.Label(self.frameBottom, image = self.__portraitNPC)
        self.__imageNPC.image = self.__portraitNPC
        self.__imageNPC.pack(anchor = tkinter.S, expand = 1, side = 'left')

        self.__lTextnpcSlot.set(npc.name)

        self.startNarration([npc.getSalesPrompt()], lambda: self.__sellGoods2(npc, doAfter), typer = 'sale')

    def __sellGoods2(self, npc, doAfter = None, destroyables = None):

        try:
            self.__buttonMoveOn.destroy()
        except:
            pass

        self.buttonsBuyGoods = []

        for good in npc.getGoods():
            if good != None:
                self.buttonsBuyGoods.append(tkinter.Button(self.frameMiddle, text = '{}\nCost: ʑ{}'.format(good.name, good.cost), command = partial(self.__buyGood, good, npc)))

        self.merchantQuitButton = tkinter.Button(self.frameMiddle, text = 'Done', command = lambda: self.__doneBuyingGoods(doAfter))

        self.merchantQuitButton.pack(expand = 1, side = 'bottom')

        for button in self.buttonsBuyGoods:
            button.pack(expand = 1, side = 'left')

    def __doneBuyingGoods(self, doAfter = None):
        self.__imageNPC.destroy()

        self.__lTextnpcSlot.set('')
        
        self.merchantQuitButton.destroy()

        try:
            for button in self.buttonsBuyGoods:
                button.destroy()
        except:
            pass

        

        if doAfter != None:
            doAfter()

    def __buyGood(self, good, npc):
        saleSuccess = False

        for i in range(0, len(npc.getGoods()), 1):
            if npc.getGoods()[i].name == good.name:
                if GlobalVariables.currentGems >= good.cost:
                    saleSuccess = True
                    if good.goodType == 'spell':
                        self.PC.inventory.addSpell(npc.getGoods().pop(i))
                        break
                    elif good.goodType == 'weapon':
                        self.PC.inventory.addWeapon(npc.getGoods().pop(i))
                        break
                    elif good.goodType == 'armor':
                        self.PC.inventory.addWeapon(npc.getGoods().pop(i))
                        break
                else:
                    self.typeOut('Looks like you don\'t have enough gemstones for that.')
        
        if saleSuccess:
            self.buttonsBuyGoods[i].destroy()
            self.buttonsBuyGoods.pop(i)
            self.setGems(GlobalVariables.currentGems - good.cost)
            reaction = random.choice(npc.getSaleReaction())
            self.typeOut(reaction)
        saleSuccess = False


            
        


        




    # def next(self, continueCommand, destroyables = None):
    #     try:
    #         self.__buttonMoveOn.destroy()
    #     except:
    #         pass

    #     self.__buttonC = tkinter.Button(self.frameMiddle, text = 'Continue', command = lambda: self.yesContinue(continueCommand))
    #     self.__buttonC.pack(expand = 1)

    # def yesContinue(self, continueCommand):
    #     try:
    #         self.__imageNPC.destroy()
    #     except:
    #         pass

    #     self.__lTextnpcSlot.set('')

    #     self.__buttonC.destroy()
    #     continueCommand()

    def NPCChat(self, npc, dialogue, doAfter = None, destroyables = None): # dialogue needs to be list
        if destroyables != None:
            self.destroyEverything(destroyables)

        self.__lTextnpcSlot.set(npc.name)

        try:
            self.__imageNPC.destroy()
        except:
            pass

        self.__portraitNPC = tkinter.PhotoImage(file = npc.getAssociatedPNG()).zoom(3, 3)
        self.__imageNPC = tkinter.Label(self.frameBottom, image = self.__portraitNPC)
        self.__imageNPC.image = self.__portraitNPC
        self.__imageNPC.pack(anchor = tkinter.S, expand = 1, side = 'left')

        self.startNarration(dialogue, doAfter)


    def NPCGreet(self, npc, doAfter = None, destroyables = None):
        if destroyables != None:
            self.destroyEverything(destroyables)

        try:
            self.__imageNPC.destroy()
        except:
            pass

        self.__lTextnpcSlot.set(npc.name)

        self.__portraitNPC = tkinter.PhotoImage(file = npc.getAssociatedPNG()).zoom(3, 3)
        self.__imageNPC = tkinter.Label(self.frameBottom, image = self.__portraitNPC)
        self.__imageNPC.image = self.__portraitNPC
        self.__imageNPC.pack(anchor = tkinter.S, side = 'left', expand = 1)

        if not npc.hasSpoken():
            self.startNarration([npc.getFirstGreeting()], doAfter)
            npc.hasSpoken(True)
        else:
            thisGreeting = random.choice(npc.getGreetings())
            self.startNarration([thisGreeting], doAfter)

    # def __merchantSale(self, npc, destroyables = None):
    #     try:
    #         self.destroyEverything(destroyables)
    #     except:
    #         pass

    #     self.__NPCGreet(npc)

    def runCombat(self, enemy, destroyables):
        GlobalVariables.Enemy = enemy
        GlobalVariables.Combat = CombatInterface.Combat()

        self.battleGui(destroyables)

        # enemy.initalMessage()
        GlobalVariables.Combat.setDisplay()
    
    def quit(self):
        self.__mainWindow.destroy()

        # while not GlobalVariables.Combat.hasEnded():
        #     if display != GlobalVariables.Combat.setDisplay():
        #         self.typeOut(display)
        #     GlobalVariables.Combat.round()

# Other GUI classes

# Quickly build a GUI with a selection of radio buttons
class RadioButtonsGUI(abc.ABC):

    def __init__(self, title):
        self.parent = GlobalVariables.GUI
        self.title = title
    
    def build(self, destroyables):
        self.info = self.collectInfo()
        itemsNames = self.info[0]
        itemDescriptions = self.info[1]
        currentItemName = self.info[2]
        currentItemDescription = self.info[3]

        self.parent.destroyEverything(destroyables)

        self.parent.typeOut(self.title)

        self.totalFrame = tkinter.Frame(self.parent.frameMiddle, bg = 'black')
        self.selectFrame = tkinter.Frame(self.totalFrame, bg = 'black')
        self.infoFrame = tkinter.Frame(self.totalFrame, bg = 'black')      

        self.radioButtons = []
        self.radioSelection = tkinter.IntVar()
        self.radioSelection.set(0)

        self.infoVar = tkinter.StringVar()
        self.infoVar.set(currentItemDescription)
        self.infoLabel = tkinter.Label(self.infoFrame, textvariable=self.infoVar)
        self.infoLabel.pack()
        self.showInfo = tkinter.Button(self.infoFrame, text="Show description", command=lambda: self.infoVar.set(itemDescriptions[self.radioSelection.get()]))
        self.showInfo.pack()

        self.infoFrame.pack(side='right')

        for i in range(0, len(itemsNames)):
            self.radioButtons.append(tkinter.Radiobutton(self.selectFrame, text=itemsNames[i], variable=self.radioSelection, value=i))
            self.radioButtons[i].pack(expand = True)

        exitButton = tkinter.Button(self.infoFrame, text='Confirm', command=self.exitFrame)
        exitButton.pack()

        self.selectFrame.pack(side='left')

        self.totalFrame.pack()
    
    def collectInfo(self):
        return []

    def exitFrame(self):
        self.parent.destroyEverything([self.totalFrame])

class SwapMainWeapon(RadioButtonsGUI):
    def exitFrame(self):
        self.parent.PC.inventory.setMainWeapon(self.radioSelection.get())
        self.parent.swapItemGui([self.totalFrame])
        
    def collectInfo(self):
        names = []
        descriptions = []
        currentName = self.parent.PC.inventory.getMainWeapon().name
        currentDescription = self.parent.PC.inventory.getMainWeapon().getStats()
        for i in self.parent.PC.inventory.getAllWeapons():
            names.append(i.name)
            descriptions.append(i.getStats())
        return names, descriptions, currentName, currentDescription
        
class SwapSideWeapon(RadioButtonsGUI):
    def exitFrame(self):
        self.parent.PC.inventory.setOffWeapon(self.radioSelection.get())
        self.parent.swapItemGui([self.totalFrame])
    
    def collectInfo(self):
        names = []
        descriptions = []
        currentName = self.parent.PC.inventory.getOffWeapon().name
        currentDescription = self.parent.PC.inventory.getOffWeapon().getStats()
        for i in self.parent.PC.inventory.getAllSideWeapons():
            names.append(i.name)
            descriptions.append(i.getStats())
        return names, descriptions, currentName, currentDescription

class SwapArmor(RadioButtonsGUI):
    def exitFrame(self):
        self.parent.PC.inventory.setArmor(self.radioSelection.get())
        self.parent.swapItemGui([self.totalFrame])
    
    def collectInfo(self):
        names = []
        descriptions = []
        currentName = self.parent.PC.inventory.getArmor().name
        currentDescription = self.parent.PC.inventory.getArmor().getStats()
        for i in self.parent.PC.inventory.getAllArmor():
            names.append(i.name)
            descriptions.append(i.getStats())
        return names, descriptions, currentName, currentDescription

class SelectSpell(RadioButtonsGUI):
    def exitFrame(self):
        self.parent.destroyEverything([self.totalFrame])
        self.parent.battleGui([self.totalFrame])
        n = self.parent.PC.actions[1].actionsUsed
        if self.radioSelection.get() == 0:
            self.parent.PC.actions[5].execute(n)      
        else:
            self.parent.PC.actions[1].castChosenSpell(self.radioSelection.get()-1, n) 
    
    def collectInfo(self):
        names = ["Channel"]
        descriptions = [self.parent.PC.actions[5].description]
        currentName = None
        currentDescription = self.parent.PC.actions[5].description
        n = self.parent.PC.actions[1].actionsUsed
        castableSpells = []
        for i in self.parent.PC.inventory.getAllSpells():
            if i.level*n <= self.parent.PC.getMagicka():
                castableSpells.append(i)
        for i in castableSpells:
            names.append(i.name)
            descriptions.append(i.description)
        return names, descriptions, currentName, currentDescription

class SelectNumActions():

    def __init__(self):
        self.parent = GlobalVariables.GUI
        self.title = "Choose how many actions you want to spend"
    
    def build(self, destroyables, action, actionsTaken):
        self.action = action
        self.parent.destroyEverything(destroyables)

        self.parent.typeOut(self.title)

        self.totalFrame = tkinter.Frame(self.parent.frameMiddle, bg = 'black')

        self.radioButtons = []
        self.radioSelection = tkinter.IntVar()
        self.radioSelection.set(0)

        for i in range(0, self.maxActions()):
            self.radioButtons.append(tkinter.Radiobutton(self.totalFrame, text=str(i), variable=self.radioSelection, value=i))
            self.radioButtons[i].pack(expand = True)

        exitButton = tkinter.Button(self.totalFrame, text='Confirm', command=self.exitFrame)
        exitButton.pack()

        self.totalFrame.pack()
    
    def maxActions(self):
        actionsRemaining = 3 - len(GlobalVariables.Combat.actionsChosen) + self.parent.PC.tempActionBuff.get()
        cost = self.parent.PC.actions[self.action].staminaCost
        if cost*actionsRemaining > self.parent.getStamina():
            return int(self.parent.getStamina()/cost)
        return actionsRemaining

    def exitFrame(self):
        self.parent.destroyEverything([self.totalFrame])
