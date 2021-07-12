'''
 * Project: Hypotenuse
 * Objective: Calculate the hypotenuse
 * Author: José Valdeir
 * Date: 07/01/2021
'''
c1 = int(input('Type the opposite side: '))
c2 = int(input('Type the adjacent side: '))
hyp = (c1**2 + c2**2)**(1/2)
print(f'Your Hypotenuse is {hyp:.3f}')

#Using the library
from math import hypot
a = int(input('Digite o valor de um cateto do triângulo:'))
b = int(input('Digite o valor do outro cateto do mesmo triângulo:'))
h = hypot(a, b)
print('O valor da hipotênusa do respectivo triângulo é {:.3f}.'.format(h))