"""
 * Project: Extracting date from a list.
 * Objective: Extract date from a list.
 * Author: José Valdeir
 * Date: 12/01/2021
"""
print("I'll find some information which you want.")
continua = 'S'
lista = []
while continua == 'S':
    n = int(input('Enter a value: '))
    lista.append(n)
    continua = str(input('Continue? [S][N]')).upper()
    while continua not in 'SsNn':
        print('Invalid Option. Try again.')
        continua = str(input('Continue? [S][N]')).upper()
    else:
        if continua in 'Nn':
            break
busca = int(input('Which number do you know how many types were tiped? '))
tbusca = 0
for c in range(0, len(lista)):
    if busca == int(lista[c]):
        tbusca += 1

lista.sort()
print(f'The number {busca} appears {tbusca} times\n'
      f'The list have {len(lista)} components\n'
      f'And they are: {lista}')
