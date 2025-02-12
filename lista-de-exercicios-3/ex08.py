#funcao recursiva que retorna o n esimo termo de fibonacci
def fibonacci(n):
    #caso base: F(0) = 0 e F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    #caso recursivo: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

#solicita ao usuario o valor de n
n = int(input("Digite o valor de n para calcular o n-ésimo termo da sequência de Fibonacci: "))

#chama a funcao e exibe o resultado
resultado = fibonacci(n)
print(f"O {n}-ésimo termo da sequência de Fibonacci é {resultado}.")
