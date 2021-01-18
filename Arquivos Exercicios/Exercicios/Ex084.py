'''
Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas,
guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''
'''
pessoas = list()
dados = list()
leve = pesada = count = 0
levelista = []
pesadalista = []


while True:
    dados.append(str(input('Digite nome: ')))
    dados.append(str(input('Qual peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    if count == 0:
        pesada = pessoas[count][1]
        leve = pessoas[count][1]
    else:
        if pessoas[count][1] > pesada:
            pesada = pessoas[count][1]
        if pessoas[count][1] < leve:
            leve = pessoas[count][1]
    count += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N]').upper())

    if op == 'N':
        break

for c in range(0, len(pessoas)):

    if pessoas[c][1] >= pesada:
        pesadalista.append(pessoas[c][0])
    if pessoas[c][1] <= leve:
        levelista.append(pessoas[c][0])

print(f'Quantidade de pessoas cadastradas {len(pessoas)}')
print(f'As pessoas mais pesadas são {pesadalista} e pesam {pesada}')
print(f'As pessoas mais levem são {levelista} e pesam {leve}')

'''
#Outra maneira segundo gabarito

dados = []
pessoas = []
menor = maior = 0

while True:
    dados.append(str(input('Digite nome: ')))
    dados.append(str(input('Qual peso: ')))
    if len(pessoas) == 0:
        menor = dados[1]
        maior = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    res = str(input('Deseja continuar [S/N]'))

    if res in 'Nn':
        break

print(f'Quantidade de pessoas cadastradas {len(pessoas)}')
print(f'O maior peso foi {maior}Kg. Peso das pessoas: ', end=' ')
for p in pessoas:
    if p[1] == maior:
        print(p[0], end=' ')
print(f'\nO menor peso foi {menor}Kg. Peso das pessoas: ', end=' ')
for p in pessoas:
    if p[1] == menor:
        print(p[0], end=' ')