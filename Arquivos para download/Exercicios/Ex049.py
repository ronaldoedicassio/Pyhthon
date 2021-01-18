"""
Fazer uma tabuada de um numero a partir da entrada pelo usuario
"""

print("{:=^40}".format("Olá, bem vindo."))
n = int(input("Digite um número inteiro: "))

print('{:x^20} Tabuada de {} {:x^20}'.format('',n,''))
for c in range(1,11):
    print('x {:^18} {}  x  {:2}  =  {:>3} {:>16}'.format('',n,c,c*n,'x'))

print('{:x^20}{:x^14}{:x^20}'.format('','',''))