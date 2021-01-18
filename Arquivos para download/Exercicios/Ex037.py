"""
Escreve um programa que leia um numero inteiro.
Escolher qual vase de conversão:

1 - para binario
2 - para octal
3 - para hexa
"""

num = int(input("Digite um numero inteiro: "))

print("*"*30)
item = int(input("Escolha a base de conversão: "
                 "\n 1 - Binario"
                 "\n 2 - Octal"
                 "\n 3 - Hexadecimal"
                 "\n Opção: "))

if item == 1:
    print("*" * len("Numero {} convertido para Binario e: {}"))
    print("Numero {} convertido para Binario e: {}".format(num,bin(num)[2:]))
    print("*" * len("Numero {} convertido para Binario e: {}"))
elif item == 2:
    print("*" * len("Numero {} convertido para OCtal e: {}"))
    print("Numero {} convertido para OCtal e: {}".format(num,oct(num)[2:]))
    print("*" * len("Numero {} convertido para OCtal e: {}"))
elif item == 3:
    print("*" * len("Numero {} convertido para hexadecimal e: {}"))
    print("Numero {} convertido para hexadecimal e: {}".format(num,hex(num)[2:]))
    print("*" * len("Numero {} convertido para hexadecimal e: {}"))
else:
    print("Opão invalida!!!")