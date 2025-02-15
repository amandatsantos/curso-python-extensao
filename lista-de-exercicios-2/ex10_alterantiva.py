""" enunciado da questão : 
10. Crie um programa que gere um número aleatório entre 1 e 10 e peça ao usuário para adivinhar.
Se o usuário acertar, exiba "Parabéns, você acertou!".
Se o número do usuário for menor, exiba "Tente um número maior!".
Se o número do usuário for maior, exiba "Tente um número menor!".

Use import random e a função random.randint(1, 10)."""


import random 
# uso da lib random com a função random.randit para gerar numeros aleatorios entre 1 e 10 ->  o retorno dessa função é um n aletorio inteiro dentro de um 'range'(distacia)? [a, b], que inclui a e b dentro do escopo.
# exemplo? random.randint(a, b) ->  random.randint(1, 5) ->  1,2,3,4,5


def jogo_adivinhacao(): # def = função = rotina

    numero_secreto = random.randint(1, 10)
    palpite = 0
    while palpite != numero_secreto: # lço de repetição while ->  que executa um bloco de código enquanto uma condição for verdadeira (ou falsa se assim determinar se essa é a condiçãõ)
    # entrada de dado
        palpite = int(input("Adivinhe o número entre 1 e 10: "))
        # condições ternario
        print("Parabéns, você acertou!" if palpite == numero_secreto else "Tente um número maior!" if palpite < numero_secreto else "Tente um número menor!")
        # <expressao1> if <condicao> else <expressao2> 
        # <expressao1> -> "Parabéns, você acertou!"  if <condicao> -> palpite == numero_secreto else <expressao2>  "Tente um número maior!"  if <condicao> ->palpite < numero_secret else <expressao2>  "Tente um número menor!"  

jogo_adivinhacao() # chamanda da função  def jogo_adivinhacao()



""" exemplo simples de  uso de ternario -> <expressao1> if <condicao> else <expressao2>
# numero = 10
# classificacao = "positivo" if numero > 0 else "negativo" if numero < 0 else "zero"
# print(f"O número é {classificacao}.") # saída: O número é negativo. """