import GlobalVariables
import Character, Enemies, Encounters
import AdventureMap
import Actions
import gui
import NPCs

import tkinter
import Conditions

# Will change to initialize to 'None' after more testing and whatnot is done

# GlobalVariables.PC = Character.Rogue()
# GlobalVariables.Enemy = Enemies.Chimera()

# Resets the game
# Each .py file should have a reset function that gets called here
def resetAll():
    pass

def restartGame():
    resetAll()
    beginGame()

def beginGame():
    locations = ['Mountains', 'Swamp', 'Forest', 'City', 'Fortress']

    
    conditions = Conditions.List()
    GlobalVariables.conditionsList = conditions.allConditions
    GlobalVariables.currentGems = 80

    # mountains = AdventureMap.Map(3, 'Mountains')
    # swamp = AdventureMap.Map(3, 'Swamp')
    # forest = AdventureMap.Map(3, 'Forest')
    # city = AdventureMap.Map(3, 'City')
    # fortress = AdventureMap.Map(4, 'Fortress')
    #GlobalVariables.FixedEncounters.append(Encounters.GenericBattle(Enemies.BlackPudding(), "A Black Pudding appears and slides towards you!"))

    # GlobalVariables.FixedEncounters.append(Encounters.LoneChimera())
    # Conditions.SetCondition('MetBob', True)
    
    GlobalVariables.FixedEncounters.append(Encounters.EncounterInTheFog())
    GlobalVariables.FixedEncounters.append(Encounters.RandomEncounter())
    GlobalVariables.FixedEncounters.append(Encounters.ChasedByChimeras())
    
    GlobalVariables.FixedEncounters.append(Encounters.WanderingMerchant())
    GlobalVariables.FixedEncounters.append(Encounters.RandomEncounter())

    GlobalVariables.FixedEncounters.append(Encounters.LookASign())
    GlobalVariables.FixedEncounters.append(Encounters.GenericBattle(Enemies.Mage(), 'A possessed mage approaches.')) # Just wanted to test this.
    GlobalVariables.FixedEncounters.append(Encounters.WanderingMerchant())
    GlobalVariables.FixedEncounters.append(Encounters.ExploreYsmayArea())
    GlobalVariables.FixedEncounters.append(Encounters.RandomEncounter())
    # GlobalVariables.FixedEncounters.append(Encounters.LoneChimera())

    GlobalVariables.FixedEncounters.append(Encounters.SearchingForFriends())
    GlobalVariables.FixedEncounters.append(Encounters.SearchingForAliveFriends())
    GlobalVariables.FixedEncounters.append(Encounters.RandomEncounter())
    GlobalVariables.FixedEncounters.append(Encounters.BoblinLovesYou())



    # GlobalVariables.FixedEncounters.append(Encounters.DualChimeras())


    GlobalVariables.GUI = gui.gui()
    GlobalVariables.GUI.startGUI()

def main():

    beginGame()

    # Eventually functions will be made for these button presses
 
        # if (keyboard.w.GetPressed()):
        #     trigger2 = True
        # else:
        #     trigger2 = Falses

        # if (trigger2 and keyboard.w.GetPressed()):
        #     ui.ClearScreen()
        #     trigger2 = False




    # Then (once they have been through all scenarios in Map 1),
    # have them choose between the FIRST scenario for 
    # Game Map 2 and Game Map 3.

if (__name__ == "__main__"):
    main()