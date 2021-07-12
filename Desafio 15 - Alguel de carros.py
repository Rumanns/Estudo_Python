'''
 * Project: Car Rental.
 * Objective: Calculate how much a car rental will cost.
 * Author: José Valdeir
 * Date: 05/01/2021
'''
import tkinter as tk
import datetime

class Tela:
    def __init__(self, master):
        self.Principal = master
        self.Principal.title('Car rent')

        self.relogio = tk.Label(self.Principal)
        self.relogio.place(anchor=tk.SE, relx='1', rely='1')
        self.relogioatt()

        self.frame1 = tk.Frame(self.Principal)
        self.frame1.pack(padx='10', pady='10')

        self.frame2 = tk.Frame(self.Principal)
        self.frame2.pack(padx='10', pady='10')

        self.frame3 = tk.Frame(self.Principal)
        self.frame3.pack(padx='10', pady='10')

        self.frame4 = tk.Frame(self.Principal)
        self.frame4.pack(padx='10', pady='10')

        self.msg1 = tk.Label(self.frame1, text=f'{"How many milles:":20}')
        self.msg1.pack(side=tk.LEFT)

        self.msg2 = tk.Label(self.frame2, text=f'{"How many miles:":20}')
        self.msg2.pack(side=tk.LEFT)

        self.box1 = tk.Entry(self.frame1)
        self.box1.pack(side=tk.LEFT)

        self.box2 = tk.Entry(self.frame2)
        self.box2.pack(side=tk.LEFT)

        self.total = tk.Button(self.frame3, text='Total', command=self.resp)
        self.total.pack(side=tk.LEFT)

    def resp(self):
        km = float(self.box1.get())
        days = int(self.box2.get())
        total = float(km*0.15)+(days*60)
        self.resp = tk.Label(self.frame4, text=f'The total to pay is:\n{total}')
        self.resp.pack(side=tk.LEFT)

    def relogioatt(self):
        agora = datetime.datetime.now()
        self.relogio['text'] = agora.strftime('%H:%M:%S')
        self.Principal.after(1000, self.relogioatt)


Principal = tk.Tk()
Tela(Principal)
Principal.mainloop()
