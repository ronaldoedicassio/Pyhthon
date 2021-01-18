'''
Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
pelo usuário. O programa será interrompido quando o número solicitado for negativo.
'''

while True:
    num = int(input("Qual tabuada quer verificar? "))
    print('-' * 30)
    if num > 0:
        for c in range(1,11):
            print(f'{num} X {c} = {num*c}')
    else:
        print('\nTabuada encerrada!!!')
        break