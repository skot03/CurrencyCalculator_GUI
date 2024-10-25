from DataProvider import DataProvider
from Parser import Parser
from CurrencyCollection import CurrencyCollection
from CalculateValue import CalculateValue
from InputValidator import get_currency_code

def main():
    collection = CurrencyCollection()
    exchanger = CalculateValue()

    provider = DataProvider()
    data = provider.getData()

    parser = Parser(data)
    parser.parse_json(collection)

    print("Dostępne waluty:")
    collection.printCollectionList()

    codeFrom = get_currency_code(collection, "\nPodaj kod waluty, z której chcesz dokonać konwersji: ")
    codeTo = get_currency_code(collection, "Podaj kod waluty, na którą chcesz dokonać konwersji: ")

    while True:
        try:
            value = float(input("Podaj kwotę do wymiany: "))
            if value <= 0:
                print("Kwota musi być liczbą dodatnią. Spróbuj ponownie.")
            else:
                break
        except ValueError:
            print("Niepoprawna kwota. Proszę podać wartość liczbową.")

    result = exchanger.exchange(codeFrom, codeTo, value, collection)
    print(f"\nWymiana {value} {codeFrom} na {codeTo}: {result} {codeTo}")

if __name__ == "__main__":
    main()
