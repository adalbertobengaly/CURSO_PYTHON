"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

# numero = input("Digite um número inteiro: ")
# if numero.isdigit():
#     print(f"{numero} é PAR!") if int(numero) % 2 == 0 else print(f"{numero} é ÍMPAR!")        
# else:  
#     print(f"{numero} não é um número inteiro")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# entrada = input("Que horas são? ")
# try:
#     horario = int(entrada)
#     if horario < 0 or horario > 23:
#         print("Horário inválido!")
#     elif horario <= 11:
#         print("Bom dia!")
#     elif horario <= 17:
#         print("Boa tarde!")
#     elif horario <= 23:
#         print("Boa noite!")
# except:
#     print("Por favor, informe números inteiros")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

# nome = input("Qual seu primeiro nome? ")
# tamanhoNome = len(nome)

# if tamanhoNome <= 4:
#     print("Seu nome é curto")
# elif tamanhoNome <= 6:
#     print("Seu nome é normal")
# else:
#     print("Seu nome é muito grande")