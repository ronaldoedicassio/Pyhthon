"""
Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input("Informe o sexo [M/F]: ").upper().strip())

while sexo != 'M' and sexo != 'F':
    sexo = str(input("Dados invalidados, digite M para Masculino e F para Feminino: ").upper().strip())

print("Dados resgistrado com sucesso")