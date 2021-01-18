"""
Faça programa que leia idade de 7 pessoas e mostre quantas tem > 21 anos e quantas são menores
"""

pessoas = ('primeira','segunda','terceira','quarta', 'quinta','sexta', 'última')

soma = 0
for c in range(0,7):
    i = int(input("Digite a idade da {} pessoa: ".format(pessoas[c])))
    if i >= 21:
        soma +=1

print("O número de pessoas com mais de 21 anos é {}, e o números de pessoas com idade menor de 21 é {}".format(soma, 7 - soma))