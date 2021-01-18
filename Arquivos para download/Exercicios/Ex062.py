'''
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

primeiro = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite a razão dessa PA: "))
c = primeiro
armazena = 0
op = 10

while op != 0:
    count = 0
    while count < op:
        print('{}'.format(c), end=' ')
        c = c + razao
        count += 1
        print('->' if count < op else '-> AGUARDANDO', end=' ')
    op = int(input("\nQuantos termos vc quer mostrar a mais? "))
    armazena += count

print("Progressão aritimetica finalizada com {} termos mostrados".format(armazena))