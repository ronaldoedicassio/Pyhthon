'''
Exercício Python 075: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.

'''

num = (int(input('Digite primeiro numero ')),
       int(input('Digite Segundo numero ')),
       int(input('Digite terceiro numero ')),
       int(input('Digite quarto numero ')))

print(f'Valores digitados foram {num}')
print(f'Q quantidade de 9 que apareceu foi {num.count(9)}')
if 3 in num:
    print(f'O primeiro número 3 apareceu na {num.index(3)+1}º posição')
else:
    print('Não foi digitado o numero 3')
print(f'Os valores pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(f'{n}', end=' ')
