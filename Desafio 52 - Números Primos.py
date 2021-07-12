"""
 * Project: Prime numbers.
 * Objective: Check if a number is prime.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
total = 0
num = int(input('Enter a number: '))
for c in range (1, num + 1):
    if num % c == 0:
        print('\033[33m', end= ' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end= ' ')
print(f'\n\033[mThe number {num} was divided {total} times')
if total == 2:
    print("This is why it's prime!")
else:
    print("This is why it's not prime!")