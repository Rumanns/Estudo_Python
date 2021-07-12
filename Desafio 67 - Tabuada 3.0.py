"""
 * Project: Numeric Table 3.0
 * Objective: Numeric table 3.0
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num = int
cont = 0
while cont >= 0:
    num = int(input('Do you want to see the numeric table of which number? '))
    if num < 0:
        break
    mult = 0
    conta = 0
    for conta in range(1, 11):
        mult = num * conta
        print('{} * {} = {}'.format(num, conta, mult))
print('Thanks fo use. Good bye!')
