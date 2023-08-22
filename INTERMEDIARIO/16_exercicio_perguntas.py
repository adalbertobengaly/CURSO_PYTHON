# Exercício - sistema de perguntas e respostas

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]

counterAcertos = 0
for questao in perguntas:

    while True: 
        print(f'Pergunta: {questao["Pergunta"]}\n')
        print('Opções:')

        for index, opcao in enumerate(questao['Opções']):
            print(f'{index}) {opcao}')

        try:
            opcao = int(input('Escolha uma opção: '))
            
            if opcao < 0 or opcao > 3:
                print('\nEscolha uma opção válida! 0 a 3.')
                continue

            respostaCorreta = questao["Opções"][opcao] == questao["Resposta"]
            break

        except ValueError:
            print('\nEscolha uma opção válida! 0 a 3.')

    if respostaCorreta:
        counterAcertos += 1
        print('Acertou! 👍\n')
    else:
        print('Errou! ❌\n')

print(f'Você acertou {counterAcertos} de {len(perguntas)} perguntas.')