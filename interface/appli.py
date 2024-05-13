# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:25:39 2024

@author: Formation
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from page_accueil import MainWindow
from first_connection import FirstConnection, Ui_erreur
from premier_pokemon import Ui_FormPokemon
from pokedex import Ui_FormPokedex


import sys


#afficher la page first connection
def afficheFirstConnection():
    Window.close()
    First_Conection.show()

#afficher la page first pokémon
def afficheFirstPokemon():
    
    texte = "ID already exists. Please choose another username."

    #si le login n'a jamais encore été utilisé alors on ouvre la nouvelle fenêtre et on choisit nos pokémon
    if ui_Form.verifyAndRegister() != texte:
        #fonction de vérification
        First_Conection.close()
        Form_Pokemon.show()
    else:
        mess.show()
    
        
def capturer(pokemon):
    """
    La fonction enregistre les pokémons capturés dans  my pokemons

    Parameters
    ----------
    pokemon : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    ui_Pokedex.listWidgetMesPokemons.addItem(QtWidgets.QListWidgetItem(pokemon))
    Form_Pokedex.show()





app = QtWidgets.QApplication(sys.argv)

#Page d'accueil
Window = QtWidgets.QMainWindow()
ui_MainWindow = MainWindow(Window)



#Page first connection
First_Conection = QtWidgets.QWidget()
app.setQuitOnLastWindowClosed(True)
ui_Form = FirstConnection(First_Conection)


#page des premieres pokémon
Form_Pokemon = QtWidgets.QWidget()
ui_Pokemon = Ui_FormPokemon()
ui_Pokemon.setupUi(Form_Pokemon)
    
#message d'erreur
mess = QtWidgets.QWidget()
ui_erreur = Ui_erreur()
ui_erreur.setupUi(mess)

#bouton 
ui_MainWindow.pushButton_2.clicked.connect(afficheFirstConnection)
ui_Form.pushButton.clicked.connect(afficheFirstPokemon)


#Pokédex
Form_Pokedex = QtWidgets.QWidget()
ui_Pokedex = Ui_FormPokedex()
ui_Pokedex.setupUi(Form_Pokedex)


#Choisir son pokémon
ui_Pokemon.pushButtonBulbasaur.clicked.connect(lambda checked, pokemon = 'Bulbasaur' : capturer(pokemon))
#Utilisation de lambda car la fonction clicked.connect ne reconnait pas les paramètres des fonctions qui se trouvent à l'intérieur
ui_Pokemon.pushButtonCharmander.clicked.connect(lambda checked, pokemon = 'Charmander' :capturer(pokemon))
ui_Pokemon.pushButtonSquirtle.clicked.connect(lambda checked, pokemon ='Squirtle' : capturer(pokemon))






app.setQuitOnLastWindowClosed(True)
Window.show()
sys.exit(app.exec_())