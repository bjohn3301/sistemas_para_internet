notas = []
while True:
    nota = float(input("Digite uma nota (-1 para sair): "))
    if nota == -1:
        break
    notas.append(nota)

if notas:
    media = sum(notas) / len(notas)
    print(f"Média: {media:.2f}")
else:
    print("Nenhuma nota foi inserida.")
