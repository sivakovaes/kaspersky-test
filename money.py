import tkinter as tk
from tkinter import StringVar, ttk

root = tk.Tk()
root.title('App')

window_width = 300
window_height = 200

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)

currency=['val1','val2','val3']
output_label = ttk.Label(foreground='red')
def option_changed():
        output_label['text'] = f'You selected: {option_var.get()}'

option_var = StringVar()
option_menu = ttk.OptionMenu(
    option_var,
    currency[0],
    currency,
    command=option_changed())

def select(option):
    print(option)


ttk.Button(root, text='Rock', command=lambda: select('Rock')).pack()
ttk.Button(root, text='Paper',command=lambda: select('Paper')).pack()
ttk.Button(root, text='Scissors', command=lambda: select('Scissors')).pack()

root.mainloop()
