"""Desenvola um programa que pergunte a distância de uma viagem em KM
Calcula o preço da passagem, cobrando R$ 0,50 por KM para viagens ate 200KM e R$0,45
para viagens mais longas"""

dis = int(input("Entre com distância da viagem que sera percorrida: "))

if dis < 201:
    print('Preço da passagem sera de R$ 0,50 por KM, totalizando R${:.2f} para percorrer os {} KM'.format(dis*0.5,dis))
else:
    print('Preço da passagem sera de R$0,45 por KM, totalizando R${:.2f} para percorrer os {} KM'.format(dis*0.45,dis))