numero = input("Digite um número inteiro: ")

if numero.lstrip('-').isdigit():  
    numero = int(numero)  

    if numero > 0:
        print("O número é positivo.")
    elif numero < 0:
        print("O número é negativo.")
    else:
        print("O número é zero.")
else:
    print("Por favor, digite um número inteiro válido.")
