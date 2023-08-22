"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_a = ['Luiz', 'Maria', 1, True, 1.2]
# lista_b = lista_a -> Neste caso, "lista_b" faz referência ao mesmo valor 
# na memória de "lista_a". 
lista_b = lista_a.copy() # copia o valor da variável

lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)