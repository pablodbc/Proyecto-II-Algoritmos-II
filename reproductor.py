# archivo principal., el main
from rep import *
from cliente import *
from interfaz import *

if __name__ == '__main__':
	if len(argv) != 2:
		print "FATAL ERROR:"
		print "> python reproductor.py <archivo>"
		exit()

	app = QApplication([])
	app.setApplicationName("JP Music Player")
	JPMP = Cliente(argv[1])
	JPMP.ventana.show()
	exit(app.exec_())