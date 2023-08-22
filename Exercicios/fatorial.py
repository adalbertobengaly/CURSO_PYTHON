def fatorial(numero: int):
    if (type(numero) is not int) or (numero < 0):
        return "Somente inteiros positivos!"
    
    if (numero == 0):
        return 1

    return numero * fatorial(numero - 1)

if __name__ == '__main__':
    print(fatorial(6.5))
    print(fatorial(-5))
    print(type(1.9) is float)