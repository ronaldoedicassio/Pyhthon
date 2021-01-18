from Ex115.Lib import arquivo
from Ex115.Lib import registro
from time import sleep

arq = 'cursoemvideo.txt'

if not registro.arquivoexiste(arq):
    registro.criararquivo(arq)

while True:
    resposta = arquivo.menu(['Ver pessoas cadastradas ', 'Cadastrar no Pessoas', 'Sair'])
    if resposta == 1:
        registro.lerarquivo(arq)
    elif resposta == 2:
        arquivo.cabeçalho('NOVO CADASTRO')
        nome = str(input('Forneça o nome: '))
        idade = arquivo.leiaint('Idade: ')
        registro.gravardados(nome,idade,arq)
    elif resposta == 3:
        arquivo.cabeçalho('Saindo do Sistema... Até Logo')
        break
    else:
        print('\033[31mOpção Invalida!\033[m')
    sleep(2)

