#Faça um progrma que leia um numero e mostre a tabela de sua tabuada

n = int(input("Digitar um numero "))

print("A tabela do número {} é".format(n))

print("-"*15)
for i in range(1,11):
    print('{} x {:2} = {}'.format(n,i,n*i))

print("-"*15)