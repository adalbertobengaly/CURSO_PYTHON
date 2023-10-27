# os.listdir para navegar em caminhos
# /Users/adalbertobengaly/Desktop/EXEMPLO
# C:\Users\adalbertobengaly\Desktop\EXEMPLO
# caminho = r'C:\\Users\\adalbertobengaly\\Desktop\\EXEMPLO'
import os

caminho = os.path.join('/home', 'adalberto', 'Documentos', 'EXEMPLO')

for pasta in os.listdir(caminho):
    caminho_completo_pasta = os.path.join(caminho, pasta)
    print("Caminho: ", caminho_completo_pasta)
    print("Pasta: ", pasta)

    if not os.path.isdir(caminho_completo_pasta):
        continue

    for arquivo in os.listdir(caminho_completo_pasta):
        print(arquivo)

    print("\n")
