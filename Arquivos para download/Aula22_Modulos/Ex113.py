'''
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
'''


def leiaint(msg):
    valor = 0
    while True:
        try:
            num = str(input(msg))
            valor = int(num)
        except(ValueError, TypeError):
            print(f'\033[1;31mErro! Digite um número inteiro\033[m')
            continue
        except (KeyboardInterrupt,StopIteration):
            print(f'\033[1;31mErro! Usuário preferiu não informar um valor\033[m')
            return 0
        else:
            return valor


def leiafloat(msg):
    valor = 0
    while True:
        try:
            num = str(input(msg))
            valor = float(num)
        except (ValueError, TypeError):
            print(f'\033[1;31mErro! Digite) um número real\033[m')
            continue
        except (KeyboardInterrupt):
            print(f'\033[1;31mErro! Usuário preferiu não informar um valor\033[m')
            return 0
        else:
            return valor


n = leiaint('Digite um número inteiro inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'Você digitou o numero inteiro  {n}')
print(f'Você digitou o numero  real {r}')
