'''
 * Project: Convert the temperature in Celsius for Fahrenheit.
 * Objective: To convert temperatures in Celsius for Fahrenheit.
 * Author: José Valdeir
 * Date: 03/01/2021
'''
import tkinter as tk
import datetime


class Tela:
    def __init__(self, master):
        self.JanelaPrincipal = master
        self.JanelaPrincipal.title('Celsius For Fahrenheit')

        self.relogio = tk.Label(self.JanelaPrincipal, font='times 10', text='Krai')
        self.relogio.place(anchor=tk.SE, relx='1', rely='1')
        self.relatt()

        self.msg1 = tk.Label(self.JanelaPrincipal, text='Type the temperature in Celsius: ')
        self.msg1.pack(side=tk.TOP)

        self.cel = tk.Entry(self.JanelaPrincipal)
        self.cel.pack(side=tk.TOP)

        self.msg2 = tk.Label(self.JanelaPrincipal, text='Degrees in Fahrenheit')
        self.msg2.pack(side=tk.TOP)

        self.calc = tk.Button(self.JanelaPrincipal, text='Calculate', command=self.calcular)
        self.calc.pack(side=tk.TOP)

    def calcular(self):
        cel = int(self.cel.get())
        fah = (cel*9/5) + 32
        self.msg2['text'] = f'The temperature in Fahrenheit is:\n{fah:.3f}'

    def relatt(self):
        agora = datetime.datetime.now()
        self.relogio['text'] = agora.strftime('%H:%M:%S')
        self.JanelaPrincipal.after(1000, self.relatt)


JanelaPrincipal = tk.Tk()
Tela(JanelaPrincipal)
JanelaPrincipal.mainloop()
