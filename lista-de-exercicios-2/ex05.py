usuario = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

if usuario == "admin" and senha == "1234":
    print("Login bem-sucedido. Bem-vindo, admin!")
else:
    print("Acesso negado.")
