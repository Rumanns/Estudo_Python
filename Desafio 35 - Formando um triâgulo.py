"""
 * Project: Assembling a triangle.
 * Objective: Creating a triangle with measures.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
a = int(input('Type a first value: '))
b = int(input('Type a second value: '))
c = int(input('Type a third value: '))
if (a + b) > c:
    if (a + c) > b:
        if (b + c) > a:
            print('These numbers can create a triangle')
else:
    print("These number don't make a triangle. Try again.")
