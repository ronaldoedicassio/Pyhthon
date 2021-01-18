"""
Escreve um programa para aprovar o empréstimo bancário para a compara de
uma casa. O programa vai perguntar:
 - valor da casa
 - Salario
 - Quantos anos ele vai pagar

 Calcule o valor da prestação mensal, sabendo que nao pode ultrapassar
 30% do salario
 desconsidere os juros de financiamento, somente considere o valor da casa para exercicio
"""

from datetime import datetime
now = datetime.now()

if now.hour < 12:
    print("Bom dia")
elif now.hour < 18 and now.hour > 12:
    print("Boa tarde")
else:
    print("boa noite")

valor = float(input("Entre com Valor da casa: "))
salario = float(input("Digite o valor do salario liquido: "))
tempo = float(input("Quantos anos pretende pagar o imovel? "))

prestação = valor/(tempo*12)

if prestação > salario*0.3:
    print("Financiamento não aprovado, pois a prestão de R${:.2f} e maior que 30% do salario {:.2f}".format(prestação, salario))
else:
    print("Financiamento aprovado!!! \nPrestações de R$ {:.2f} serão cobradas no proxímo mês".format(prestação))