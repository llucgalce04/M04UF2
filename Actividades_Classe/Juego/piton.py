#!/usr/bin/python3 

import xmltodict
import random


enemy_files= ["enemy1.xml", "enemy2.xml", "enemy3.xml"]
random_file= random.choice(enemy_files)

xml_file_enemy= open(random_file, "r")

diccionario = xmltodict.parse(xml_file_enemy.read())

enemy1= diccionario["enemys"]["enemy"]
("Nombre: "+enemy1["name"])
("Daño: "+enemy1["damage"])
("Vida: "+enemy1["health"])
("Nivel: "+enemy1["level"])


vida= int(30)

vida_enemy1= int((enemy1["health"]))
daño_enemy= int((enemy1["damage"]))
nombre_enemy1= str((enemy1["name"]))

while True:

	teclado = input ("Introduce que quieres hacer, para ver tu vida escribe: vida, para atacar escirbe: ataca, para ver las stats de los enemigos escribe: stats y para salir escribe: salir\n")

	if teclado == "vida":
		
		print ("Tu vida es: " + str(vida))
	
	elif teclado == "ataca":

		daño= int(random.randrange(5))
		daño_enemy1= int(random.randrange(daño_enemy))

		vida_enemy1= vida_enemy1 - daño
		vida= vida - daño_enemy1
		print ("Le has sacado " + str(daño) + " de vida, ahora el enemigo tiene: "+ str(vida_enemy1) + " de vida\n")
		print (str(nombre_enemy1) + " tambien te ha atacado, te ha sacado "+ str(daño_enemy1) + " de vida, ahora tienes " + str(vida) + " de vida\n")
	
	elif teclado == "stats":
		
		enemy1= diccionario["enemys"]["enemy"]
		
		print("Nombre: "+enemy1["name"])
		
		print("Daño: "+enemy1["damage"])
		
		print("Vida: "+enemy1["health"])
		
		print("Nivel: "+enemy1["level"])

	elif teclado == "salir":
		break
	
	if vida <= 0:
		print("Mala suerte papu")
		break

	elif vida_enemy1 <= 0:
		print("Acabaste con el")
		break
