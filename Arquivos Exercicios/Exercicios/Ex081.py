'''

Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''

lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja inserir novo elemento:[S/N')).upper()

    if op == 'N':
        lista.sort(reverse=True)
        print(f'Quantidade de elementos digitados foram {len(lista)}')
        print(f'Lista ordenda {lista}')
        if 5 in lista:
            print('Valor 5 esta na lista')
        else:
            print('Valor 5 não foi digitado')
        break