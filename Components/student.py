class Student:
    # Constructor
    def __init__(self, id, name, surname) -> None:
        # Variables de instancia
        self.__id = id
        self.__name = name
        self.__surname = surname
    # Metodos
    #   Setters
    def setID(self, id:int) -> None:
        self.__id = id
    def setName(self, name:str) -> None:
        self.__name = name
    def setSurName(self, surname:str) -> None:
        self.__surname = surname
    #   Getters
    def getID(self) -> int:
        return self.__id
    def getName(self) -> str:
        return self.__name
    def getSurName(self) -> str:
        return self.__surname