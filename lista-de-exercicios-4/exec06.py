# func que recebe uma tupla e retorna as operacoes
def operacoes(tupla):
    a, b = tupla
    return a + b, a-b, a/b,  a * b

# chama a funçao com uma tupla
resultados = operacoes((5, 3))

# exibe os resultados
print(f"soma: {resultados[0]}, subttração {resultados[1]} , divisão {resultados[2]}, multiplicação: {resultados[3]}")

# todo -> poderia ter entrada do usurio 