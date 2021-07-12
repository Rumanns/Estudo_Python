"""
 * Project: Larger and smaller values 2
 * Objective: Larger and smaller values 2
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num = 0
total = 0
maior = 0
menor = 0
media = 0
cont = 0
continua = 's'
while continua in 'SsNn':
    if continua in 'Ss':
        cont += 1
        num = int(input('Enter a number: '))
        total += num
        if num > maior:
            maior = num
        if cont == 1:
            menor = num
        if num < menor:
            menor = num
        continua = str(input('Do you want to continue? [s/n] '))
    elif continua in 'Nn':
        print('{}'.format(total))
        media = total / cont
        print('The average between the values is {:3}.\n'
              'The bigger value typed is: {}\n'
              'And the smaller value is: {}'.format(media, maior, menor))
        continua = ' '
        break
