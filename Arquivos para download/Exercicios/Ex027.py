"""Faça programa que leia o nome, e mostre o primeiro e ultimo nome seprado

ex.: Ana Julia Silva

Primeiro nome: Ana
Ulimo nome: Silva"""

nome = str(input('Digite nome completo: '))
nome = nome.split()

print('Primeiro nome é: {} \nÚlimo Nome: {}'.format(nome[0], nome[len(nome)-1]))