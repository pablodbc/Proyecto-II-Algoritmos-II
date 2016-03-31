from indice import *
from rep import *
from listaReproduccion import *

def initCliente(nombreArchivo):
	mensajeBienvenida()
	estadoConsola(False)
	reproductor = Reproductor()
	indiceGenero  = Indice()
	indiceArtista = Indice()
	reproductor.lista = listaReproduccion()
	listaOriginal = listaReproduccion()
	importar(reproductor,indiceGenero,indiceArtista,nombreArchivo,1)
	x = reproductor.lista.head
	for i in range(reproductor.lista.size):
		listaOriginal.agregar_final(x.cancion)
		x = x.next
	return reproductor, indiceGenero, indiceArtista, listaOriginal

def mensajeBienvenida():
	print "Bienvenido a JP Music Player :)"
	
def restaurarLista(reproductor,listaOriginal):
	reproductor.lista = listaReproduccion()
	x = listaOriginal.head
	for i in range(listaOriginal.size):
		reproductor.lista.agregar_final(x.cancion)
		x = x.next
	reproductor.cancionActual = listaOriginal.head

def eliminarCancion(reproductor,titulo,artista):
	node = Cancion(titulo,artista,None,None)
	reproductor.lista.eliminar(node)
	if reproductor.cancionActual.cancion.titulo.lower() == titulo.lower() and reproductor.cancionActual.cancion.artista.lower() == artista.lower():
		reproductor.media.setCurrentSource(Phonon.MediaSource(reproductor.cancionActual.next.cancion.archivo))
	reproductor.cancionActual = reproductor.lista.head

def ordenarPorTitulo(reproductor):
	reproductor.lista.ordenarTitulo()
	reproductor.cancionActual = reproductor.lista.head

def ordenarPorArtista(reproductor):
	reproductor.lista.ordenarArtista()
	reproductor.cancionActual = reproductor.lista.head

def buscarGenero(indiceGenero,reproductor,genero):
	x = indiceGenero.search(genero)
	if x is not None:
		reproductor.setLista(x)
	else:
		print "No se encontraron resultados."

def buscarArtista(indiceArtista,reproductor,artista):
	x = indiceArtista.search(artista)
	if x is not None:
		reproductor.setLista(x)
	else:
		print "No se encontraron resultados"

def importar(reproductor,indiceGenero,indiceArtista,nombreArchivo,flag = 0):
	lista = listaReproduccion()
	try:
		f = open(nombreArchivo,"r")
	except:
		print "El archivo no existe"
		exit()
	for linea in f:
		datosCancion = linea.strip("\n").split("\t")
		if len(datosCancion) != 4:
			print "ERROR: Formato de archivo invalido"
			print "<titulo> [TAB] <artista> [TAB] <genero> [TAB] <ruta archivo de audio>"
			exit()
		ruta = datosCancion[3].split(".")
		if len(ruta) != 2:
			print "ERROR: Especifique extension de archivo de audio"
			exit()
		elif ruta[1] != "mp3" and ruta[1] != "AVI" and ruta[1] != "OGG":
			print "ERROR: Extension de archivo de audio invalido"
			exit()
		else:
			cancion = Cancion(datosCancion[0],datosCancion[1],datosCancion[2],datosCancion[3])
			lista.agregar(cancion)
	f.close()

	x = lista.head
	for i in range(lista.size):
		reproductor.lista.agregar_final(x.cancion)
		indiceGenero.insertGenero(x.cancion)
		indiceArtista.insertArtista(x.cancion)
		x = x.next
	if flag == 1:
		reproductor.setLista(reproductor.lista)

def estadoConsola(activo):
	if activo:
		print "############ CONSOLA ACTIVA ############"
	else:
		print "############ CONSOLA INACTIVA ############"
		print "Presione ENTER sobre ventana del reproductor para activar"


def advertenciaConsola():
	print "Se esta reproduciendo musica. No puede utilizar la consola"

def menuConsola(ventana):
	reproductor = ventana.reproductor
	indiceGenero = ventana.indiceGenero
	indiceArtista = ventana.indiceArtista
	listaOriginal = ventana.listaOriginal
	print "Seleccione una de las siguientes opciones:"
	print"""
		1. Importar una lista de canciones
		2. Eliminar una cancion de la lista actual
		3. Ordenar Las canciones de la lista por titulo
		4. Ordenar las canciones de la lista por artista
		5. Buscar todas las canciones de un artista
		6. Buscar todas las canciones de un genero
		7. Restaurar lista original
		8. Volver al reproductor
		9. Salir 
		"""

	while True:
		try:
			print "Opcion: ",
			opcion = int(input())
			assert(opcion >=1 and opcion <= 9)
			break
		except:
			print "Opcion invalida, vuelva a intentarlo"

	if opcion == 1:
		print "Introduzca la ruta del archivo: ",
		while True:
			try:
				archivo = raw_input()
				importar(reproductor,indiceGenero,indiceArtista,archivo)
				ventana.cargarListaReproduccion(reproductor.lista)
				break
			except:
				print "Introduzca un archivo valido: ",
	
	if opcion == 2:
		print "Introduzca el titulo de la cancion: ",
		titulo = raw_input()
		print "Introduzca el artista de la cancion: ",
		artista = raw_input()
		eliminarCancion(reproductor,titulo,artista)
		ventana.cargarListaReproduccion(reproductor.lista)
	
	if opcion == 3:
		ordenarPorTitulo(reproductor)
		ventana.cargarListaReproduccion(reproductor.lista)
		reproductor.media.setCurrentSource(Phonon.MediaSource(reproductor.cancionActual.cancion.archivo))
	
	if opcion == 4:
		ordenarPorArtista(reproductor)
		ventana.cargarListaReproduccion(reproductor.lista)
		reproductor.media.setCurrentSource(Phonon.MediaSource(reproductor.cancionActual.cancion.archivo))
	
	if opcion == 5:
		print "Ingrese el nombre del artista: ",
		artista = raw_input()
		buscarArtista(indiceArtista,reproductor,artista.lower())
		ventana.cargarListaReproduccion(reproductor.lista)
	
	if opcion == 6:
		print "Ingrese el nombre del genero: ",
		genero = raw_input()
		buscarGenero(indiceGenero,reproductor,genero)
		ventana.cargarListaReproduccion(reproductor.lista)
	
	if opcion == 7:
		restaurarLista(reproductor,listaOriginal)
		ventana.cargarListaReproduccion(reproductor.lista)
		reproductor.media.setCurrentSource(Phonon.MediaSource(reproductor.cancionActual.cancion.archivo))
	
	if opcion == 8:
		pass

	if opcion == 9 : exit()	