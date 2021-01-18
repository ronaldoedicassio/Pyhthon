"""
Leia duas notas e mostre

REPROVADO - < 5.0
RECUPERAÇÂO - >5.0 < 6.9
APROVADO - > 7.0
"""
nota1 = float(input("Entre com nota 1: "))
nota2 = float(input("Entre com nota 2: "))

media = (nota1 + nota2) / 2
if media < 5:
    print("REPROVADO")
elif media < 6.9:
    print("RECUPERAÇÂO")
else:
    print("APROVADO")