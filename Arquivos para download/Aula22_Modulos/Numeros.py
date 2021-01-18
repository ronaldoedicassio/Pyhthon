from uteis import numeros
#programa principal
num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'O fataorial de {num} e {fat}')
print(f'Dobro do {num} e {numeros.dobro(num)}')