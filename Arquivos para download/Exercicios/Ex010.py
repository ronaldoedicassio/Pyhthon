#Crie programa que leia quantidade de dinheiro que a pessoa tem na carteria e converta para dolar, considere cotação do dolar 5,70

n = float(input("Quanto de dinheiro vc tem na tua carteira?"))
print('Dinheiro que vc tem {} convertido em moeda americana, baseado na cotação de R$5.70, corresponde em $ {:.2f}'.format(n,n/5.7))