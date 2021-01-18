'''
Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante
‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)
'''


def leiaint(msg):
    valor = 0
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            break
        else:
            print(f'\033[1;31mErro! Digite um número inteiro\033[m')

    return valor


n = leiaint('Digite um número inteiro: ')
print(f'Você digitou o numero  {n}')




