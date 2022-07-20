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

fabrica.extend(['Teccel','Guepro']) # - add uma lista

#fabrica.append('copinho') # - add apenas um valor
fabrica.insert(1,'quilhas') # - adiciona informação no indicice que eu escolhi (no caso 1 apos o 0)

print(fabrica)