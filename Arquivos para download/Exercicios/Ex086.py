'''
Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''

matrix = [[],[],[]]

for l in range (0,3):
    for c in range (0,3):
        matrix[c].append(int(input(f'Digite o valor [{l},{c}]')))
print('#..'*8)
for l in range (0, 3):
    for c in range (0,3):
        print(f'[{matrix[l][c]:^5}]', end=' ')
    print()