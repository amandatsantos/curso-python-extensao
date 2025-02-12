n = int(input("Digite um número: "))

print("Contagem Progressiva:") 
for i in range(1, n + 1): #contagem progressiva de 1 ate n
    print(i, end=" ")

#pula uma linha para separar as contagens
print("\n")

print("Contagem Regressiva:")
for i in range(n, 0, -1): #contagem regressiva de n ate 1
    print(i, end=" ")
