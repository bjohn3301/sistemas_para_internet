def exercicio(lado1, lado2, lado3):
    if lado1 == lado2 == lado3:
        return "Triângulo equilátero"
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        return "Triângulo isósceles"
    else:
        return "Triângulo escaleno"

if __name__ == '__main__':

    try:
        # Escreva seus testes aqui
        assert exercicio(3, 3, 3) == "Triângulo equilátero"
        assert exercicio(3, 3, 4) == "Triângulo isósceles"
        assert exercicio(3, 4, 5) == "Triângulo escaleno"

    except Exception as e:
        # Não mexer! Mensagem de erro.
        print(f'Erro: {e}')

    else:
        # Não mexer! Mensagem de sucesso.
        print('Programa executado com sucesso!')
