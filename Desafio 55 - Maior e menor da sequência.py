"""
 * Project: Larger and Smaller of the sequence.
 * Objective: Check the larger and smaller of a sequence.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
total = int(input('How many persons will be analyzed: '))
maior = 0
menor = 0
for c in range(1, total+1):
    peso = float(input(f'Enter the mass of person {c}: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'The larger mass is {maior} and the smaller mass is {menor}')
