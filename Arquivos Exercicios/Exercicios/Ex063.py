'''
Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
de uma Sequência de Fibonacci. Exemplo:

0 – 1 – 1 – 2 – 3 – 5 – 8
'''

n = int(input("Quantos numeros vc quer mostrar "))
soma = 0
primeiro = 0
segundo = 1

print('{}'.format('0 - 1'), end='')

while n > 2:
    print(' - ' if n > 0 else '', end='')
    soma = primeiro + segundo
    print('{}'.format(soma),end='')
    primeiro = segundo
    segundo = soma
    n -= 1
print(' - FIM')