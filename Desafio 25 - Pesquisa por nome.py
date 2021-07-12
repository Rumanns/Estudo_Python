"""
 * Project: Finding a word.
 * Objective: To find a word in a text.
 * Author: José Valdeir
 * Date: 07/01/2021
"""
text = input('Type a text: ')
word = input('Type a word to find: ')
text = text.lower().strip()
print(f'The word {word} is in position {text.find(word)}.')
