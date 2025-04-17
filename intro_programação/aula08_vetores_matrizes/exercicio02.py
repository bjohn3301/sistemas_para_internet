import random

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    tentativa = int(input("Adivinhe o número entre 1 e 100: "))
    tentativas += 1

    if tentativa < numero_secreto:
        print("Maior...")
    elif tentativa > numero_secreto:
        print("Menor...")
    else:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        break
