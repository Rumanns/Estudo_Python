"""
 * Project: Arithmetic progression 3.0
 * Objective: Arithmetic progression 3.0
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num1 = int(input('Enter a starter number: '))
num2 = int(input('Enter the reason: '))
cont = 0
print('The 10 first terms are: {},'.format (num1),end=' ')
termos = 0
mais = 10
while mais != 0:
    termos = termos + mais
    while cont < termos:
        cont += 1
        num1 = num1 + num2
        print('{}, '.format(num1), end='')
    print('PAUSA')
    mais = int(input('How many terms do you want to see more of? '))
print('Progression finalised with {} terms'.format(termos))
