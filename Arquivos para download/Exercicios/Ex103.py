'''
Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador,
mesmo que algum dado não tenha sido informado corretamente.
'''
def ficha(nome='',gol=0):
    if nome == '':
        print(f'O jogador desconhecido fez {gol} no campeonato')
    else:
        print(f'O jogador {nome} fez {gol} no campeonato')


nome = str(input('Nome do jogador: '))
gol = str(input('Quaatidade de gols: '))

if gol.isnumeric():
    gol = int(gol)
else:
    gol = 0
ficha(nome,gol)