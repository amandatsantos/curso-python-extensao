def soma_lista(numeros):
    return sum(numeros)

# 1- criar uma lista vazia
lista = []

# 2- entrada do usuario para inserir numeros na lista
while True:
    numero = input("Insira um número na lista (ou 'somar' para finalizar e somar os itens da lista): ")
    
    if numero.lower() == "somar":
        break  # 2 -sai do loop se o user digitar 'somar'

    else:
        lista.append(int(numero))  # converte para inteiro e adiciona à lista
        print(f"\nlista atualizada: {lista} | Total de numeros: {len(lista)}")


# exibindo a soma dos elementos
print("\nsoma dos elementos:", soma_lista(lista))



