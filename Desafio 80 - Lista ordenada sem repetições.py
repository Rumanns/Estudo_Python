"""
 * Project: Ordered list without repetition
 * Objective: Organize five values.
 * Author: José Valdeir
 * Date: 11/01/2021
"""
print("I'll organize five entries, for you!")
lis = []
for c in range(0, 5):
    n = input(f'Enter a number: ')
    if c == 0 or n > lis[-1]:
        lis.append(n)
    else:
        pos = 0
        while pos < len(lis):
            if n <= lis[pos]:
                lis.insert(pos, n)
                break
            pos += 1
print(lis)
