"""
Desenvolva programa que leia primeiro termo e a razão de uma PA. No final mostre os 10 primeiros termos dessa progressão

an = a1 + (n-1)r
"""
primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão dessa PA: "))
decimo = primeiro + (10-1)*razao

for c in range(primeiro,decimo,razao):
    print('{}'.format(c), end=' -> ')

print('Fim')