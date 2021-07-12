"""
 * Project: Pair Numbers.
 * Objective: Show the pair numbers in a range.
 * Author: José Valdeir
 * Date: 09/01/2021
"""
n1 = int(input('Enter a number: '))
n2 = int(input('Enter other number: '))
l = []

for n in range(n1, n2+1):
    if n % 2 == 0:
        l.append(n)

print(f'The numbers pairs in the range are:\n {l}')
