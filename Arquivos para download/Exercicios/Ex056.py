"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do
grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
"""
somaidade = 0
homemmaisvelho = 0
homemnome = ' '
qtdmulher = 0
for p in range(1,5):
    print("----{}ª Pessoa ----".format(p))
    nome = str(input("Digite Nome: ")).upper()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo M/F:" )).upper()
    somaidade += idade

    if p ==1 and sexo == 'M':
        homemmaisvelho = idade
        homemnome = nome
    else:
        if homemmaisvelho < idade and sexo == 'M':
            homemmaisvelho = idade
            homemnome = nome
    if sexo == 'F' and idade < 20:
        qtdmulher +=1


print("Media da idade das pessoas é: {} anos".format(somaidade/4))
print("Homem mais velho é o : {}".format(homemnome))
print("Quantidade de mulher menor de idade é {}".format(qtdmulher))
