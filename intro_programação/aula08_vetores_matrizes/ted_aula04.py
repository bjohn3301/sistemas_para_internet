import random

q = []
for i in range(20):
    while True:
        valor = random.randint(1, 100)
        if valor > 0:
            q.append(valor)
            break

maior = max(q)
menor = min(q)
pos_maior = q.index(maior)
pos_menor = q.index(menor)

print(f"maior valor: {maior}, na posição: {pos_maior}")
print(f"menor valor: {menor}, na posição: {pos_menor}")
