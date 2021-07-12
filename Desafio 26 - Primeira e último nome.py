"""
 * Project: How many times appears the letter.
 * Objective: Count letters.
 * Author: José Valdeir
 * Date: 08/01/2021
"""
text = input('Type the text: ').lower()
let = input('Type the letter which you want to count: ')

print(f'The letter "{let}" shows {text.count(let)} times\n'
      f'The first time is in the position {text.find(let)+1}\n'
      f'The ultimate time is in the position {text.rfind(let)}\n'
      f'And the text have {len(text)} letters')
