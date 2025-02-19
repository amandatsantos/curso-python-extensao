def contar_ocorrencias(tupla, elemento):
    return tupla.count(elemento)

valores = (10, 20, 30, 10, 40, 50, 10, 60)
elemento_busca = 10
print(f"O numero {elemento_busca} aparece {contar_ocorrencias(valores, elemento_busca)} vezes.")

#todo- entrada user