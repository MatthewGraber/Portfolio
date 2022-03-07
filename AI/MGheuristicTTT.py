"""
MGheuristicTTT.py
Matthew Graber
3/3/2022
A program that lets you play tic-tac-toe against an AI
If you play enough, you might learn the meaning of futility
"""

from functools import partial
import tkinter
import tkinter.messagebox
import time

# These are the 'lines' that can be scored on
lines = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)
    )
corners = (0, 2, 6, 8)
edges = (1, 3, 5, 7)

class Board:
    def __init__(self):

        self.environment = (" ", " ", " ", " ", " ", " ", " ", " ", " ")
        self.Rules = generateRules()

        self.totalMoves = 0 # Tracks the total moves taken so far

        self.main = tkinter.Tk()
        self.frames = []
        self.stringVars = []
        self.buttons = []

        for i in range(0, 3):
            self.frames.append(tkinter.Frame())
        
        for i in range(0, 9):
            self.stringVars.append(tkinter.StringVar())
            self.stringVars[i].set(" ")
            button = tkinter.Button(self.frames[int(i/3)], textvariable=self.stringVars[i], borderwidth=2, relief="solid", font = ('Comic Sans MS', 20), width=2, height=1, command = partial(self.setToX, i))
            button.pack(side = "left")
            self.buttons.append(button)

        for j in range(0, 3):
            self.frames[j].pack(side = "top")
            
        self.main.mainloop()      
    
    def setEnvironment(self, env):
        self.environment = env
        for i in range(0, 9):
            self.stringVars[i].set(env[i])

    def setToX(self, num):
        if self.stringVars[num].get() == " ":
            newEnv = self.environment[0:num] + ("X",) + self.environment[num+1:]
            self.setEnvironment(newEnv)
            self.referee()
            
    def checkForVictory(self, player):
        for i in lines:
            numX = 0
            for j in i:
                if self.environment[j] == player:
                    numX += 1
            if numX == 3:
                return True
        return False
    
    # Computes the new move using a heuristic
    def NPC(self):
        t1 = (time.perf_counter_ns())
        ex = reflex_agent(self.environment, self.Rules)
        print("RT:", time.perf_counter_ns()-t1) # Prints the time it takes the reflex agent to run
        highScore = 0
        currentScore = 0
        currentMove = 0
        t2 = (time.perf_counter_ns())
        for i in range(0, len(ex)):
            currentScore = heuristic(ex[i][0])
            if currentScore > highScore:
                highScore = currentScore
                currentMove = i
        print("HT:", time.perf_counter_ns()-t2) # Prints the time it takes the heuristic to run
        self.setEnvironment(ex[currentMove][0])
        return

    # Prints winner or continues game graphically
    def referee(self):
        self.totalMoves += 1
        if self.checkForVictory("X"):
            tkinter.messagebox.showinfo(title="Victory", message="You have won!")
            self.main.destroy()
            return
        elif self.totalMoves == 9:
            tkinter.messagebox.showinfo(title="Tie", message="Tie! No victor. Maybe now you'll understand the futility of this game.")
            self.main.destroy()
            return
        self.NPC()
        self.totalMoves += 1
        if self.checkForVictory("O"):
            tkinter.messagebox.showinfo(title="Defeat", message="You have been defeated!")
            self.main.destroy()
        return

# Determines which move to use
def heuristic(env):
    score = 0
    for i in lines:
        # Counts the number of X's and O's in this line
        numX = 0
        numO = 0
        for j in i:
            if env[j] == "X":
                numX += 1
            elif env[j] == "O":
                numO += 1
        # If there's win, we always take it
        if numO == 3:
            return 100
        # If there's a win for X, we avoid it unless we find a win later
        elif numO == 0 and numX == 2:
            score -= 100
        # If there's two O's and no X's, this is worth 3 points
        elif numO == 2 and numX == 0:
            score += 3
        # If there's one O and no X's, this move is worth 1 point
        elif numO == 1 and numX == 0:
            score += 1
    # Check for the sneaky corner trick
    if ((env[0] == "X") + (env[2] == "X") + (env[6] == "X") + (env[8] == "X") >= 2):
        for i in edges:
            score += (env[i] == "O")
                
    return score

# A generic class to check to see if a given move is legal
class Move:
    # player = "X" or "O", space = 0 to 8
    def __init__(self, player, space):
        self.player = player
        self.space = space
        if player == "X":
            self.check = self.checkX
        else:
            self.check = self.checkO

    # Returns the new environment after moving
    def act(self, env):
        newEnv = env[0:self.space] + (self.player,) + env[self.space+1:]
        return newEnv

    # Checks to see if it is a legal move for X
    def checkX(self, env):
        checksum = 0
        for i in env:
            if i == "X":
                checksum += 1
            elif i == "O":
                checksum -= 1
        if checksum != 0:
            return False
        elif env[self.space] == ' ':
            return True
        else:
            return False

    # Checks to see if it is a legal move for O
    def checkO(self, env):
        checksum = 0
        for i in env:
            if i == "X":
                checksum += 1
            elif i == "O":
                checksum -= 1
        if checksum != 1:
            return False
        elif env[self.space] == ' ':
            return True
        else:
            return False

# Reflex agent
def reflex_agent(env, Rules):
    expansion = []
    for rule in Rules:
        if rule[0](env) > 0:  
            e = rule[1](env)       
            expansion.append((e, rule[1]))
    return expansion

# Generates all rules
def generateRules():
    Rules = []
    for i in range(0, 9):
        newMove = Move("X", i)
        Rules.append((newMove.check, newMove.act))
        newMove = Move("O", i)
        Rules.append((newMove.check, newMove.act))
    return Rules

if __name__ == "__main__":
    board = Board()
