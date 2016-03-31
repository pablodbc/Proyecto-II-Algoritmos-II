from rep import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sys import *
from cliente import *

class Interfaz(QWidget):

	def __init__(self,reproductor,indiceArtista,indiceGenero,listaOriginal):
		super(Interfaz, self).__init__()
		self.setWindowTitle("JP Music Player")
		self.setFixedSize(400,600)
		self.reproductor = reproductor
		self.indiceArtista = indiceArtista
		slef.indiceGenero = indiceGenero
		self.listaOriginal = listaOriginal
		palette = QPalette()
		palette.setBrush(QPalette.Background,QBrush(QPixmap("imagenes/fondo.jpg")))
		self.setPalette(palette)
		self.setWindowIcon(QIcon('imagenes/icono.jpg'))
		QFontDatabase.addApplicationFont("font/TTF files/Track.ttf")
		self.playClick = False
		
		# Cuadros de texto
		self.sonando = QLabel("Not playing   ",self)
		self.tituloCancionActual = QLabel("",self)
		self.artistaCancionActual = QLabel("",self)
		self.duracionCancionActual = QLabel("",self)
		self.tiempoTranscurridoCancionActual = QLabel("",self)
		self.barra = QLabel("",self)
		self.sonando.setStyleSheet("font-style: oblique; font-size: 10pt; font-family: Track; color:#2f4f4f;")
		self.tituloCancionActual.setStyleSheet("font-style: strong; font-size: 14pt; font-family: Track; color:#2f2f2f; margin:10px 10px 0px 10px;")
		self.artistaCancionActual.setStyleSheet("font-size: 11pt; font-family: Track; color:#2f3f3f; margin:0px 10px 10px 10px;")
		self.duracionCancionActual.setStyleSheet("font-size: 10pt; font-family: Track; color:#2f4f4f;")
		self.tiempoTranscurridoCancionActual.setStyleSheet("font-size: 10pt; font-family: Track; color:#2f4f4f;")

		# Botones
		self.pause      = QPushButton(" ",self)
		self.play       = QPushButton(" ",self)
		self.stop       = QPushButton(" ",self)
		self.atras      = QPushButton(" ",self)
		self.siguiente  = QPushButton(" ",self)

		# No sombrear
		self.play.setFocusPolicy(Qt.NoFocus)
		self.pause.setFocusPolicy(Qt.NoFocus)
		self.stop.setFocusPolicy(Qt.NoFocus)
		self.atras.setFocusPolicy(Qt.NoFocus)
		self.siguiente.setFocusPolicy(Qt.NoFocus)
		
		# que hacer al hacer click
		self.connect(self.play,      SIGNAL("clicked()"),self._play)
		self.connect(self.pause,     SIGNAL("clicked()"),self._pause)
		self.connect(self.stop,      SIGNAL("clicked()"),self._stop)
		self.connect(self.atras,     SIGNAL("clicked()"),self._atras)
		self.connect(self.siguiente, SIGNAL("clicked()"),self._siguiente)

		# Diseno de botones
		self.play.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/play.svg); background-position: center; background-repeat: no-repeat")
		self.pause.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/pause.svg); background-position: center; background-repeat: no-repeat")
		self.stop.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/stop.svg); background-position: center; background-repeat: no-repeat")
		self.atras.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/previous.svg); background-position: center; background-repeat: no-repeat")
		self.siguiente.setStyleSheet("border: 0px; width: 50; height: 50; background-image: url(imagenes/next.svg); background-position: center; background-repeat: no-repeat")

		# Bloque de barra de botones
		self.barraDeBotones = QHBoxLayout()
		self.barraDeBotones.addWidget(self.atras)
		self.barraDeBotones.addWidget(self.stop)
		self.barraDeBotones.addWidget(self.play)
		self.barraDeBotones.addWidget(self.pause)
		self.barraDeBotones.addWidget(self.siguiente)

		# Bloque de tabla de canciones
		self.tablaCanciones = QTableWidget()
		self.tablaCanciones.setColumnCount(1)
		self.tablaCanciones.verticalHeader().setVisible(False)
		self.tablaCanciones.horizontalHeader().setVisible(False)
		self.tablaCanciones.setShowGrid(False)
		self.tablaCanciones.setFocusPolicy(Qt.NoFocus)
		self.tablaCanciones.setEditTriggers(QAbstractItemView.NoEditTriggers)
		self.tablaCanciones.horizontalHeader().setResizeMode(QHeaderView.Stretch)
		self.tablaCanciones.setStyleSheet("background-color: transparent;");

		# Bloque de cancion actual
		self.datos = QHBoxLayout()
		self.bloqueSonando = QHBoxLayout()
		self.tiempos = QHBoxLayout()
		self.tiempos.addStretch(1)
		self.tiempos.addWidget(self.tiempoTranscurridoCancionActual)
		self.tiempos.addWidget(self.barra)
		self.tiempos.addWidget(self.duracionCancionActual)
		self.tiempos.insertSpacing(3,10)
		self.tiempos.insertSpacing(2,10)
		self.aux  = QVBoxLayout()
		self.aux2 = QHBoxLayout()
		self.aux2.addStretch(1)
		self.aux2.addWidget(self.sonando)
		self.aux.addLayout(self.aux2)
		self.aux.addLayout(self.tiempos)
		self.bloqueSonando.addStretch(1)
		self.bloqueSonando.addLayout(self.aux)
		self.datosCancion = QVBoxLayout()
		self.datosCancion.addWidget(self.tituloCancionActual)
		self.datosCancion.addWidget(self.artistaCancionActual)
		self.datosCancion.insertSpacing(1,3)
		self.datos.addLayout(self.datosCancion)
		self.datos.addLayout(self.bloqueSonando)

		# Barra cancion
		self.barraCancion = Phonon.SeekSlider(self.reproductor.media)
		self.barraCancion.setStyleSheet("""
		QSlider::groove:horizontal { background: transparent; height: 20px;} 
		QSlider::sub-page:horizontal { background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #66e, stop: 1 #bbf); background: qlineargradient(x1: 0, y1: 0.2, x2: 1, y2: 1, stop: 0 #bbf, stop: 1 #55f); height: 20px;}
		QSlider::add-page:horizontal { background: transparent; height: 20px;}
		QSlider::handle:horizontal {background: transparent; border: 0px; width: 0px; margin-top: 0px; margin-bottom: 0px; border-radius: 0px;}""")

		# Tiempo de actualizacion
		self.reproductor.media.setTickInterval(1000)
		self.reproductor.media.tick.connect(self.actualizar)

		# Layout principal
		self.layoutPrincipal = QVBoxLayout()
		self.layoutPrincipal.addLayout(self.datos)
		self.layoutPrincipal.addWidget(self.tablaCanciones)
		self.layoutPrincipal.addWidget(self.barraCancion)
		self.layoutPrincipal.addLayout(self.barraDeBotones)
		self.setLayout(self.layoutPrincipal)
		self.layoutPrincipal.insertSpacing(0,10)
		self.layoutPrincipal.insertSpacing(2,10)

	def _play(self):
		self.reproductor.Play()
		self.cambiarDatosCancionActual()
		self.sonando.setText("Now playing   ")
		self.playClick = True
	def _pause(self):
		self.reproductor.Pause()
		self.sonando.setText("Paused    ")
		self.playClick = False
	def _stop(self):
		self.reproductor.Stop()
	def _atras(self):
		self.reproductor.Atras()
		self.cambiarDatosCancionActual()
		self.sonando.setText("Now playing   ")
	def _siguiente(self):
		self.reproductor.Siguiente()
		self.cambiarDatosCancionActual()
		self.sonando.setText("Now playing   ")		
	def cambiarDatosCancionActual(self):
		self.tituloCancionActual.setText(self.reproductor.cancionActual.cancion.titulo)
		self.artistaCancionActual.setText(self.reproductor.cancionActual.cancion.artista)

	def cargarListaReproduccion(self,lista):
		self.tablaCanciones.setRowCount(lista.size)
		node = lista.head
		for i in range(lista.size):
			item = QLabel("<br><b>"+str(i+1)+". "+node.cancion.titulo+"</b><br><small><span style='margin:10px 5px 15px 20px;'>"+node.cancion.artista+"<br>"+node.cancion.genero+"</span></small><br>")
			item.setContentsMargins(15,0,15,0)
			item.setStyleSheet('font-size: 10pt; font-family: Track; color:#2f4f4f;')
			self.tablaCanciones.setCellWidget(i,0,item)
			node = node.next
		self.tablaCanciones.resizeRowsToContents()

	def actualizar(self, time):
		tiempoTranscurrido = self.reproductor.media.currentTime()
		tiempo1 = QTime(0, (tiempoTranscurrido / 60000) % 60, (tiempoTranscurrido / 1000) % 60)
		tiempo2 = QTime(0, (self.reproductor.media.totalTime() / 60000) % 60, (self.reproductor.media.totalTime() / 1000) % 60)
		self.tiempoTranscurridoCancionActual.setText(tiempo1.toString('mm:ss'))
		self.duracionCancionActual.setText(tiempo2.toString('mm:ss'))
		self.barra.setText("/")

	def seEstaReproduciendoMusica(self):
		return self.playClick

	def keyPressEvent(self, event):
		if event.key() == Qt.Key_Return:
			if not self.seEstaReproduciendoMusica():
				while True:
					print "i"

#if __name__ == '__main__':
#	app = QApplication([])
#	app.setApplicationName("JP Music Player")
#	QFontDatabase.addApplicationFont("font/TTF files/Track.ttf")
#	ventana = Interfaz()
#	l = listaReproduccion()
#	l.agregar(Cancion("melancholy hill","gorillaz","algo","gorillaz.mp3"))
#	l.agregar(Cancion("algo","b","a","b.mp3"))
#	l.agregar(Cancion("vcr","xx","indie","vcr.mp3"))
#	l.agregar(Cancion("hill","gorillaz","algo","gorillaz.mp3"))
#	l.agregar(Cancion("algo adicional","b","a","b.mp3"))
#	l.agregar(Cancion("vcr otro mas","xx","indie","vcr.mp3"))
#	l.agregar(Cancion("melancholy hill bla","gorillazasdasdasdasdasdasdasd1","algo","gorillaz.mp3"))
#	l.agregar(Cancion("abcabc","b","a","b.mp3"))
#	l.agregar(Cancion("hola a todos","xx","indie","vcr.mp3"))
#	l.agregar(Cancion("hill hill","gorillaz","algo","gorillaz.mp3"))
#	l.agregar(Cancion("algo algo","b","a","b.mp3"))
#	l.agregar(Cancion("vcr vcr","xx","indie","vcr.mp3"))
#	ventana.cargarListaReproduccion(l)
#	ventana.show()
#	app.exec_()


		