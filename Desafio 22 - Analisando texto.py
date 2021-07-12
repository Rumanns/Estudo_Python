"""
 * Project: Analysing texts
 * Objective: To analyse texts.
 * Author: José Valdeir
 * Date: 07/01/2021
"""

name = str(input('Type a complete name: '))
print(f'The name in lower case is {name.lower()}\n'
      f'The name in upper case is {name.upper()}\n'
      f'The name has {len(name)} letters\n'
      f'The first name has {name.find(" ")}')
