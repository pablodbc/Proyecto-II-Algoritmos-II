class Cancion:
	def __init__(self,titulo,artista,genero,file=None):
		self.titulo = titulo
		self.artista = artista
		self.genero = genero
		self.file = file
	def esIgual(self,cancion):
		return self.titulo == cancion.titulo and self.artista == cancion.artista
	def esMenorArtista(self,cancion):
		return self.artista < cancion.artista or(self.artista == cancion.artista  and self.titulo <= cancion.titulo)
	def esMenorTitulo(self,cancion):
		return self.titulo < cancion.titulo or(self.titulo == cancion.titulo  and self.artista <= cancion.artista)
	def getTitulo(self):
		return self.titulo
	def getGenero(self):
		return self.genero
	def getArtista(self):
		return self.artista
	def getFile(self):
		return self.file
	def __str__(self):
		print self.titulo,self.artista,self.genero
		return ""

class nodoLista:
	def __init__(self,cancion):
		self.cancion = cancion
		self.prev = None
		self.next = None
	def __str__(self):
		print self.cancion.titulo,self.cancion.artista,self.cancion.genero
		return ""


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

	def buscar(self,cancion):
		x = self.head
		for i in xrange(self.size):
			if x.cancion.esIgual(cancion) : return x
			x = x.next
		return None
	def eliminar(self,cancion):
		x = self.buscar(cancion)
		if x != None:
			if x == self.head:
				x.prev.next = x.next
				x.next.prev = x.prev
				self.head = x.next
				self.size-=1
			else:
				x.prev.next = x.next
				x.next.prev = x.prev
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


t = listaReproduccion()
t.agregar(Cancion("r","a","a"))
t.mostrar()
print
t.ordenarArtista()
t.mostrar()

