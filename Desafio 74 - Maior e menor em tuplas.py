"""
 * Project: Larger and Smaller on tuplas.
 * Objective: Larger ans smaller on tuplas
 * Author: José Valdeir
 * Date: 10/01/2021
"""
from random import randint
numal = (randint(0,60), randint(0,60),randint(0,60),randint(0,60),randint(0,60))
print(f'The values randed are {len(numal)}:')
for n in numal:
    print(f'{n} ', end='')
print(f'The smaller is {[min(numal)]} and bigger is {[max(numal)]}')
