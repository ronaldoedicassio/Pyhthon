'''
Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário
qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''
print('{:=^40}'.format(''))
print("{:^40}".format("Bem Vindo ao meu banco"))
print('{:=^40}'.format(''))

dinheiro = int(input("Digite o valor a ser sacado: R$"))

'''count50 = count20 = count10 = count1 = 0

while dinheiro > 0:
    if dinheiro % 50 == 0:
        count50 +=1
        dinheiro -=50
    elif dinheiro % 20 == 0:
        count20 +=1
        dinheiro -=20
    elif dinheiro % 10 ==0:
        count10 +=1
        dinheiro -=10
    elif dinheiro % 1 == 0:
        count1 +=1
        dinheiro -=1

print('{:*^40}'.format('Numero de Cedulas'))
if count50 > 0:
    print("Total de cedula de 50 são: {}".format(count50))
if count20 > 0:
    print("Total de cedula de 20 são: {}".format(count20))
if count10 > 0:
    print("Total de cedula de 10 são: {}".format(count10))
if count1 > 0:
    print("Total de cedula de 1 são: {}".format(count1))
'''

#outra maneira de fazer baseado na logica da resolução
ced = 50
count = 0

print('{:*^40}'.format('\n'))
while True:
    if dinheiro >= ced:
        dinheiro -= ced
        count += 1
    else:
        if count > 0:
            print(f'Total de {count} cedulas de {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        count = 0

        if dinheiro == 0:
            break

print('{:*^40}'.format(''))