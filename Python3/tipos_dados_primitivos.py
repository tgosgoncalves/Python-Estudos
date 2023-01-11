print('Tipos de dados \n')

print('*****************')

print('str/string = Texto \n')

print('Int (inteiro) = 12345\n')

print(f'Float/ flutuante = {100.00}\n')

print('Bool/Boleano = True ou False \n')

# exemplo

print('Tiago', type('Tiago'))
print(10, type(10))
print(10.22, type(10.22))
print(10==10, type(10==10))
print(10==22, type(10==22))

# type cast / converter um tipo para putro

print('Tiago', type('Tiago'), bool('Luiz'))

# algumas string em branco ou com zero são tidas como False

print('Desafio: Mostrar na tela Nome, Idade, Altura e Maioridade\n')

print('Meu nome é: Tiago')
idade = 26
print(f'Idade: {idade} anos')
print('Altura:', end='')
print(176.00)
resultado = idade > 18
print(f'Maior de idade:{resultado}') 
