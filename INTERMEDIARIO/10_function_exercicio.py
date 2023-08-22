# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o númerto recebido como parâmetro.

def multiplicarVezes(fator):
    def multiplicar(numero):
        return fator * numero
    
    return multiplicar
    
duplicar = multiplicarVezes(2)
triplicar = multiplicarVezes(3)
quadruplicar = multiplicarVezes(4)

print(duplicar(2))
print(triplicar(2))
print(quadruplicar(2))
