"""Emtrar com um ano e dizer se ele e bissesto"""

ano = int(input('Digite ano '))

if ano % 4 == 0:
    print('{} é um ano bissexto '.format(ano))
else:
    print('{} não e um ano bissexto '.format(ano))