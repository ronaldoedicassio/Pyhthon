# Criar programa que leia um numero real qualquer pelo teclado
# e mostre na tela a sua porção inteira.
# Ex.: Digite um numero:6.126
# O numero 6.126 tem a parte inteira 6.

from math import floor

n1 = float(input("Digite um numero: "))
print("O numero {} tem a parte inteira {}".format(n1,floor(n1)))
