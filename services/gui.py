import tkinter as tk
from tkinter import ttk
import requests
from services.get_api_values import get_values
from services.excel import generate_report


WINDOW_TITLE = 'App'
ETHERIUM = 'Etherium'
BITCOIN = 'Bitcoin'
LITECOIN = 'Litecoin'


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title(WINDOW_TITLE)
        self.default_paddings = {'padx': 5, 'pady': 5}
        self.set_window_geometry()
        self.currency_types = (BITCOIN, ETHERIUM,  LITECOIN)
        self.current_currency_type = tk.StringVar()
        self.create_wigets()
        self.print_currency_cost()
        self.values = get_values()
        # self.generate_reports = generate_report()
        self.get_currency_costs()
        self.get_currency_cost()

    def set_window_geometry(self):
        self.window_width = 600
        self.window_height = 400

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        self.geometry(
            f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')



    def print_currency_cost(self, *args):
        
        output_label = ttk.Label(self, foreground='red',font=("Helvetica", 14))
        output_label.grid(column=0, row=2, sticky=tk.W,
                            **self.default_paddings)
        output_label['text'] = f'{self.current_currency_type.get()} exchange rate in dollars now: {self.get_currency_cost()}'
    
    def get_currency_costs(self):
        return self.get_values()
    
    def get_currency_cost(self):
        val=self.get_currency_costs()
        currency_type = self.current_currency_type.get()
        if currency_type == BITCOIN:
            currency_value = val[0]
        elif currency_type == ETHERIUM:
            currency_value = val[1]
        elif currency_type == LITECOIN:
            currency_value = val[2]
        else:
            print('error')
        return currency_value

    def create_wigets(self):        

        label = ttk.Label(self,  text='Select currency:')
        label.grid(column=0, row=0, sticky=tk.W, **self.default_paddings)

        option_menu = ttk.OptionMenu(
            self,
            self.current_currency_type,
            self.currency_types[0],
            *self.currency_types
        )
        option_menu.grid(column=1, row=0, sticky=tk.W, **self.default_paddings)
        button = ttk.Button(self, text='Get Cost', 
                            command=self.print_currency_cost)
        button.grid(column=1, row=3, sticky=tk.W, **self.default_paddings)

        button_xlsl = ttk.Button(self, text='To Excel', 
                            command=generate_report(self.get_currency_costs()))
        button_xlsl.grid(column=2, row=5, sticky=tk.W, **self.default_paddings)
