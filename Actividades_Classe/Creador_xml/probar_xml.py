#!/usr/bin/python3

# Solicitar al usuario que ingrese los valores para las variables
enemy_name = input("Ingresa el nombre del enemigo: ")
enemy_health = input("Ingresa la salud del enemigo: ")
enemy_damage = input("Ingresa el tipo de daño del enemigo: ")
enemy_level = input("Ingresa el nivel del enemigo: ")

# Crear la cadena de XML utilizando las variables ingresadas
xml_string = '<?xml version="1.0" encoding="UTF-8"?>\n\n<enemys>\n\n<enemy id_enemy= "1">\n    <name>{}</name>\n    <health>{}</health>\n    <damage>{}</damage>\n    <level>{}</level>\n    </enemy>\n</enemys>'.format(enemy_name, enemy_health, enemy_damage, enemy_level)

archivo = open("ejemplo.xml", "w")

archivo.write(xml_string)

archivo.close()

