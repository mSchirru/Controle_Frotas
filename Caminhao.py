import Fila
import Pilha

class Caminhao(object):
	def __init__(self):
		self.placa = ""
		self.conjuntoItens = Pilha.Stack() #Itens do tipo ItemEntrega a serem empilhados
		self.conjuntoLocais = Fila.Queue()  #Locais do tipo Local a serem enfileirados

def criar_caminhao():
	caminhao = Caminhao()
	caminhao.placa = input("Insira a placa do caminhao: ")
	caminhao.conjuntoItens = Pilha.Stack()
	caminhao.conjuntoLocais = Fila.Queue()
	return caminhao
