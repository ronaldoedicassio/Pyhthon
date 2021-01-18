'''
Exercício Python 092:
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade)
em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
from datetime import date
cadastro = dict()

cadastro['Nome'] = str(input('Digite o nome: '))
cadastro['Idade'] = (date.today().year) - int(input('Digite o ano de nascimento: '))
cadastro['CTPS'] = int(input('Entre com numero da CTPS: '))
if cadastro['CTPS'] > 0:
    cadastro['AnoContratacao'] = int(input('Digite ano de contratação: '))
    cadastro['Salario'] = float(input('Digite o salário: '))
    cadastro['Aposentar'] = cadastro['Idade'] + (35-(date.today().year - cadastro['AnoContratacao']))

for k, v in cadastro.items():
    print(f'{k} tem o valor de {v}')