# os.walk para navegar de caminhos de forma recursiva
# os.walk é uma função que permite percorrer uma estrutura de diretórios de
# maneira recursiva. Ela gera uma sequência de tuplas, onde cada tupla possui
# três elementos: o diretório atual (root), uma lista de subdiretórios (dirs)
# e uma lista dos arquivos do diretório atual (files).
import os
from itertools import count

caminho = os.path.join('/home', 'adalberto', 'Documentos', 'EXEMPLO')
counter = count()
for root, dirs, files in os.walk(caminho):
    the_counter = next(counter)
    print(the_counter, 'Pasta atual', root)

    for dir_ in dirs:
        print(' ', the_counter, 'DIR:', dir_)

    for file_ in files:
        caminho_completo_arquivo = os.path.join(root, file_)
        print(' ', the_counter, 'FILE:', caminho_completo_arquivo)

arquivo_para_deletar = os.path.join(
    caminho, 'pasta_arquivos1/Ferramentas de criação de conteudo')

print(arquivo_para_deletar)
# SÓ FAÇA ISSO se souber o que está fazendo!
# os.unlink(arquivo_para_deletar)  # Deleta arquivos
