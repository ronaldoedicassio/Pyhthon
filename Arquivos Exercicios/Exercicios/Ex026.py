"""Faça progrma que leia uma frase e mostre:
 - Quantas letras A tem nessa frase
 - Em que posição ela aparece a primeira vez
 - Em que posição ela aparece na última vez"""

frase = str(input('Escreva uma frase: ')).upper().strip()

print('Esta frase: - {} - tem {} letras A'.format(frase,frase.count('A')))
print('A primmeira letra a da frase esta na posição : {} '.format(frase.find('A')+1))
print('A última letra a da frase esta na posição : {} '.format(frase.rfind('A')+1))
cont: int = 0
aux = 0

while cont < frase.upper().count('A'):
    aux = 1 + frase.upper().find('A', aux, len(frase))
    cont = cont+1

print('Última posição do A esta em: {}'.format(aux))


