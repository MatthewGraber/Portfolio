"""
Holds all global variables
All variables must be initalized as empty to prevent circular import errors
GlobalConstants may NEVER import another module for object definition
"""
# Current PC
PC = None
# Current enemy the PC is facing
Enemy = None
# Current Combat the PC is in
Combat = None
# Ooey Gooey
GUI = None
# Encounter
Encounter = None
RandomEncounters = []
FixedEncounters = []
# Increments by 1 before being used
CurrentEncounterNumber = -1
# Conditions List
conditionsList = []
# Gems
currentGems = None