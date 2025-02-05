import random

numero_aleatorio = random.randint(1, 10)

palpite = int(input("Tente adivinhar o número entre 1 e 10: "))

if palpite == numero_aleatorio:
    print("Parabéns, você acertou!")
elif palpite < numero_aleatorio:
    print("Tente um número maior!")
else:
    print("Tente um número menor!")
