"""
Entrar com a data de nascimento, e mostre a categoria que pertence

Até 9 anos - MIRIM
Até 14 anos - INFANTIL
Até 19 anos - JUNIOR
Até 20 anos - SÊNIOR
Acima: MASTER
"""
from datetime import datetime

idade = int(input("Digite o ano de nascimento: "))

"Calculo da Idade"
now = datetime.now()
calIdade = now.year - idade

if calIdade < 9:
    print("Olá, você pertence a categoria MIRIM, pois tem {} anos de idade".format(calIdade))
elif calIdade < 14:
    print("Olá, você pertence a categoria INFANTIL, pois tem {} anos de idade".format(calIdade))
elif calIdade < 19:
    print("Olá, você pertence a categoria JUNIOR, pois tem {} anos de idade".format(calIdade))
elif calIdade < 20:
    print("Olá, você pertence a categoria SÊNIOR, pois tem {} anos de idade".format(calIdade))
else:
    print("Olá, você pertence a categoria MASTER, pois você tem {} anos de idade".format(calIdade))



