"""
 * Project: Composite list and data analysis.
 * Objective: Composite list and data analysis.
 * Author: José Valdeir
 * Date: 13/01/2021
"""
geral = list()
dados = list()
maior = menor = 0
while True:
    dados.append(str(input('Enter a name: ')))
    dados.append(float(input('Enter the mass: ')))
    if len(geral) == 0:
        menor = maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    geral.append(dados[:])
    dados.clear()

    sair = input('Do you want to continue? [Y][N]').upper()
    while sair not in 'YyNn':
        sair = input('Wrong Choice. Try again.\nGet out? [Y][N]')
    if sair in 'Yy':
        ok = 1
    else:
        break
print(geral)
print(f'You have registered {len(geral)} people')
print(f'The biggest weight is {maior} Kg')
for p in geral:
    if p[1] == maior:
        print(f'The people: {p[0]} weigh {p[1]} Kg')
print(f'The smallest weight is {menor} Kg')
for p in geral:
    if p[1] == menor:
        print(f'The people: {p[0]} weigh {p[1]}')
