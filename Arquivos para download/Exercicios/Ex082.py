'''
Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas
listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre
o conteúdo das três listas geradas.
'''

lista = []
listapar = []
listaimpar =[]

while True:
    lista.append(int(input('Digite um número: ')))

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continuar: [S/N]')).upper()

    if op == 'N':
        for c in lista:
            if c % 2 == 0:
                listapar.append(c)
            else:
                listaimpar.append(c)
        print(f'Lista digitada: {lista}')
        print(f'Lista de pares: {listapar}')
        print(f'Lista de impares: {listaimpar}')
        break