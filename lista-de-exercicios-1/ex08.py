# 8. Peça um preço e calcule o valor com 10% de desconto.

preco = float(input("Digite o preço do produto: "))
desconto = preco * 0.10
preco_final = preco - desconto
print(f"O preço com 10% de desconto é: R${preco_final:.2f}")