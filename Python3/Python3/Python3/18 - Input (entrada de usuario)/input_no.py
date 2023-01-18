'''
Entrada de dados, jogar imput dentro de uma varivel
'''

nome = input('Qual é o seu nome?:')
idade = input('Quantos anos você tem?:')
ano_nacimento = 2023 - int(idade)  # Convertendo a string para inteiro senao não da para fazer essa conta, tudo que é digitado vira STR
print(f'Olá {nome}, você vem sempre aqui? \n vique voce tem {idade} anos e naceu em {ano_nacimento}' )