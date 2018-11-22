class Local(object):
	def __init__(self):
		self.nome = ""
		self.identificador = ""
		self.itens = []

def criar_local():
	local = Local()
	local.nome = input("Insira o nome do local: ")
	local.identificador = input("Insira o identificador do local: ")
	local.itens = []
	return local




