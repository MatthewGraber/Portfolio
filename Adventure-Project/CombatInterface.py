"""
CombatInterface.py
By Matthew Graber
"""

# Temporary imports for testing
from Actions import Action
import Character, Enemies, Spells

import GlobalVariables
import tkinter, time

class Combat:
    def __init__(self):
        self.PC = GlobalVariables.PC
        self.enemy = GlobalVariables.Enemy
        self.currentRound = 0
        self.enemyActing = True
        self.PCacting = True
        self.countering = False
        self.actionsChosen = []
        self.currentStaminaCost = 0
        self.currentMagickaCost = 0

    def round(self):
        # print("Actions chosen", self.actionsChosen)
        self.PCHitMain = False
        self.PCHitOff = False
        if len(self.actionsChosen) >= 3:
            if self.PCacting:
                self.executePCActions()
                # self.selectedActionVar.set('')
            else:
                self.PCacting = True
            
    def chooseAction(self, a):
        if len(self.actionsChosen) < 3 and GlobalVariables.GUI.canTakeActions:
            if self.PC.actions[a].canTakeAction(self.currentStaminaCost):
                self.actionsChosen.append(a)
                GlobalVariables.GUI.typeOut("Action " + str(4 - self.PC.energy) + ": " + self.PC.actions[a].name)
                self.PC.energy -= 1
                self.currentStaminaCost += self.PC.actions[a].staminaCost
                actionDisplay = ''
                for i in range(1, len(self.actionsChosen) + 1):
                    actionDisplay += "Action " + str(i)+ ": " + self.PC.actions[self.actionsChosen[i-1]].name + ". "
                # self.selectedActionVar.set(actionDisplay)
                if len(self.actionsChosen) >= 3:
                    self.round()
            else:
                GlobalVariables.GUI.typeOut("Not enough stamina!")
    
    def exectueEnemyActions(self):
        if not self.enemy.alive:
            self.PC.endOfCombat()
            if self.PC.alive:
                GlobalVariables.Encounter.victoryGui([GlobalVariables.GUI.combatFrame])
                self.enemyActing = False
            else:
                GlobalVariables.Encounter.defeatGui([GlobalVariables.GUI.combatFrame])
        else:
            if self.enemyActing:
                self.enemy.attackCycle()
        
            else:
                self.enemyActing = True
                self.enemy.hasHit = False
            if self.countering:
                self.PC.inventory.getMainWeapon().counter()
            
            self.PC.endOfRound()
            self.enemy.sendMessage(self.enemy.displayMessage)

            self.currentRound += 1
            self.actionsChosen = []
            self.currentStaminaCost = 0
            self.currentMagickaCost = 0
            # self.selectedActionVar.set('')
            # self.selectedActionLabel.update()

            if not self.PC.alive:
                GlobalVariables.Encounter.defeatGui([GlobalVariables.GUI.combatFrame])

    def executePCActions(self):
        action1 = self.actionsChosen[0]
        action2 = self.actionsChosen[1]
        action3 = self.actionsChosen[2]

        self.actionQue = []

        if action1 == action2:
            if action2 == action3:
                self.actionQue.append([action1, 3])
                # self.PC.actions[action1].execute(3)
            else:
                self.actionQue.append([action1, 2])
                self.actionQue.append([action3, 1])
                # self.PC.actions[action1].execute(2)
                # self.PC.actions[action3].execute(1)
        elif action1 == action3:
            self.actionQue.append([action1, 2])
            self.actionQue.append([action2, 1])
            # self.PC.actions[action1].execute(2)
            # self.PC.actions[action2].execute(1)
        elif action2 == action3:
            self.actionQue.append([action1, 1])
            self.actionQue.append([action2, 2])
            # self.PC.actions[action1].execute(1)
            # self.PC.actions[action2].execute(2)
        else:
            self.actionQue.append([action1, 1])
            self.actionQue.append([action2, 1])
            self.actionQue.append([action3, 1])
            # self.PC.actions[action1].execute(1)
            # self.PC.actions[action2].execute(1)
            # self.PC.actions[action3].execute(1)w
        # Set currentAction to -1 and immediately update it
        # Because each action calls nextAction when it ends, we have to update the currentAction before executing it
        self.currentAction = -1
        self.nextAction()

    def nextAction(self):
        GlobalVariables.GUI.updateStats()
        if (self.currentAction < len(self.actionQue)-1):
            self.currentAction += 1
            self.PC.actions[self.actionQue[self.currentAction][0]].execute(self.actionQue[self.currentAction][1])
        else:
            self.exectueEnemyActions()
    
    def setDisplay(self):
        allDisplayInfo = self.enemy.display()

        # allDisplayInfo += "\n\n"
        # allDisplayInfo += self.PC.display()
        # self.informationVar.set(allDisplayInfo)
        # self.informationLabel.update()
        # self.selectedActionLabel.update()
        GlobalVariables.GUI.updateStats()
        GlobalVariables.GUI.typeOut(allDisplayInfo)

        time.sleep(1)

    def hasEnded(self):
        if not (self.PC.alive and self.enemy.alive):
            return True
        return False
 

def main():
    GlobalVariables.PC = Character.Rogue()
    GlobalVariables.PC.inventory.addSpell(Spells.MageArmor())
    GlobalVariables.Enemy = Enemies.Chimera()
    GlobalVariables.Combat = Combat()
    # while commy.enemy.alive and commy.PC.alive:
    #     print("Round:", commy.currentRound)
    #     print("HP:", commy.PC.getHp())
    #     print("Enemy HP:", commy.enemy.getHp())
    #     commy.round()

if __name__ == "__main__":
    main()