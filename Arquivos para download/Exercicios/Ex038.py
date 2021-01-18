"""
Escreve programa que compare dois numeros inteiros e mostre as msg:

o primeiro numero e maior que o segundo
o segundo numero e maior que o primeiro
nao existe valor maior, os numeros são iguais
"""

num1 = int(input("Digite primeiro numero inteiro "))
num2 = int(input("Digite o segundo numero inteiro "))

if num1 > num2:
    print("O primeiro numero {} e maior que o segundo numero {}".format(num1,num2))
elif num2 > num1:
    print("O segundo numero {} e maior que o primeiro numero {}".format(num2,num1))
else:
    print("Não existe valor maior, os numeros {} e {} são iguais".format(num1,num2))