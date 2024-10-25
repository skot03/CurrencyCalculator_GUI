import requests
from IDataProvider import IDataProvider

class DataProvider(IDataProvider):
    _link = "https://api.nbp.pl/api/exchangerates/tables/a/"
    _instance = None

    def __init__(self):
        if DataProvider._instance is not None:
            raise Exception("To singleton!")
        else:
            DataProvider._instance = self

    def getData(self):
        response = requests.get(self._link)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception("Problem z fetchowaniem Api.")
