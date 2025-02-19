
def ordenar_tupla(tupla):
    return tuple(sorted(tupla))

# tuplas são imutaveis  logo se deve pasa o valor de uma x para um y para alterar algum valor n se altera a q esta se criar uma nova com os valores da antorir
tupla = (64, 34, 25, 12, 22, 11, 90)
tupla_ordenada = ordenar_tupla(tupla)
print("Tupla ordenada:", tupla_ordenada)
