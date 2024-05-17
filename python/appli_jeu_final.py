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
from Map_Def import PokemonMap
import os
import json
data =  os.path.join(os.path.dirname(__file__),'data', 'data_user.json')


import sys



class App:
    def __init__(self):
        
        #Page d'accueil
        self.Window = QtWidgets.QMainWindow()
        self.ui_MainWindow = MainWindow()
        self.ui_MainWindow.setupUi(self.Window)

        self.ui_MainWindow.pushButton_2.clicked.connect(self.afficheFirstConnection) #ouvrir la page first connection
        #self.ui_MainWindow.pushButtonValider.clicked.connect(self.ui_MainWindow.verifyLogin) # Connecter le bouton de connexion à la fonction de vérification
        self.ui_MainWindow.pushButtonValider.clicked.connect(self.check) # Charger tout les données de l'utilisateur


            

        self.Window.show()

    #afficher la page first connection
    def afficheFirstConnection(self):
        
        #Page first connection
        self.First_Conection = QtWidgets.QWidget()
        
        
        self.ui_Form = FirstConnection(self.First_Conection)
        
        self.ui_Form.pushButton.clicked.connect(self.afficheFirstPokemon) #afficher la page de choix de pokémon

        self.Window.close()
        self.First_Conection.show()
        


    #afficher la page first pokémon
    def afficheFirstPokemon(self):
        
        texte = "ID already exists. Please choose another username."
        Text, self.FirstID = self.ui_Form.verifyAndRegister()
        
        #Map
        self.map = PokemonMap(self.FirstID)
        self.map.hide() #il reste cacher pour le moment
    
        #si le login n'a jamais encore été utilisé alors on ouvre la nouvelle fenêtre et on choisit nos pokémon
        if Text != texte:
            

            
            #page des premieres pokémon
            self.Form_Pokemon = QtWidgets.QWidget()
            self.ui_Pokemon = Ui_FormPokemon(self.Form_Pokemon)
            # self.ui_Pokemon.setupUi(self.Form_Pokemon)
            
            self.First_Conection.close() #fermer la page précédente
            self.Form_Pokemon.show() 
            print("ID :",self.FirstID)
            
            
            #Choisir son pokémon
            #Utilisation de lambda car la fonction clicked.connect ne reconnait pas les paramètres des fonctions qui se trouvent à l'intérieur
            self.ui_Pokemon.pushButtonBulbasaur.clicked.connect(lambda checked, pokemon = 'Bulbasaur', ID =  self.FirstID: self.ui_Pokemon.enregistrer(pokemon,ID))#enregistrer le pokémons choisi dans le fichier
            self.ui_Pokemon.pushButtonBulbasaur.clicked.connect(lambda checked, FirstID = self.FirstID  : self.map.ui_pokedex.laoding(FirstID))#importer depuis le fichier json dans le pokédex
            self.ui_Pokemon.pushButtonBulbasaur.clicked.connect(self.openMap)

            self.ui_Pokemon.pushButtonCharmander.clicked.connect(lambda checked, pokemon = 'Charmander', ID =  self.FirstID :self.ui_Pokemon.enregistrer(pokemon, ID))
            self.ui_Pokemon.pushButtonCharmander.clicked.connect(lambda checked, FirstID = self.FirstID  : self.map.ui_pokedex.laoding(FirstID))#importer depuis le fichier json dans le pokédex
            self.ui_Pokemon.pushButtonCharmander.clicked.connect(self.openMap)

            self.ui_Pokemon.pushButtonSquirtle.clicked.connect(lambda checked, pokemon ='Squirtle', ID =  self.FirstID : self.ui_Pokemon.enregistrer(pokemon,ID))
            self.ui_Pokemon.pushButtonSquirtle.clicked.connect(lambda checked, FirstID = self.FirstID  : self.map.ui_pokedex.laoding(FirstID))#importer depuis le fichier json dans le pokédex
            self.ui_Pokemon.pushButtonSquirtle.clicked.connect(self.openMap)

            


    
        else:
            #message d'erreur si le login a déjà été utilisé
            self.mess = QtWidgets.QWidget()
            self.ui_erreur = Ui_erreur()
            self.ui_erreur.setupUi(self.mess)


            self.mess.show()
            
    def check(self):
        """
         la fonction recharge la partie de l'utilisateur avec tous ses pokémons
    
        """
        texte = "Login failed. Please try again."
        Text, self.ID = self.ui_MainWindow.verifyLogin()
        
        #Map
        self.map = PokemonMap(self.ID)
        self.map.hide() #il reste cacher pour le moment
        
        #Si mot de passe et login correct
        if Text != texte:

            self.map.ui_pokedex.laoding(self.ID)
            
            #Fermeture de tous les fenêtres inutiles
            self.Window.close()
            self.map.show()

            
                
        else:
            #message d'erreur si le login ou mot de passe incorrect
            self.mess_err = QtWidgets.QWidget()
            self.ui_erreur_log = Ui_erreur_login()
            self.ui_erreur_log.setupUi(self.mess_err)
            self.mess_err.show()
        

        
            

    
    def openMap(self):
        self.map.show()
        
        self.Form_Pokemon.close()# on ferme la page des choix de pokémon


    


    
    

 
if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    application = App()
    sys.exit(app.exec_())#exécuter l'app
    app.setQuitOnLastWindowClosed(True)









    








