"""Faça um programa que leia um numero de 0 a 9999 e mostre na tela cada
um dos digitos separados

Ex.:
Digite um número: 1834

unidade: 4
Dezenas: 3
Centenas: 8
Milhar: 1

"""
num1 = int(input('Digite um numero menor que 9999: '))

print('Milhar: {}'.format(num1 // 1000))
print('Centena: {}'.format((num1 // 100) - (num1 // 1000)*10))
print('Dezenas: {}'.format((num1 // 10) - (num1 // 100)*10))
print("Unidade: {}".format((num1 // 1) - (num1 // 10)*10))
