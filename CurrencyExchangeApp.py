import tkinter as tk
from tkinter import messagebox
from CurrencyCollection import CurrencyCollection
from CalculateValue import CalculateValue
from DataProvider import DataProvider
from Parser import Parser

class CurrencyExchangeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Exchange")

        # Initialize the data
        self.collection = CurrencyCollection()
        self.exchanger = CalculateValue()

        self.load_data()

        # Currency From
        tk.Label(root, text="From Currency Code:").pack()
        self.codeFrom = tk.Entry(root)
        self.codeFrom.pack()

        # Currency To
        tk.Label(root, text="To Currency Code:").pack()
        self.codeTo = tk.Entry(root)
        self.codeTo.pack()

        # Amount
        tk.Label(root, text="Amount:").pack()
        self.amount = tk.Entry(root)
        self.amount.pack()

        # Convert Button
        self.convert_btn = tk.Button(root, text="Convert", command=self.convert_currency)
        self.convert_btn.pack()

        # Result Label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def load_data(self):
        provider = DataProvider()
        data = provider.getData()
        parser = Parser(data)
        parser.parse_json(self.collection)

    def convert_currency(self):
        try:
            codeFrom = self.codeFrom.get().upper()
            codeTo = self.codeTo.get().upper()
            amount = float(self.amount.get())
            result = self.exchanger.exchange(codeFrom, codeTo, amount, self.collection)
            self.result_label.config(text=f"{amount} {codeFrom} = {result:.2f} {codeTo}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyExchangeApp(root)
    root.mainloop()
