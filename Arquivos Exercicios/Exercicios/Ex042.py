"""
Refazer o exercicio 35 e acrescentar o tipo de triangulo que forma

EQUILATERO
ISÓSCELES
ESCALENO
"""

print("Analisador de triangulo")
r1 = float(input('Entre com valor da reta 1 '))
r2 = float(input('Entre com valor da reta 2 '))
r3 = float(input('Entre com valor da reta 3 '))


print("="*40)
if r1 + r2 > r3 and r1 + r3 > r2 and r2+ r3 > r1:
    print('\033[1;33;41mSim e possível formar um trianquilo\33[m')

    if r1 == r2 == r3:
        print("\nEsse triangulo e \033[7mEQUILATERO\33[m - todos os lados são iguais\n")
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print("\nEsse triangulo e \033[7mISÓSCELES\33[m - dois lados são iguais\n")
    else:
        print("\nEesse triangulo e \033[7mESCALENO\33[m - Todos os lados são diferentes")


else:
    print('\033[1;33;41mNão e possível formar um triangulo\33[m')

print("="*40)