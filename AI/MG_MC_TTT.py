"""
MG_MC_TTT.py
Matthew Graber
2/26/2022
An AI that plays Tic Tac Toe using a Monte-Carlo method to determine its behaviour
"""

from ast import Raise
from functools import partial
from random import choice
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

Rules = []

class Board:
    def __init__(self):
        global Rules
        Rules = generateRules()
        self.environment = (" ", " ", " ", " ", " ", " ", " ", " ", " ")

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
    
    # Computes the new move using a heuristic
    def NPC(self):
        t1 = (time.perf_counter_ns())
        ex = reflex_agent(self.environment)
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
        if checkForVictory(self.environment, "X"):
            tkinter.messagebox.showinfo(title="Victory", message="You have won!")
            self.main.destroy()
            return
        elif checkForEnd(self.environment):
            tkinter.messagebox.showinfo(title="Tie", message="Tie! No victor. Maybe now you'll understand the futility of this game.")
            self.main.destroy()
            return
        self.NPC()
        checkForEnd(self.environment)
        if checkForVictory(self.environment, "O"):
            tkinter.messagebox.showinfo(title="Defeat", message="You have been defeated!")
            self.main.destroy()
        return

# Determines which move to use
def heuristic(env):
    predictedWins = 0
    for i in range(50):
        e = env
        for j in range(8):
            nextMoves = reflex_agent(e)
            y = choice(nextMoves)
            e = y[0]
            if checkForVictory(e, "X"):
                predictedWins -=1
                break
            if checkForVictory(e, "O"):
                predictedWins += 1
                break
            if checkForEnd(e):
                break
            if j == 7:
                raise Exception("Monte Carlo not stopping.")
    return predictedWins + 50

def checkForVictory(env, player):
    for i in lines:
        numX = 0
        for j in i:
            if env[j] == player:
                numX += 1
        if numX == 3:
            return True
    return False

def checkForEnd(env):
    for i in env:
        if i == " ":
            return False
    return True

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
def reflex_agent(env):
    expansion = []
    for rule in Rules:
        if rule[0](env) > 0:  
            e = rule[1](env)       
            expansion.append((e, rule[1]))
    return expansion

# Generates all rules
def generateRules():
    for i in range(0, 9):
        newMove = Move("X", i)
        Rules.append((newMove.check, newMove.act))
        newMove = Move("O", i)
        Rules.append((newMove.check, newMove.act))
    return Rules

if __name__ == "__main__":
    board = Board()