'''
Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos.
'''

maior = qtdh = qtdm = countidade =0
while True:
    print('-'*30)
    idade = int(input('Qual idade: '))
    sexo = str(input('Sexo M/F: ')).upper().strip()[0]
    if idade > 18:
        maior += 1
    if sexo == 'M':
        qtdh += 1
    if sexo == 'F' and idade < 20:
        qtdm += 1
    op = str(input('Quer continua S/N')).upper()
    if op == 'N':
        break

print(f'QDE  de pessoas maior de 18 anos {maior}')
print(f'QDE de homens cadastrados {qtdh}')
print(f'QTD de  mulheres tem menos de 20 anos {qtdm}')