def miniMaxSum(arr):
    maiorSoma = sum(arr) - min(arr)
    menorSoma = sum(arr) - max(arr)

    print(f'{menorSoma} {maiorSoma}')


miniMaxSum([1, 3, 5, 7, 9])

