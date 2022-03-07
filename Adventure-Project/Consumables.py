class Consumable:
    def __init__(self):
        self.name = 'potion'
        self.restoration = 3
        self.cost = 6

class Potion(Consumable):
    def __init__(self):
        Consumable.__init__(self)
        self.name = 'Potion'
        self.restoration = 3
        self.cost = 6