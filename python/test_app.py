# -*- coding: utf-8 -*-
"""
Created on Wed May 15 13:31:55 2024

@author: sylvi
"""
from PyQt5 import QtCore, QtGui, QtWidgets
from page_accueil import MainWindow, Ui_erreur_login
from first_connection import FirstConnection, Ui_erreur
from premier_pokemon import Ui_FormPokemon
from pokedex import Ui_FormPokedex
from Marche_BCP_moi import PokemonMap
import os
import json
data =  os.path.join(os.path.dirname(__file__),'data', 'data_user.json')


import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtCore import QTimer
import sys
import json

# Assurez-vous que toutes les classes comme Ui_FormPokedex, MainWindow, etc. sont correctement importées ou définies.

def afficheFirstConnection():
    Window.close()
    First_Connection.show()

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

Form_Pokedex = QtWidgets.QWidget()
ui_Pokedex = Ui_FormPokedex()
Pokedex = ui_Pokedex.setupUi(Form_Pokedex)

Window = QtWidgets.QMainWindow()
ui_MainWindow = MainWindow()
ui_MainWindow.setupUi(Window)
ui_MainWindow.pushButton_2.clicked.connect(afficheFirstConnection)
ui_MainWindow.pushButtonValider.clicked.connect(lambda: [ui_MainWindow.verifyLogin(), check()])

First_Connection = QtWidgets.QWidget()
app.setQuitOnLastWindowClosed(True)
ui_Form = FirstConnection(First_Connection)
ui_Form.pushButton.clicked.connect(afficheFirstPokemon)

Form_Pokemon = QtWidgets.QWidget()
ui_Pokemon = Ui_FormPokemon()
ui_Pokemon.setupUi(Form_Pokemon)

mess = QtWidgets.QWidget()
ui_erreur = Ui_erreur()
ui_erreur.setupUi(mess)

mess_err = QtWidgets.QWidget()
ui_erreur_log = Ui_erreur_login()
ui_erreur_log.setupUi(mess_err)

def open_new_interface(event):
    # Fonction pour ouvrir une nouvelle interface
    new_interface = QtWidgets.QWidget()  # Créez une instance de QWidget
    ui_pokedex = PokemonMap()  # Créez une instance de votre classe Ui_FormPokedex
    ui_pokedex.setupUi(new_interface)  # Appelez la méthode setupUi() avec votre nouvelle interface en tant qu'argument
    new_interface.show()

ui_Pokemon.pushButtonBulbasaur.clicked.connect(lambda: [capturer('Bulbasaur'), openMap()])
ui_Pokemon.pushButtonCharmander.clicked.connect(lambda: [capturer('Charmander'), openMap()])
ui_Pokemon.pushButtonSquirtle.clicked.connect(lambda: [capturer('Squirtle'), openMap()])
button_label.mousePressEvent = open_new_interface()



# Map = PokemonMap()

app.setQuitOnLastWindowClosed(True)
Window.show()
sys.exit(app.exec_())