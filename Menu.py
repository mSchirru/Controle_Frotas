import ItemEntrega
import Local
import Caminhao


itens = []
locais = []
caminhoes = []

def main():
    choice = '0'
    while choice != '5':
        print("\n **************************")
        print("MENU")
        print("[1] Pontos de Entrega")
        print("[2] Inserir item de entrega;")
        print("[3] Inserir caminhão")
        print("[4] Associar item a ponto de entrega")
        print("[5] Associar ponto de entrega a caminhão")
        print("[6] Realizar entregas")
        print("[0] Sair")

        choice = input ("Please make a choice: ")

        if choice == "5":
            print("Go to another menu")
        elif choice == "4":
            print("Do Something 4")
        elif choice == "3":
            novo_caminhao = Caminhao.criar_caminhao()
            if any(caminhao.placa == novo_caminhao.placa for caminhao in caminhoes):
                print("Esta placa já está em uso!")
            else:
                caminhoes.append(novo_caminhao)
            print("Lista de caminhoes:", [caminhao.placa for caminhao in caminhoes])

        elif choice == "2":
            novo_item = ItemEntrega.criar_item()
            if any(item.identificador == novo_item.identificador for item in itens):
                print("Este identificador já está em uso!")
            else:
                itens.append(novo_item)
            print("Lista de itens:", [item.nome for item in itens])

        elif choice == "1":
            menu_pontoEntrega()


        else:
            print("I don't understand your choice.")

def menu_pontoEntrega():
    choice = '-'
    while choice != '0':
        print("[1] Inserir ponto de entrega")
        print("[2] Remover pontos de entrega")
        print("[3] Verificar os dados de um ponto")
        print("[0] Sair")

        choice = input("Please make a choice: ")

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
                                                                          [item for item in locais[index_detalhes]
                                                                          .itens]))





