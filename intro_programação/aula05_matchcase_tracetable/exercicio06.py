def exercicio(salario):
    if salario <= 2000:
        return "Isento"
    elif salario <= 3500:
        imposto = salario * 0.10
        return f"Imposto: R${imposto:.2f}"
    else:
        imposto = salario * 0.15
        return f"Imposto: R${imposto:.2f}"

if __name__ == '__main__':

    try:
        # Escreva seus testes aqui
        assert exercicio(1500) == "Isento"
        assert exercicio(2500) == "Imposto: R$250.00"
        assert exercicio(4000) == "Imposto: R$600.00"

    except Exception as e:
        # Não mexer! Mensagem de erro.
        print(f'Erro: {e}')

    else:
        # Não mexer! Mensagem de sucesso.
        print('Programa executado com sucesso!')
