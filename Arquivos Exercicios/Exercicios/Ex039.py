"""
Digite o ano de nascimento

Faltam x anos para alistamento
Esse e o ano de alistamento militar
Você e maior de 18 anos e passou da idade de alistamento
"""
from datetime import datetime

ano = int(input("Digite o ano de nascimento "))
now = datetime.now()

if now.year - ano < 18:
    print("Voce tem {} anos de idade, faltam {} anos para alistamento militar".format( now.year - ano,18 + (ano - now.year)))
elif now.year - ano > 18:
        print("Você tem {} anos de idade, ja passou {} anos do alistamento".format(now.year - ano, (now.year - ano)-18))
else:
    print("Esse e o ano de alistamento militar")