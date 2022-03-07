import Decisions
import Conditions

class Event:
    def __init__(self):
        self.conditionName = '' # link to "names" of conditions in Conditions.py
        self.location = 'Mountains'
        self.Decision = None
        self.story = []

class EncounterInTheFog(Event):
    def __init__(self):
        Event.__init__(self)
        self.conditionName = 'Foggy'
        self.Decision = Decisions.dealwBob
        self.story = ['As you traverse across a rocky mountainside, you hear a giggle.', '\"Hee... hee...\"', '\"Hee har!\"', 'The fog is too thick for you to be able to tell what it is, but think you see a shadow zip through the cloudy air somewhere in the distance.', '... or was it right in front of you?', 'The air is too thick with fog for you to be able to see anything, and you fear something may be about to attack you....']

class ChasedByChimeras(Event):
    def __init__(self):
        self.conditionName = 'Clear'
        self.Decision = Decisions.dealwChimeras
        self.story = ['As you traverse across a rocky mountainside, you hear a screech—no, a howl—no.... What is it?', 'You look back and don\'t see anything at first. As you take a look, the adrenaline immediately kicks in.', 'Chimeras.', 'You think they\'ve seen you.', 'You could hide now, as you\'re able to see a few good hiding spots in this area, but they might find you faster than if you\'re able to gain some distance first.']

class LookASign(Event):
    def __init__(self):
        self.Decision = Decisions.leftOrRight
        self.conditionName = 'RanFromBoblin'
        self.story = ['You come across a sign.', 'It reads: "LEFT: SWAMP     RIGHT: YSMAY\'S HUT"', 'You can practically see the swampland from here, and you know that the Magelike will be waiting for you somewhere over there.', 'You can also choose to go check and see who this "Ysmay" person is, but it might delay your journey. Night will soon fall.']

class ExploreYsmayArea(Event):
    def __init__(self):
        self.Decision = Decisions.lookAround
        self.conditionName = 'NearYsmay'
        self.story = ['Now that that\'s over with... Ysmay\'s hut... you\'re at the end of the trail, so... maybe you should leave.', 'On the other hand, if you stay and look around for another hour, then what\'s the worst that could happen?']

class SearchingForFriends(Event):
    def __init__(self):
        self.story = ['Now that you\'re in the swamp, you just need to find the Magelike\'s precise location.', 'Luckily, your Magelike friends have told you exactly what you need to do at this point.', 'You cast a frizzly compass, and use the keywords that the Magelike told you to use.', '"Specter."', '"Sunshine."', '"Obsidian."', '"Bolt."', 'The frizzly compass begins to spin around and point in the direction of the Magelike.', 'You head in that direction.', 'You arrive to find each of your Magelike friends\' dead bodies lying on the ground. No... no, no no no.', 'You spent far too long in the mountains, and you let the Magelike die.', 'It\'s your fault.', '"YOU."', 'The Annith looks at you menacingly.', '"COME WITH ME"']
        self.conditionName = 'FriendsAreKilled'
        self.Decision = Decisions.goWithHer
        self.location = 'swamp'

class SearchingForAliveFriends(Event):
    def __init__(self):
        self.story = ['Now that you\'re in the swamp, you just need to find the Magelike\'s precise location.', 'Luckily, your Magelike friends told you exactly what you need to do at this point.', 'You cast a frizzly compass, and use the keywords that the Magelike told you to use.', '"Specter."', '"Sunshine."', '"Obsidian."', '"Bolt."', 'The frizzly compass begins to spin around and point in the direction of the Magelike.', 'You head in that direction.', 'You see that your friends are in combat with some beasts. They also appear to be fighting one of their own (someone who you don\'t recognize).', 'You rush toward them, prepared to join the small battle, when you feel the air crack like a whip through your soul.', 'The opposing Magelike lets out a burst of magicka which pulses with levels of strength you have never encountered before.', 'You are knocked to the ground by the explosion, and your insides feel like they\'re melting.', 'As you begin to recover, you notice that your Magelike friends are not getting up with you.', 'The Magelike who released the supposed death spell is now gone, and you aren\'t sure which way you saw them go.', 'An Annith runs up to you.', '"What was that?" she asks.']
        self.Decision = Decisions.whichWayDidTheyGo
        self.conditionName = 'FriendsAreNotKilled'

class BoblinLovesYou(Event):
    def __init__(self):
        self.story = ['You continue to travel through the dense jungle.', 'You take a break and sit on top of a giant cliff with Matilda.', 'You can see the city in the distance.', '"Heee hee... hee! Hee har!"', 'Boblin: The Goblin emerges from behind you!', '"I come with gifts!"', 'You are feeling very impulsive!']
        self.Decision = Decisions.shoveBoblin
        self.conditionName = 'MetBob'
        
# class Swampilicious(Event):
#     def __init__(self):
#         self.conditionName = 
#         self.Decision =
#         self.story = ['']