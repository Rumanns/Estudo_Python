"""
 * Project: Triangles
 * Objective: Analise the type of triangle.
 * Author: José Valdeir
 * Date: 09/01/2021
"""

a = int(input('Enter a side of triangle measure: '))
b = int(input('Enter other side measure: '))
c = int(input('Enter the ultimate side measure '))
if a + b > c:
    if a + c > b:
        if b + c > a:
            if a == b or b == c:
                print('The triangle is isosceles')
                if a == b and b == c:
                    print('The triangle is equilateral')
            else:
                print('The triangle is scalene')
else:
    print('Is not possible to make a a triangle.')
