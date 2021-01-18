#Faça programa leia altura e largura de uma parede em metros e mostre a quantidade de tinta necessária para pinta-la,
#sabendo que cada litro de tinta pinta 2m².

h = float(input("Entre com Altura da parede"))
l = float(input("Entre com Largura da parede"))

a = h*l
print('Quantida de tinta para pintar a parede de {} m²  é: {} litros'.format(a,a/2))
