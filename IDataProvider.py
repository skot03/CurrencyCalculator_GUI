from abc import ABC, abstractmethod

class IDataProvider(ABC):
    @abstractmethod
    def getData(self):
        pass
