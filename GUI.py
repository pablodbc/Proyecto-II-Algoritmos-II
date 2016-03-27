import os
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.phonon import *

class Reproductor(QWidget):
	def __init__(self):
		super(Reproductor, self).__init__()
		self.setWindowTitle(self.tr("Jose te odio"))
		self.setMinimumSize(800,600)
		vbox = QVBoxLayout(self)
		self.re = Phonon.createPlayer(Phonon.MusicCategory)
		self.slide = Phonon.SeekSlider(self.re,self)
		vbox.addWidget(self.slide)

		#Buttons
		self.play = QPushButton(
			self.style().standardIcon(QStyle.SP_MediaPlay)," ")
		self.pause = QPushButton(
			self.style().standardIcon(QStyle.SP_MediaPause)," ")
		self.stop = QPushButton(
			self.style().standardIcon(QStyle.SP_MediaStop)," ")
		self.select = QPushButton("...")
		self.name = QLabel("Jose te odio")

		hbox = QHBoxLayout()
		hbox.addWidget(self.play)
		hbox.addWidget(self.pause)
		hbox.addWidget(self.stop)
		hbox.addWidget(self.select)
		vbox.addLayout(hbox)
		vbox.addWidget(self.name)

		#Yo-Ho Yo-Ho
		self.connect(self.play, SIGNAL("clicked()"),self._play)
		self.connect(self.pause, SIGNAL("clicked()"),self._pause)
		self.connect(self.stop, SIGNAL("clicked()"),self._stop)
		self.connect(self.select, SIGNAL("clicked()"),self._select)

	def _play(self):
		self.re.play()
	def _pause(self):
		self.re.pause()
	def _stop(self):
		self.re.stop()
	def _select(self):
		path = unicode(QFileDialog.getOpenFileName(self,"Song"))
		indice = path.rfind("/")
		self.re.setCurrentSource(Phonon.MediaSource(path))
		self.name.setText(path[indice+1 if indice >= 0 else 0:])
if __name__ == '__main__':
	app = QApplication([])
	w = Reproductor()
	w.show()
	sys.exit(app.exec_())