''''
Exercício Python 72:
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até
vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

extenso =('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:

    num = int(input("Digite um numero entre 0 e 20: "))

    if  0 <= num <= 20:
        print(f'Numero digitado foi {extenso[num]}')
        break
    else:
        print('Tente novamnte,', end=' ')


