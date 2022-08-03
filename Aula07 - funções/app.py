#def big_mec():

#    print('Sanduiche Big Mec')


#big_mec()


def cliente(nome1):

    print(f'Cliente: {nome1}')


def fazer_big_mec(nome):

    print(f'Sanduiche: {nome}')


def fritar_batata(tamanho):

    print(f'Batata: {tamanho}')


def preparar_bebida(tipo,tamanho):

    print(f'Bebida: {tipo}, {tamanho}')



#fazer_big_mec('Tiago')

#fritar_batata('Grande')

#preparar_bebida('Suco', 'Medio')


#def combo1(nome, tamanho_batata, tipo_bebida, tamanho_bebida):


    cliente('Tiago')

    fazer_big_mec('Big Mec')

    fritar_batata('Grande')

    preparar_bebida('Suco', 'grande')


#combo1('Tiago', 'Big Mec' 'Grande', 'Suco', 'grande')

def soma_num(num1, num2):
    return num1 + num2

#resultado = soma_num(10,10)
#print(resultado)

def maior_num(lista_num):
    lista_num.sort() #ordena do maior para o menor
    lista_num.reverse() #inverte a lista
    maior_num = lista_num[0] #pega o primeiro indice
    return maior_num

resultado = maior_num([333, -5, 10, 222, 555, 777])
print(resultado)