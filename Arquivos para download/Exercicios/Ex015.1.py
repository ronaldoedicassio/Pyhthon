#Calcular valor do aluguel do carro, informando o numero de dias alugado e KM rodado, sabendo que a diaria e de R$ 60,00 e R$0,15 km
d = int(input("Informe número de dias alugado?"))
k = float(input("Informe km rodados"))

print('O valor total do aluguel do carro é:{:.2f}'.format(d*60+k*0.15))