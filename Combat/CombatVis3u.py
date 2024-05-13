# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CombatVis3u.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QMainWindow, QApplication, QLabel
from PyQt5.QtCore import Qt, QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QSoundEffect
from PyQt5.QtGui import QColor, QFont, QPainter, QPixmap, QImage
from PyQt5 import *

current_dir = os.path.dirname(__file__)
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(parent_dir)

import Poke as poke
import test_graph as t #MODIFIER QUAND FICHIER DEFINITIF
import fight as f
import ChoixPokemon.ChoixPokemonVisu3u as ch
import VictoireVis3u as v
import DefaiteVis3u as d


def bas_image(image):
    img = image.toImage()
    hauteur = img.height()
    largeur = img.width()

    for h in range(hauteur-1, -1, -1):
        for l in range(largeur):
            color = img.pixelColor(l, h)

            if color.alpha() != 0:
                return h
            
    return 0



class Combat_ui(object):

        
    def setupUi(self, MainWindow):

        #self.pokemon_utilise = list(self.inventaire_joueur.pokedex.values())[0]
        self.adversaire = self.pokemon_sauvage

        self.pokedex = poke.Pokedex()
        self.pokedex.charger_pokedex("pokemon_first_gen.csv")



        # Création de l'objet MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Combat contre " + self.pokemon_sauvage.name.split()[0])
        MainWindow.resize(1000, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Ajout du son
        self.musique = QMediaPlayer(self.centralwidget)
        self.musique.setMedia(QMediaContent(QUrl.fromLocalFile("Combat/battle.mp3")))
        self.musique.setVolume(100)
        self.musique.play()

        # Création de l'arrière plan
        self.Fond = QtWidgets.QLabel(self.centralwidget)
        self.Fond.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.Fond.setText("")
        self.Fond.setPixmap(QtGui.QPixmap("Combat/BackgroundCombat.png"))
        self.Fond.setScaledContents(True)
        self.Fond.setObjectName("Fond")

        # Ajout du type du pokemon adverse
        self.TypeEnemy = QtWidgets.QLabel(self.centralwidget)
        self.TypeEnemy.setGeometry(QtCore.QRect(409, 98, 60, 60))
        self.TypeEnemy.setPixmap(QtGui.QPixmap("data/" + self.adversaire.type.__class__.__name__ + ".png")) #
        self.TypeEnemy.setScaledContents(True)
        self.TypeEnemy.setObjectName("TypeEnemy")

        # Ajout du type de mon pokemon
        self.TypeAllie = QtWidgets.QLabel(self.centralwidget)
        self.TypeAllie.setGeometry(QtCore.QRect(605, 448, 60, 60))
        self.TypeAllie.setPixmap(QtGui.QPixmap("data/" + self.pokemon_utilise.type.__class__.__name__ + ".png")) #
        self.TypeAllie.setScaledContents(True)
        self.TypeAllie.setObjectName("TypeAllie")


        #Création de l'objet barre de vie de notre pokemon
        self.progressBarAllie = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarAllie.setGeometry(QtCore.QRect(620, 397, 371, 23))
        self.progressBarAllie.setMaximum(self.pokedex.pokedex[self.pokemon_utilise.name.split()[0]].hp)
        self.progressBarAllie.setValue(self.pokemon_utilise.hp)
        self.progressBarAllie.setFormat("")
        self.progressBarAllie.setObjectName("progressBarAllie")

        # Créer une étiquette pour afficher les points de vie de notre pokemon
        self.label_hp_allie = QtWidgets.QLabel(self.centralwidget)
        self.label_hp_allie.setGeometry(QtCore.QRect(624, 399, 371, 23))
        self.label_hp_allie.setObjectName("label_hp_allie")
        self.label_hp_allie.setStyleSheet('color: black; font-size: 16px; font-family: "Minecraft";')
    
        # Affichage de la bar d'hp de notre pokemon
        self.affiche_progress_bar(self.progressBarAllie, self.label_hp_allie, self.pokemon_utilise.hp)


        # Création de la barre de vie de m'adversaire
        self.progressBarEnemy = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBarEnemy.setGeometry(QtCore.QRect(110, 189, 371, 23))
        self.progressBarEnemy.setMaximum(self.pokedex.pokedex[self.adversaire.name.split()[0]].hp)
        self.progressBarEnemy.setValue(self.adversaire.hp)
        self.progressBarEnemy.setFormat("")
        self.progressBarEnemy.setObjectName("progressBarEnemy")

        # Créer une étiquette pour afficher les points de vie de l'adversaire
        self.label_hp_adversaire = QtWidgets.QLabel(self.centralwidget)
        self.label_hp_adversaire.setGeometry(QtCore.QRect(114, 191, 371, 23))
        self.label_hp_adversaire.setObjectName("label_hp_adversaire")
        self.label_hp_adversaire.setStyleSheet('color: black; font-size: 16px; font-family: "Minecraft";')
        
        # Affichage de la bar d'hp de l'adversaire
        self.affiche_progress_bar(self.progressBarEnemy, self.label_hp_adversaire, self.adversaire.hp)

        # Affichage de notre pokémon
        self.image_poke = QtWidgets.QLabel(self.centralwidget)
        self.image_poke.setGeometry(QtCore.QRect(60, 230, 400, 400))
        self.image_poke.setText("")
        self.image_poke.setPixmap(QtGui.QPixmap("Pokemons/"+self.pokemon_utilise.name.split()[0]+"/"+self.pokemon_utilise.name.split()[0]+"_dos.png"))
        self.image_poke.setScaledContents(True)
        self.image_poke.setObjectName("Pokemon inventaire_joueur")

        # Affichage pokémon adverse
        self.image_adv = QtWidgets.QLabel(self.centralwidget)
        self.image_adv.setGeometry(QtCore.QRect(550, 40, 400, 400))
        self.image_adv.setText("")
        self.image_adv.setPixmap(QtGui.QPixmap("Pokemons/"+self.adversaire.name.split()[0]+"/"+self.adversaire.name.split()[0]+"_face.png"))
        self.img_adv_largeur = QtGui.QPixmap("Pokemons/"+self.adversaire.name.split()[0]+"/"+self.adversaire.name.split()[0]+"_dos.png").width()
        self.bas_img_adv = bas_image(QtGui.QPixmap("Pokemons/"+self.adversaire.name.split()[0]+"/"+self.adversaire.name.split()[0]+"_face.png"))
        self.image_adv.move(550, 80-self.bas_img_adv)
        self.image_adv.setScaledContents(True)
        self.image_adv.setObjectName("Pokemon adverse")



        # Point d'attaque et de défense de notre pokémon
        self.label = QLabel(str(self.pokemon_utilise.attack), self)
        self.label.setGeometry(128, 583, 200, 50)
        self.label.setStyleSheet('color: black; font-size: 30px; font-family: "Hello World";')  
        self.label = QLabel(str(self.pokemon_utilise.defense), self)
        self.label.setGeometry(128, 657, 200, 50)
        self.label.setStyleSheet('color: black; font-size: 30px; font-family: "Hello World";')

        # Point d'attaque et de défense de l'adversaire
        self.label = QLabel(str(self.adversaire.attack), self)
        self.label.setGeometry(323, -2, 200, 50)
        self.label.setStyleSheet('color: red; font-size: 25px; font-family: "Hello World";')  
        self.label = QLabel(str(self.adversaire.defense), self)
        self.label.setGeometry(339, 34, 200, 50)
        self.label.setStyleSheet('color: red; font-size: 25px; font-family: "Hello World";')

        # Bouton de l'attaque normale
        self.AttaqueNormale = QtWidgets.QPushButton(self.centralwidget)
        self.AttaqueNormale.setGeometry(QtCore.QRect(353, 558, 169, 161))
        self.AttaqueNormale.setText("")
        self.AttaqueNormale.setObjectName("AttaqueNormale")

        # Bouton de l'attaque speciale
        self.AttaqueSpeciale = QtWidgets.QPushButton(self.centralwidget)
        self.AttaqueSpeciale.setGeometry(QtCore.QRect(561, 558, 169, 161))
        self.AttaqueSpeciale.setText("")
        self.AttaqueSpeciale.setObjectName("AttaqueSpeciale")

        # Bouton pour changer de pokemon
        self.Pokedex = QtWidgets.QPushButton(self.centralwidget)
        self.Pokedex.setGeometry(QtCore.QRect(770, 558, 169, 161))
        self.Pokedex.setText("")
        self.Pokedex.setObjectName("Pokedex")

        # Bouton pour fuir
        self.Fuite = QtWidgets.QPushButton(self.centralwidget)
        self.Fuite.setGeometry(QtCore.QRect(800, 0, 300, 300))
        self.Fuite.setText("")
        self.Fuite.setObjectName("Fuite")

        

        # On met tout en avant (dans le bon ordre) pour que les objets soient au premier plan 
        self.Fond.raise_()
        self.image_poke.raise_()
        self.image_adv.raise_()

        # Affichage de notre pokémon
        self.points_attaque = QtWidgets.QLabel(self.centralwidget)
        self.points_attaque.setGeometry(QtCore.QRect(0, 0, 1000, 750))
        self.points_attaque.setText("")
        self.points_attaque.setPixmap(QtGui.QPixmap("Combat/combat.png"))
        self.points_attaque.setScaledContents(True)
        self.points_attaque.setObjectName("Points d'attaque")

        
        self.progressBarAllie.raise_()
        self.progressBarEnemy.raise_()
        self.AttaqueNormale.raise_()
        self.AttaqueSpeciale.raise_()
        self.Pokedex.raise_()
        self.Fuite.raise_()
        self.label_hp_adversaire.raise_()
        self.label_hp_allie.raise_()
        self.TypeEnemy.raise_()
        self.TypeAllie.raise_()


        self.AttaqueNormale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.AttaqueSpeciale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Pokedex.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")
        self.Fuite.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")


        MainWindow.setCentralWidget(self.centralwidget)

        self.Fuite.clicked.connect(self.fuite_buton)

        #self.tour_joueur = True
        #self.tours_depuis_attaque_joueur = 2  # Tours écoulés depuis la dernière attaque spéciale du joueur
        self.tours_depuis_attaque_ordi = 2  # Tours écoulés depuis la dernière attaque spéciale de l'ordinateur
        self.apres_pokedex = False

        # Affichage nom du pokémon utilisé
        self.nom_poke = QLabel(self.pokemon_utilise.name.split()[0], self)
        self.nom_poke.setGeometry(660, 432, 300, 100)  # Définir la position et la taille du QLabel
        self.nom_poke.setAlignment(Qt.AlignCenter)  # Aligner le texte au centre 
        font = QFont("Minecraft", 40)  # Police et taille
        self.nom_poke.setFont(font)
        self.nom_poke.setStyleSheet('color: black;')  

        # Affichage nom du pokémon adverse
        self.nom_poke = QLabel(self.adversaire.name.split()[0], self)
        self.nom_poke.setGeometry(93, 80, 300, 100)  # Définir la position et la taille du QLabel
        self.nom_poke.setAlignment(Qt.AlignCenter)  # Aligner le texte au centre 
        font = QFont("Minecraft", 40)  # Police et taille
        self.nom_poke.setFont(font)
        self.nom_poke.setStyleSheet("color: black;")  

        if self.tours_depuis_attaque_joueur < 2:
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(128, 128, 128, 128)")
        else:
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(128, 128, 128, 0)")

        if self.apres_pokedex:
            self.tour_ordi()


        
        # Connectez le signal clicked du bouton à la méthode correspondante
        self.AttaqueNormale.clicked.connect(self.on_attaque_normale_clicked)
        self.AttaqueSpeciale.clicked.connect(self.on_attaque_speciale_clicked)

        self.Pokedex.clicked.connect(self.open_pokedex)


    def open_pokedex(self): # A revoir
        self.apres_pokedex = True
        self.close()
        self.tours_depuis_attaque_joueur += 1
        self.pokedex_window = ch.ChoixPokemonWindow(self.adversaire, self.inventaire_joueur, self.pokedex_sauvages, self.tour_joueur, self.tours_depuis_attaque_joueur)  
        self.pokedex_window.show()


    def fuite_buton(self):
        self.apres_pokedex = False
        self.pokemon_utilise.hp = self.pokedex.pokedex[self.pokemon_utilise.name.split()[0]].hp
        self.adversaire.hp = self.pokedex.pokedex[self.adversaire.name.split()[0]].hp
        self.close() 

    def on_attaque_normale_clicked(self):
        self.apres_pokedex = False
        self.Pokedex.setEnabled(False)
        self.Fuite.setEnabled(False)
        if self.tour_joueur:
            # Attaque normale du joueur
            self.pokemon_utilise.attaquer(self.adversaire)
            self.progressBarEnemy.setValue(self.adversaire.hp)
            self.affiche_progress_bar(self.progressBarEnemy, self.label_hp_adversaire, self.adversaire.hp)

            # On désactive le bouton d'attaque pour empêcher les attaques multiples dans le même tour
            self.AttaqueNormale.setEnabled(False)

            # On incrémente le nombre de tour depuis l'ataque spéciale du joueur
            self.tours_depuis_attaque_joueur += 1

            # On passe au tour de l'ordi
            self.tour_joueur = False

            if self.adversaire.hp <= 0: # On vérifie si l'adversaire est battu
                QTimer.singleShot(1000, self.close)
                QTimer.singleShot(1000, self.open_victory)

            else:
                # L'ordi peut attaquer
                self.tour_attaque_ordi = True
                QTimer.singleShot(1000, self.tour_ordi)
        

    def on_attaque_speciale_clicked(self):
        self.apres_pokedex = False
        self.Pokedex.setEnabled(False)
        self.Fuite.setEnabled(False)
        if self.tours_depuis_attaque_joueur >= 2:
            # Attaque spéciale du joueur
            self.pokemon_utilise.attaque_speciale_joueur(self.adversaire)
            self.progressBarEnemy.setValue(self.adversaire.hp)
            self.affiche_progress_bar(self.progressBarEnemy, self.label_hp_adversaire, self.adversaire.hp)

            # On désactive le bouton d'attaque spéciale pour empêcher les attaques multiples dans le même tour
            self.AttaqueSpeciale.setEnabled(False)
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(128, 128, 128, 128)")

            # On met à jour la disponibilité de l'attaque spéciale
            self.tours_depuis_attaque_joueur = 0  # On réinitialise le compteur de tours après l'attaque spéciale du joueur

            if self.adversaire.hp <= 0: # On vérifie si l'adversaire est battu
                QTimer.singleShot(1000, self.close)
                QTimer.singleShot(1000, self.open_victory)

            else:
                # On attend 2 secondes puis l'adversaire attaque
                self.tour_attaque_ordi = True
                QTimer.singleShot(1000, self.tour_ordi)

        

    def tour_ordi(self):
        self.apres_pokedex = False
        # On vérifie si l'ordi a son attaque spéciale de prête 
        if self.tours_depuis_attaque_ordi >= 2:
            # Si oui alors il l'utilise
            self.adversaire.attaque_speciale_joueur(self.pokemon_utilise)
            self.progressBarAllie.setValue(self.pokemon_utilise.hp)
            self.affiche_progress_bar(self.progressBarAllie, self.label_hp_allie, self.pokemon_utilise.hp)
        
            # On récative le bouton d'attaque du joueur
            self.AttaqueNormale.setEnabled(True)
            self.Pokedex.setEnabled(True)
            self.Fuite.setEnabled(True)

            # On passe au tour du joueur
            self.tour_joueur = True

            # Mettez à jour l'état de disponibilité de l'attaque spéciale de l'ordinateur
            self.tours_depuis_attaque_ordi = 0  # Réinitialisez le compteur de tours depuis l'attaque spéciale



        else:
            # Si l'attaque spéciale n'est pas disponible alors l'adversaire attaque normalement 
            self.adversaire.attaquer(self.pokemon_utilise)
            self.progressBarAllie.setValue(self.pokemon_utilise.hp)
            self.affiche_progress_bar(self.progressBarAllie, self.label_hp_allie, self.pokemon_utilise.hp)
        
            # On récative le bouton d'attaque du joueur
            self.AttaqueNormale.setEnabled(True)
            self.Pokedex.setEnabled(True)
            self.Fuite.setEnabled(True)

            # On incrémente le compteur de tours depuis la dernière attaque spéciale de l'adversaire
            self.tours_depuis_attaque_ordi += 1

            # On passe au tour du joueur
            self.tour_joueur = True
            self.tour_attaque_ordi = False


        if self.tours_depuis_attaque_joueur >= 2: # On met à jour si besoin le bouton d'attaque spéciale
            self.AttaqueSpeciale.setEnabled(True)
            self.AttaqueSpeciale.setStyleSheet("background-color: rgba(255, 255, 255, 0); border: none;")

        if self.pokemon_utilise.hp <= 0: # On vérifie si le joueur a perdu
                QTimer.singleShot(1000, self.close)
                self.pokemon_utilise.hp = self.pokedex.pokedex[self.pokemon_utilise.name.split()[0]].hp
                self.adversaire.hp = self.pokedex.pokedex[self.adversaire.name.split()[0]].hp
                QTimer.singleShot(1000, self.open_loose)



    def affiche_progress_bar(self, bar, label, hp):
        if hp <= 0.25 * bar.maximum():
            bar.setStyleSheet("""                                                                
                QProgressBar {
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                }
                    
                QProgressBar::chunk {
                    background-color: #FF0000; /* Couleur de la barre de progression */   
                    border-radius: 100px;
                }                                
            """) 
        
        else:
            bar.setStyleSheet("""   
                QProgressBar { color: red;}                                                            
                QProgressBar {                            
                    border: 2px solid grey;
                    border-radius: 5px;
                    background-color: #FFFFFF; /* Couleur de fond de la barre de progression */
                }

                QProgressBar::chunk {
                    background-color: #00FF00; /* Couleur de la barre de progression */
                    border-radius: 100px;
                }                                                             
            """)
        # Mettre à jour le texte de l'étiquette des points de vie de notre pokemon
        label.setText(str(hp))
        label.raise_()

    def open_victory(self):
        self.victory_window = v.VictoireWindow(self.adversaire, self.pokedex_sauvages, self.inventaire_joueur, self.pokemon_utilise, self.pokedex)
        self.victory_window.show()

    def open_loose(self):
        self.Pokedex.setEnabled(False)
        self.Fuite.setEnabled(False)
        self.victory_window = d.DefaiteWindow(self.adversaire, self.pokedex_sauvages, self.inventaire_joueur, self.pokemon_utilise, self.pokedex)
        self.victory_window.show()


    







class FightWindow(QMainWindow, Combat_ui):
    def __init__(self, pokemon_sauvage, pokemon_utilise, pokedex_sauvages, inventaire_joueur, tour_joueur,  tour_depuis_ataque_joueur, parent=None):
        self.pokemon_sauvage = pokemon_sauvage # Le pokémon rencontré
        self.inventaire_joueur = inventaire_joueur # L'inventaire du joueur avec ses pokémons
        self.pokemon_utilise = pokemon_utilise # Le pokémon qu'il utilise
        self.pokedex_sauvages = pokedex_sauvages # Le pokedex avec tous les pokémons sauvages
        self.tour_joueur = tour_joueur
        self.tours_depuis_attaque_joueur = tour_depuis_ataque_joueur
        super(FightWindow, self).__init__(parent)
        self.setupUi(self)
        

