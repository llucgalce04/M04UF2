#!/usr/bin/python3

archivo = open("numerito.txt")

linea = archivo.readline()

lista = linea.split(";")

print(lista[2])

archivo.close()


archivo = open("textitos.txt", "w")

archivo.write("ola que ase")

archivo.close()
