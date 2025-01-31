# 7. Peça uma letra ao usuário e diga se é uma vogal ou uma consoante.

letra = input("Digite uma letra: ").lower()
if letra in "aeiou":
    print(f"A letra '{letra}' é uma vogal.")
elif letra.isalpha():
    print(f"A letra '{letra}' é uma consoante.")
else:
    print("Isso não é uma letra válida!")