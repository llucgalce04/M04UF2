#!/usr/bin/python3

import xmltodict
import pprint

xml_file = open("coc.xml", "r")

diccionario = xmltodict.parse(xml_file.read())

#pp = pprint.PrettyPrinter(indent=2)

#pp.pprint(diccionario)

numero = int(input("Introduce un numero del 1 al 3: "))-1
#arrays, diccionarios --> nombre generuco tupla
character = diccionario["characters"]["character"][numero]
print("Nombre: "+character["name"])
print("Daño: "+character["damage"])
print("Vida: "+character["health"])
print("Rareza: "+character["rare"])
