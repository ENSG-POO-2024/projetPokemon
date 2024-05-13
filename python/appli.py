# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:25:39 2024

@author: Formation
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from page_accueil import MainWindow, Ui_erreur_login
from first_connection import FirstConnection, Ui_erreur
from premier_pokemon import Ui_FormPokemon
from pokedex import Ui_FormPokedex
from Marche_BCP import PokemonMap
import os
import json
data =  os.path.join(os.path.dirname(__file__),'data', 'data_user.json')


import sys


#afficher la page first connection
def afficheFirstConnection():
    Window.close()
    First_Conection.show()

#afficher la page first pokémon
def afficheFirstPokemon():
    
    texte = "ID already exists. Please choose another username."
    Text, ID = ui_Form.verifyAndRegister()

    #si le login n'a jamais encore été utilisé alors on ouvre la nouvelle fenêtre et on choisit nos pokémon
    if Text != texte:
        #fonction de vérification
        First_Conection.close()
        Form_Pokemon.show()
        return ID

    else:
        mess.show()
    
        
def capturer(pokemon):
    """
    La fonction enregistre les pokémons capturés dans  my pokemons

    """

    ui_Pokedex.listWidgetMesPokemons.addItem(QtWidgets.QListWidgetItem(pokemon))
    Text, ID = ui_MainWindow.verifyLogin()
    
    #Si le ID est vide alors on est dans first coonection
    if ID == '':
        Text, ID =  ui_Form.verifyAndRegister()
        with open(data, "r") as file:
            users = json.load(file)
        users[ID]['MyPokemons'].append(pokemon)
        
        #Modifier le fichier
        with open(data, "w") as file:
            json.dump(users, file)
        
    
    #Si pas première connexion
    else:
        Text, ID =  ui_Form.verifyAndRegister()
        with open(data, "r") as file:
            users = json.load(file)
        users[ID]['MyPokemons'].append(pokemon)
        
        #Modifier le fichier
        with open(data, "w") as file:
            json.dump(users, file) 


    


    
def openMap():
    Map.show()
    
    #Fermeture de tous les fenêtres inutiles
    First_Conection.close()
    Window.close()
    Form_Pokemon.close()
    
    

def openPokedex():
    Form_Pokedex.show()
        
def check():
    """
     la fonction recharge la partie de l'utilisateur avec tous ses pokémons

    """
    texte = "Login failed. Please try again."
    Text, ID = ui_MainWindow.verifyLogin()
    
    #Si mot de passe et login correct
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


#Pokédex
Form_Pokedex = QtWidgets.QWidget()
ui_Pokedex = Ui_FormPokedex()
Pokedex = ui_Pokedex.setupUi(Form_Pokedex)



#Page d'accueil
Window = QtWidgets.QMainWindow()
ui_MainWindow = MainWindow()
ui_MainWindow.setupUi(Window)
ui_MainWindow.pushButton_2.clicked.connect(afficheFirstConnection) #ouvrir la page first connection
ui_MainWindow.pushButtonValider.clicked.connect(ui_MainWindow.verifyLogin) # Connecter le bouton de connexion à la fonction de vérification
ui_MainWindow.pushButtonValider.clicked.connect(check) # Charger tout les données de l'utilisateur


#Page first connection
First_Conection = QtWidgets.QWidget()
app.setQuitOnLastWindowClosed(True)
ui_Form = FirstConnection(First_Conection)
ui_Form.pushButton.clicked.connect(afficheFirstPokemon) #afficher la page de choix de pokémon



#page des premieres pokémon
Form_Pokemon = QtWidgets.QWidget()
ui_Pokemon = Ui_FormPokemon()
ui_Pokemon.setupUi(Form_Pokemon)
    
#message d'erreur si le login a déjà été utilisé
mess = QtWidgets.QWidget()
ui_erreur = Ui_erreur()
ui_erreur.setupUi(mess)

#message d'erreur si le login ou mot de passe incorrect
mess_err = QtWidgets.QWidget()
ui_erreur_log = Ui_erreur_login()
ui_erreur_log.setupUi(mess_err)






#Choisir son pokémon
# ui_Pokemon.pushButtonBulbasaur.clicked.connect(lambda checked, pokemon = 'Bulbasaur' : ui_Pokemon.choixpoke_init(pokemon))
#Utilisation de lambda car la fonction clicked.connect ne reconnait pas les paramètres des fonctions qui se trouvent à l'intérieur
ui_Pokemon.pushButtonBulbasaur.clicked.connect(lambda checked, pokemon = 'Bulbasaur'  : capturer(pokemon))
ui_Pokemon.pushButtonBulbasaur.clicked.connect(openMap)
ui_Pokemon.pushButtonCharmander.clicked.connect(lambda checked, pokemon = 'Charmander' :capturer(pokemon))
ui_Pokemon.pushButtonCharmander.clicked.connect(openMap)
ui_Pokemon.pushButtonSquirtle.clicked.connect(lambda checked, pokemon ='Squirtle' : capturer(pokemon))
ui_Pokemon.pushButtonSquirtle.clicked.connect(openMap)

#Map
Map = PokemonMap()
Map.button.clicked.connect(openPokedex)





app.setQuitOnLastWindowClosed(True)
Window.show()
#exécuter l'app
sys.exit(app.exec_())