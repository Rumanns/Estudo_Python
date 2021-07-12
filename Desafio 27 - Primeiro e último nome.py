"""
 * Project: First and last name.
 * Objective: Show the first and last name typed.
 * Author: José Valdeir
 * Date: 08/01/2021
"""

name = input('Type a name: ').split()
print(f'The first name is "{name[0]}" and the last name is "{name[len(name)-1]}"')
