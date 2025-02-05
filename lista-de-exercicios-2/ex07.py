valor_compra = input("Digite o valor total da compra: ")

if valor_compra.replace('.', '', 1).isdigit():  
    valor_compra = float(valor_compra)  

    # aplica os descontos conforme a regra
    if valor_compra > 500:
        desconto = valor_compra * 0.20  
    elif valor_compra >= 200:
        desconto = valor_compra * 0.10  
    else:
        desconto = 0  

    valor_final = valor_compra - desconto

    print(f"Desconto aplicado: R$ {desconto:.2f}")
    print(f"Valor final da compra: R$ {valor_final:.2f}")
else:
    print("Por favor, digite um valor numérico válido.")
