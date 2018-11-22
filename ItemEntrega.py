class ItemEntrega(object):
	def __init__(self):
		self.nome = ""
		self.identificador =""

def criar_item():
	item = ItemEntrega()
	item.nome = input("Insira o nome do item: ")
	item.identificador = input("Insira o identificador do item: ")
	return item

