'''
Exercício Python 099: Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''
def maior(*valores):
    maior = 0
    for c in valores:
        if c > maior:
            maior = c
    print(f'Maior número é: {maior} dos {len(valores)} informados')


count = 0
num = list()
while True:
    num.append(int(input(f'Digite o {count}° valor: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja inserir outro número: [S/N]')).upper()
        if op in 'SN':
            break
        else:
            print('Digite S para continuar e N para sair')
    if op == "N":
        break
    count += 1
print(num)
maior(num)
maior(6,8,9,10,6,7,9,90)