# Generates a road map for the adventurer's journey

import Encounters
import random

class Map:
    def __init__(self, maxPositions, biome):
        self.map = []

        self.__maxPositions = maxPositions
        # This establishes which environments are going to be laid out in the map.
        self.__environments = Encounters.Mountains.allScenarios
        self.__spawnThresholds = []
        self.__currentChance = 0
        
        for environment in self.__environments:
            # Sets up mechanic for spawning based on percentages in constants.
            self.__spawnThresholds.append(environment.chanceAppearance + self.__currentChance)
            self.__currentChance += environment.chanceAppearance
        
        for position in range(0, self.__maxPositions, 1):
            # Actually assigns a position to each location
            self.determiner = random.randint(1, 100) / 100

            for locEnvironment in range(0, len(self.__environments), 1):
                if (locEnvironment == 0):
                    if (self.determiner < self.__spawnThresholds[locEnvironment]):
                        self.map.append(self.__environments[locEnvironment])
                elif (self.__spawnThresholds[locEnvironment - 1] < self.determiner and self.determiner < self.__spawnThresholds[locEnvironment]):
                    self.map.append(self.__environments[locEnvironment])

    def getScenarioList(self):
        return self.map