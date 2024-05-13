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


pikachu = dico_poke["Pikachu"]
bulbasaur = dico_poke["Bulbasaur"]

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
        self.ui.pushButton.clicked.connect(self.combat)
        ##Fuite
        self.ui.pushButton_2.clicked.connect(self.fuite)
        self.show()

    def desac_boutons(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)

        
    def activ_boutons(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        
    def reinitialise(self):
        self.ui.pushButton.clicked.disconnect()
        self.ui.pushButton_2.clicked.disconnect()
        
        
        
        

    def set_text_attaque_neutre(self,pokemon1,pokemon2,PV_def):
        """
        Définit ce qu'il se passe lorsque l'on clique sur attaque neutre
        """
        ##Calculs des dégats

        HP_perdus = pokemon1.attack-pokemon2.defense
        
        
        if HP_perdus>=0:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                    \n{pokemon2.name} perd {HP_perdus}PV """)
            pokemon2.HP -= HP_perdus
            
            
            ##Affichage des dégats    
            percent = int(100*pokemon2.HP/PV_def)
            self.ui.progressBar_2.setProperty("value",percent)
            self.ui.lcdNumber_2.display(pokemon2.HP)
            

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
        
            
            if HP_perdus>=0:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                        \n{pokemon2.name} perd {HP_perdus}PV """)
                pokemon2.HP -= HP_perdus
                
                ##Affichage des dégats    
                percent = int(100*pokemon2.HP/PV_def)
                self.ui.progressBar_3.setProperty("value",percent)
                self.ui.lcdNumber_4.display(pokemon2.HP)
                
    
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
       
        self.ui.textBrowser.append("fin attaque auto")
        
    def attack(self):
        ## Début du combat
        joueur = pikachu  # Pokemon du joueur
        sauvage = bulbasaur # Pokemon sauvage
        PV_att, PV_def = joueur.HP, sauvage.HP ##Attribution des pv
        
        
        ## Mise à zéro des slots
        self.activ_boutons()
        self.reinitialise()
        
    
        print("test")
        print(f"{pikachu.HP}  PV DE PIKACHU")
        
    
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
            self.ui.pushButton.clicked.connect(lambda: QTimer.singleShot(3000, lambda: self.attaque_auto(defenseur,attaquant,PV_att)))
            
            
            ##Action bouton 2
            self.ui.pushButton_2.clicked.connect(lambda: self.set_text_attaque_speciale(attaquant, defenseur,PV_def))
            self.ui.pushButton_2.clicked.connect(self.desac_boutons)
            self.ui.pushButton_2.clicked.connect(lambda: QTimer.singleShot(3000, lambda: self.attaque_auto(defenseur, attaquant, PV_att)))
            print("fin de tour")
            
            
    
        else:
            pass
            # ##Attaque auto puis attaque du joueur 
            #     PV_att, PV_def = PV_def, PV_att
            #     attaquant = sauvage
            #     defenseur = joueur
                
            #     self.ui.textBrowser.setText(f"Début du combat !\n{joueur.name} VS {sauvage.name} \n{sauvage.name} vous attaque !")
            #     self.desac_boutons()
            #     self.attaque_auto(attaquant, defenseur,PV_def)
            #     QTimer.singleShot(3000, lambda: self.activ_boutons())
            #     # self.ui.textBrowser.setText(f"{attaquant.name} attaque ! Choisissez votre attaque")
                
            #     ## Choix de l'attaque 
                
            #     self.ui.pushButton.setText("Attaque Neutre")
            #     self.ui.pushButton_2.setText("Attaque Spéciale")
            #     ##Action bouton 1
            #     self.ui.pushButton.clicked.connect(lambda: self.set_text_attaque_neutre( defenseur,attaquant,PV_def))
            #     self.ui.pushButton.clicked.connect(self.desac_boutons)
                
                
            #     ##Action bouton 2
            #     self.ui.pushButton_2.clicked.connect(lambda: self.set_text_attaque_speciale( defenseur,attaquant,PV_def))
            #     self.ui.pushButton_2.clicked.connect(self.desac_boutons)
            #     self.ui.textBrowser.append("fin du tour test")
            #     return()   
        # if PV_def <= 0 or PV_att <=0:
        #     # break
        #     self.ui.textBrowser.append(f"{defenseur.name} a été vaincu !")
        #     self.ui.textBrowser.append(f"{attaquant.name} remporte la victoire !")
                
        #         # attaquant, defenseur = defenseur, attaquant
        #         # PV_att,PV_def = PV_def,PV_att
        #         # # Changer de rôle entre attaquant et défenseur pour le prochain tour
        
        return()
        
        
    def combat(self):
        for i in range(0,5):
            print(f"test {i}")
            self.attack()
            i+=1
            
            # if pikachu.HP <=0 or pigeon.HP<=0:
            #     self.ui.textBrowser.setText(f"le combat est perdu ")
            #     return()

    
    
    
    
    
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
    pigeon = dico_poke['Pidgeot']

    main()
    