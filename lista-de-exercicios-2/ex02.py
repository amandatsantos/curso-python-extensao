idade = input("Digite sua idade: ")

if idade.isdigit():
    idade = int(idade)

    if idade >= 18:
        print("Pode dirigir.")
    else:
        print("Não pode dirigir.")
else:
    print("Por favor, digite um número válido.")
