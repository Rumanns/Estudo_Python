'''
 * Project: Date and time
 * Objective: Show the date and time from personal computer in one window.
 * Author: José Valdeir
 * Date: 07/01/2021
'''
import tkinter as tk
import datetime

class Tela:
    def __init__(self, master):
        self.Principal = master
        self.Principal.title('Watch')

        self.relogio = tk.Label(self.Principal)
        self.relogio.place(anchor=tk.CENTER, relx='0.5', rely='0.5')
        self.att()

    def att(self):
        agora = datetime.datetime.now()
        self.relogio['text'] = agora.strftime('%D\n%H:%M:%S')
        self.Principal.after(1000, self.att)


Principal = tk.Tk()
Tela(Principal)
Principal.mainloop()