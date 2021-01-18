from Ex108 import moeda

m = float(input('Digite um preço: R$'))
print(f'Metade do {moeda.moeda(m)} é {moeda.moeda(moeda.metade(m))}')
print(f'Dobro de {moeda.moeda(m)} é {moeda.moeda(moeda.dobro(m))}')
print(f'Desconte de 10% de {moeda.moeda(m)} é {moeda.moeda(moeda.diminuir(m, 10))}')