"""
 * Project: Options menu.
 * Objective: Options menu.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num1 = int(input('Enter a value: '))
menu = int(input('Chose a option:\n'
          '[1]Sum\n'
          '[2]Multiply\n'
          '[3]Bigger\n'
          '[4]Other numbers\n'
          '[5]Get Out:\n'))
num2 = int(input('Digite outro valor: '))
while menu == 1:
    result = num1 + num2
    print('{} + {} =  {}'.format(num1, num2, result))
    while menu == 1:
        menu = 0
while menu == 2:
    result = num1 * num2
    print('The result is {}'.format(result))
    while menu == 2:
        menu = 0
while menu == 3:
    if num1 > num2:
        print('{} is bigger than {}'.format(num1, num2))
    else:
        print('{} is bigger than {}'.format(num2, num1))
    while menu == 3:
        menu = 0
while menu == 4:
    num1 = int(input('Enter a number:'))
    num2 = int(input('Enter other number:'))
    while menu == 4:
        menu = 0
while menu == 5:
    print('Thanks. Bye bye!')
    while menu == 5:
        menu = 0