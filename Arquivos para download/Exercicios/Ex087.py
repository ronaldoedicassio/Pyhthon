'''
Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''
matrix = [[0,0,0],[0,0,0],[0,0,0]]
soma = coluna = maior = count = 0

for l in range(0,3):
    for c in range(0,3):
        matrix[l][c] = int(input(f'Digite Valor: [{l},{c}]'))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            soma += matrix[l][c]
        if c == 2:
            coluna += matrix[l][c]
        if l == 1:
            if c == 0:
                maior = matrix[l][c]
            if matrix[l][c] > maior:
                maior = matrix[l][c]
    print()
print('*--'*10)
print(f'Soma dos valores pares são {soma}')
print(f'Soma dos valores da coluna 3 é: {coluna}')
print(f'O maior valor da linha 2 é: {maior}')

