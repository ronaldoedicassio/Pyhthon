# o mesmo professor do desafio anterio quer sortear a ordem de
# apresentação dos trabalho dos alunos, faça um programa que leia o
# nome dos alunos e mostre a ordem sorteada

import random
nome1 = str(input("Digite nome do primeiro aluno: "))
nome2 = str(input("Digite nome do segundo aluno: "))
nome3 = str(input("Digite nome do terceiro aluno: "))
nome4 = str(input("Digite nome do quarto aluno: "))

nomes = [nome1,nome2,nome3,nome4]
random.shuffle(nomes)

print("Segue a lista de apresentação: \n"
      "Primeiro: {} \nSegundo: {} "
      "\nTerceiro: {} \nQuarto: {}"
      .format(nomes[0],nomes[1],nomes[2],nomes[3]))