"""
Detector de palindrome
"""
frase = str(input("Digite uma frase: ").upper())

#tratando a frase
frase = frase.strip() # removendo os espaços do final e inicio da frase
frase = frase.split() # dividindo a frase
frase = ''.join(frase) # formando a nova frase sem espaço

"""

t = int(((len(frase))-1)/2)
max = int(len(frase))

somacerto = 0

for c in range(0,t):
    if frase[c] == frase[max-1]:
        somacerto = somacerto + 1
    max = max -1

if somacerto == t:
    print("Frase e um polindrome")
else:
    print("Frase normal")

"""
inverso = ''
junto = frase

'''
#Utilizando o for
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
'''
#utilizando apenas fatiamento de string
inverso = junto[::-1]

print('O inverso da frase {} e {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um polindrome')
else:
    print('Não temos um polindrome')