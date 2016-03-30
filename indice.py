from fnvhash import fnv1a_32 as fm 
from listaReproduccion import *
class nodoIndice:
	def __init__(self,clave,lista):
		self.clave = clave
		self.lista = lista
		self.next = None
		self.prev = None

class dlist:
	def __init__(self):
		self.head = None

	def insert(self,node):
		node.next = self.head
		if self.head != None:
			self.head.prev = node
		self.head = node

	def search(self, clave):
		node = self.head
		while node != None and node.clave.lower() != clave.lower():
			node = node.next
		return node

class Indice:
	def __init__(self,size = 5):
		self.size = size
		self.slot = [dlist() for i in range(self.size)]
		self.nodes = 0

	def fh(self,clave):
		return fm(clave.lower())%self.size

	def rehash(self):
		N = self.size
		A = list(self.slot)
		self.size = 2*self.size + 1
		self.slot = [ dlist() for i in xrange(self.size) ]
		self.nodes = 0
		for i in xrange(N):
			x = A[i].head
			while x!=None:
				self.insertNode(x)
				x = x.next

	def insertNode(self, node):
		m = self.fh(node.clave)
		x = self.slot[m].search(node.clave)
		if x == None:
			self.slot[m].insert(node)
			self.nodes += 1
		else:
			x.lista.agregar_final(node.lista.head.cancion)
		if (float(self.nodes)/self.size)*100 >= 80:
			self.rehash()

	def insertArtista(self,cancion):
		l = listaReproduccion()
		l.agregar(cancion)
		node = nodoIndice(cancion.artista,l)
		self.insertNode(node)

	def insertGenero(self,cancion):
		l = listaReproduccion()
		l.agregar(cancion)
		node = nodoIndice(cancion.genero,l)
		self.insertNode(node)

	def search(self,clave):
		m = self.fh(clave)
		x = self.slot[m].search(clave)
		if x != None : return x.lista