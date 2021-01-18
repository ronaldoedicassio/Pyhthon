"""Entre com  valores de 3 restas e verifique se a mesma consegue formar um triangulo"""

print("Analisador de triangulo")
r1 = float(input('Entre com valor da reta 1 '))
r2 = float(input('Entre com valor da reta 2 '))
r3 = float(input('Entre com valor da reta 3 '))


print("="*35)
if r1 + r2 > r3 and r1 + r3 > r2 and r2+ r3 > r1:
    print('\033[1;33;41mSim e possível formar um trianquilo\33[m')
else:
    print('\033[1;33;41mNão e possível formar um triangulo\33[m')

print("="*35)