alunos = {
    "legolas": 8.5,
    "frodo": 6.0,
    "aragon": 7.8,
    "galadriel": 9.2,
    "bilbo bolseiro": 5.5
}

aprovados = {}
reprovados = {}
for nome, nota in alunos.items():
    if nota >= 7.0:
        aprovados[nome] = nota
    else:
         reprovados[nome] = nota

print("Alunos aprovados:", aprovados)
print("Alunos reprovados:", reprovados)

media = sum(alunos.values()) / len(alunos)
print("Média geral das notas:", round(media, 2))

# hobbits precisam de reforço