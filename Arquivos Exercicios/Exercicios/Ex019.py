#Um professor quer sortear um dos seus quatro alunos.
#Faça um programa que ajuda ele lendo o nome deles e escreva o escolhido

import random
nome1 = str(input("Digite nome do primeiro aluno: "))
nome2 = str(input("Digite nome do segundo aluno: "))
nome3 = str(input("Digite nome do terceiro aluno: "))
nome4 = str(input("Digite nome do quarto aluno: "))

nomes = [nome1,nome2,nome3,nome4]

print("O sortudo foi: {}".format(random.choice(nomes)))
