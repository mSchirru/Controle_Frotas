class Caminhao(object):
	def __init__(self):
		self.placa = ""
		self.conjuntoItens = [] #Itens do tipo ItemEntrega a serem empilhados
		self.conjuntoLocais = [] #Locais do tipo Local a serem enfileirados

def criar_caminhao():
	caminhao = Caminhao()
	caminhao.placa = input("Insira a placa do caminhao: ")
	caminhao.conjuntoItens = []
	caminhao.conjuntoLocais = []
	return caminhao
