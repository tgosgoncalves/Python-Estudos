'''
Entrada de dados, jogar imput dentro de uma varivel

nome = input('Qual é o seu nome?:')
idade = input('Quantos anos você tem?:')
ano_nacimento = 2023 - int(idade)  # Convertendo a string para inteiro senao não da para fazer essa conta, tudo que é digitado vira STR
print(f'Olá {nome}, você vem sempre aqui? \n vique voce tem {idade} anos e naceu em {ano_nacimento}' )

'''

'''
Calculadora
'''
numero_1 = input('Digite um número:')
numero_2 = input('Digite um número:')
# operrador = input('Digite um operador')

print(numero_1 + numero_2)
