def exercicio(nota1, nota2):
    media = (nota1 + nota2) / 2
    if media >= 6:
        return f"Aprovado\nMédia: {media:.2f}"
    else:
        return f"Reprovado\nMédia: {media:.2f}"

if __name__ == '__main__':

    try:
        # Escreva seus testes aqui
        assert exercicio(7, 5) == "Reprovado\nMédia: 6.00"
        assert exercicio(8, 9) == "Aprovado\nMédia: 8.50"

    except Exception as e:
        # Não mexer! Mensagem de erro.
        print(f'Erro: {e}')

    else:
        # Não mexer! Mensagem de sucesso.
        print('Programa executado com sucesso!')
