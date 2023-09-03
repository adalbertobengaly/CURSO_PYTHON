# Exercício - Unir listas
# Crie uma função zipper (como o zipper de roupas)
# O trabalho dessa função será unir duas
# listas na ordem.
# Use todos os valores da menor lista.
# Ex.:
# ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado
# [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte', 'Rio de Janeiro']
ufs = ['BA', 'SP', 'MG', 'RJ']

def zipperListas(listaA, listaB):
    listaUnida = []
    sizeA, sizeB = len(listaA), len(listaB)
    lengthLista = sizeA if sizeA < sizeB else sizeB

    for i in range(lengthLista):
        lista = []
        lista.append(listaA[i])
        lista.append(listaB[i])
        listaUnida.append(tuple(lista))
    
    return listaUnida

print(zipperListas(cidades, ufs))