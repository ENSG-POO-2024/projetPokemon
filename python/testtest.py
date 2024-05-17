# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:22:23 2024

@author: Sebastien C.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from page_accueil import MainWindow, Ui_erreur_login
from first_connection import FirstConnection, Ui_erreur
from premier_pokemon import Ui_FormPokemon
from pokedex import Ui_FormPokedex
from Marche_BCP_moi import PokemonMap
import os
import json
import sys

data = os.path.join(os.path.dirname(__file__), 'data', 'data_user.json')

# afficher la page first connection
def afficheFirstConnection():
    Window.close()
    First_Connection.show()

# afficher la page first pokémon
def afficheFirstPokemon():
    texte = "ID already exists. Please choose another username."
    Text, ID = ui_Form.verifyAndRegister()

    if Text != texte:
        First_Connection.close()
        Form_Pokemon.show()
        return ID
    else:
        mess.show()

def capturer(pokemon):
    """
    La fonction enregistre les pokémons capturés dans my pokemons
    """
    ui_Pokedex.listWidgetMesPokemons.addItem(QtWidgets.QListWidgetItem(pokemon))
    Text, ID = ui_MainWindow.verifyLogin()

    if ID == '':
        Text, ID = ui_Form.verifyAndRegister()
        with open(data, "r") as file:
            users = json.load(file)
        users[ID]['MyPokemons'].append(pokemon)

        with open(data, "w") as file:
            json.dump(users, file)
    else:
        Text, ID = ui_Form.verifyAndRegister()
        with open(data, "r") as file:
            users = json.load(file)
        users[ID]['MyPokemons'].append(pokemon)

        with open(data, "w") as file:
            json.dump(users, file)

def openMap():
    Map.show()
    First_Connection.close()
    Window.close()
    Form_Pokemon.close()

def openPokedex():
    Form_Pokedex.show()

def check():
    """
    La fonction recharge la partie de l'utilisateur avec tous ses pokémons
    """
    texte = "Login failed. Please try again."
    Text, ID = ui_MainWindow.verifyLogin()

    if Text != texte:
        with open(data, "r") as file:
            users = json.load(file)
            listPoke = users[ID]["MyPokemons"]
            for k in range(len(listPoke)):
                nomPoke = listPoke[k]
                ui_Pokedex.listWidgetMesPokemons.addItem(QtWidgets.QListWidgetItem(nomPoke))
            openMap()
    else:
        mess_err.show()

app = QtWidgets.QApplication(sys.argv)

# Pokédex
Form_Pokedex = QtWidgets.QWidget()
ui_Pokedex = Ui_FormPokedex()
Pokedex = ui_Pokedex.setupUi(Form_Pokedex)

# Page d'accueil
Window = QtWidgets.QMainWindow()
ui_MainWindow = MainWindow()
ui_MainWindow.setupUi(Window)
ui_MainWindow.pushButton_2.clicked.connect(afficheFirstConnection)
ui_MainWindow.pushButtonValider.clicked.connect(ui_MainWindow.verifyLogin)
ui_MainWindow.pushButtonValider.clicked.connect(check)

# Page first connection
First_Connection = QtWidgets.QWidget()
app.setQuitOnLastWindowClosed(True)
ui_Form = FirstConnection(First_Connection)
ui_Form.pushButton.clicked.connect(afficheFirstPokemon)

# Page des premiers pokémons
Form_Pokemon = QtWidgets.QWidget()
ui_Pokemon = Ui_FormPokemon()
ui_Pokemon.setupUi(Form_Pokemon)

# Message d'erreur si le login a déjà été utilisé
mess = QtWidgets.QWidget()
ui_erreur = Ui_erreur()
ui_erreur.setupUi(mess)

# Message d'erreur si le login ou mot de passe est incorrect
mess_err = QtWidgets.QWidget()
ui_erreur_log = Ui_erreur_login()
ui_erreur_log.setupUi(mess_err)

# Choisir son pokémon
def choisir_pokemon(pokemon):
    capturer(pokemon)
    openMap()

ui_Pokemon.pushButtonBulbasaur.clicked.connect(lambda checked, pokemon='Bulbasaur': choisir_pokemon(pokemon))
ui_Pokemon.pushButtonCharmander.clicked.connect(lambda checked, pokemon='Charmander': choisir_pokemon(pokemon))
ui_Pokemon.pushButtonSquirtle.clicked.connect(lambda checked, pokemon='Squirtle': choisir_pokemon(pokemon))

# Map
Map = PokemonMap()
Map.hide()  # Assurez-vous que la carte est cachée au début

app.setQuitOnLastWindowClosed(True)
Window.show()
sys.exit(app.exec_())