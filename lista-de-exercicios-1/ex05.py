# 5. (Desafio) Solicite dois números ao usuário (um valor mínimo e um máximo). Gere um número aleatório entre eles e mostre o resultado. 
# Dica: Use o módulo random.

import random

minimo = int(input("Digite o valor mínimo: "))
maximo = int(input("Digite o valor máximo: "))
numero_aleatorio = random.randint(minimo, maximo)
print(f"O número aleatório gerado entre {minimo} e {maximo} é: {numero_aleatorio}")