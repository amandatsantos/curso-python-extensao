#funcao que calcula a media entre dois numeros
def calcula_media(n1, n2):
    return (n1 + n2) / 2

#solicita dois numers ao usuario
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

#calcula a media 
media = calcula_media(num1, num2)
print(f"A média entre {num1} e {num2} é {media}")
