"""
Leia seis números inteiros e mostre apenas a soma dos numeros pares
"""

posição = ('primeiro','segundo','terceiro','quarto','quinto', 'sexto')
soma = 0
for c in range(0,6):
    n = int(input("Digite um {} numero: ".format(posição[c])))
    if n % 2 == 0:
        soma += n

print("Soma de todos os numeros pares digitados foi de {}".format(soma))