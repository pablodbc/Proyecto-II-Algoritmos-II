from reproductor import *
from PyQt4.QtCore import *
from sys import *

class Interfaz(QWidget):

	def __init__(self):
		super(Interfaz, self).__init__()
		self.setWindowTitle("BMPE")
		self.resize(600,600)
		self.reproductor = Reproductor()
		
		self.tituloCancionActual  = QLabel("algo aqui (o nada) al principio",self)
		self.artistaCancionActual = QLabel("algo aqui (o nada) al principio",self)

		self.pause      = QPushButton(self)
		self.play       = QPushButton(self)
		self.stop       = QPushButton(self)
		self.atras      = QPushButton(self)
		self.siguiente  = QPushButton(self)

		# No sombrear
		self.play.setFocusPolicy(Qt.NoFocus)
		self.pause.setFocusPolicy(Qt.NoFocus)
		self.stop.setFocusPolicy(Qt.NoFocus)
		self.atras.setFocusPolicy(Qt.NoFocus)
		self.siguiente.setFocusPolicy(Qt.NoFocus)

		# Posicion de elementos de GUI
		self.tituloCancionActual.move(10,10)
		self.artistaCancionActual.move(10,30)
		self.play.move(200,250)
		self.stop.move(300,250)
		self.pause.move(400,250)
		self.atras.move(100,250)
		self.siguiente.move(500,250)
		
		# que hacer al hacer click
		self.connect(self.play,      SIGNAL("clicked()"),self._play)
		self.connect(self.pause,     SIGNAL("clicked()"),self._pause)
		self.connect(self.stop,      SIGNAL("clicked()"),self._stop)
		self.connect(self.atras,     SIGNAL("clicked()"),self._atras)
		self.connect(self.siguiente, SIGNAL("clicked()"),self._siguiente)

		# Diseno de botones
		self.play.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/play.png); background-position: center; background-repeat: no-repeat")
		self.pause.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/pause.png); background-position: center; background-repeat: no-repeat")
		self.stop.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/stop.png); background-position: center; background-repeat: no-repeat")
		self.atras.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/atras.png); background-position: center; background-repeat: no-repeat")
		self.siguiente.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/siguiente.png); background-position: center; background-repeat: no-repeat")

	def _play(self):
		self.reproductor.Play()
		self.cambiarDatosCancionActual()
	def _pause(self):
		self.reproductor.Pause()
	def _stop(self):
		self.reproductor.Stop()
	def _atras(self):
		self.reproductor.Atras()
		self.cambiarDatosCancionActual()
	def _siguiente(self):
		self.reproductor.Siguiente()
		self.cambiarDatosCancionActual()

	def cambiarDatosCancionActual(self):
		self.tituloCancionActual.setText(self.reproductor.cancionActual.cancion.titulo)
		self.artistaCancionActual.setText(self.reproductor.cancionActual.cancion.artista)

if __name__ == '__main__':
	app = QApplication([])
	app.setApplicationName("hola")
	ventana = Interfaz()
	l = listaReproduccion()
	l.agregar(Cancion("c","a","a","a.mp3"))
	l.agregar(Cancion("b","b","a","b.mp3"))
	l.agregar(Cancion("a","c","a","a.mp3"))
	ventana.reproductor.setLista(l)
	ventana.show()
	app.exec_()


		