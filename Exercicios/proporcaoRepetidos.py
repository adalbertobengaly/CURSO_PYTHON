def proporcaoRepetidos(arr):
    listaSemRepetidos = []

    for x in arr:
        if x not in listaSemRepetidos:
            listaSemRepetidos.append(x)

    listaProporcao = [] 

    for x in listaSemRepetidos:
        listaProporcao.append(arr.count(x))

    lengthArr = len(arr)

    for x in listaProporcao:
        fracao = x / lengthArr
        print(f'{fracao:.6f}')

proporcaoRepetidos([1, 1, 2, 2, 3, 5, 6, 6])