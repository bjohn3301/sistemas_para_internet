clubes = []

for i in range(5):
    nome = input("digite o nome de um clube: ")
    clubes.append(nome)

busca = input("digite o nome do clube para buscar: ")

if busca in clubes:
    print("achei")
else:
    print("não achei")
