from CurrencyCollection import CurrencyCollection

def get_currency_code(collection: CurrencyCollection, prompt: str) -> str:

    while True:
        code = input(prompt).upper()
        if any(currency.GetCode() == code for currency in collection.getCollectionList()):
            return code
        else:
            print(f"Nieprawidlowy kod '{code}'. Podaj prawidlowy kod.")
