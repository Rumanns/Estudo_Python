"""
 * Project: Date of group.
 * Objective: Analise date of group
 * Author: José Valdeir
 * Date: 10/01/2021
"""
cont = 1
Homens = 0
Moças = 0
Outro = 0
I = 0
print(f'Participants {cont}')
while True:
    idade = int(input('Enter a age: '))
    sexo = ' '
    while sexo not in 'MFO':
        sexo = str(input('Enter the sex: [M/F/O]')).upper().strip()[0]
    if idade > 18:
        I += 1
    if sexo == 'M':
        Homens += 1
    if sexo =='F':
        if idade > 20:
            Moças += 1
    if sexo == 'O':
        Outro += 1

    cad = str(input('Other register? [S/N] ')).upper().strip()[0]
    if cad in 'Ss':
        cont += 1
        print(f'Register {cont}')
    elif cad in 'Nn':
        break
print(f'{I} People over 18 were registered.\n'
      f'{Outro} people of diverse genders were registered.\n'
      f'{Moças} under 20 were registered\n'
      f'And {Homens} men\n')
