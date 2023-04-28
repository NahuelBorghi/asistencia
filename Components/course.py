class Course:
    # Constructor
    def __init__(self, id:int, name:str) -> None:
        # Variables de instancia
        self.__id = id
        self.__name = name
    # Metodos
    #   Setters
    def setID(self, id:int) -> None:
        self.__id = id
    def setName(self, name:str) -> None:
        self.__name = name
    #   Getters
    def getID(self) -> int:
        return self.__id
    def getName(self) -> str:
        return self.__name