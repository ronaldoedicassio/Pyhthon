"""
Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
"""
import random
from time import sleep

palpites = 0
num_c =  random.randrange(0,10)
num_d = int(input("Adivinhe qual numero estou pensando entre 0 e 10? "))
print("\033[1;32;40mPROCESSANDO!!!\033[m")
sleep(1)
while num_d != num_c:
    if num_d > num_c:
        print("Numero digitado e maior que o numero escolhido pelo computador")
    else:
        print("Numero digitado e menor que o numero escolhido pelo computador")
    num_d = int(input("\033[1;30;41mErrou, Digite novamente!!!!\033[m \n -> "))
    palpites +=1

print("\033[1;30;42mFinalmente acertou miseravel em {} tentativas\033[m".format(palpites))