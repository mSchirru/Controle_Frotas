import ItemEntrega
import Local
import Caminhao

itens = []
locais = []
caminhoes = []

def main():
    choice = '-'
    while choice != '0':
        print("\n\n************ MENU **************")
        print("*[1] Pontos de Entrega")
        print("*[2] Itens de Entrega")
        print("*[3] Caminhões")
        print("*[4] Associar item a ponto de entrega")
        print("*[5] Associar ponto de entrega a caminhão")
        print("*[6] Realizar entregas")
        print("*[0] Sair")
        print("*********************************** \n")

        choice = input ("Insira sua escolha: ")

        if choice == "6":
            realizar_entregas()

        elif choice == "5":
            associar_local_caminhao()

        elif choice == "4":
            associar_item_ptentrega()

        elif choice == "3":
            menu_Caminhoes()

        elif choice == "2":
            menu_ItensEntrega()

        elif choice == "1":
            menu_pontoEntrega()

        elif choice == "0":
            print("Até a próxima.")


        else:
            print("Escolha uma opção viavel")

def menu_pontoEntrega():
    choice = '-'
    while choice != '0':
        print("\n\n************ SUBMENU **************")
        print("[1] Inserir ponto de entrega")
        print("[2] Remover pontos de entrega")
        print("[3] Verificar os dados de um ponto")
        print("[0] Sair")
        print("*********************************** \n")

        choice = input("Insira sua escolha: ")

        if choice == "1":
            novo_local = Local.criar_local()
            if any(local.identificador == novo_local.identificador for local in locais):
                print("Este identificador já está em uso!")
            else:
                locais.append(novo_local)
                print("{} adicionado com sucesso a lista de locais!".format(novo_local.nome))


        elif choice == "2":
            print("---------- Lista de Locais: ----------")
            aux = 0
            for local in locais:

                print("| [{}] Local: {} | Identificador: {} |".format(aux, local.nome, local.identificador))
                aux += 1
            print("--------------------------------------")

            index_deletar = int(input("Insira o numero do local a ser deletado: "))
            print("Tem certeza que deseja deletar {} da sua lista de locais?".format(locais[index_deletar].nome))
            escolha_deletar = input("[0] Confirmar\n[1] Cancelar")
            if escolha_deletar == "0":
                locais.pop(index_deletar)

        elif choice == "3":
            print("---------- Lista de Locais: ----------")
            aux = 0
            for local in locais:
                print("| [{}] Local: {} | Identificador: {} |".format(aux, local.nome, local.identificador))
                aux += 1
            print("--------------------------------------")

            index_detalhes = int(input("Insira o numero do local a ser detalhado: "))

            if len(locais[index_detalhes].itens) == 0:
                print("Local: {} | Indentificador: {} | Itens: {}".format(locais[index_detalhes].nome,
                                                                          locais[index_detalhes].identificador,
                                                                          "Não há itens"))
            else:
                print("Local: {} | Indentificador: {} | Itens: {}".format(locais[index_detalhes].nome,
                                                                          locais[index_detalhes].identificador,
                                                                          [item.nome for item in locais[index_detalhes]
                                                                          .itens]))

def menu_ItensEntrega():
    choice = '-'
    while choice != '0':
        print("\n\n************ SUBMENU **************")
        print("[1] Inserir item de entrega")
        print("[2] Remover item de entrega")
        print("[3] Verificar os itens de entrega")
        print("[0] Sair")
        print("*********************************** \n")

        choice = input("Insira sua escolha: ")

        if choice == "1":
            novo_item = ItemEntrega.criar_item()
            if any(item.identificador == novo_item.identificador for item in itens):
                print("Este identificador já está em uso!")
            else:
                itens.append(novo_item)
                print("{} adicionado com sucesso a lista de itens!".format(novo_item.nome))



        elif choice == "2":
            print("---------- Lista de Itens: ----------")
            aux = 0
            for item in itens:
                print("| [{}] Item: {} | Identificador: {} |".format(aux, item.nome, item.identificador))
                aux += 1
            print("--------------------------------------")

            index_deletar = int(input("Insira o numero do item a ser deletado: "))
            print("Tem certeza que deseja deletar {} da sua lista de itens?".format(itens[index_deletar].nome))
            escolha_deletar = input("[0] Confirmar\n[1] Cancelar")
            if escolha_deletar == "0":
                itens.pop(index_deletar)

        elif choice == "3":
            print("---------- Lista de Itens: ----------")
            aux = 0
            for item in itens:
                print("| [{}] Item: {} | Identificador: {} |".format(aux, item.nome, item.identificador))
                aux += 1
            print("--------------------------------------")

def menu_Caminhoes():
    choice = '-'
    while choice != '0':
        print("\n\n************ SUBMENU **************")
        print("[1] Inserir caminhão")
        print("[2] Remover caminhão")
        print("[3] Verificar detalhes de um caminhão")
        print("[0] Sair")
        print("*********************************** \n")

        choice = input("Insira sua escolha: ")

        if choice == "1":
            novo_caminhao = Caminhao.criar_caminhao()
            if any(caminhao.placa == novo_caminhao.placa for caminhao in caminhoes):
                print("Esta placa já está em uso!")
            else:
                caminhoes.append(novo_caminhao)
            print("Lista de caminhoes:", [caminhao.placa for caminhao in caminhoes])



        elif choice == "2":
            print("---------- Lista de Caminhões: ----------")
            aux = 0
            for caminhao in caminhoes:
                print("| [{}] Placa: {}".format(aux, caminhao.placa))
                aux += 1
            print("--------------------------------------")

            index_deletar = int(input("Insira o numero do caminhao a ser deletado: "))
            print("Tem certeza que deseja deletar o caminhao de placa {} da sua lista?".format(itens[index_deletar].nome))
            escolha_deletar = input("[0] Confirmar\n[1] Cancelar")
            if escolha_deletar == "0":
                caminhoes.pop(index_deletar)

        elif choice == "3":
            print("---------- Lista de Caminhões: ----------")
            aux = 0
            for caminhao in caminhoes:
                print("| [{}] Placa: {} ".format(aux, caminhao.placa))
                aux += 1
            print("--------------------------------------")

            index_detalhes = int(input("Insira o numero do caminhão a ser detalhado: "))

            if caminhoes[index_detalhes].conjuntoLocais.is_empty():
                print("Placa: {} | {}".format(caminhoes[index_detalhes].placa, "Fora de circulação"))
            else:
                print("Placa: {} \nLocais: {} \nItens: {}".format(caminhoes[index_detalhes].placa,caminhoes[index_detalhes].conjuntoLocais.printQueue(),caminhoes[index_detalhes].conjuntoItens.printStack()))

def associar_item_ptentrega():
    print("\n\n---------- Lista de Locais: ----------")
    aux = 0
    for local in locais:
        print("| [{}] Local: {} | Identificador: {} |".format(aux, local.nome, local.identificador))
        aux += 1
    print("--------------------------------------")

    escolha_local = int(input("Selecione primeiramente o local de entrega: "))

    print("\n\n---------- Lista de Itens: ----------")
    aux = 0
    for item in itens:
        print("| [{}] Item: {} | Identificador: {} |".format(aux, item.nome, item.identificador))
        aux += 1
    print("--------------------------------------")

    choice = '-'
    while choice != '1':
        escolha_item = int(input("Selecione o item de entrega: "))
        locais[escolha_local].itens.append(itens[escolha_item])
        print("\nItem: {} adicionado ao Local: {}".format(itens[escolha_item].nome, locais[escolha_local].nome))
        choice = input("\n[0] Adicionar novo item | [1] Sair")

def associar_local_caminhao():
    print("---------- Lista de Caminhões: ----------")
    aux = 0
    for caminhao in caminhoes:
        print("| [{}] Placa: {}".format(aux, caminhao.placa))
        aux += 1
    print("--------------------------------------")

    escolha_caminhao = int(input("Selecione primeiramente o caminhao de entrega: "))

    print("---------- Lista de Locais: ----------")
    aux = 0
    for local in locais:
        print("| [{}] Local: {} | Identificador: {} |".format(aux, local.nome, local.identificador))
        aux += 1
    print("--------------------------------------")

    choice = '-'
    while choice != '1':
        escolha_local = int(input("Selecione o local por ordem de entrega: "))

        caminhoes[escolha_caminhao].conjuntoLocais.enqueue(locais[escolha_local])


        print("Local: {} adicionado ao Caminhao: {}".format(locais[escolha_local].nome,
                                                            caminhoes[escolha_caminhao].placa))

        flag = input("[0] Adicionar novo item | [1] Sair")
        if flag == '1':
            aux = 1
            for local in caminhoes[escolha_caminhao].conjuntoLocais.return_queue():
                for item in local.itens:
                    caminhoes[escolha_caminhao].conjuntoItens.push(item)
            choice = '1'
        else:
            choice = '0'

def realizar_entregas():
    for caminhao in caminhoes:
        locais = 0
        itens = 0
        print("\nPercurso do caminhão: {}".format(caminhao.placa))
        for local in caminhao.conjuntoLocais.return_queue():
            print("\nVisitado o local: {}. Foram entregues os seguintes itens:".format(local.nome))
            locais += 1
            for item in local.itens:
                itens += 1
                print(item.nome)
        print("\nTotal de pontos de entrega: {} \nTotal de itens entregues: {}".format(locais, itens))
















