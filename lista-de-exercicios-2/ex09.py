num1 = input("Digite o primeiro número: ")
num2 = input("Digite o segundo número: ")

if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():
    num1 = float(num1)
    num2 = float(num2)

    operador = input("Digite o operador (+, -, *, /): ")

    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            resultado = "Erro: divisão por zero!"
    else:
        resultado = "Operador inválido."

    print(f"Resultado: {resultado}")
else:
    print("Por favor, digite números válidos.")
