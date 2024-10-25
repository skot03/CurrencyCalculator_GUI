from abc import ABC, abstractmethod

class ICurrencyCollection(ABC):
    @abstractmethod
    def addElementtoCollection(self, code: str, name: str, rate: float):
        pass

    @abstractmethod
    def getCollectionList(self) -> list:
        pass

    @abstractmethod
    def printCollectionList(self):
        pass

    @abstractmethod
    def removeElementFromCollection(self, code: str):
        pass
