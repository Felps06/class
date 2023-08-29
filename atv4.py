
lista_compras = []

while True:
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Editar item")
    print("4 - Listar itens")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        item = input("Digite o item que deseja adicionar: ")
        lista_compras.append(item)
        print("Item adicionado à lista!")

    elif opcao == "2":
        item = input("Digite o item que deseja remover: ")
        if item in lista_compras:
            lista_compras.remove(item)
            print("Item removido da lista!")
        else:
            print("Item não encontrado na lista!")

    elif opcao == "3":
        item_antigo = input("Digite o item que deseja editar: ")
        if item_antigo in lista_compras:
            index = lista_compras.index(item_antigo)
            novo_item = input("Digite o novo valor para o item: ")
            lista_compras[index] = novo_item
            print("Item editado com sucesso!")
        else:
            print("Item não encontrado na lista!")

    elif opcao == "4":
        if len(lista_compras) > 0:
            print("Lista de Compras:")
            for item in lista_compras:
                print(item)
        else:
            print("A lista de compras está vazia!")

    elif opcao == "0":
        break

    else:
        print("Opção inválida!")

print("Obrigado por usar a Lista de Compras!")