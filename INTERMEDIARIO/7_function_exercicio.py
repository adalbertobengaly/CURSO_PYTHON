# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiply(*args):
    total_multiplicado = 1
    for numero in args:
        total_multiplicado *= numero

    return total_multiplicado

numeros_mult = multiply(1, 5, 6, 7, 9, 10, 3)
print(numeros_mult)  

# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def parOuImpar(numero):
    if numero % 2 == 0:
        return f"{numero} é PAR!"
    
    return f"{numero} é ÍMPAR!"
    
print(parOuImpar(5))
print(parOuImpar(8))