def plusMinus(arr):
    positivos = 0
    negativos = 0
    zeros = 0

    for x in arr:
        if x > 0:
            positivos += 1
        elif x < 0:
            negativos += 1
        else:
            zeros += 1

    listaPropocao = [positivos, negativos, zeros]
    lengthArr = len(arr)

    for x in listaPropocao:
        proporcao = x / lengthArr
        print(f'{proporcao:.6f}')

plusMinus([-4, 3, -9, 0, 4, 1])
print()
plusMinus([1, 2, 3, -1, -2, -3, 0, 0])
    
