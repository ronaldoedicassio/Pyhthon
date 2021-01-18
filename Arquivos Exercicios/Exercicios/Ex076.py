'''
Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na
sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.

'''

preco = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 26, 'Estojo', 3.98, 'Transferidor', 4.53, 'Compasso', 9.99, 'Mochila', 113.5, 'Canetas', 18.6, 'Livro', 122.6)

print('-'*40)
print('{:^40}'.format('LISTAGEM DE PREÇOS'))
print('-'*40)

for n in range(0, len(preco),2):
    print('{:.<30} R${:>7.2f}'.format(preco[n],preco[n+1]))
    #print(f'{preco[n]:.<30} R${preco[n+1]:>7.2f}')
print('-'*40)