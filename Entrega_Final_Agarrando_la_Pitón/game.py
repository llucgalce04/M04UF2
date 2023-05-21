#!/usr/bin/python3
# -*- coding: utf-8 -*-
import random
import xmltodict
import json
from enemy import Enemy
from player import Player
class Game:
    def __init__(self):
        self.enemies = []
        self.current_enemy = 0
        self.player = Player()

    def load_enemies_xml(self, filename):
        xml_file = open(filename)
        data = xml_file.read()
        xml_file.close()

        enemy_dict = xmltodict.parse(data)
        enemy_data = enemy_dict['enemies']['enemy']

        for enemy_info in enemy_data:
            name = enemy_info['name']
            damage_enemy = int(enemy_info['damage'])
            health = int(enemy_info['health'])
            description = enemy_info['description']

            enemy = Enemy(name, damage_enemy, health, description)
            self.enemies.append(enemy)

    def start(self):
        print("\nBienvenido a Agarrando la Pitón, un juego Python simple pero lleno de diversión y desafíos emocionantes. Prepárate para embarcarte en una aventura única en la que te enfrentarás a una serpiente gigante y pondrás a prueba tus habilidades.\n")

        print("\nA medida que avances en el juego, la dificultad aumentará y se te presentarán desafíos adicionales. ¿Tendrás lo necesario para superar los obstáculos y convertirte en el maestro de la jungla al atrapar a la tremenda pitón?\n")
        
        if self.current_enemy == 0:
            load_option = input("\n¿Quieres cargar una partida guardada? si o no \n")
            if load_option == "si":
                load_format = input("\n¿En qué formato está guardada la partida? xml o json) \n")
                load_filename = input("\nIntroduce el nombre del archivo de partida: \n")

                if load_format == "xml":
                    self.load_game_xml(load_filename)
                elif load_format == "json":
                    self.load_game_json(load_filename)
                else:
                    print("Arxivo no valido, iniciando una nueva partida")
        nombre = input("\n¿Cual es tu nombre?\n")

        enemy = self.enemies[self.current_enemy]  
        print("\nSTATS DE " +str(nombre))
        print("Salud: "+ str(self.player.health))
        print("Nivel: "+str (self.player.level))
        print("Experincia: "+str(self.player.experience))


        while True:

            enemy = self.enemies[self.current_enemy]
            print("\nNombre: " + str(enemy.name))
            print("\nDaño: " + str(enemy.damage_enemy))
            print("\nSalud: " + str(enemy.health))
            print("\nDescripción: " + str(enemy.description))
            option = input("\nQue quieres  hacer: ataca/guardar_partida/nada/salir\n")

            if option == "ataca":
                
                damage = random.randint(0, 20)
                enemy.health -= damage
                if enemy.health <= 0:
                    enemy.health = 0
                    print("\nLe has quitado "+str(damage) + " puntos de vida al enemigo\n")
                    print("\nAhora el enemigo tiene "+str(enemy.health) +" puntos de vida\n")
                    print("\nHas derrotado al enemigo. ¡Felicidades!\n")
                    self.current_enemy += 1

                else:
                    enemy_damage = random.randint(0, enemy.damage_enemy)
                    self.player.health -= enemy_damage
                    print("\nLe has quitado "+str(damage) + " puntos de vida al enemigo\n")
                    print("\nAhora el enemigo tiene "+str(enemy.health) +" puntos de vida\n")
                    print("\nEl te ha quitado "+str(enemy_damage)+" puntos de vida\n")
                    print("\nAhora tienes "+str(self.player.health)+" de vida\n")
                
            elif option == "guardar_partida":
                save_format = input("\n¿Como quieres guardar la partida? (xml/json) \n")
                save_filename = input("\nIntroduce el nombre del archivo de guardado: \n")

                if save_format == "xml":
                    self.save_game_xml(save_filename)
                elif save_format == "json":
                    self.save_game_json(save_filename)
                else:
                    print("Formato de guardado no válido.")
            elif option == "salir":
                break
            else:
                print("Que hace bobo, muevete o haz algo bitcho palo.")
            
            if self.current_enemy >= len(self.enemies):
                print("\n¡THE END! FELICIDADES HAS TERMINADO EL JUEGO ESPERO QUE TE HAYA GUSTADO\n")
                break
                


            if self.player.health <= 0:
                print("Has perdido papu, pero el KENEN PAPU TE REVIVIO pero como deves volver a empezar desde 0.")
                break

    def save_game_xml(self, filename):
        data = {
            'current_enemy': self.current_enemy,
            'enemy_health': self.enemies[self.current_enemy].health,
            'player_health': self.player.health,
            'player_experience': self.player.experience,
            'player_level': self.player.level,
        }

        xml_data = xmltodict.unparse({'game': data}, pretty=True)
        with open(filename, 'w') as xml_file:
            xml_file.write(xml_data)
        print("Partida guardada en XML correctamente.")

    def load_game_xml(self, filename):
        with open(filename, 'r') as xml_file:
            data = xml_file.read()
        game_data = xmltodict.parse(data)['game']
        
        self.current_enemy = int(game_data['current_enemy'])
        self.enemies[self.current_enemy].health = int(game_data['enemy_health'])
        self.player.health = int(game_data['player_health'])
        self.player.damage = 0
        self.player.level = int(game_data['player_level'])
        self.player.experience = int(game_data['player_experience'])
        print("Partida cargada correctamente.")

    def save_game_json(self, filename):
        data = {
            'current_enemy': self.current_enemy,
            'enemy_health': self.enemies[self.current_enemy].health,
            'player_health': self.player.health,
            'player_level': self.player.level,
            'player_experience': self.player.experience
        }
        
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print("Partida guardada en JSON correctamente.")

    def load_game_json(self, filename):
        with open(filename, 'r') as json_file:
            game_data = json.load(json_file)
        
        self.current_enemy = int(game_data['current_enemy'])
        self.enemies[self.current_enemy].health = int(game_data['enemy_health'])
        self.player.health = int(game_data['player_health'])
        self.player.level = int(game_data['player_level'])
        self.player.experience = int(game_data['player_experience'])
        print("Partida cargada desde JSON correctamente.")

#############################################################################################
#INSTANCIA EL JUEGO##########################################################################
#############################################################################################
juego = Game()
juego.load_enemies_xml("enemies.xml")
juego.start()

