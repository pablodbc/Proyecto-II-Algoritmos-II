from cancion import *
class nodoLista:
	def __init__(self,cancion):
		self.cancion = cancion
		self.prev = None
		self.next = None


class listaReproduccion:
	def __init__(self):
		self.head = None
		self.size = 0
	def agregar(self,cancion):
		node = nodoLista(cancion)
		if self.head == None:
			node.next = node
			node.prev = node
			self.head = node
			self.size += 1
		else:
			if self.buscar(cancion) == None:
				node.next = self.head
				self.head.prev.next = node
				node.prev = self.head.prev
				self.head.prev = node
				self.head = node
				self.size+=1
	def agregar_final(self,cancion):
		node = nodoLista(cancion)
		if self.head == None:
			node.next = node
			node.prev = node
			self.head = node
			self.size += 1
		else:
			if self.buscar(cancion) == None:
				self.head.prev.next = node
				node.prev = self.head.prev
				self.head.prev = node
				node.next = self.head
				self.size+=1

	def buscar(self,cancion):
		x = self.head
		for i in xrange(self.size):
			if x.cancion.esIgual(cancion) : return x
			x = x.next
		return None
	def eliminar(self,cancion):
		x = self.buscar(cancion)
		if x != None:
			x.prev.next = x.next
			x.next.prev = x.prev
			if x == self.head : self.head = x.next
			self.size-=1
	def comp(self,a,b,c):
		if c == 0:
			return a.cancion.esMenorTitulo(b.cancion)
		else:
			return a.cancion.esMenorArtista(b.cancion)

	def ordenarTitulo(self):
		self.head.prev.next = None
		self.head.prev = None
		self.head = self.mergesort(self.head,0)
		x = self.head
		while x!=None and x.next != None: 
			x = x.next
		self.head.prev = x
		x.next = self.head

	def ordenarArtista(self):
		self.head.prev.next = None
		self.head.prev = None
		self.head = self.mergesort(self.head,1)
		x = self.head
		while x!=None and x.next != None: 
			x = x.next
		self.head.prev = x
		x.next = self.head

	def mergesort(self,head,flag):
		if head == None or head.next == None:
			return head
		second = self.split(head)
		head = self.mergesort(head,flag)
		second = self.mergesort(second,flag)
		return self.merge(head,second,flag)

	def merge(self,head,second,flag):
		if head == None : return second
		if second == None : return head

		if self.comp(head,second,flag):
			head.next = self.merge(head.next,second,flag)
			head.next.prev = head
			head.prev = None
			return head
		else:
			second.next = self.merge(head,second.next,flag)
			second.next.prev = second
			second.prev = None
			return second

	def split(self,head):
		fast = head
		slow = head
		while fast.next != None and fast.next.next != None:
			fast = fast.next.next
			slow = slow.next
		tmp = slow.next
		slow.next = None
		return tmp

	def mostrar(self):
		x = self.head
		for i in range(self.size):
			print x.cancion.titulo,x.cancion.artista,x.cancion.genero
			x = x.next
#t = listaReproduccion()
#t.agregar_final(Cancion("abgc","hhhbb","kkkk","jjjj"))
#t.agregar_final(Cancion("gfhg","ssddbb","kkkk","jjjj"))
#t.agregar_final(Cancion("abcc","qqqqq","kkkk","jjjj"))
#t.agregar_final(Cancion("qwe","dd","kkkk","jjjj"))
#t.mostrar()
#t.ordenarTitulo()
#print
#t.mostrar()
#print
#t.ordenarArtista()
#t.mostrar()
