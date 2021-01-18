'''
Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

lista = []

while True:
    if not lista:
        lista.append(int(input('Insira o primeiro número na lista: ')))
        print('Valor adicionado com sucesso!')
    else:
        num = int(input('Insira um número na lista: '))
        while num in lista:
            num = int(input("Digite um valor único: "))
        lista.append(num)
        print('Valor adicionado com sucesso!')

    op = ' '
    while op not in 'SN':
        op = str(input('Deseja continua? S/N').upper())

    if op == 'N':
        break

lista.sort()
print(f'Lista digitada {lista}')
