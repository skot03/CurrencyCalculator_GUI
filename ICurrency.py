from abc import ABC, abstractmethod

class ICurrency(ABC):
    @abstractmethod
    def SetName(self, name: str):
        pass

    @abstractmethod
    def SetCode(self, code: str):
        pass

    @abstractmethod
    def SetRate(self, rate: float):
        pass

    @abstractmethod
    def GetName(self) -> str:
        pass

    @abstractmethod
    def GetCode(self) -> str:
        pass

    @abstractmethod
    def GetRate(self) -> float:
        pass
