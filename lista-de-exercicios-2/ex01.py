ano_nascimento = input("Digite seu ano de nascimento: ")
ano_atual = input("Digite o ano atual: ")


if ano_nascimento.isdigit() and ano_atual.isdigit():
    ano_nascimento = int(ano_nascimento)
    ano_atual = int(ano_atual)
    
    idade = ano_atual - ano_nascimento

    print(f"Você tem {idade} anos.")
else:
    print("Por favor, insira apenas números válidos para os anos.")
