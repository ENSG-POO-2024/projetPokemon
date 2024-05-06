# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:26:06 2024

@author: Formation
"""


import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap, QPainter, QKeyEvent
from PyQt5.QtCore import Qt


class PokemonMap(QWidget):
    def __init__(self):
        super().__init__()

        # Taille de la fenêtre et de la carte
        self.window_width = 800
        self.window_height = 600
        self.map_width = 1000
        self.map_height = 800

        # Position initiale du personnage
        self.player_x = (self.window_width + 20) // 2
        self.player_y = (self.window_height - 5) // 2

        # Charger l'image de la carte Pokémon
        self.map_image = QPixmap("Grass_Type.webp")

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
        # Dessiner le personnage
        painter.fillRect(self.player_x, self.player_y, 10, 10, Qt.blue)

    def keyPressEvent(self, event):
        # Gérer les mouvements du personnage avec les touches du clavier
        if event.key() == Qt.Key_Left:
            self.player_x = max(0, self.player_x - 35)
        elif event.key() == Qt.Key_Right:
            self.player_x = min(self.window_width - 35, self.player_x + 35)
        elif event.key() == Qt.Key_Up:
            self.player_y = max(0, self.player_y - 25)
        elif event.key() == Qt.Key_Down:
            self.player_y = min(self.window_height - 25, self.player_y + 25)
        self.update()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PokemonMap()
    sys.exit(app.exec_())