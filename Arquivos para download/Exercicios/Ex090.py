'''
Exercício Python 090: Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

ficha = {'nome': ' ', 'media': ' '}

ficha['nome'] = str(input('Digite Nome: '))
ficha['media'] = float(input('Digite media da nota: '))
if ficha['media'] >= 7:
    ficha['situação'] = 'Aprovado'
elif 5 <= ficha['media'] < 7:
    ficha['situação'] = 'Recuperação'
else:
    ficha['situação'] = 'Reprovado'
print(f'- Situação é {ficha["situação"]}')

'''    
if ficha['situação'] >= 7:
    print(f'- \033[7;32;40m Aprovado\033[m')
elif 5 <= ficha['media'] < 7:
    print('- \033[7;33;40m Recuperação\033[m')
else:
    print('- \033[7;31;40m Reprovado \033[m')
'''
print('-'*10)
for k, v in ficha.items():
    print(f'- {k} e \033[7;32;40m{v}\033[m')