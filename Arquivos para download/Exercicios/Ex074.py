'''
Exercício Python 074: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

n = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print(n)

menor = maior = 0

'''
for c in range(0,len(n)):

    if c == 0:
        menor = n[c]
        maior = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        elif n[c] < menor:
            menor = n[c]

print(f'Menor numero {menor} e o maior {maior}')

'''

#outra maneira  para encontrar o menor e maior
print(f'O maior numero é {max(n)}')
print(f'O menor numero é {min(n)}')