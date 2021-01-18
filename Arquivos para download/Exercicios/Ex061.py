'''
Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
 termos da progressão usando a estrutura while.

 an = a1 + (n-1)r

'''

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão dessa PA: "))
decimo = primeiro + (10-1)*razao
c = primeiro
while c < decimo:
    print('{}'.format(c), end=' ')
    c = c + razao
    print('->' if c < (decimo) else '-> Fim', end=' ')
