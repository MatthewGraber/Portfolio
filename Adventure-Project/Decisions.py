import abc
import Main
import Consequences

consequences = Consequences.allConsequences()

class Decision(abc.ABC):
    narrative = ''
    choices = []
    consequences = []
    consequenceChances = []

class dealwBob(Decision):
    choices = ['Swing your main weapon rapidly (you could hit something)', 'Run away blindly (you will probably be safe)']
    consequences = [[consequences.IrritateBoblin, consequences.StartleBoblin], [consequences.EscapeBoblin, consequences.FallOffCliff, consequences.BoblinSurprise]]
    consequenceChances = [[.5, .5], [.65, .15, .2]]

class dealwChimeras(Decision):
    choices = ['Search for a good hiding spot now', 'Run, then hide']
    consequences = [[consequences.getBittenByChimera, consequences.findHidingSpot], [consequences.catchingUpToYou, consequences.enterSecretLair]]
    consequenceChances = [[.6, .4], [.68, .32]]

class leftOrRight(Decision):
    choices = ['Go left (Swamp)', 'Go right (Ysmay)']
    consequences = [[consequences.getLostFromSign, consequences.makeItToSwamp], [consequences.findYsmayByFollowingSign]]
    consequenceChances = [[.35, .65], [1]]

class lookAround(Decision):
    choices = ['Stay and look around for a while', 'Turn around and head back toward the swamp']
    consequences = [[consequences.hiYsmay, consequences.kidnapped], [consequences.makeItToSwamp]]
    consequenceChances = [[.5, .5], [1]]

class goWithHer(Decision):
    choices = ['Go with her', 'Attempt to assassinate her', 'Ask her who she is', 'Demand to know what happened']
    consequences = [[consequences.findOutWhoSheIs], [consequences.assassinateMatilda, consequences.failAssassinateMatilda], [consequences.findOutWhoSheIs], [consequences.demandInfoFromMatilda]]
    consequenceChances = [[1], [.3, .7], [1], [1]]

class whichWayDidTheyGo(Decision):
    choices = ['Ask the Annith which way the Magelike went']
    consequences = [[consequences.comeWme]]
    consequenceChances = [[1]]

class shoveBoblin(Decision):
    choices = ['Shove Boblin off of the cliff (teaches him a lesson)', 'Shove Matilda off of the cliff (why are you even considering this?)', 'Jump off of the cliff (are you okay?)']
    consequences = [[consequences.BoblinPathInstantiated], [consequences.MatildaFalls, consequences.MatildaFightsBack], [consequences.JumpedOffCliff]]
    consequenceChances = [[1], [.6, .4], [1]]