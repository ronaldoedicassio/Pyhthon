"""Crie um programa que leia o nome completo de uma pessoa e mostre:

 - O nome com todos as letras maiusculas
 - O nome com todos minusculas
 - Quantas letras ao todo sem considerar os espaços
 - Quantas letras tem o primeiro nome
"""

frase = str(input("Digite teu nome completo:"))

print('Nome Completo: {}'.format(frase))
print('Nome em Letras Maiuscula: {}'.format(frase.upper()))
print('Nome em minuscula: {}'.format(frase.lower()))
print('Quantidade de letras sem espaço: {}'.format(len("".join(frase.split()))))

frase1 = frase.split()
print('Quantidade de letras do primeiro nome: {}'.format(len(frase1[0])))