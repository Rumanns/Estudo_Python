"""
 * Project: Counting units, dozens, hundreds and thousands.
 * Objective: To separate the units, dozens, hundreds and thousands.
 * Author: José Valdeir
 * Date: 07/01/2021
"""
n = int(input('Type a number: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Units: {u}.\n'
      f'Dozens: {d}.\n'
      f'hundreds: {c}.\n'
      f'thousands: {m}.')
