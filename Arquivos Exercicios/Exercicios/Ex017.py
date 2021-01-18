# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
# de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa

from math import pow, sqrt, hypot
n1 = float(input("Digite o valor do  cateto oposto: "))
n2 = float(input("Digite o valor do  cateto adjacente: "))

#h = sqrt(pow(n1,2)+pow(n2,2))
h = hypot(n1,n2)
print(("O valor da hipotenusa e: {:.2f}".format(h)))