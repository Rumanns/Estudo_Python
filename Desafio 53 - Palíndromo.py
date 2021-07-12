"""
 * Project: Palindrome
 * Objective: Palindrome checker
 * Author: José Valdeir
 * Date: 10/01/2021
"""
frase = str(input('Enter a phrase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('The phrase is a palindrome')
else:
    print('The phrase is not a palindrome')
