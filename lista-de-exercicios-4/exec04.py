"Uma forma simples de ordenar um vetor com n inteiros em ordem crescente é encontrar o menor elemento e colocá-lo na primeira posição, depois encontrar o segundo menor e colocá-lo na segunda posição, e assim por diante até o final."

#func de ordencao da lista - vetor
def ordenar_lista(vetor):
    vetor.sort()
    return vetor


vetor = [64, 34, 25, 12, 22, 11, 90]
vetor_ordenado = ordenar_lista(vetor)
print("Vetor ordenado:", vetor_ordenado)
