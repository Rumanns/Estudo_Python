"""
 * Project: Finding elements on the periodic table.
 * Objective: Find elements on the periodic table.
 * Author: José Valdeir
 * Date: 10/01/2021
"""
elementos = ('zero','Hidrogênio', 'Hélio', 'Lítio', 'Berílio','Boro','Carbono','Nitrogênio','Oxigênio','Flúor','Neônio',
             'Sódio','Magnésio','Alumínio','Silício','Fósforo','Enxofre','Cloro','Argônio','Potássio','Cálcio',
             'Escândio','Titânio','Vanádio','Cromo','Manganês','Ferro','Cobalto','Níquel','Cobre','Zinco','Gálio',
             'Germânio','Arsênio','Selênio','Bromo','Criptônio','Rubídio','Estrôncio','Ítrio','Zircônio','Nióbio',
             'Molibdênio','Tecnécio','Rutênio','Ródio','Paládio','Prata','Cádmio','Índio','Estanho','Antimônio',
             'Telúrio','Iodo','Xenônio','Césio','Bário','Lantânio','Cério','Praseodímio','Neodímio','Promécio',
             'Samário','Európio','Gadolínio','Térbio','Disprósio','Hólmio','Érbio','Túlio','Itérbio','Lutécio','Háfnio',
             'Tântalo','Tungstênio','Rênio','Ósmio','Iridio','Platina','Ouro','Mercúrio','Tálio','Chumbo','Bismuto',
             'Polônio','Astato','Radônio','Frâncio','Rádio','Actínio','Tório','Protactínio','Urânio','Netúnio',
             'Plutônio','Amerício','Cúrio','Berquélio','Califórnio','Einstêinio','Férmio','Mendelévio','Nobélio',
             'Laurêncio','Rutherfórdio','Dúbnio','Seabórgio','Bóhrio','Hássio','Meitnério','Darmstácio','Roentgênio',
             'Copernício','Niônio','Fleróvio','Moscóvio','Livermório','Tenessínio','Oganessônio')

print(elementos[1:6])

print(elementos[-5:])

print(sorted(elementos))

while True:
    elemento = str(input('Enter the element which you want to find: '))
    if elemento in elementos:
        print(f'The position of element {elemento} is {elementos.index(elemento)}°')
        break
    else:
        print('Element no found. Try again.')
        print(f'{elemento}')
