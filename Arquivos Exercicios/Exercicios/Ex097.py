'''
Faça programa que tenha uma função chamada escreva() que recebe um texto qualquer e mostre uma msg com tamanho adaptivel

ex.:
esvreva 'Ola'
saída:
---
ola
---
'''
def escreva(txt):
    t = len(txt)+4
    print('~' * t)
    print(f'{txt:^{t}}')
    print('~' * t)


frase = str(input('Digite uma frase: '))
escreva(frase)
