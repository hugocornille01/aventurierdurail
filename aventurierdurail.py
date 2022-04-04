import json


class AventurierDuRail:
    __filePath: str
    __paths: [str]

    def __init__(self, filePath):
        self.__filePath = filePath
        self.__loadConfiguration()

    @property
    def Paths(self) -> [str]:
        return self.__paths

    def __loadConfiguration(self):
        with open(self.__filePath) as file:
            self.__paths = json.load(file)
