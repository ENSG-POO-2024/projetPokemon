# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:54:33 2024

@author: Sebastien C.
"""

import sys
import csv
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel
from PyQt5.QtGui import QPixmap, QFont, QPainter, QFontMetrics
from PyQt5.QtCore import Qt, QRect, QTimer
import pandas as pd
import json
import random
import numpy as np
import os
import time
import pokemon
from pokemon import Pokemon, dico_poke
from combat import Ui_MainWindow
from CombatMain_def import CombatMain
from pokedex import Ui_FormPokedex


coords = pd.read_csv('..\data\pokemon_coordinates.csv')
Joueur = os.path.join(os.path.dirname(__file__),'image','Ash.png')
NOM = coords.pokemon
COORD = coords.coordinates

data =  os.path.join(os.path.dirname(__file__),'data', 'data_user.json')


Bulbasaur = os.path.join(os.path.dirname(__file__), 'image', 'Bullbizarre.png')
Charmander = os.path.join(os.path.dirname(__file__), 'image', 'Salameche.png')
Squirtle = os.path.join(os.path.dirname(__file__), 'image', 'Carapuce.png')

# Création d'un dictionnaire avec les Pokémon Bulbasaur, Charmander et Squirtle
dico_pokemon = {"Bulbasaur" : Bulbasaur,
    "Charmander": Charmander,
    "Squirtle": Squirtle}







### Création des dictionnaires #########################################

def CF(C):
    """
    

    Parameters
    ----------
    C : Data Frame.
    
    DESCRIPTION: Choisir les premiers pokémons du DataFrame et transfomer leurs coordonnées en liste de couples

    Returns
    -------
    cf : Liste.

    """
    c = []
    cf = []
    for ligne in C:
        c.append(ligne)
    CC = [json.loads(coord) for coord in c]
    Coord_Poke = CC[:10]
    for k in range(len(Coord_Poke)):
        xf = int(Coord_Poke[k][0] + random.randint(0,700))
        yf = int(Coord_Poke[k][1] + random.randint(0,500))
        cf.append((xf,yf))
    return cf

def Nf():
    """
    DESCRIPTION: Choisir les premiers pokémons du DataFrame et transfomer leurs noms en liste de string

    Returns
    -------
    NF : Liste.

    """
    nf = NOM[:10]
    NF = []
    for ligne in nf:
        NF.append(ligne)
    return NF
        

NF =Nf() 
cf = CF(COORD)
dico_poke = {cle: valeur for cle, valeur in zip(NF, cf)}  # Création d'un dictionnaire à l'aide de deux listes

pk = []

Machop = os.path.join(os.path.dirname(__file__),'pokemon','machop.png')
pk.append(Machop)
Machoke = os.path.join(os.path.dirname(__file__),'pokemon','machoke.png')
pk.append(Machoke)
Dugtrio = os.path.join(os.path.dirname(__file__),'pokemon','dugtrio.png')
pk.append(Dugtrio)
Tauros = os.path.join(os.path.dirname(__file__),'pokemon','tauros.png')
pk.append(Tauros)
Snorlax = os.path.join(os.path.dirname(__file__),'pokemon','snorlax.png')
pk.append(Snorlax)
Mankey = os.path.join(os.path.dirname(__file__),'pokemon','mankey.png')
pk.append(Mankey)
Electrode = os.path.join(os.path.dirname(__file__),'pokemon','electrode.png')
pk.append(Electrode)
Exeggcute = os.path.join(os.path.dirname(__file__),'pokemon','exeggcute.png')
pk.append(Exeggcute)
Weedle = os.path.join(os.path.dirname(__file__),'pokemon','weedle.png')
pk.append(Weedle)
Venonat = os.path.join(os.path.dirname(__file__),'pokemon','venonat.png')
pk.append(Venonat)
dico_poke_img = {cle: valeur for cle, valeur in zip(NF, pk)}


###################################################


class PokemonMap(QWidget):
    def __init__(self, ID):
        super().__init__()
        
        #ID du joueur
        self.ID = ID
        
        # Taille de la fenêtre et de la carte
        self.window_width = 800
        self.window_height = 600
        self.map_width = 1000
        self.map_height = 800

        # Position initiale du personnage
        self.player_x = (self.window_width - 10) // 2
        self.player_y = (self.window_height - 10) // 2

        self.pokemon_data = dico_poke          # Dictionnaire des Pokémon avec leurs noms et coordonnées 

        self.proximity_radius = 80             # Rayon de proximité pour détecter les Pokémons

        self.map_image = QPixmap("Grass_Type.webp")  # Charger l'image de la carte Pokémon
        
        
        self.button_label = QLabel(self) #Création bouton
        self.button_label.setGeometry(self.window_width - 80, self.window_height - 580, 50, 50)
        self.button_label.setPixmap(QPixmap("Pokedex.png"))  #Afficher une image sur le bouton
        self.button_label.setScaledContents(True)  # Redimensionner l'image pour s'adapter au QLabel
        self.button_label.mousePressEvent = self.open_new_interface
            
        
        self.player_image = QPixmap(Joueur).scaled(50, 50, Qt.KeepAspectRatio)   # Charger et redimensionner l'image du joueur
        
        self.pokemon_image = QPixmap("testgrass.png").scaled(30, 30, Qt.KeepAspectRatio) # Charger et redimensionner l'image des pokémons

        self.setGeometry(100, 100, self.window_width, self.window_height)  # Définir la taille de la fenêtre

        self.setWindowTitle("Pokemon Map")   # Titre de la fenêtre
        
        # self.new_interface = QtWidgets.QWidget()  # Créer une instance de QWidget
        # self.ui_pokedex = Ui_FormPokedex()  # Créer une instance de Ui_FormPokedex
        # self.ui_pokedex.setupUi(self.new_interface)  # Appeler la méthode setupUi() 

        self.show()   # Afficher la fenêtre

        #interface pokédex
        self.new_interface = QtWidgets.QWidget()  # Créer une instance de QWidget
        self.ui_pokedex = Ui_FormPokedex(self.new_interface)  # Créer une instance de Ui_FormPokedex
        self.ui_pokedex.setupUi(self.new_interface)  # Appeler la méthode setupUi() 


    def paintEvent(self, event ):
        """
        
        DESCRIPTION: Dessine la carte, le personnage et les pokémons à proximité.

        Returns
        -------
        Une carte avec un personnage au centre et des pokémons cachés

        """
        ID = self.ID
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.map_width, self.map_height, self.map_image)  # Dessiner la carte Pokémon
        painter.drawPixmap(self.player_x, self.player_y, self.player_image)        # Dessiner le joueur
        for pokemon_name, coord in self.pokemon_data.items():                      # Calculer les distances entre le joueur et les pokémons
            pokemon_x, pokemon_y = coord
            distance = ((pokemon_x - self.player_x) ** 2 + (pokemon_y - self.player_y) ** 2) ** 0.5
            if distance < self.proximity_radius:
                IMG = QPixmap(dico_poke_img[pokemon_name]).scaled(50, 50, Qt.KeepAspectRatio)
                painter.drawPixmap(coord[0], coord[1],IMG)         # Dessiner les Pokémons 
                font = QFont()
                font.setBold(True)                                                # Mettre la police en gras
                painter.setFont(font)
                font_metrics = QFontMetrics(painter.font())
                text_width = font_metrics.width(pokemon_name) +10
                if distance < 10:
                    
                    with open(data, "r") as file:
                        users = json.load(file)
                        nom = users[ID]["MyPokemons"][0]



                    
                    self.main_window = CombatMain(nom ,pokemon_name, dico_pokemon[nom] ,dico_poke_img[pokemon_name])                        # Lance l'interface du combat
                    self.main_window.show()
                    QTimer.singleShot(3000, lambda name=pokemon_name: self.remove_pokemon(name))
                
                

    def remove_pokemon(self, pokemon_name):
        """
        DESCRIPTION: Supprime un Pokémon du dictionnaire.
        """
        if pokemon_name in self.pokemon_data:
            del self.pokemon_data[pokemon_name]
            self.update()  # Montrer les changements
        
        
        
    def open_new_interface(self, event):
        """
        
        DESCRIPTION: Ouvre une nouvelle interface
        Returns
        -------
        Ouverture du Pokédex

        """

        self.new_interface.show()  # Afficher la nouvelle interface
        
 


    def keyPressEvent(self, event):
        """
        
        DESCRIPTION: Déplace le personnage grâce aux touches du clavier

        Returns
        -------
        Déplacement du personnage

        """
        if event.key() == Qt.Key_Left:
            self.player_x = max(0, self.player_x - 20)                          # max pour gérer les bords
        elif event.key() == Qt.Key_Right:
            self.player_x = min(self.window_width - 20, self.player_x + 20)     # min pour gérer les bords
        elif event.key() == Qt.Key_Up:
            self.player_y = max(0, self.player_y - 20)
        elif event.key() == Qt.Key_Down:
            self.player_y = min(self.window_height - 20, self.player_y + 20)
        self.update()
        
        
        
        
        
    def capturer(self, pokemon, ID):
        """
        La fonction enregistre les pokémons capturés dans  my pokemons et dans le fichier json
    
        """
        #on rajoute le pokémon capturer dans le pokédex
        self.ui_pokedex.listWidgetMesPokemons.addItem(QtWidgets.QListWidgetItem(pokemon)) #on reprend la notation  de Marche_BCP_moi pour utiliser le pokédex de la map
        
        #on enregistre dans le pokémon dans le fichier json
        with open(data, "r") as file:
            users = json.load(file)
        users[ID]['MyPokemons'].append(pokemon)
                    
        #Modifier le fichier
        with open(data, "w") as file:
            json.dump(users, file) 
            
    # def closepoke(self):
    #     """
    #     la fonction ferme le pokedex

    #     Returns
    #     -------
    #     None.

    #     """
    #     self.new_interface.close()

        
    #     #changer l'image du pokémon combat dans la fenêtre combat
        
        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokemonMap()
    app.setQuitOnLastWindowClosed(True)  
    sys.exit(app.exec_())
    
