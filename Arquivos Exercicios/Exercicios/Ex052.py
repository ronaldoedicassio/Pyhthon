"""
Faça programa que calcule se um número e primo
"""

n = int(input("Digite um número: "))
soma = 0

for c in range (1,n+1):
    if n % c == 0:
        soma = soma + 1
if soma > 2:
    print("Numero não é primo")

if soma == 2:
    print("Numero primo")