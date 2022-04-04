from path import Path


class Graph:
    __paths: [Path]
    __towns: [str]

    def __init__(self):
        self.__paths = []
        self.__towns = []

    @property
    def Paths(self) -> [Path]:
        return self.__paths

    @property
    def Towns(self):
        if len(self.__towns) == 0:
            for path in self.Paths:
                for town in path['nodes']:
                    if town not in self.__towns:
                        self.__towns.append(town)
        return self.__towns

    def getTotalWeight(self):
        totalWeight = 0
        for path in self.Paths:
            totalWeight += path['weight']
        return totalWeight
