"""
Elabore um programa que leia o preço do produto e calcule o valor final considerando o condição de pagamento

- a vista no dinheiro - 10% de desconto
- a vista no cartão - 5% de desconto
- em ate 2X no cartão - preço normal
- em 3X ou mais 20% de juros
"""
print("{:=^40}".format(" Lojas Siqueira "))
preco = float(input("Entre com valor do produto: "))
cond = int(input("\033[1;30;43m Condição de pagamento:  \033[m"
                 "\n\033[7m 1 - A vista no dinheiro \033[m"
                 "\n\033[7m 2 - A vista no Cartão   \033[m"
                 "\n\033[7m 3 - Parcelar no cartão  \033[m"
                  "\n\033[7m OP ==> \033[m"))

if cond == 1:
    print("Preço a ser pago pelo produto com desconto será de R${:.2f} reais, você tera um desconto de R${:.2f}".format((preco*0.9),(preco*0.10)))
elif cond == 2:
    print("Preço a ser pago pelo produto com desconto sera de R${:.2f} reais, você tera um desconte de R${:.2f}".format(preco*0.95,preco*0.05))
elif cond == 3:
    cond1 = int(input("\n\033[1;31;40Digite o número de parcelas\033[m "))
    if cond1 == 2:
        print("Preço do produto em 2 parcelas sera R${:.2f} reais, o preço de cada parcela será R${:.2f} reais".format(preco, preco/2))
    else:
        print("Preco do produto em {} parcelas sera de R${:.2f} reais, o preço de cada parcela será R${:.2f} reais".format(cond1,preco*1.2,(preco*1.2)/cond1))
else:
    print("\033[1;31m OPÇÃO INVÁLIDA \033[m")