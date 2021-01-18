'''
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o
manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.
'''
c = (
    '\033[m',        # 0 - sem cores
    '\033[0;30;41m', # 1 - vermelho
    '\033[0;30;42m', # 2 - verde
    '\033[0;30;43m', # 3 - Amarelo
    '\033[0;30;44m', # 4 - Azul
    '\033[0;30;45m', # 5 - Roxo
    '\033[0;30;46m', # 6 - Azul
    '\033[0;30;47m', # 7 - Cinza
    );


def titulo(msg,cor=0):
    tam = len(msg)+4
    print(c[cor],end='')
    print('~'*tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0],end='')


def ajuda(msg):
    titulo(f'Acessando o manual do comando \'{msg}\'', 6)
    print(c[7],end='')
    help(msg)
    print(c[0],end='')


msg = ''
while True:
    titulo('SISTEMA DE AJUDA PYTHON',2)
    msg = str(input('Digite o comando ou biblioteca: ')).lower()
    if msg == 'fim':
        titulo('ATÉ LOGO',1)
        break
    else:
        ajuda(msg)
