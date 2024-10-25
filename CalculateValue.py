from ICalculateValue import ICalculateValue
from CurrencyCollection import CurrencyCollection

class CalculateValue(ICalculateValue):
    def __init__(self):
        pass

    def exchange(self, codeFrom: str, codeTo: str, value: float, container: CurrencyCollection) -> float:
        valueFrom = None
        valueTo = None

        for currency in container.getCollectionList():
            if currency.GetCode() == codeFrom:
                valueFrom = currency.GetRate()
            if currency.GetCode() == codeTo:
                valueTo = currency.GetRate()

        if valueFrom is None:
            raise ValueError(f"Kod waluty '{codeFrom}' nie znaleziony.")

        if valueTo is None:
            raise ValueError(f"Kod waluty '{codeTo}' nie znaleziony.")

        return value * (valueFrom / valueTo)
