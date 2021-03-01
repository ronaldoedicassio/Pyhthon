#f = c * 9/5

valoretanol = float (input("Entre com valor em Etanol ?"))
valorgas = float (input("Entre com valor em Gasolina ?"))

if ( valoretanol/valorgas < 0.70):
    print("Melhor opção e abastecer com gasolina")
else:
    print("Abastecer com Etanol")

#print("O Valor em fahrenheit é: {:.2f} °F".format(temperatura*(9/5) + 32))
