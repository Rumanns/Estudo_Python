"""
 * Project: Unique values in a list.
 * Objective: Unique values in a list.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
nome = []
idade = []
continuar = 'S'
nr = 1
while True:
    print(f'{f" Register {nr} ":=^30}')
    name = str(input('Enter a name: ')).capitalize()
    if name in nome:
        print('Name registered.Try again')
        nr -= 1
    else:
        nome.append(name)
        age = int(input('Enter a age: '))
        idade.append(idade)
    continuar = str(input('Continue? [S][N]'))
    if continuar in 'Nn':
        break
    elif continuar not in 'Ss':
        print('Wrong choice. Try again')
        nr -= 1
    else:
        nr += 1

print(f'Was registered {nr} persons.')
