numero = int(input("Digite um número: "))
with open("tabuada.txt", "w") as arquivo:
    for i in range(1, 11):
        linha = f"{numero} x {i} = {numero * i}\n"
        arquivo.write(linha)
