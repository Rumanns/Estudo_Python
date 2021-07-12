"""
 * Project: Arithmetic Progression 2
 * Objective: Arithmetic Progression 2
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num1 = int(input('Enter a starter number: '))
num2 = int(input('Enter the reason: '))
print('The first terms of this AP are:\n{}, '.format(num1), end='')
c = 0
while c < 10:
    num1 += num2
    print('{}, '.format(num1), end='')
    c += 1
