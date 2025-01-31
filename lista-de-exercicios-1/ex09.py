# 9. Peça um número de dois dígitos e exiba a soma dos dígitos (exemplo: 25 → 2+5=7).

num = int(input("Digite um número de dois dígitos: "))
if 10 <= num <= 99:  
    dezena = num // 10
    unidade = num % 10
    soma = dezena + unidade
    print(f"A soma dos dígitos de {num} é {soma}")
else:
    print("Por favor, digite um número de dois dígitos.")