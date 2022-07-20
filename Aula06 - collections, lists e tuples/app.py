# 1 - collections (listas de dados)
fabrica = ['Tiago','Thiago','Andrey','Angelo','Isabella','Marcelo','Mateus','Cabral','Andre']
# indice      0        1        2       3          4         5         6        7       8
#            -9       -8       -7      -6         -5        -4        -3       -2      -1
#print(fabrica[0]) - retorna um indice
#print((fabrica[-5])) - retorna um indice de traz pra frente
#print(fabrica[2:]) - retorna a partir do indice 2
#print(fabrica[3:6]) - retorna a partir do indice 3 e um indice antes do ultimo informado 

fabrica[3] = 'Lolo' #- pode ser usado para alterar um item 
#print(fabrica)

#fabrica.extend(['Teccel','Guepro']) # - add uma lista

#fabrica.append('copinho') # - add apenas um valor
#fabrica.insert(1,'quilhas') # - adiciona informação no indicice que eu escolhi (no caso 1 apos o 0)
#fabrica.pop() # - remove o ultimo valor
#fabrica.remove('Tiago') # - Remove o nome que eu passar
#fabrica.clear()
#print(fabrica)

#print(fabrica.index('Thiago')) # - mostra o valor do indice
#print(fabrica.count('Thiago')) # - conta quantos indices tem com o mesmo nome

#idade_fabrica = [28,38,18,36,40,44,24,22,33]
#idade_fabrica.sort() # - ordena por ordem crescente (funcina com strings)
#idade_fabrica.reverse() # - ordena em ordem decrecente (funcina com strings)
#print(idade_fabrica)

# FORMAS DE CPIAR LISTA - (copia de referencia - mesmo espaco de memoria)

#fabrica2 = fabrica
#fabrica.remove('Tiago')
#print((fabrica2))

# FORMAS DE CPIAR LISTA - (copia de referencia - espaco de memoria diferente)

#fabrica2 = fabrica.copy()
#fabrica.remove('Tiago')
#print(fabrica2)
#print(fabrica)

#