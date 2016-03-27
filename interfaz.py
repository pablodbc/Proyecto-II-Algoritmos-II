from reproductor import *
from PyQt4.QtCore import *
from sys import *

class Interfaz(QWidget):

	def __init__(self):
		
		super(Interfaz, self).__init__()
		self.setWindowTitle("Jose te odio")
		self.resize(800,400)
		self.reproductor = Reproductor()
		
		self.play       = QPushButton(" ",self)
		self.pause      = QPushButton(self.style().standardIcon(QStyle.SP_MediaPause)," ",self)
		self.stop       = QPushButton(self.style().standardIcon(QStyle.SP_MediaStop)," ",self)
		self.atras      = QPushButton(" ",self)
		self.siguiente  = QPushButton(" ",self)

		self.play.setFocusPolicy(Qt.NoFocus)

		self.play.move(200,250)
		self.stop.move(300,250)
		self.pause.move(400,250)
		self.atras.move(100,250)
		self.siguiente.move(500,250)
		
		self.connect(self.play,      SIGNAL("clicked()"),self._play)
		self.connect(self.pause,     SIGNAL("clicked()"),self._pause)
		self.connect(self.stop,      SIGNAL("clicked()"),self._stop)
		self.connect(self.atras,     SIGNAL("clicked()"),self._atras)
		self.connect(self.siguiente, SIGNAL("clicked()"),self._siguiente)
		self.name = QLabel("Jose te odio")

		#self.play.setIcon(QIcon("caballo.jpg"))
		#self.play.setIconSize(QSize(100,100))
		self.play.setStyleSheet("border: 0px; width: 100; height: 50; background-image: url(play.png); background-position: center; background-repeat: no-repeat")
		self.pause.setStyleSheet("width: 100; height: 50")


	def _play(self):
		self.reproductor.Play()
	def _pause(self):
		self.reproductor.Pause()
	def _stop(self):
		self.reproductor.Stop()
	def _atras(self):
		self.reproductor.Atras()
	def _siguiente(self):
		self.reproductor.Siguiente()


if __name__ == '__main__':
	app = QApplication([])
	app.setApplicationName("hola")
	w = Interfaz()
	#w.setFocusPolicy(Qt.NoFocus)
	l = listaReproduccion()
	l.agregar(Cancion("a","a","a","gorillaz.mp3"))
	l.agregar(Cancion("a","b","a","vcr.mp3"))
	l.agregar(Cancion("a","c","a","Dead Inside.mp3"))
	l.agregar(Cancion("a","d","a","pompeii.mp3"))
	w.reproductor.setLista(l)
	w.show()
	app.exec_()


		