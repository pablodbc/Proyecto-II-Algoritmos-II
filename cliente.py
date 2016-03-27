from interfaz import *
from indice import *
from reproductor import *

class Cliente():
	def __init__(self,nombreArchivo):
		self.reproductor = Reproductor()
		self.indiceGenero  = Indice()
		self.indiceArtista = Indice()
		self.reproductor.lista = listaReproduccion()
		self.listaOriginal = listaReproduccion()
		self.importar(nombreArchivo,1)
		x = self.reproductor.lista.head
		for i in range(self.reproductor.lista.size):
			self.listaOriginal.agregar_final(x.cancion)
			x = x.next
	
	def restaurarLista(self):
		self.reproductor.lista = listaReproduccion()
		x = self.listaOriginal.head
		for i in range(self.listaOriginal.size):
			self.reproductor.lista.agregar_final(x.cancion)
			x = x.next

	def eliminarCancion(self,titulo,artista):
		node = Cancion(titulo,artista,None,None)
		self.reproductor.lista.eliminar(node)

	def ordenarPorTitulo(self):
		self.reproductor.lista.ordenarTitulo()

	def ordenarPorArtista(self):
		self.reproductor.lista.ordenarArtista()

	def buscarGenero(self,genero):
		x = self.indiceGenero.search(genero)
		if x is not None:
			self.reproductor.setLista(x)
		else:
			print "No se encontraron resultados."

	def buscarArtista(self,artista):
		x = self.indiceArtista.search(artista)
		if x is not None:
			self.reproductor.setLista(x)
		else:
			print "No se encontraron resultados"

	def importar(self,nombreArchivo,flag = 0):
		lista = listaReproduccion()
		try:
			f = open(nombreArchivo,"r")
		except:
			print "El archivo no existe"
			exit()
		for linea in f:
			datosCancion = linea[:-1].split("\t")
			if len(datosCancion) != 4:
				print "ERROR: Formato de archivo invalido"
				print "<titulo> [TAB] <artista> [TAB] <genero> [TAB] <ruta archivo de audio>"
				exit()
			ruta = datosCancion[3].split(".")
			if len(ruta) != 2:
				print "ERROR: Especifique extension de archivo de audio"
				exit()
			elif ruta[1] != "mp3" and ruta[1] != "AVI" and ruta[1] != "OGG":
				print "ERROR: Archivo de audio invalido"
				exit()
			else:
				cancion = Cancion(datosCancion[0],datosCancion[1],datosCancion[2],datosCancion[3])
				lista.agregar(cancion)
		f.close()
	
		x = lista.head
		for i in range(lista.size):
			self.reproductor.lista.agregar_final(x.cancion)
			self.indiceGenero.insertGenero(x.cancion)
			self.indiceArtista.insertArtista(x.cancion)
			x = x.next
		if flag == 1:
			self.reproductor.setLista(self.reproductor.lista)

if __name__ == '__main__':
	if len(argv) != 2:
		print "FATAL ERROR:"
		print "> python reproductor.py <archivo>"
		exit()
	app = QApplication([])
	app.setApplicationName("BMPE")	
	BMPE = Cliente(argv[1])
	flag = True
	print "Bienvenido a BMPE :)"
	while True:
		print "Seleccione una de las siguientes opciones:"
		print"""
		1. Importar una lista de canciones
		2. Eliminar una cancion de la lista actual
		3. Ordenar Las canciones de la lista por titulo
		4. Ordenar las canciones de la lista por artista
		5. Buscar todas las canciones de un artista
		6. Buscar todas las canciones de un genero
		7. Restaurar lista anterior
		8. Salir 
		"""

		while True:
			try:
				opcion = int(input())
				assert(opcion >=1 and opcion <= 9)
				break
			except:
				print "Opcion invalida, vuelva a intentarlo"
		
		if opcion == 8 : exit()

		if opcion == 1:
			print "Introduzca la ruta del archivo: ",
			while True:
				try:
					archivo = raw_input()
					BMPE.importar(archivo)
					break
				except:
					print "Introduzca un archivo valido: ",
		
		if opcion == 9:
			BMPE.reproductor.lista.mostrar()
			print BMPE.indiceArtista.size
			print BMPE.indiceGenero.size

		if opcion == 2:
			print "Introduzca el titulo de la cancion: ",
			titulo = raw_input()
			print "Introduzca el artista de la cancion: ",
			artista = raw_input()
			BMPE.eliminarCancion(titulo,artista)

		if opcion == 3:
			BMPE.ordenarPorTitulo()

		if opcion == 4:
			BMPE.ordenarPorArtista()

		if opcion == 5:
			print "Ingrese el nombre del artista: ",
			artista = raw_input()
			BMPE.buscarArtista(artista.lower())

		if opcion == 6:
			print "Ingrese el nombre del genero: ",
			genero = raw_input()
			BMPE.buscarGenero(genero)

		if opcion == 7:
			BMPE.restaurarLista()