"""
 * Project: Largest and smaller value on list.
 * Objective: Largest and smaller value on list.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num = []
for cont in range(0, 5):
    num.append(int(input('Enter a number to be added: ')))
print('-='*25)

print(f'The biggest number is: {max(num)} on position {num.index(max(num))+1}°'
      f'\nThe smaller number is: {min(num)} on position {num.index(min(num))+1}°')
print('-='*25)