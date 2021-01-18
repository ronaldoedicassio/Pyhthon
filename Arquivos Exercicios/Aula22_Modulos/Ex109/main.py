from Ex109 import moeda

m = float(input('Digite um preço: R$'))
print(f'Metade do {moeda.moeda(m)} é {moeda.metade(m,True)}')
print(f'Dobro de {moeda.moeda(m)} é {moeda.dobro(m,True)}')
print(f'Desconte de 10% de {moeda.moeda(m)} é {moeda.diminuir(m, 10,True)}')