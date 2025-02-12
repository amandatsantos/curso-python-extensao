#funcao que verifica se uma palavra é um palindromo
def e_palindromo(palavra):
    #compara a palavra original com a palavra invertida
    return palavra == palavra[::-1]

#solicita uma palavra ao usurio
palavra = input("Digite uma palavra: ")

#verifica se a palavra é um palindromo e exibe o resultado
if e_palindromo(palavra):
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")
