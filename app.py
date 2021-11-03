import tkinter as tk
from tkinter import ttk


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('App')

        self.window_width = 300
        self.window_height = 200

        self.screen_width = self.winfo_screenwidth()
        self.screen_height = self.winfo_screenheight()

        self.center_x = int(self.screen_width/2 - self.window_width / 2)
        self.center_y = int(self.screen_height/2 - self.window_height / 2)
        self.geometry(f'{self.window_width}x{self.window_height}+{self.center_x}+{self.center_y}')

        self.currency =('val1','val2','val3')

        self.option_var = tk.StringVar(self)
        self.create_wigets()

    def select(self, option):
        paddings = {'padx': 5, 'pady': 5}
        baton=ttk.Button(self, text='Print v consol', command=lambda: self.print_in_consol(self.option_var.get()))
        baton.grid(column=1, row=3, sticky=tk.W, **paddings)

    def print_in_consol(self, option):
        print(option)

    def create_wigets(self):
        paddings = {'padx': 5, 'pady': 5}

        label = ttk.Label(self,  text='Select currency:')
        label.grid(column=0, row=0, sticky=tk.W, **paddings)
        option_menu = ttk.OptionMenu(
            self,
            self.option_var,
            self.currency[0],
            *self.currency,
            command=self.select)

        baton=ttk.Button(self, text='Print v consol', command=lambda: self.print_in_consol(self.option_var.get()))
        baton.grid(column=1, row=3, sticky=tk.W, **paddings)

        option_menu.grid(column=1, row=0, sticky=tk.W, **paddings)
        self.output_label = ttk.Label(self, foreground='red')
        self.output_label.grid(column=0, row=1, sticky=tk.W, **paddings)

    def option_changed(self, *args):
        self.output_label['text'] = f'currency: {self.option_var.get()}'


if __name__ == "__main__":
    app = App()
    app.mainloop()
