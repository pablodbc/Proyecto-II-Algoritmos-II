class Cancion:
	def __init__(self,titulo,artista,genero,archivo):
		self.titulo = titulo
		self.artista = artista
		self.genero = genero
		self.archivo = archivo
	def esIgual(self,cancion):
		return self.titulo.lower() == cancion.titulo.lower() and self.artista.lower() == cancion.artista.lower()
	def esMenorArtista(self,cancion):
		return self.artista.lower() < cancion.artista.lower() or(self.artista.lower() == cancion.artista.lower()  and self.titulo.lower() <= cancion.titulo.lower())
	def esMenorTitulo(self,cancion):
		return self.titulo.lower() < cancion.titulo.lower() or(self.titulo.lower() == cancion.titulo.lower()  and self.artista.lower() <= cancion.artista.lower())
	def getTitulo(self):
		return self.titulo
	def getGenero(self):
		return self.genero
	def getArtista(self):
		return self.artista
	def getArchivo(self):
		return self.archivo