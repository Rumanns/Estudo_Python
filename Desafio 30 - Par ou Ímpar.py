"""
 * Project: Pair or Odd.
 * Objective: To analyse if a number is pair or odd.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
import math

num = int(input('Type a number:'))


if num % 2 == 0:
    print(f'The number {num} is pair.')
else:
    print(f'The number {num} is odd.')
