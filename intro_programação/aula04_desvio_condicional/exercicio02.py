conta = input("número da conta: ")
saldo = float(input("saldo: "))
debito = float(input("débito: "))
credito = float(input("crédito: "))
saldo_atual = saldo - debito + credito
print("saldo atual:", saldo_atual)
print("saldo positivo" if saldo_atual >= 0 else "saldo negativo")
