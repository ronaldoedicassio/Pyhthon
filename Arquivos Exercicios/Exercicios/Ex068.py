'''
Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

import random

count = 0
while True:
    c = random.randint(0,9)
    print('~' * 30)
    num = int(input("Digite um valor: "))
    esc = str(input('P/I ?').upper().strip()[0])
    print('~' * 30)
    soma = c + num

    if esc == 'P':
        if soma % 2 == 0:
            count +=1
            print(f'Computador jogou {c} e você jogou {num}. Total deu {num + c} - PAR ')
        else:
            print('Você Perdeu')
            break
    elif esc == 'I':
        if soma % 2 == 0:
            print('Você Perdeu')
            break
        else:
            count +=1
            print(f'Computador jogou {c} e você jogou {num}. Total deu {num + c} - IMPAR ')
    print('Vamos jogar novamente')
print('-'*30)
print(f'GAME OVER, você venceu {count} vezes')
print('-'*30)