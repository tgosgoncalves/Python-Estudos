
nome = 'Tiago Gonçalves'
idade = 27
altura = 1.80
maioridade = idade > 18
peso = 92
imc = peso // altura ** 2

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('Peso atual:', peso)
print('Maioridade Civil:', maioridade)
print(imc)

print(f'O usuario {nome}, tem {altura} de altura, e {peso} quilos. \nAtualmente o seu IMC é: {imc}.')
print(f'O usuario {}, tem {} de altura, e {} quilos. \nAtualmente o seu IMC é: {}'.format(nome, altura, peso, imc))