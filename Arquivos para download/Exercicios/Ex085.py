'''
Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma
lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

lista = [[],[]]
coutp = counti = 0
for c in range(0, 7):
    num = int(input("Entre com número:"))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(lista)
print(f'Lista de pares {sorted(lista[0])}')
print(f'Lista de imparer {sorted(lista[1])}')