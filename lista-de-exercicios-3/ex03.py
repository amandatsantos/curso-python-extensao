num = int(input("Digite um número para ver sua tabuada: "))

#tabuada de 1 a 10
print(f"Tabuada do {num}:")
for i in range(1, 11):  #percorre os numeros de 1 a 10
    resultado = num * i  #multiplica o numero pelo contador
    print(f"{num} x {i} = {resultado}")  
