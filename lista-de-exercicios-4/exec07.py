contatos = {
    "rick": "99999-1234",
    "morty": "98888-5678",
    "clonerick": "97777-9101"
}

def buscar_contato(nome):
    return contatos.get(nome, "Contato não encontrado")

nome_busca = "rick"
print(f"Telefone de {nome_busca}: {buscar_contato(nome_busca)}")
