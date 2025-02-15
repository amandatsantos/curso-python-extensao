# dict 1 reinos
personagens_reinos = {
    "Frodo": "Condado",
    "Aragorn": "Gondor",
    "Gandalf": "Cinza",
    "Legolas": "Mirkwood",
    "Gimli": "Erebor",
    "Boromir": "Gondor"
}

# dict 2: nomes e idades
personagens_idades = {
    "Frodo": 33,
    "Aragorn": 87,
    "Gandalf": 2019,  
    "Legolas": 2931,  
    "Gimli": 139,     
    "Boromir": 41
}

# iterandoo os dict
for nome, idade in personagens_idades.items():
    if nome in personagens_reinos:
        personagens_reinos[nome] = (personagens_reinos[nome], idade)

# mostra o dict iterado
print("Dicionario mesclado com Reino e Idade:")
for nome, info in personagens_reinos.items():
    reino, idade = info
    print(f"{nome}: Reino - {reino}, Idade - {idade}")
