valor = float(input())
if valor > 100:
    desconto = valor * 0.10
elif valor >= 50:
    desconto = valor * 0.05
else:
    desconto = 0
total = valor - desconto
print(f"Desconto: R${desconto:.2f}\nTotal a pagar: R${total:.2f}")
