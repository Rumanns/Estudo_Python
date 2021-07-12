"""
 * Project: Analysing Products Prices
 * Objective: Analysing Products Prices
 * Author: José Valdeir
 * Date: 10/01/2021
"""
qtdpd = caro = barato = itemcaro = itembarato = total = 0
cont = 1
while True:
    continuar = ' '
    produto = str(input('Product : '))
    preço = int(input('Price: '))
    if cont == 1:
        caro = preço
        barato = preço
        itemcaro = produto
        itembarato = produto
        cont += 1
    if preço > caro:
        caro = preço
        itemcaro = produto
    if preço < barato:
        barato = preço
        itembarato = produto
    total += preço

    while continuar not in 'SN':
        print('-'*30)
        continuar = str(input('Continue? [S/N] ')).upper().strip()[0]
    if continuar == 'S':
            qtdpd += 1
    else:
        break
print('-'*50)
print(f'The most expensive product was {itemcaro} for {caro}R$\n'
      f'The cheapest product was {itembarato} for {barato}R$\n'
      f'And there were {qtdpd} products for {total}')
