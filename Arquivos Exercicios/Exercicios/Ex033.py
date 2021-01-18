"""Ler 3 numeros e dizer qual e o menor e o maior"""


num1 = int(input('Digite primeiro numero '))
num2 = int(input('Digite primeiro numero '))
num3 = int(input('Digite primeiro numero '))

menor = num3

if num1 > num2 and num1 > num3:
    menor = num1
if num2 > num1 and num2 > num3:
    menor = num2

maior = num3
if num1 < num2 and num1 < num3:
    maior = num1
if num2 < num1 and num2 < num3:
    maior = num2

print("O menor numero digitado e: {} \nO maior número digitado é: {}".format(menor, maior))
