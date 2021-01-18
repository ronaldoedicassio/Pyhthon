"""Escreve um program que leia a velocidade de um carro

se ele ultrapssar 80km/h, mostre uma mensagem dixendo que el foi multado

A multa vai custa R$7,00 por cada KM acima do limite"""

vel = float(input("Digite a velocidade atual do carro: "))

if vel > 80:
    print('Se fudeu, levou multa de R$ {}, pois excedeu em {} Km/h o limite de velocidade de 80km'.format(((vel-80)*7),vel-80))
else:
    print('Motorista prudente')