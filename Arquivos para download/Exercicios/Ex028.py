"""Escreve um programa que faça computador pensar em um numero inteiro entre
0 e 5 e peça para o usuario tentar descobri qual foi o numero escolhido pelo computador

o programa devera escrever na tela se o usuário venceu ou perdeu"""

import random
from time import sleep


num_c =  random.randrange(0,5)
num_d = int(input("Adivinhe qual numero estou pensando entre 0 e 5? "))
print("\033[1;32;40mPROCESSANDO!!!\033[m")
sleep(3)
if num_c == num_d:
    print("\033[1;30;42mAcertou miseravel\033[m")
else:
    print("\033[1;30;41mErrou!!!!\033[m")