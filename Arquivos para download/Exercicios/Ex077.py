'''
Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você
deve mostrar, para cada palavra, quais são as suas vogais.
'''

palavras = ('APRENDER', 'LOGO', 'LOGICO', 'PYTHON','ALGORITMO', 'COMPUTACAO')

for p in palavras:
    print(f'\nNa palavra {p} temos as vogais ', end=' ')
    for letra in p:
        if letra in 'AEIOU':
            print(letra, end=' ')
