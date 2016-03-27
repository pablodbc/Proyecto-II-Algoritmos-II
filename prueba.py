def importar(nombreArchivo):
	with open(nombreArchivo, "r") as f:
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


importar("canciiones.txt")