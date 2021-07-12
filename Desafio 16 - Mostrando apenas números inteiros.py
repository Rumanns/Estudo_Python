'''
 * Project: Integer part
 * Objective: Show the integer part from a number.
 * Author: José Valdeir
 * Date: 06/01/2021
'''
import tkinter as tk
from math import trunc

class Tela:
    def __init__(self, master):
        self.principal = master
        self.principal.title('Integer part')

        self.frame1 = tk.Frame(self.principal)
        self.frame1.pack()

        self.msg1 = tk.Label(self.principal, text='Type a number with their broken part: ')
        self.msg1.pack(side=tk.TOP)

        self.box = tk.Entry(self.principal)
        self.box.pack(side=tk.TOP)
        self.box.bind("<Return>", self.inteira)

    def inteira(self, event):
        i = trunc(float(self.box.get()))
        self.result = tk.Label(self.principal, text=f'{i}')
        self.result.pack(side=tk.TOP)

principal = tk.Tk()
Tela(principal)
principal.mainloop()