"""
Calcular IMC - ler altura e peso

abaixo de 18.5: Abaixo do peso
Entre 18.5 e 25: Peso ideal
25 até 30: Sobrepeso
30 até 40: Obesidade
acime de 40: Obesidade mórdida
"""
peso = float(input("Entre com o peso em KG: "))
altura = float(input("Entre com altura em metros: "))

IMC = peso/(altura*altura)

if IMC < 18.5:
    print("Você esta \033[7mabaixo do peso\033[m, seu IMC e de {:.2f}".format(IMC))
elif IMC < 25:
    print("Você esta no peso ideal, seu IMC e de {:.2f}".format(IMC))
elif IMC < 30:
    print("Você esta no \033[7mSobrepeso\033[m, seu IMC e de {:.2f}".format(IMC))
elif IMC < 40:
    print("Você esta no \033[7mObesidade\033[m, seu IMC e de {:.2f}".format(IMC))
else:
    print("Você esta no \033[7mObesidade mórdida\033[m, seu IMC e de {:.2f}".format(IMC))