"""Crie um programa que leia o nome da pessoa e verifique se tem SILVA nesse nome"""

nome = str(input('Digite teu nome: '))

if 'SILVA' in nome.upper() :
    print('O nome {} tem a palavra SILVA'.format(nome))
else:
    print('O nome {} não tem a palavra SILVA'.format(nome))