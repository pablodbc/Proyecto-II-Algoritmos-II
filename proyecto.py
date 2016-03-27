from PyQt4.phonon import *
from listaReproduccion import *
class Reproductor:
	def __init__(self):
		self.media = Phonon.MediaObject()
		self.lista = None
		self.cancionActual = None
	def Play(self):
		self.media.play()
	def Pause(self):
		self.media.pause()
	def Stop(self):
		self.media.stop()
	def siguiente(self):
		self.Stop()
		self.cancionActual = self.cancionActual.next
		self.Play()
	def atras(self):
		self.Stop()
		self.cancionActual = self.cancionActual.prev
		self.Play()
	def setLista(self,lista):
		self.lista = lista
		self.cancionActual = self.lista.head
t = Reproductor()
