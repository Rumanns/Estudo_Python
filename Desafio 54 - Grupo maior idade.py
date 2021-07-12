"""
 * Project: Older group
 * Objective: Check older group
 * Author: José Valdeir
 * Date: 10/01/2021
"""
from datetime import date
atual = date.today().year
menor = 0
maior = 0
cont = 0
ano = int(input('Enter how many persons will be analyzed: '))
for c in range(0, ano):
    cont += 1
    ano = int(input(f"Enter person's year of birth {cont}°: "))
    if ano < atual-18:
        maior += 1
    else:
        menor += 1
print(f'Altogether there are {menor} minors and {maior} adults')
