

def leiadinheiro(msg):
    """
    Função para validar a entrada
    :param msg: mensagem de texto para informar o preço
    :return: retorna o valor preço no convertido para float
    """
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada =='':
            print(f'\033[0;31m ERRO! O valor {entrada} não é um preço Invalido\033[m')
        else:
            valido = True
            return float(entrada)
