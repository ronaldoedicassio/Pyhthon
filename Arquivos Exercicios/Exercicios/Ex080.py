'''
Exercício Python 080: Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''
lista = []

'''maior = menor = 0
for c in range(0,5):
    num = int(input('Digite um valor: '))
    if not lista:
        lista.append(num)
        print('Valor adicionado no final da lista')
        menor = maior = num
    else:
        if num > maior:
            lista.append(num)
            print('Valor adicionado no final da lista')
            maior = num
        elif num < menor:
            lista.insert(0,num)
            print('Valor adicionado na posição 0 da lista')
            menor = num
        else:
            auxmenor = menor
            auxmaior = maior
            for i in range(0,len(lista)):
                if num > auxmenor:
                    auxmenor = lista[i+1]
                else:
                    if auxmenor < auxmaior:
                        auxmenor = lista[i+1]
                    else:
                        lista.insert(i-1,num)
                        print(f'Valor inserido na posição {i-1} da lista')
'''
#outra maneira sergundo gabarito

for c in range(0,5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Valor adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if num < lista[pos]:
                lista.insert(pos,num)
                print(f'Valor adicionado na posição {pos} da lista')
                break
            pos += 1
print(f'Segue a lista ordenada de forma manual: {lista}')
