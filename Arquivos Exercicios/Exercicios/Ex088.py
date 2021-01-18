'''
Exercício Python 088: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.O programa vai perguntar quantos
jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''
from random import randint
from time import sleep
jogos = int(input('Digite quantidade de jogos desejada: '))
listamae = []
print('*'*20)
for c in range(1,61):
    listamae.append(c)
for c in range(0,jogos):
    listajogo = listamae[:]
    jogo = [0,0,0,0,0,0]
    aux = 0
    fim = 60
    for j in range(0,6):
        aux = randint(1,fim)
        jogo[j] = aux
        del listajogo[aux-1]
        fim -= 1
    jogo.sort()
    print(f'Jogo {c+1}: {jogo}', end=' ')
    sleep(1)
    print()
