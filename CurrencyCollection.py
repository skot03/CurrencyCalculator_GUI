from ICurrencyCollection import ICurrencyCollection
from Currency import Currency

class CurrencyCollection(ICurrencyCollection):
    def __init__(self):
        self.currencies = []

    def addElementtoCollection(self, code: str, name: str, rate: float):
        currency = Currency(code, name, rate)
        self.currencies.append(currency)

    def getCollectionList(self) -> list:
        return self.currencies

    def printCollectionList(self):
        for currency in self.currencies:
            print(f"Kod: {currency.GetCode()}, Nazwa: {currency.GetName()}, Wspolczynnik: {currency.GetRate()}")

    def removeElementFromCollection(self, code: str):
        found = False
        for element in self.currencies:
            if element.GetCode() == code:
                self.currencies.remove(element)
                found = True
                break
        if not found:
            print(f"Waluta z kodem {code} nie znaleziona.")
