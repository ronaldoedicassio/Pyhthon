'''
Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
 média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele
 quer ou não continuar a digitar valores.
'''

maior = menor = count = soma = 0
op = 's'

while op == 's':
    num = int(input('Digite um numero:'))
    if count == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
    count += 1
    soma += num
    op = str(input('Deseja continuar [s/n]'))

print("Você digitou {} numeros e a média foi {:.2f}".format(count,(soma/count)))
print("O maior numero digitado e {} e o menor {}".format(maior,menor))