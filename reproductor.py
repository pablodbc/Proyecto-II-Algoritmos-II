from PyQt4.QtGui import *
from PyQt4.phonon import *
from listaReproduccion import *
class Reproductor:
	def __init__(self):
		self.media = Phonon.MediaObject()
		self.lista = None
		self.cancionActual = None
		self.audioOutput = Phonon.AudioOutput(Phonon.MusicCategory)
		Phonon.createPath(self.media, self.audioOutput)
	def Play(self):
		self.media.play()
	def Pause(self):
		self.media.pause()
	def Stop(self):
		self.media.stop()
	def Siguiente(self):
		self.Stop()
		self.cancionActual = self.cancionActual.next
		self.media.setCurrentSource(Phonon.MediaSource(self.cancionActual.cancion.archivo))
		self.Play()
	def Atras(self):
		self.Stop()
		self.cancionActual = self.cancionActual.prev
		self.media.setCurrentSource(Phonon.MediaSource(self.cancionActual.cancion.archivo))
		self.Play()
	def setLista(self,lista):
		self.lista = lista
		self.cancionActual = self.lista.head
		self.media.setCurrentSource(Phonon.MediaSource(self.cancionActual.cancion.archivo))


#app = QApplication([])
#app.setApplicationName("BMPE")
#t = listaReproduccion()
##t.agregar(Cancion("a","c","a","b.mp3"))
##t.agregar(Cancion("b","b","b","a.mp3"))
##t.agregar(Cancion("c","a","c","b.mp3"))
#t.agregar(Cancion("d","d","c","d.mp3"))
#a = Reproductor()
#a.setLista(t)
##print a.media.queue
#a.Play()
##print a.media.currentSource
#while True:
#	pass