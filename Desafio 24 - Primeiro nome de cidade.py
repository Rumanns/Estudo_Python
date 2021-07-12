"""
 * Project: The first letters.
 * Objective: To verify if firs word is which the person type.
 * Author: José Valdeir
 * Date: 07/01/2021
"""
text = input('Type a text: ').lower().split()
word = input('Type a word to find: ')
print(word == text[0])
