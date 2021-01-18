from Ex107 import moeda

m = float(input('Digite um preço: '))
print(f'Metade do {m} é {moeda.metade(m)}')
print(f'Dobro de {m} é {moeda.dobro(m)}')
print(f'Desconte de 10% de {m} é {moeda.diminuir(m, 10)}')