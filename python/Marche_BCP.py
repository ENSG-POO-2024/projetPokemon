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
from PyQt5.QtCore import Qt, QRect
import pandas as pd
import json
import random
import numpy as np
import os
# # Importez la fonction de combat depuis votre autre module
# from pokemon_combat import launch_battle

import pokemon
from pokemon import Pokemon, dico_poke
from combat import Ui_MainWindow
from combatMain import MainWindow

from pokedex import Ui_FormPokedex


coords = pd.read_csv('..\data\pokemon_coordinates.csv')
Joueur = os.path.join(os.path.dirname(__file__),'image','Ash.png')
NOM = coords.pokemon
COORD = coords.coordinates

# Création du dictionnaire

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


class PokemonMap(QWidget):
    def __init__(self):
        super().__init__()

        # Taille de la fenêtre et de la carte
        self.window_width = 800
        self.window_height = 600
        self.map_width = 1000
        self.map_height = 800

        # Position initiale du personnage
        self.player_x = (self.window_width - 10) // 2
        self.player_y = (self.window_height - 10) // 2

        self.pokemon_data = dico_poke          # Dictionnaire des Pokémon avec leurs noms et coordonnées 

        self.proximity_radius = 50             # Rayon de proximité pour détecter les Pokémons

        self.map_image = QPixmap("Grass_Type.webp")  # Charger l'image de la carte Pokémon
        
        # Créer un bouton pour ouvrir la nouvelle interface
        # self.button = QPushButton("Ouvrir", self)
        # self.button.setGeometry(self.window_width - 100, self.window_height - 50, 80, 30)
        # self.button.clicked.connect(self.open_new_interface)
        
        
        self.button_label = QLabel(self) #Création bouton
        self.button_label.setGeometry(self.window_width - 80, self.window_height - 580, 50, 50)
        self.button_label.setPixmap(QPixmap("Pokedex.png"))  #Afficher une image sur le bouton
        self.button_label.setScaledContents(True)  # Redimensionner l'image pour s'adapter au QLabel
        self.button_label.mousePressEvent = self.open_new_interface
            
        

        self.player_image = QPixmap(Joueur).scaled(50, 50, Qt.KeepAspectRatio)   # Charger et redimensionner l'image du joueur
        
        self.pokemon_image = QPixmap("testgrass.png").scaled(30, 30, Qt.KeepAspectRatio) # Charger et redimensionner l'image des pokémons

        self.setGeometry(100, 100, self.window_width, self.window_height)  # Définir la taille de la fenêtre

        self.setWindowTitle("Pokemon Map")   # Titre de la fenêtre

        self.show()   # Afficher la fenêtre

    def paintEvent(self, event):
        """
        
        DESCRIPTION: Dessine la carte, le personnage et les pokémons à proximité.

        Returns
        -------
        Une carte avec un personnage au centre et des pokémons cachés

        """
        painter = QPainter(self)
        painter.drawPixmap(0, 0, self.map_width, self.map_height, self.map_image)  # Dessiner la carte Pokémon
        painter.drawPixmap(self.player_x, self.player_y, self.player_image)        # Dessiner le joueur
        for pokemon_name, coord in self.pokemon_data.items():                      # Calculer les distances entre le joueur et les pokémons
            pokemon_x, pokemon_y = coord
            distance = ((pokemon_x - self.player_x) ** 2 + (pokemon_y - self.player_y) ** 2) ** 0.5
            if distance < self.proximity_radius:
                IMG = QPixmap(dico_poke_img[pokemon_name]).scaled(50, 50, Qt.KeepAspectRatio)
                painter.drawPixmap(coord[0], coord[1],IMG)         # Dessiner les Pokémons 
                # painter.fillRect(coord[0], coord[1], 10, 10, Qt.black)
                font = QFont()
                font.setBold(True)                                                # Mettre la police en gras
                painter.setFont(font)
                font_metrics = QFontMetrics(painter.font())
                text_width = font_metrics.width(pokemon_name) +10
                # font_metrics = QFontMetrics(painter.font())
                # text_width = font_metrics.horizontalAdvance(pokemon_name)
                # painter.drawText(pokemon_x - text_width // 2 + 15, pokemon_y - 5, pokemon_name)  # Afficher le texte sur le pokémon
                # Créer une instance de la MainWindow et l'afficher
                self.main_window = MainWindow()
                self.main_window.show()
                
    
    
    
    # # Vérifiez si le personnage est à proximité d'un Pokémon et lancez le combat si c'est le cas
    #     self.check_for_battle()

    # def check_for_battle(self):
    #     for pokemon_name, coord in self.pokemon_data.items():
    #         pokemon_x, pokemon_y = coord
    #         distance = ((pokemon_x - self.player_x) ** 2 + (pokemon_y - self.player_y) ** 2) ** 0.5
    #         if distance < self.proximity_radius:
    #             # Lancez le combat avec le Pokémon à proximité
    #             defeated = launch_battle(pokemon_name)
    #             if defeated:
    #                 # Supprimez le Pokémon de la carte s'il est battu
    #                 del self.pokemon_data[pokemon_name]
    #                 break  # Sortez de la boucle pour ne pas traiter les autres Pokémon
                
                # # Créez une instance de MainWindow et montrez-la
                #  self.main_window = MainWindow()
                #  self.main_window.show()
                #  break  # Sortez de la boucle pour ne pas traiter les autres Pokémon
                
    # def open_new_interface(self, event):
    #     # Fonction pour ouvrir une nouvelle interface
    #     # self.new_window = QWidget()
    #     # self.new_window.setGeometry(200, 200, 400, 300)
    #     # self.new_window.setWindowTitle("Nouvelle Interface")
    #     # self.new_window.show()
        
    #     new_interface = Ui_FormPokedex()
    #     # self.new_interface.show()
    #     # app = QtWidgets.QApplication(sys.argv)
    #     # Form_Pokedex = QtWidgets.QWidget()
    #     # app.setQuitOnLastWindowClosed(True)
    #     # ui_pokedex = Ui_FormPokedex()
    #     # ui_pokedex.setupUi(Form_Pokedex)
    #     # Form_Pokedex.show()
    #     # sys.exit(app.exec_())
        
        
    def open_new_interface(self, event):
        # Fonction pour ouvrir une nouvelle interface
        self.new_interface = QtWidgets.QWidget()  # Créez une instance de QWidget
        self.ui_pokedex = Ui_FormPokedex()  # Créez une instance de votre classe Ui_FormPokedex
        self.ui_pokedex.setupUi(self.new_interface)  # Appelez la méthode setupUi() avec votre nouvelle interface en tant qu'argument
        self.new_interface.show()  # Affichez la nouvelle interface
        
    # def open_new_interface2(self, event):
    #     # Fonction pour ouvrir une nouvelle interface
    #     self.new_window = QWidget()
    #     self.new_window.setGeometry(200, 200, 400, 300)
    #     self.new_window.setWindowTitle("Nouvelle Interface")
    #     self.new_window.show()


    def keyPressEvent(self, event):
        """
        
        DESCRIPTION: Déplace le personnage grâce aux touches du clavier

        Returns
        -------
        Déplacement du personnage

        """
        if event.key() == Qt.Key_Left:
            self.player_x = max(0, self.player_x - 20)                          # max(0) pour gérer les bords
        elif event.key() == Qt.Key_Right:
            self.player_x = min(self.window_width - 20, self.player_x + 20)     # min pour gérer les bords
        elif event.key() == Qt.Key_Up:
            self.player_y = max(0, self.player_y - 20)
        elif event.key() == Qt.Key_Down:
            self.player_y = min(self.window_height - 20, self.player_y + 20)
        # self.check_for_battle()
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokemonMap()
    sys.exit(app.exec_())