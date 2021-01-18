"""
Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo:
5! = 5 x 4 x 3 x 2 x 1 = 120
"""
from math import factorial
num = int(input('Entre com o número: '))
n = num
produto = 1
print("Fatorial de {}! -> ".format(num), end='')
while n > 1:
    produto = produto * n
    n -= 1
    print('{}'.format(n), end= '')
    print(' x ' if n > 1 else ' = ', end='')

print(produto)

#usando metodo pronta
print("Valor pela metodo pronto {}".format(factorial(num)))