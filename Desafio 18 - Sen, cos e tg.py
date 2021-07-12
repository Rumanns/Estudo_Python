'''
 * Project: Sin, cos tan
 * Objective: To calculate sin, cos and tangent
 * Author: José Valdeir
 * Date: 07/01/2021
'''
import math
n = int(input("Type a number to know it's sine, cosine and tangent: "))
sin = math.sin(n)
cos = math.cos(n)
tan = math.tan(n)

print(f'The sine is {sin:.3f}\n'
      f'The cosine is {cos:.3f}\n'
      f'The tangent is {tan:.3f}')
