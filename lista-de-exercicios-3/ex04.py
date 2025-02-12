num = int(input("Digite um número para calcular o fatorial: "))

#inicializa o resultado como 1 (pois 0! = 1)
fatorial = 1
contador = num  #variavel para decrementar

#loop while para multiplicar os numeros de n ate 1
while contador > 1:
    fatorial *= contador
    contador -= 1  #decrementa o contador

print(f"O fatorial de {num} é {fatorial}")
