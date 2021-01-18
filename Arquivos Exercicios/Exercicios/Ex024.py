"""Crie um programa que leia o nome da cidade e se ele começa com Santo"""

cidade = str(input('Digite nome da cidade: ')).strip()

if cidade.find('Santo') == 0:
    print('Cidade {} começa com o nome SANTO'.format(cidade))

else:
    print('Cidade {} não começa com SANTO'.format(cidade))