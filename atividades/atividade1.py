#vamos fazer um simulador de caixa eletronico

cedulas = [100, 50, 20, 10, 5, 2, 1]

quantidades_cedulas = [1, 1, 1, 1, 1, 1, 2]

print("Bem-vindo ao simulador de caixa eletrônico!")

pagamento = int(input("Digite o valor que deseja sacar: "))

if pagamento < 0:
    print("Valor invalido. Por favor, digite um valor positivo.")
else:
    print(f"voce solicitou o saque de R${pagamento}.")
    print("O caixa eletrônico possui as seguintes cédulas disponíveis:")
    if cedulas in quantidades_cedulas:
        for i in range(len(cedulas)):
            print(f"{quantidades_cedulas[i]} cédula(s) de R${cedulas[i]}")

#o for serve para percorrer a lista de cédulas e quantidades disponíveis, exibindo ao usuário a quantidade de cada cédula que o caixa eletrônico possui. então ele fala assim, "o caixa eletrônico possui as seguintes cédulas disponíveis: 1 cédula(s) de R$100, 1 cédula(s) de R$50, 1 cédula(s) de R$20, 1 cédula(s) de R$10, 1 cédula(s) de R$5, 1 cédula(s) de R$2, 2 cédula(s) de R$1".

# o i serve para pegar o toda variavel de cedulas e quantidades_cedulas, ele ve as variaveis e vai pegando uma por uma, e vai exibindo na tela. o len serve para pegar o tamanho da lista, ou seja, quantos elementos tem na lista. o range serve para criar um intervalo de numeros, nesse caso ele vai de 0 até o tamanho da lista -1, ou seja, ele vai percorrer todos os elementos da lista. entao falando de uma forma mais simples, o range vai pegar o tamanho da lista, vai olhar quantos elementos tem na lista, e cria o intervalo de numeros, e o for vai percorrer esse intervalo de numeros, e vai pegando os elementos da lista, e vai exibindo na tela.