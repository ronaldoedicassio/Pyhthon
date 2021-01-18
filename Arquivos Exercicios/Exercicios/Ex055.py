"""
Faça progrma que leia os pesos de 5 pessoas e mostre o maior peso e o menor peso
"""

pessoas = ('primeira','segunda','terceira','quarta', 'última')

"""peso = float(input("Digite o peso da {} ".format(pessoas[0])))
menor = peso
maior = peso

for c in range(1,5):

    if peso >= maior:
        maior = peso
    elif peso <= menor:
        menor = peso

    peso = float(input("Digite o peso da {} ".format(pessoas[c])))

if peso >= maior:
    maior = peso
elif peso <= menor:
    menor = peso
"""

menor = 0
maior = 0

for c in range(1,5):
    peso = float(input("Digite o peso da {} ".format(pessoas[c])))
    if c ==1:
        menor = peso
        maior = peso
    else:
        if peso >= maior:
            maior = peso
        elif peso <= menor:
            menor = peso


print("O mais pesado {} kg e o mais leve {} kg".format(maior,menor))