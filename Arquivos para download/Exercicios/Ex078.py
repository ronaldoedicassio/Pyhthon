'''
Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi
o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

lista = list()
posmaior = list()
posmenor = list()

maior = menor = 0

for n in range(0,5):
    lista.append(int(input(f'Digite numero da posição {n} ')))
    if n == 0:
        menor = lista[n]
        maior = lista[n]
    else:
        if lista[n] <= menor:
            menor = lista[n]
        if lista[n] >= maior:
            maior = lista[n]

for i, c in enumerate(lista):
    if c == maior:
        posmaior.append(i)
    if c == menor:
        posmenor.append(i)

print(f'Lista digitada: {lista}')
print(f'Maior numero da lista e {maior} e aparece na posição: ',end='')
for m in posmaior:
    print(m, end=' ')
print(f'\nMenor numero da lista e {menor} e aparece na posição: ',end='')
for m in posmenor:
    print(m, end=' ')