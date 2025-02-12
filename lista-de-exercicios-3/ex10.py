#funcao recursiva para contar a quantidade de digitos de um numero
def conta_digitos(n):
    #caso base: se n for menor que 10, tem apenas 1 digito
    if n < 10:
        return 1
    #caso recursivo: dividimos o numero por 10 e chamamos a funcao novamente
    return 1 + conta_digitos(n // 10)

numero = int(input("Digite um número: "))
resultado = conta_digitos(numero)
print(f"O número {numero} tem {resultado} dígitos.")
