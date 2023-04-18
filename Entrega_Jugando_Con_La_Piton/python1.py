#!/usr/bin/python3 

import xmltodict
import random


xml_file_enemy1= open("enemy1.xml", "r")

diccionario = xmltodict.parse(xml_file_enemy1.read())



enemy1= diccionario["enemys"]["enemy"]
("Nombre: "+enemy1["name"])
("Daño: "+enemy1["damage"])
("Vida: "+enemy1["health"])
("Nivel: "+enemy1["level"])




while True:
	
	vida= int(30)

	vida_enemy1= int((enemy1["health"]))

	zero= int(0)

	teclado = input ("Introduce que quieres hacer, para ver tu vida escribe: vida, para atacar escirbe: ataca y para salir escribe: salir\n")

	if teclado == "vida":
		
		print ("Tu vida es: " + str(vida))
	
	elif teclado == "ataca":

		daño= int(random.randrange(5))
		daño_enemy1= int(random.randrange(2))

		vida_enemy1= vida_enemy1 - daño
		vida= vida - daño_enemy1
		print ("Le has sacado " + str(daño) + " de vida, ahora el enemigo tiene: "+ str(vida_enemy1) + " de vida")
		print ("La piton tambien te ha atacado, te ha sacado "+ str(daño_enemy1) + " de vida, ahora tienes " + str(vida) + " de vida")
	
	elif teclado == "stats":
		
		enemy1= diccionario["enemys"]["enemy"]
		
		print("Nombre: "+enemy1["name"])
		
		print("Daño: "+enemy1["damage"])
		
		print("Vida: "+enemy1["health"])
		
		print("Nivel: "+enemy1["level"])

	elif teclado == "salir":
		break
	
	elif vida == 0:
		print("Mala suerte papu")
		break

	elif vida_enemy1 == 0:
		print("Acabaste con ell")
		break
		

