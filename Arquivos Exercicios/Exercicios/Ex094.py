'''
Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

cadastro = list()
pessoas = dict()
somaidade = 0
while True:
    sexo = op = ' '
    pessoas['nome'] = str(input('Digite o nome da pessoa: '))

    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F]')).upper()
        if sexo not in 'MF':
            print('Digite M para masculino e F para feminino')
    pessoas['sexo'] = sexo
    idade = int(input('forneça idade: '))
    pessoas['idade'] = idade
    somaidade += idade
    cadastro.append(pessoas.copy())

    while op not in 'SN':
        op = str(input('Deseja continua? [S/N]')).upper()
        if op not in 'SN':
            print('Digite S para continuar ou N para sair')

    if op == 'N':
        break
print(cadastro)
media = somaidade/len(cadastro)
print(f'A) Quantidade de pessoas cadastradas foram : {len(cadastro)}')
print(f'B) Media de idade das pessoas foram: {media:.1f} anos')
print(f'C) Lista das mulheres:')
for v in cadastro:
    if v['sexo'] == 'F':
        print(f'{v["nome"]:^5}')
print(f'D) As pessoas acima media de idade: ')

for p in cadastro:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'{k} = {v}',end=' ')
    print()
print('ENCERRADO')