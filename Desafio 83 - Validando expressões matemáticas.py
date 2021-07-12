"""
 * Project: Validating math expressions.
 * Objective: Validates mathematical expressions by parentheses.
 * Author: José Valdeir
 * Date: 13/01/2021
"""
exp = input('Type the expression which you want to validate:\n').strip()
p1 = 0
p2 = 0

for n in range(0, len(exp)):
    if exp[n] == '(':
        p1 += 1
    elif exp[n] == ')':
        p2 += 1
if p1 == p2:
    print('The expression is correct.')
else:
    print("The expression isn't correct")
