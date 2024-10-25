import json
from CurrencyCollection import CurrencyCollection

class Parser:
    def __init__(self, data):
        self.data = data

    def parse_json(self, container: CurrencyCollection):
        try:
            data = json.loads(self.data)
        except json.JSONDecodeError as e:
            raise Exception(f"Nie udało się przetworzyć JSON: {e}")

        rates = data[0].get("rates", [])

        if not rates:
            raise ValueError("Błąd podczas przetwarzania danych: Nie znaleziono żadnych poprawnych kursów walut.")

        for item in rates:
            code = item.get("code")
            name = item.get("currency")
            rate = item.get("mid")

            if code and name and rate:
                container.addElementtoCollection(code, name, float(rate))
            else:
                raise ValueError(f"Brak danych dla waluty: {item}")

        if not any(currency.GetCode() == "PLN" for currency in container.getCollectionList()):
            container.addElementtoCollection("PLN", "Polski Złoty", 1.0)
