from town import Town


class Path:
    __weight: int
    __towns: [Town]

    def __init__(self, weight: int, town1: Town, town2: Town):
        self.__weight = weight
        self.__towns = []
        self.__towns.append(town1)
        self.__towns.append(town2)

    @property
    def Weight(self) -> int:
        return self.__weight

    @property
    def Towns(self) -> [Town]:
        return self.__towns