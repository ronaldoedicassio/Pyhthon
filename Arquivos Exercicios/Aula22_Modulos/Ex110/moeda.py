def aumentar(n=0,taxa=0,formato = False):
    """
    Função para aumentar o valor do preço conforme a taxa informada
    :param n: preço
    :param taxa: taxa para aumentar
    :param formato: retorno do preço no formato de dinheiro
    :return: retorno do preço no formato informado
    """
    preco = n + (n*taxa/100)
    return preco if formato is False else moeda(preco)


def diminuir(n=0,taxa=0, formato=False):
    """
    Função para realizar um desconto de acordo com a taxa informada
    :param n: preço
    :param taxa: taxa para desconto
    :param formato: retorno do preço no formato de dinheiro
    :return: retorno do preço no formato informado
    """
    preco = n - (n*taxa/100)
    return preco if formato is False else moeda(preco)


def dobro(n=0, formato=False):
    """
    Função que dobra o valor informado
    :param n: preço
    :param formato:retorno do preço no formato de dinheiro
    :return: retorno do valor no formato informado
    """
    preco = n*2
    return preco if formato is False else moeda(preco)


def metade(n=0, formato=False):
    """
    Função que calcula a metade do valor informado
    :param n: preço
    :param formato::retorno do preço no formato de dinheiro
    :return: retorno do valor no formato informado
    """
    preco = n/2
    return preco if formato is False else moeda(preco)


def moeda(preco=0, moeda ='R$'):
    """
    Função de formatação
    :param preco: preço informado
    :param moeda: tipo da moeda, por padrão esta em Reais
    :return: retorno do valor formatado
    """
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco,aum,desc):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Preço com aumento de {aum}%: \t{aumentar(preco,aum,True)}')
    print(f'Preço com desconto de {desc}%: \t{diminuir(preco,desc,True)}')
    print(f'Dobro do preço: \t{dobro(preco,True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print('-' * 30)