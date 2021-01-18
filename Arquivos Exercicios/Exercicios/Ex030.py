"""Crie um programa que leia um numero e informe se ele e par ou impar"""

num = int(input('Digite um numero: '))

if num % 2 == 0:
    print('Numero digitado {} e um numero par'.format(num))
else:
    print('Numero digitado {} e um impar par'.format(num))