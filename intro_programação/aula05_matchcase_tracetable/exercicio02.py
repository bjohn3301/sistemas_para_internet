def exercicio(quantidade_estoque, quantidade_maxima, quantidade_minima):
    media = (quantidade_maxima + quantidade_minima) / 2
    if quantidade_estoque >= media:
        return "Não efetuar compra"
    else:
        return "Efetuar compra"

if __name__ == '__main__':

    try:
        # Escreva seus testes aqui
        assert exercicio(30, 50, 20) == "Efetuar compra"
        assert exercicio(40, 50, 20) == "Não efetuar compra"

    except Exception as e:
        # Não mexer! Mensagem de erro.
        print(f'Erro: {e}')

    else:
        # Não mexer! Mensagem de sucesso.
        print('Programa executado com sucesso!')
