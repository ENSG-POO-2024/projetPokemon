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
import random
import pokemon
from pokemon import Pokemon, dico_poke
from combat import Ui_MainWindow  
from PyQt5.QtCore import QTimer
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
    def desac_boutons(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)

        
    def set_text_attaque_neutre(self,pokemon1,pokemon2,PV_def):
        """
        Définit ce qu'il se passe lorsque l'on clique sur attaque neutre
        """
        ##Calculs des dégats

        HP_perdus = pokemon1.attack-pokemon2.defense
        
        print("test1 -avant attaque",pokemon2.HP)
        if HP_perdus>=0:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                    \n{pokemon2.name} perd {HP_perdus}PV """)
            pokemon2.HP -= HP_perdus
            
            ##Affichage des dégats    
            percent = int(100*pokemon2.HP/PV_def)
            self.ui.progressBar_2.setProperty("value",percent)
            self.ui.lcdNumber_2.display(pokemon2.HP)
            print("test2 - après attaque",pokemon2.HP)

        else:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                    \n{pokemon2.name} ne perd aucun PV """)
                                    
                                    
                        
        
    def set_text_attaque_speciale(self,pokemon1,pokemon2,PV_def):
        """
        Définit ce qu'il se passe lorsque l'on clique sur attaque spéciale
        """
        HP_perdus = pokemon1.Sattack-pokemon2.Sdef
        
        if HP_perdus>=0:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                    \n{pokemon2.name} perd {HP_perdus}PV !""")
            pokemon2.HP  -= HP_perdus
            ##Affichage des dégats
            percent = int(100*pokemon2.HP/PV_def)
            self.ui.progressBar_2.setProperty("value",percent)
            self.ui.lcdNumber_2.display(pokemon2.HP)
           
        else:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                    \n{pokemon2.name} ne perd aucun PV !""")
                                          
                    
        
    def attaque_auto(self,pokemon1,pokemon2,PV_def):
        nombre = random.randint(0,2)
        
        ## Attaque neutre
        if nombre ==1:

            HP_perdus = pokemon1.attack-pokemon2.defense
        
            print("test1 -avant attaque",pokemon2.HP)
            if HP_perdus>=0:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                        \n{pokemon2.name} perd {HP_perdus}PV """)
                pokemon2.HP -= HP_perdus
                
                ##Affichage des dégats    
                percent = int(100*pokemon2.HP/PV_def)
                self.ui.progressBar_3.setProperty("value",percent)
                self.ui.lcdNumber_4.display(pokemon2.HP)
                print("test2 - après attaque",pokemon2.HP)
    
            else:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                        \n{pokemon2.name} ne perd aucun PV """)
                
        ## Attaque spéciale
        else:
            # self.set_text_attaque_speciale(pokemon2,pokemon1,PV_def)
            HP_perdus = pokemon1.Sattack-pokemon2.Sdef
        
            if HP_perdus>=0:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                        \n{pokemon2.name} perd {HP_perdus}PV !""")
                pokemon2.HP  -= HP_perdus
                ##Affichage des dégats
                percent = int(100*pokemon2.HP/PV_def)
                self.ui.progressBar_3.setProperty("value",percent)
                self.ui.lcdNumber_4.display(pokemon2.HP)
               
            else:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                        \n{pokemon2.name} ne perd aucun PV !""")
        print("validation attaque auto")
        
    def attack(self):
        ## Début du combat
        joueur = pikachu  # Pokemon du joueur
        sauvage = bulbasaur # Pokemon sauvage
        PV_att, PV_def = joueur.HP, sauvage.HP ##Attribution des pv
    
        self.ui.textBrowser.setText(f"Début du combat !\n{joueur.name} VS {sauvage.name} \nQuelle attaque choisissez-vous ?")
        
        ## Déroulé du combat 
        # if joueur.speed >= sauvage.speed: ##Cas où le joueur commence
        #     attaquant = joueur
        #     defenseur = sauvage
        # else:
        #     PV_att, PV_def = PV_def, PV_att  # On échange les PV 
        #     attaquant = sauvage
        #     defenseur = joueur
            
        
            ## Cas où le joueur commence :
        if joueur.speed >= sauvage.speed:
   
            attaquant = joueur
            defenseur = sauvage
 
            self.ui.textBrowser.setText(f"{attaquant.name} attaque ! Choisissez votre attaque")
                
                ## Choix de l'attaque
            self.ui.pushButton.setText("Attaque Neutre")
            self.ui.pushButton_2.setText("Attaque Spéciale")
                
                ## Connecter les signaux des boutons à des fonctions qui gèrent les attaques
                ## Désactive les boutons en attendant l'attaque automatique 
            
            ##Action bouton 1
            self.ui.pushButton.clicked.connect(lambda: self.set_text_attaque_neutre(attaquant, defenseur,PV_def))
            self.ui.pushButton.clicked.connect(self.desac_boutons)
            self.ui.pushButton.clicked.connect(lambda: self.attaque_auto(defenseur,attaquant,PV_att))
            
            
            ##Action bouton 2
            self.ui.pushButton_2.clicked.connect(lambda: self.set_text_attaque_speciale(attaquant, defenseur,PV_def))
            self.ui.pushButton_2.clicked.connect(self.desac_boutons)
            self.ui.pushButton_2.clicked.connect(lambda: self.attaque_auto(defenseur,attaquant,PV_att))
            
            # #Activer le bouton après un délai de 3 secondes
            # timer = QTimer()
            # timer.singleShot(3000, lambda: self.ui.pushButton.setEnabled(True))
            # timer.singleShot(3000, lambda: self.ui.pushButton_2.setEnabled(True))
            
               ##Puis attaque auto

            
            # self.ui.pushButton.setEnabled(True)
            # self.ui.pushButton_2.setEnabled(True)
                
    
        else:
            PV_att, PV_def = PV_def, PV_att
            attaquant = sauvage
            defenseur = joueur
            
                # Simulation de l'attaque automatique
            self.ui.pushButton.setEnabled(False)
            self.attaque_auto(attaquant, defenseur)
            self.ui.pushButton.setEnabled(True)
            # Mettre à jour le texte dans textBrowser pour refléter le combat
            self.ui.textBrowser.append(f"{defenseur.name} perd {attaquant.attack} PV.")
            self.ui.textBrowser.append(f"{defenseur.name} a maintenant {defenseur.HP} PV.")
    
            # Vérifier si le Pokémon défenseur a été vaincu
        
        if PV_def <= 0 or PV_att <=0:
            # break
            self.ui.textBrowser.append(f"{defenseur.name} a été vaincu !")
            self.ui.textBrowser.append(f"{attaquant.name} remporte la victoire !")
                
                # attaquant, defenseur = defenseur, attaquant
                # PV_att,PV_def = PV_def,PV_att
                # # Changer de rôle entre attaquant et défenseur pour le prochain tour
        
            
        
        
        
        
        
        
   
    def fuite(self):
        self.ui.textBrowser.setText("Vous avez choisi de fuir !")
        ## Voir comment on peut sortir de la fenetre + fin du combat 


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setQuitOnLastWindowClosed(True)  
    sys.exit(app.exec_())


if __name__ == "__main__":
    
    pikachu = dico_poke["Pikachu"]
    bulbasaur = dico_poke["Bulbasaur"]
    

    main()
    