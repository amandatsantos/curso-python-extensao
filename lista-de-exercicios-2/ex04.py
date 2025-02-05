nota = input("Digite sua nota (0 a 100): ")

if nota.isdigit():
    nota = int(nota)
    
    if 0 <= nota <= 100: 
        
        if nota >= 90:
            print("Aprovado com excelência.")
        elif nota >= 70:
            print("Aprovado.")
        elif nota >= 50:
            print("Recuperação.")
        else:
            print("Reprovado.")
    else:
        print("Por favor, digite um número entre 0 e 100.")
else:
    print("Entrada inválida. Digite um número inteiro entre 0 e 100.")
