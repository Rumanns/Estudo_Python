"""
 * Project: Treating values
 * Objective: Sum of the numbers.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num = 0
sn = 'n'
c = 0
while sn == 'n':
    numv = 0
    while numv != 999:
        numv = int(input('Enter a number: \n(If you want to get out type: 999): '))
        num += numv
        c += 1
    num = num - numv
    print('The sum total is {} and the total of number is {}'.format(num, c))
    sn = str(input('Do you want to stop the score? s/n: '))
print('Ok, thanks, by! o/')
