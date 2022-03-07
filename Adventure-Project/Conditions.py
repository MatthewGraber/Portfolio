import GlobalVariables

class Condition:
    def __init__(self):
        self.name = ''
        self.met = False
        self.counter = 0 # Initial checks
        self.max = 3 # Checks needed for condition to be met

class BoblinPathInstantiated(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'BoblinPathInstantiated'

class HaroldIsAVampire(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'HaroldIsAVampire'
        self.max = 4

class LearnedOfContinuanceKey(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'LearnedOfContinuanceKey'
        self.max = 1

class EncounteredMythergius(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'EncounteredMythergius'
        self.max = 1

class Foggy(Condition): # This is specific to mountains region
    def __init__(self):
        Condition.__init__(self)
        self.name = 'Foggy'

class Clear(Condition): # Also for Mountains
    def __init__(self):
        Condition.__init__(self)
        self.name = 'Clear'

class ChimerasAreHungryForYou(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'ChimerasAreHungryForYou'

class YouAreWanted(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'YouAreWanted'

class RanFromBoblin(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'RanFromBoblin'

class NearYsmay(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'NearYsmay'

class FriendsAreKilled(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'FriendsAreKilled'

class FriendsAreNotKilled(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.met = True
        self.name = 'FriendsAreNotKilled'

class KilledMatilda(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'KilledMatilda'

class FoundYsmay(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'FoundYsmay'

class MetBob(Condition):
    def __init__(self):
        Condition.__init__(self)
        self.name = 'MetBob'

class No(Condition): # No Condition; Always true
    def __init__(self):
        Condition.__init__(self)
        self.name = 'No'
        self.met = True

class List: # Reference list from global variables (NOT HERE)
    def __init__(self):
        self.allConditions = [MetBob(), FoundYsmay(), KilledMatilda(), FriendsAreNotKilled(), FriendsAreKilled(), No(), NearYsmay(), BoblinPathInstantiated(), HaroldIsAVampire(), LearnedOfContinuanceKey(), EncounteredMythergius(), Foggy(), Clear(), ChimerasAreHungryForYou(), YouAreWanted(), RanFromBoblin()]
    
def CheckCondition(conditionName):
    for condition in GlobalVariables.conditionsList:
        if conditionName == condition.name:
            if condition.met:
                return True
            else:
                return False

def SetCondition(conditionName, value):
    for condition in GlobalVariables.conditionsList:
        if conditionName == condition.name:
            condition.met = value