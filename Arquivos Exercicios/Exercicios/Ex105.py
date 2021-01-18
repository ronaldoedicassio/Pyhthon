'''
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
– Quantidade de notas
– A maior nota
– A menor nota
– A média da turma
– A situação (opcional)
'''
def notas(*valores, situação = False):
    """
    -> Função notas e para analisar notas e situação de vários alunos
    :param valores:uma ou mais notas dos alunos(aceita varias notas
    :param situação:valor opcional, indicando ou não se deve adcionar a situação
    :return:dicionário com várias informações sobre a turma
    """
    n = dict()
    n['total'] = len(valores)
    n['maior'] = max(valores)
    n['menor'] = min(valores)
    n['media'] = sum(valores)/len(valores)

    if situação:
        if n['media'] >= 7:
            n['situação'] = 'BOA'
        elif n['media'] >= 5:
            n['situação'] = 'RAZOÁVEL'
        else:
            n['situação'] = 'PESSÍMA'
    return n


resp = notas(6,6.7,3,2,10,situação=True)
print(resp)
help(notas)