# Exercício - Salve sua classe em JSON
# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.
import json
CAMINHO_ARQUIVO = 'aula8.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


if __name__ == '__main__':
    p1 = Pessoa('Adalberto', 26)
    p2 = Pessoa('Natália', 25)
    pessoas = [vars(p1), vars(p2)]

    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
        json.dump(
            pessoas,
            arquivo,
            ensure_ascii=False,
            indent=2
        )
