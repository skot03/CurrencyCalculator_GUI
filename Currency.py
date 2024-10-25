from ICurrency import ICurrency

class Currency(ICurrency):
    def __init__(self, code: str, name: str, rate: float):
        self.name = name
        self.rate = rate
        self.code = code

    def SetName(self, name: str):
        self.name = name

    def SetCode(self, code: str):
        self.code = code

    def SetRate(self, rate: float):
        self.rate = rate

    def GetName(self) -> str:
        return self.name

    def GetCode(self) -> str:
        return self.code

    def GetRate(self) -> float:
        return self.rate

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
