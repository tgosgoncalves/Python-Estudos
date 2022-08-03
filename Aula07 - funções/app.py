#def big_mec():
#    print('Sanduiche Big Mec')

#big_mec()

def fazer_big_mec(nome):
    print(f'Sanduiche: Big Mec {nome}')

def fritar_batata(tamanho):
    print(f'Batata: {tamanho}')

def preparar_bebida(tipo,tamanho):
    print(f'Bebida: {tipo}, {tamanho}')


#fazer_big_mec('Tiago')
#fritar_batata('Grande')
#preparar_bebida('Suco', 'Medio')

def combo1(nome, tamanho_batata, tipo_bebida, tamanho_bebida):

    fazer_big_mec('Tiago')
    fritar_batata('Grande')
    preparar_bebida('Suco', 'grande')

combo1('Tiago', 'Grande', 'Suco', 'grande')
