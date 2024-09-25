# Recebe dois números
primeironumero = float(input('Digite um número\n '))
segundonumero = float(input('Digite outro número\n '))

# Função que realiza as operações
def operacoes():
    while True:
        print("\nEscolha a operação que deseja realizar:")
        print("1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Sair")

        opcao = input("Digite o número da operação desejada: ")

        # Soma
        if opcao == "1":
            somados = primeironumero + segundonumero
            print(f'A soma dos números é: {somados}')

        # Subtração
        elif opcao == "2":
            subtraidos = primeironumero - segundonumero
            print(f'A subtração dos números é: {subtraidos}')

        # Multiplicação
        elif opcao == "3":
            multiplicados = primeironumero * segundonumero
            print(f'A multiplicação dos números é: {multiplicados}')

        # Divisão
        elif opcao == "4":
            if segundonumero != 0:  # Verifica se o segundo número é diferente de 0 para evitar erro de divisão
                divididos = primeironumero / segundonumero
                print(f'A divisão dos números é: {divididos:.2f}')
            else:
                print("Não é possível dividir por zero.")

        # Sair
        elif opcao == "5":
            print("Encerrando o programa.")
            break

        # Opção inválida
        else:
            print("Opção inválida, tente novamente.")

# Chama a função de operações novamente
operacoes()

