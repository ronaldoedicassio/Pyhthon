"""
Faça programa que calcule a soma entre todos os numeros impares que são multiplos de 3 e que se encontram no intervalo de 1 ate 500
"""
soma = 0
for c in range(1,501,2):
    if c % 3 == 0:
        soma += c

print("Valor da Soma: {} ".format(soma))