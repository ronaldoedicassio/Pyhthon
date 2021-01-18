'''
Exercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de
visualização de detalhes do aproveitamento de cada jogador.
'''
jogador = dict()
gols = list()
time = list()

while True:
    jogador['Nome'] = str(input('Digite o nome do jogador: '))
    partidas = int(input('Entre com numeros de partidas: '))

    for c in range(0, partidas):
        gol = int(input(f'  Informa numero de gols na partida {c}: '))
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['Total'] = sum(gols)
    gols.clear()
    time.append(jogador.copy())

    while True:
        op = str(input('Deseja continuar [S/N]')).upper()
        if op in 'SN':
            break
        print(f'Digite S para continuar e N para sair')
    if op == 'N':
        break

print('*'*40)
#imprimindo o Cabeçalho
print(f'{"Cod "}', end='')
for c in jogador:
    print(f'{c:<15}', end='')
print()
print('=' * 40)

for k, v in enumerate(time): #esse for pode e usado para lista
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()

while True:
    op = int(input('Deseja ver detalhes de qual jogador: [999 para sair]'))

    if op < len(time):
        print('='*40)
        print(f'Levantamento do jogador {time[op]["Nome"]}')

        for p in range(0,len(jogador['gols'])):
            print(f' => Na partida {p} fez {jogador["gols"][p]} gols')
        print('=' * 40)
    if op >= len(time) and op != 999:
        print(f'Digite um valor entre 0 e {len(time)-1}')
    if op == 999:
        print('Volte Sempre!!!')
        break