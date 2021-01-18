#Fazer um programa qualquer que leia um angulo e mostre o valor COS, SEN TAN

from math import sin,cos,tan,radians

n1= float(input("Entre com valor do angulo: "))

print("O SEN do angulo {}° é: {:.2f}".format(n1,sin(radians(n1))))
print("O COS do angulo {}° é: {:.2f}".format(n1,cos(radians(n1))))
print("O TAN do angulo {}° é: {:.2f}".format(n1,tan(radians(n1))))