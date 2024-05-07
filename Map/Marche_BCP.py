# -*- coding: utf-8 -*-
"""
Created on Mon May  6 20:54:33 2024

@author: sylvi
"""

import sys
import csv
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QFont, QPainter, QFontMetrics
from PyQt5.QtCore import Qt, QRect
import pandas as pd
import json
import random
import numpy as np


coords = pd.read_csv('..\data\pokemon_coordinates.csv')
NOM = coords.pokemon
COORD = coords.coordinates

def C(C):
    c = []
    for ligne in C:
        c.append(ligne)
    CC = [json.loads(coord) for coord in c]
    return CC

def CF():
    cf = []
    CC = C(COORD)
    Coord_Poke = CC[:10]
    for k in range(len(Coord_Poke)):
        xf = int(Coord_Poke[k][0] + random.randint(0,700))
        yf = int(Coord_Poke[k][1] + random.randint(0,500))
        cf.append((xf,yf))
    return cf

def Nf():
    nf = NOM[:10]
    NF = []
    for ligne in nf:
        NF.append(ligne)
    return NF
        

NF =Nf()
cf = CF()
dico_poke = {cle: valeur for cle, valeur in zip(NF, cf)}


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

        # Dictionnaire des Pokémon avec leurs noms et coordonnées
        self.pokemon_data = dico_poke  

        # Rayon de proximité pour détecter les Pokémon
        self.proximity_radius = 50

        # Charger l'image de la carte Pokémon
        self.map_image = QPixmap("Grass_Type.webp")

        # Charger et redimensionner l'image du joueur
        self.player_image = QPixmap("Joueur.jpg").scaled(30, 30, Qt.KeepAspectRatio)
        
        self.pokemon_image = QPixmap("testgrass.png").scaled(30, 30, Qt.KeepAspectRatio)

        # Définir la taille de la fenêtre
        self.setGeometry(100, 100, self.window_width, self.window_height)

        # Titre de la fenêtre
        self.setWindowTitle("Pokemon Map")

        # Afficher la fenêtre
        self.show()

    def paintEvent(self, event):
        painter = QPainter(self)
        # Dessiner la carte Pokémon
        painter.drawPixmap(0, 0, self.map_width, self.map_height, self.map_image)
        # Dessiner le joueur
        painter.drawPixmap(self.player_x, self.player_y, self.player_image)
        # Dessiner les Pokémon
        for pokemon_name, coord in self.pokemon_data.items():
            pokemon_x, pokemon_y = coord
            distance = ((pokemon_x - self.player_x) ** 2 + (pokemon_y - self.player_y) ** 2) ** 0.5
            if distance < self.proximity_radius:
                painter.drawPixmap(coord[0], coord[1], self.pokemon_image)
                # painter.fillRect(coord[0], coord[1], 10, 10, Qt.black)
                font = QFont()
                font.setBold(True)  # Définir la police en gras
                painter.setFont(font)
                font_metrics = QFontMetrics(painter.font())
                text_width = font_metrics.width(pokemon_name) +10
                # font_metrics = QFontMetrics(painter.font())
                # text_width = font_metrics.horizontalAdvance(pokemon_name)
                painter.drawText(pokemon_x - text_width // 2, pokemon_y - 10, pokemon_name)


    def keyPressEvent(self, event):
        # Gérer les mouvements du personnage avec les touches du clavier
        if event.key() == Qt.Key_Left:
            self.player_x = max(0, self.player_x - 20)
        elif event.key() == Qt.Key_Right:
            self.player_x = min(self.window_width - 20, self.player_x + 20)
        elif event.key() == Qt.Key_Up:
            self.player_y = max(0, self.player_y - 20)
        elif event.key() == Qt.Key_Down:
            self.player_y = min(self.window_height - 20, self.player_y + 20)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokemonMap()
    sys.exit(app.exec_())