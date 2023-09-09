# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
from aula8_classe_json_a import CAMINHO_ARQUIVO, Pessoa

if __name__ == '__main__':
    with open(CAMINHO_ARQUIVO, 'r') as arquivo:
        dados = json.load(arquivo)

        if isinstance(dados, list):
            for i in range(len(dados)):
                pessoa = Pessoa(**dados[i])
                print(vars(pessoa))
        else:
            pessoa = Pessoa(**dados)
            print(vars(pessoa))
        