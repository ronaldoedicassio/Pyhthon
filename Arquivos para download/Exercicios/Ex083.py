'''
Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
'''

aberto = fechada = c = 0
exp = str(input('Digite uma expressão'))
while c < len(exp):
    if exp[0] == ')':
        print('Expressão não e valida')
        break
    elif exp[c] == '(':
        aberto +=1
    elif exp[c] == ')':
        fechada +=1
    c += 1
if c > 0:
    if fechada == aberto:
        print(f'Expressão e validada {exp}')
    else:
        print('Expressão não e valida')
