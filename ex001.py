print('Ola, mundo!')

nome = input('Qual é o seu nome? ')
print(f'Prazer em te conhecer, {nome}!')

print('Vamos analisar algo que você digitar...')

n = input('Digite algo: ')
print(n.isalpha()) #Aqui ele vai verificar se o que foi digitado é apenas letras

n= input('Digite algo: ')
print(n.isnumeric()) #Aqui ele vai verificar se o que foi digitado é apenas números

n= input('Digite algo: ')
print(n.isalnum()) #Aqui ele vai verificar se o que foi digitado é apenas letras e números

