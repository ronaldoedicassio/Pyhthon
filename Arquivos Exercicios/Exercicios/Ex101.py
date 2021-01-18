'''
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de
nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
'''

def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        return f'Com {idade} NÃO VOTA'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} o VOTO e OPCIONAL'
    else:
        return f'Com {idade} VOTO OBRIGATÓRIO'


ano = int(input('Qual ano de nascimento: '))
voto(ano)
print(voto(ano))
