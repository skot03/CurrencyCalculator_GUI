from abc import ABC, abstractmethod
from CurrencyCollection import CurrencyCollection

class ICalculateValue(ABC):
    @abstractmethod
    def exchange(self, codeFrom: str, codeTo: str, value: float, container: CurrencyCollection) -> float:
        pass
