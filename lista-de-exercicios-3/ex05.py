#funcao que verifica se um numero é primo
def e_primo(n):
    #numeros menores ou iguais a 1 nao sao primos
    if n <= 1:
        return False
    
    #verifica se o numero tem divisores alem de 1 e ele mesmo
    for i in range(2, n):
        if n % i == 0:  #se o numero for divisivel por i, nao e primo
            return False
    return True  #se nao tiver divisores alem de 1 e ele mesmo, é primo

#solicita um numero ao usuario
num = int(input("Digite um número para verificar se é primo: "))


if e_primo(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
