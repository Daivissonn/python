def verificar_idade():
        while True:
            nome = input("Digite seu nome: ").strip()
            if not nome:
                print("O nome não pode ser vazio. Por favor, digite novamente.")
            elif nome.isdigit():
                print("O nome não pode ser um número. Por favor, digite novamente.")
            else:
                print(f"Olá, {nome}!")
                break

        while True:
            try:
                idade = int(input("Digite sua idade: "))
                if idade < 0:
                    raise ValueError("A idade não pode ser um número negativo.")
                if idade > 100:
                    raise ValueError("A idade não pode ser maior que 100 anos.")
                break
            except ValueError as erro:
                print(f"Erro: {erro} Digite um número válido.")

        if idade >= 18:
            print(f"\n{nome}, você é maior de idade.")
        else:
            print(f"\n{nome}, você é menor de idade.")
    # VEJA AQUI: Zero espaços antes da palavra 'verificar_idade()'
verificar_idade()