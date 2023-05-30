# Entrada com identificador
print("Bem vindo ao controle de estoque da bicicletaria Levi Vieira de Sousa")
print('-' * 60)

# Função para cadastrar peça
def cadastrarPeca(codigo):
    # Cria um dicionário vazio para armazenar os dados da peça
    peca = {}

    # Atribui o código exclusivo da peça ao dicionário
    peca['Código'] = codigo

    # Solicita ao usuário as informações da peça e as armazena no dicionário
    peca['Nome'] = input("Digite o nome da peça: ")
    peca['Fabricante'] = input("Digite o fabricante da peça: ")
    peca['Valor'] = float(input("Digite o valor da peça: "))

    # Retorna o dicionário contendo os dados da peça
    return peca


# Função para consultar peças
def consultarPeca(pecas):
    while True:
        print("Escolha a opção desejada:")
        print("1) Consultar Todas as Peças")
        print("2) Consultar Peças por Código")
        print("3) Consultar Peças por Fabricante")
        print("4) Retornar")

        opcao = input("Digite a opção desejada: ")

        if opcao == '1':
            if pecas:
                # Exibe todas as peças cadastradas
                print("Todas as Peças:")
                for peca in pecas:
                    print('-'*60)
                    print("Código:", peca['Código'])
                    print("Nome:", peca['Nome'])
                    print("Fabricante:", peca['Fabricante'])
                    print("Valor:", peca['Valor'])
            else:
                print("Não há peças cadastradas.")
        elif opcao == '2':
            # Solicita ao usuário o código da peça a ser consultada
            codigo = int(input("Digite o código da peça: "))

            # Procura a peça com o código informado e exibe seus dados
            for peca in pecas:
                if peca['Código'] == codigo:
                    print("Peça encontrada:")
                    print('-'*60)
                    print("Código:", peca['Código'])
                    print("Nome:", peca['Nome'])
                    print("Fabricante:", peca['Fabricante'])
                    print("Valor:", peca['Valor'])
                    break
            else:
                print("Nenhuma peça encontrada com o código informado.")
        elif opcao == '3':
            # Solicita ao usuário o fabricante da peça a ser consultada
            fabricante = input("Digite o fabricante da peça: ")

            # Procura as peças com o fabricante informado e exibe seus dados
            encontradas = []
            for peca in pecas:
                if peca['Fabricante'] == fabricante:
                    encontradas.append(peca)
            if encontradas:
                print("Peças encontradas:")
                for peca in encontradas:
                    print('-'*60)
                    print("Código:", peca['Código'])
                    print("Nome:", peca['Nome'])
                    print("Fabricante:", peca['Fabricante'])
                    print("Valor:", peca['Valor'])
            else:
                print("Nenhuma peça encontrada com o fabricante informado.")
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Digite uma opção válida.")


# Função para remover peça
def removerPeca(pecas):
    # Solicita ao usuário o código da peça a ser removida
    codigo = int(input("Digite o código da peça que deseja remover: "))

    pecas_restantes = []

    # Procura a peça com o código informado e adiciona as outras peças à nova lista
    encontrada = False
    for peca in pecas:
        if peca['Código'] == codigo:
            encontrada = True
            print("Peça removida com sucesso.")
        else:
            pecas_restantes.append(peca)

    if not encontrada:
        print("Nenhuma peça encontrada com o código informado.")

    return pecas_restantes

# Lista de peças
pecas = []

# Contador de código
codigo = 1

# Loop principal do programa
while True:
    print("Selecione uma opção:")
    print("1) Cadastrar Peças")
    print("2) Consultar Peças")
    print("3) Remover Peças")
    print("4) Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == '1':
        # Chama a função de cadastrar peça e adiciona a peça cadastrada na lista de peças
        nova_peca = cadastrarPeca(codigo)
        pecas.append(nova_peca)
        codigo += 1
        print("Peça cadastrada com sucesso.")
    elif opcao == '2':
        # Chama a função de consultar peças
        consultarPeca(pecas)
    elif opcao == '3':
        # Chama a função de remover peça e atualiza a lista de peças
        pecas = removerPeca(pecas)
    elif opcao == '4':
        break
    else:
        print("Opção inválida. Digite uma opção válida.")
