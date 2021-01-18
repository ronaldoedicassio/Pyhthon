'''
Exercício Python 098: Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim
e passo. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''
from time import sleep
def contador(i,f,p):
    print('=-'*30)
    if p < 0:
        p *=-1
    if p == 0:
        p = 1

    print(f'Contando de {i} até {f}, de {p} em {p}')

    if f > i:
        while i <= f:
            print(i, end=' ')
            sleep(0.2)
            i += p
        print('FIM')
    else:
        while i >= f:
            print(i, end=' ')
            sleep(0.2)
            i -= p
        print('FIM')


contador(1,10,1)
contador(10,0,-2)
print('=-' *30)
print('Agora e sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)
