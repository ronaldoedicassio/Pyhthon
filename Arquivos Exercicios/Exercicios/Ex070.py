'''
Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o
usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato.
'''

qtdprodutos = count = total = produtocaro = countprodutocaro = menor =0
nomeprodutocaro = ' '
nomeprodutobarato = ' '
op = 's'
while True:
    produto = str(input("Digite o nome do produto: "))
    preco = float(input("Digite o preço do produto: R$"))
    total += preco
    count += 1

    if preco > 1000:
        countprodutocaro += 1
    if preco < produtocaro:
        nomeprodutocaro = produto
        produtocaro = preco
    if count == 1 or preco < menor:
        menor = preco
        nomeprodutobarato = produto

    op = ' '
    while op not in 'SN':
        op = str(input("Deseja continuar a comprar? [S/N]")).upper().strip()[0]

    if op not in 'S':
        break

print('{:-^40}'.format('Fim da compra'))
print(f'O Valor gasto na compra foi: R$ {total :.2f}')
print(f'Quantidade de produto que custam mais que R$1000,00 é: {countprodutocaro}')
print(f'Produto mais caro foi {nomeprodutocaro} e o preço foi R${produtocaro :.2f}')
print(f'O produto mais barato foi {nomeprodutobarato} e o preço dele R${menor :.2f}')