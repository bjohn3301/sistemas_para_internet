def exercicio(numero):
    if numero > 50:
        return "Maior que 50"
    elif numero < 50:
        return "Menor que 50"
    else:
        return "Igual a 50"

if __name__ == '__main__':

    try:
        # Escreva seus testes aqui
        assert exercicio(60) == "Maior que 50"
        assert exercicio(40) == "Menor que 50"
        assert exercicio(50) == "Igual a 50"

    except Exception as e:
        # Não mexer! Mensagem de erro.
        print(f'Erro: {e}')

    else:
        # Não mexer! Mensagem de sucesso.
        print('Programa executado com sucesso!')
