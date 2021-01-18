'''
Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos
os valores pares sorteados pela função anterior.
'''
from random import randint
num = []
def sorteia():
    for c in range(0,5):
        num.append(randint(0,99))
    print(f'Lista dos numeros sorteador foram: {num}')

def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Soma dos numeros pares foi: {soma}')



sorteia()
somapar(num)