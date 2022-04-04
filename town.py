class Town:
    __name: str

    def __init__(self, name):
        self.__name = name

    @property
    def Name(self) -> str:
        return self.__name
