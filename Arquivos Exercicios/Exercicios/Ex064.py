'''
Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a
soma entre eles (desconsiderando o flag).
'''

soma = 0
op = 0
count = 0
while op != 999:
    op = int(input("Digite um numero ou 999 para sair: "))
    if op != 999:
        soma +=op
        count +=1
print("QTD de numeros digitados foram {}, e a soma deles e: {}".format(count,soma))