'''
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que
indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não
na tela o processo de cálculo do fatorial.
'''
def fatorial(n, show = False):
    """
    => Calculo do fatorial de um número.
    :param n: O numero a ser calculado o fotarorial
    :param show: (opcional) Mostrar ou não a conta do fatorial
    :return: O valor do fatorial de um número  n.
    """
    valor = n
    print(f'{n}! =>',end=' ')
    if show == True:
        while n > 0:
            print(f'{n}', end=' ')
            n -= 1
            if n > 0:
                print('x',end=' ')
            else:
                print('=',end=' ')

    for c in range(1,valor):
        valor *=c

    return valor


print(fatorial(10, True))
help(fatorial)