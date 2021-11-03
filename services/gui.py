import tkinter as tk
from tkinter import ttk
from services.api import get_values


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
        self.currency_types = (ETHERIUM, BITCOIN, LITECOIN)
        self.current_currency_type = tk.StringVar()
        self.create_wigets()

    def set_window_geometry(self):
        self.window_width = 300
        self.window_height = 200

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.center_x = int(self.screen_width / 2 - self.window_width / 2)
        self.center_y = int(self.screen_height / 2 - self.window_height / 2)
        self.geometry(
            f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')

    def get_currency_cost(self):
        currency_type = self.current_currency_type.get()
        if currency_type == BITCOIN:
            currency_value = get_values()[0]
        elif currency_type == ETHERIUM:
            currency_value = get_values()[1]
        elif currency_type == LITECOIN:
            currency_value = get_values()[2]
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

        output_label = ttk.Label(self, foreground='red')
        output_label.grid(column=0, row=1, sticky=tk.W,
                          **self.default_paddings)

        button = ttk.Button(self, text='Get Cost',
                            command=self.get_currency_cost)
        button.grid(column=1, row=3, sticky=tk.W, **self.default_paddings)

        # self.output_label = ttk.Label(self, foreground='red')
        # self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)

        def option_changed(self, *args):
            output_label['text'] = f'{self.current_currency_type} exchange rate in dollars now: {self.get_currency_cost()}'
