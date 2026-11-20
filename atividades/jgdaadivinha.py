#vamos criar um jogo de adivinhação de números
import random #isso importa a biblioteca random para gerar números aleatórios

numero_secreto = random.randint(1,100) #gera um número aleatório entre 1 e 100
tentativas = 0 #inicializa o número de tentativas
def verificar_diferenca(numero_usuario, numero_secreto):
    diferenca = abs(numero_usuario - numero_secreto) 
    
    #calcula a diferença entre o número do usuário e o número secreto
    #abs é uma função que retorna o valor absoluto de um número, ou seja, sem sinal negativo entao se o numero do usuario for 10 e o numero secreto for 12, a diferenca sera 2, e se o numero do usuario for 12 e o numero secreto for 10, a diferenca sera 2 tambem, entao ele vai sempre retornar um valor positivo e nao negativo porque o valor absoluto é sempre positivo

    if diferenca == 1: #se a diferença for 1
        print("VEIIII, TA APELANDOOOOOOOO")
    elif diferenca <= 5: #se a diferença for maior que 5
        print("VEI, TA QUASEEEE, TA QUASE LA, MAS NAO TA LA AINDA")
    elif diferenca <= 10: #se a diferença for maior que 10
        print("DA PARA DIZER QUE VOCE TA PERTO")
    else: #se a diferença for menor ou igual a 2
        print("TA LONGE PRA PORRA")

print("Bem-vindo ao jogo de adivinhação!")
print("\n nesse desafio, voce vai tentar adivinhar um numero de 1 a 100, e o computador vai te dar dicas se o numero que voce digitou é maior ou menor que o numero secreto. Boa sorte!")

numero_usuario = int(input("Digite um número entre 1 e 100: ")) #pede para o usuário digitar um número
tentativas += 1 #incrementa o número de tentativas

while numero_usuario != numero_secreto: #enquanto o número do usuário for diferente do número secreto
    verificar_diferenca(numero_usuario, numero_secreto)

    print("-" * 30) #imprime uma linha de separação
    numero_usuario = int(input("Digite outro número entre 1 e 100: ")) #pede para o usuário digitar outro número
    tentativas += 1 #incrementa o número de tentativas

if numero_usuario == numero_secreto: #se o número do usuário for igual ao número secreto
    print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!") #imprime uma mensagem de parabéns e o número de tentativas

#vamos colocar um laço de repetição para que o usuário possa tentar adivinhar o número secreto até acertar
#e colocar uma mensagem se ele esta 1 numero de diferença maior ou menor que o numero secreto
