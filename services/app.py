import tkinter as tk
from tkinter import ttk
import requests
from .api import request_currency, request_currency_by_type
from .excel import process_xlsx


WINDOW_TITLE = 'App'
ETHERIUM = 'Etherium'
BITCOIN = 'Bitcoin'
LITECOIN = 'Litecoin'


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.default_paddings = {'padx': 5, 'pady': 5}
        self.set_window_geometry()
        self.currency_types = (BITCOIN, ETHERIUM,  LITECOIN)
        self.current_currency_type = tk.StringVar()
        self.create_wigets()

    def set_window_geometry(self):
        self.window_width = 600
        self.window_height = 400

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        self.geometry(
            f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}'
        )

    def print_currency_cost(self):
        output_label = ttk.Label(
            foreground='red', font=("Helvetica", 14)
        )
        output_label.grid(
            column=0, row=2, sticky=tk.W,
            **self.default_paddings
        )

        currency_type = self.current_currency_type.get()
        currency_cost = self.get_currency_cost(currency_type)

        output_label['text'] = f'{currency_type} exchange rate in dollars now: {currency_cost}'

    def generate_report(self):
        currency = request_currency()
        process_xlsx(**currency)

    def get_currency_cost(self, currency_type):
        options = {
            BITCOIN: "BTC",
            ETHERIUM: "ETH",
            LITECOIN: "LTC",
        }

        currency_value = request_currency_by_type(
            currency_type=options.get(currency_type, "BTC")
        )
        return currency_value

    def create_wigets(self):
        label = ttk.Label(
            self,  text='Select currency:', font=("Helvetica", 14)
        )
        label.grid(column=0, row=0, sticky=tk.W, **self.default_paddings)

        ttk.Style().configure("TButton", padding=6, relief="flat", background="#000")
        ttk.Style().configure("TMenubutton", padding=6, relief="flat", background='white')

        option_menu = ttk.OptionMenu(
            self,
            self.current_currency_type,
            self.currency_types[0],
            *self.currency_types
        )
        option_menu.grid(column=1, row=0, sticky=tk.W, **self.default_paddings)

        button = ttk.Button(
            self, text='Get Cost', command=self.print_currency_cost
        )
        button.grid(column=1, row=3, sticky=tk.W, **self.default_paddings)

        button_xlsl = ttk.Button(
            self, text='To Excel',
            command=self.generate_report
        )
        button_xlsl.grid(column=2, row=3, sticky=tk.W, **self.default_paddings)
