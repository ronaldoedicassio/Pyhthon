'''
Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

listageral = []

while True:
    listageral.append(str(input('Digite nome: ')))
    listageral.append(float(input('Digite primeira nota: ')))
    listageral.append(float(input('Digite segunda nota: ')))
    op = ' '
    while op not in 'SN':
        op = str(input('Deseja deseja adicionar novo aluno? [S/N]').upper())
    if op == 'N':
        tamanholista = len(listageral)
        print('-.'*30)
        count = ordem = 0
        print(f'{"N°":<} {"Nome":<10} {"MÉDIA":>10}')
        print('.'*30)

        while count < tamanholista:
            media = (listageral[count+1]+listageral[count+2]) / 2
            print(f'{ordem:<} {listageral[count]:<10} {media:>10}')
            count += 3
            ordem += 1
        print('-' * 30)
        break

while True:
    count = int(input('Mostrar detalhes de qual aluno: (999 para sair)'))
    if count <= ordem-1:
        print(f'As notas de {listageral[count*3]} foram {listageral[count*3+1]} {listageral[count*3+2]}')
        print('-' * 30)
    else:
        if count > ordem-1 and count != 999:
            print(f'Digite um valor entre 0 e {ordem} ou 999 para sair')
        else:
            break
