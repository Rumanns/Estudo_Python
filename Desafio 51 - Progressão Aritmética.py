"""
 * Project: Arithmetic progression.
 * Objective: Arithmetic progression.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
num = int(input('Enter the first of your A.P.: '))
raz = int(input('Enter the function of your A.P.: '))
for c in range(-1, 9):
    num = raz + num
    print(num, end=' → ')
