# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:29:45 2024

@author: Formation
"""



import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi

import pokemon
from pokemon import Pokemon, dico_poke
from combat import Ui_MainWindow  
# from image1_rc import *  # Import du module contenant les ressources

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('combat.ui', self)  # Remplacez 'votre_fichier.ui' par le nom de votre fichier .ui
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Interface combat')  # Changez le titre selon vos besoins
        self.setWindowIcon(QIcon('votre_icone.ico'))  # Changez le nom de l'icône selon vos besoins

        ## Set le nom des pokémons
        self.ui.label_8.setText(f"{pikachu.name}")
        self.ui.label_5.setText(f"{bulbasaur.name}")
        self.ui.textBrowser.setText(f"{bulbasaur.name} vous attaque ! Voulez vous l'attaquer ou fuir ?")
        
        ##Définit les pv 
        self.ui.progressBar_2.setProperty("value",100)
        self.ui.progressBar_3.setProperty("value",100)
        
        self.ui.lcdNumber.display(bulbasaur.HP)#Bouge pas
        self.ui.lcdNumber_2.display(bulbasaur.HP)
        self.ui.lcdNumber_3.display(pikachu.HP)#Bouge pas 
        self.ui.lcdNumber_4.display(pikachu.HP)
        
        
        ## Choix attaque/fuite
        ##Attaque
        self.ui.pushButton.clicked.connect(self.attack)
        ##Fuite
        self.ui.pushButton_2.clicked.connect(self.fuite)
        
       
        
        
        self.show()
        
        
    def attack(self):
        self.ui.textBrowser.setText("Vous acceptez le combat ! Quelle attaque choisissez vous ?")
        self.ui.pushButton.setText("Attaque Neutre")
        self.ui.pushButton_2.setText("Attaque Spéciale")
        
   
    def fuite(self):
        self.ui.textBrowser.setText("Vous avez choisi de fuir !")
        ## Voir comment on peut sortir de la fenetre
        
# def start_combat(self):
#         pikachu = dico_poke["Pikachu"]
#         bulbasaur = dico_poke["Bulbasaur"]
        
#         # Exécuter la fonction de combat entre Pikachu et Bulbasaur
#         Pokemon.combat(pikachu, bulbasaur)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setQuitOnLastWindowClosed(True)  
    sys.exit(app.exec_())






if __name__ == "__main__":
    
    pikachu = dico_poke["Pikachu"]
    bulbasaur = dico_poke["Bulbasaur"]

    main()