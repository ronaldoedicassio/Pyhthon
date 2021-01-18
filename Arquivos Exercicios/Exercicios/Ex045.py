"""
Crie um programa para jogar jokenpô - Pedra, papel e tesoura

Pedra ganha da tesoura (amassando-a ou quebrando-a).
Tesoura ganha do papel (cortando-o).
Papel ganha da pedra (embrulhando-a).

"""
import emoji
"import random"


"play1 = random.randrange(1,4)"
play1 = 1

play2 = int(input("Escolha uma opção:"
                  "\n 1 - Pedra"
                  "\n 2 - Papel"
                  "\n 3 - Tesoura"
                  "\n OP ==> "))

print(emoji.emojize('Python is :thumbsup:', use_aliases=True))

"""if play1 == 1 and play2 == 2 :
    print("Voce perdeu, pois {} ganha de {}".format(emoji.emojize(":punch:"),emoji.emojize(":raised_hand:")))
"""

