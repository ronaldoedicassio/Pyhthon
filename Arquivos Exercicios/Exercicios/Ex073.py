'''
Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Corinthians.
'''

pos = ('São Paulo','Atlético-MG','Flamengo','Grêmio','Fluminense','Internacional','Palmeiras','Santos','Ceará','Fortaleza','Corinthians',
       'Athletico PR','Bahia','Red Bull Bragantino','Atlético-GO','Sport','Vasco','Coritiba','Botafogo','Goiás')

print('-='*15)
print(f'Os primeiros 5 colocados são: {pos[:5]}')
print('-='*15)
print(f'Os quatros últimos são: {pos[-4:]}')
print('-='*15)
print(f'Ordem alfabetica dos times {sorted(pos)}')
print('-='*15)
print(f'O corinthians esta na {pos.index("Corinthians")+1} posição')
print('-='*15)