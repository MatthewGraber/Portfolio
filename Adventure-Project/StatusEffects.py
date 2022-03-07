import GlobalVariables

class TempBuff:
    def __init__(self):
        self.buff = []
    
    def addBuff(self, source, value, duration, stacks = False):
        for i in self.buff:
            if i[0] == source:
                if i[2] < duration and not stacks:
                    i[2] = duration
                elif stacks and str(i[2]).isnumeric():
                    i[2] += duration
                if i[1] < value and not stacks:
                    i[1] = value
                elif stacks:
                    i[1] += value
                return
        self.buff.append([source, value, duration])
    
    def reduceAll(self):
        for i in self.buff:
            if str(i[2]).isnumeric():
                i[2] -= 1
                if i[2] == 0:
                    GlobalVariables.GUI.typeOutDelay(i[0] + " status effect has ended.")
                    self.buff.remove(i)
    
    def endSingleCombatEffects(self):
        for i in self.buff:
            if str(i[2]).isnumeric():
                self.buff.remove(i)
            elif i[2].upper() == "ENCOUNTER":
                self.buff.remove(i)
    
    def getBuffTypes(self):
        names = []
        for i in self.buff:
            names.append(i[0])
        return names

    def get(self):
        totalBuff = 0
        for i in self.buff:
            totalBuff += i[1]
        return totalBuff