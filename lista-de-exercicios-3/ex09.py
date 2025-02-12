#funcao recursiva que multiplica dois numeros usando somas sucessivas
def multiplica(n1, n2):
    #caso base: se n2 for 0, a multiplicação é 0
    if n2 == 0:
        return 0
    #caso recursivo: n1 + multiplica(n1, n2-1)
    return n1 + multiplica(n1, n2 - 1)

#solicita os numeros ao usuário
n1 = int(input("Digite o primeiro número (n1): "))
n2 = int(input("Digite o segundo número (n2): "))

#chama a funcao e exibe o resultado
resultado = multiplica(n1, n2)
print(f"O resultado de {n1} multiplicado por {n2} é {resultado}.")
