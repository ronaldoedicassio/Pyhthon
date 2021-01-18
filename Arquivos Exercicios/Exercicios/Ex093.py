'''
Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = dict()
gols = list()

jogador['Nome'] = str(input('Digite o nome do jogador: '))
partidas = int(input('Entre com numeros de partidas: '))

for c in range(0, partidas):
    gol = int(input(f'Informa numero de gols na partida {c}: '))
    gols.append(gol)
jogador['gols'] = gols
jogador['Total'] = sum(gols)

print('-='*30)
print(jogador)
print('-='*30)
for k,v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)

for c in range(0, len(jogador['gols'])):
    print(f'=> Na partida {c} , fez {jogador["gols"][c]} gols')

print(f'Total de {(jogador["Total"])} gols em todas as partidas')