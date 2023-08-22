
while True:
    question = input("Deseja calcular? S/N \nR: ").upper()
    if question == "S":
        try:
            num_1 = float(input("Digite o primeiro número: "))
            num_2 = float(input("Digite o segundo número: "))

            operador = input("Digite a operação (+ - * /): ")

            if operador == "+":
                print(num_1 + num_2)
            elif operador == "-":
                print(num_1 - num_2)
            elif operador == "*":
                print(num_1 * num_2)
            elif operador == "/":
                print(num_1 / num_2)
            else:
                print("Operador inválido! Escolha entre + - * /")
        except:
            print("Digite apenas números!")
    elif question == "N":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")


