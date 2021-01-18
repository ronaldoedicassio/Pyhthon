'''
Faça programa que tenha função area(), que receba as dimensões retangular e mostre area do terreno
'''
def area(c,l):
    print('-'* 30)
    print('Calculo area do terreno')
    print('*'*30)
    print(f'Valor da area é: {c*l}m²')
    print('*'* 30)


c = float(input('Digite o comprimento do terreno: '))
l = float(input('Digite a largura do terreno: '))
area(c,l)