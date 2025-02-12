
n = int(input("Digite um número inteiro: "))

#inicializa a variavel para armazenar a soma
soma_pares = 0

#percorre todos os numeros de 1 ate n
for i in range(1, n + 1):
    if i % 2 == 0:  #verifica se o numero é par
        soma_pares += i  #soma o numero par


print(f"A soma de todos os números pares de 1 até {n} é {soma_pares}")
