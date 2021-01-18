"""
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
"""
from time import sleep

op = 0

num1 = int(input("Entre com o primeiro valor: "))
num2 = int(input("Entre com o segundi valor: "))

while op != 5:
    op = int(input('''Escolha uma opção:
                    [ 1 ] somar
                    [ 2 ] multiplicar                    
                    [ 3 ] maior                    
                    [ 4 ] novos números                    
                    [ 5 ] sair do programa
                    
                    Opção => '''))
    if op > 5:
        print("\n \033[1;30;41mOpção invalida!!!\033[m\n")
        sleep(1)

    if op == 1:
        print("\n \033[1;30;42m Soma -> {} + {} = {}{}\n".format(num1,num2,num1+num2,"\033[m"))
        sleep(1)

    if op == 2:
        print("\n \033[1;30;42m Multiplicação -> {} x {} = {}{}\n".format(num1, num2, num1 * num2, "\033[m"))
        sleep(1)

    if op == 3:
        if num1 > num2:
            print("\n \033[1;30;42m O primeiro Numero {} e maior que o segundo número {}{}\n".format(num1, num2, "\033[m"))
            sleep(1)
        else:
            print("\n \033[1;30;42m O Segundo Numero {} e maior que o primeiro número {}{}\n".format(num2, num1, "\033[m"))
            sleep(1)

    if op ==4:
        num1 = int(input("Entre com o primeiro valor: "))
        num2 = int(input("Entre com o segundi valor: "))

print("FIM!")