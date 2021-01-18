def aumentar(n=0,taxa=0):
    preco = n + (n*taxa/100)
    return preco


def diminuir(n=0,taxa=0):
    preco = n - (n*taxa/100)
    return preco


def dobro(n=0):
    preco = n*2
    return preco


def metade(n=0):
    preco = n/2
    return preco


def moeda(preco=0, moeda ='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')