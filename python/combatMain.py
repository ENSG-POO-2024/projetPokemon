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
from new_combat import Ui_MainWindow
from PyQt5.QtCore import QTimer,QObject, pyqtSignal
# from image1_rc import *  # Import du module contenant les ressources


pikachu = dico_poke["Pikachu"]
bulbasaur = dico_poke["Bulbasaur"]

class MainWindow(QMainWindow):
    attackFinished = pyqtSignal()

    
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('combat.ui', self)  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Interface combat') 
        self.setWindowIcon(QIcon('votre_icone.ico')) 

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
        
        # self.simpleSig.connect(self.simpleSlot)#############test
        # self.attackFinished.connect(self.attack)
        
        ## Choix attaque/fuite
        ##Attaque
        self.ui.pushButton.setText("Attaque")
        self.ui.pushButton.clicked.connect(self.combat)
        ##Fuite
        self.ui.pushButton_2.setText("Fuite")
        self.ui.pushButton_2.clicked.connect(self.fuite)
        # self.attackFinished.connect(self.combat)
        
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_3.setText("...")
        self.ui.pushButton_4.setEnabled(False)
        self.ui.pushButton_4.setText("...")
        
        self.show()

    def desac_boutons(self):
        self.ui.pushButton.setEnabled(False)
        self.ui.pushButton_2.setEnabled(False)

    def desac_boutons_down(self):
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(False)
        
    def activ_boutons(self):
        self.ui.pushButton.setEnabled(True)
        self.ui.pushButton_2.setEnabled(True)
        
    def activ_boutons_down(self):
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(True)
        
    # def reinitialise(self):
    #     self.ui.pushButton.clicked.disconnect()
    #     self.ui.pushButton_2.clicked.disconnect()
        
        
        
        

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
            if pokemon2.HP<=0:
                pokemon2.HP=0
            else:
                pass
            
            
            ##Affichage des dégats    
            percent = int(100*pokemon2.HP/PV_def)
            self.ui.progressBar_2.setProperty("value",percent)
            self.ui.lcdNumber_2.display(pokemon2.HP)
            

        else:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                        \n C'est inefficace...
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
            ##Affichage des 
            if pokemon2.HP<=0:
                pokemon2.HP=0
            else:
                pass
            
            percent = int(100*pokemon2.HP/PV_def)
            self.ui.progressBar_2.setProperty("value",percent)
            self.ui.lcdNumber_2.display(pokemon2.HP)
            
           
        else:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                        \n C'est inefficace...
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
                if pokemon2.HP<=0:
                    pokemon2.HP=0
                else:
                    pass

                
                ##Affichage des dégats    
                percent = int(100*pokemon2.HP/PV_def)
                self.ui.progressBar_3.setProperty("value",percent)
                self.ui.lcdNumber_4.display(pokemon2.HP)
                
    
            else:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                            \n C'est inefficace...
                                        \n{pokemon2.name} ne perd aucun PV """)
                
        ## Attaque spéciale
        else:
            # self.set_text_attaque_speciale(pokemon2,pokemon1,PV_def)
            HP_perdus = pokemon1.Sattack-pokemon2.Sdef
        
            if HP_perdus>=0:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                        \n{pokemon2.name} perd {HP_perdus}PV !""")
                pokemon2.HP  -= HP_perdus
                if pokemon2.HP<=0:
                    pokemon2.HP=0
                else:
                    pass
                ##Affichage des dégats
                percent = int(100*pokemon2.HP/PV_def)
                self.ui.progressBar_3.setProperty("value",percent)
                self.ui.lcdNumber_4.display(pokemon2.HP)
               
            else:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                            \n C'est inefficace...
                                        \n{pokemon2.name} ne perd aucun PV !
                                        """)
       
        self.ui.textBrowser.append("fin attaque auto")
        
    def attack(self):
        print("test_attaque")
        ## Début du combat
        joueur = pikachu  # Pokemon du joueur
        sauvage = bulbasaur # Pokemon sauvage
        PV_att, PV_def = joueur.HP, sauvage.HP ##Attribution des pv
        
        
        
        # self.
        self.ui.pushButton.setEnabled(False)
        self.activ_boutons_down()
    
        # print("test")
        # print(f"{pikachu.HP}  PV DE PIKACHU")
        
        
    
            ## Cas où le joueur commence :
        if joueur.speed >= sauvage.speed:
            attaquant = joueur
            defenseur = sauvage
            
            
            if defenseur.HP ==0:
                QTimer.singleShot(1000, lambda: self.combat_perdu())
            elif attaquant.HP ==0:
                QTimer.singleShot(1000, lambda: self.combat_gagne())
            else:
                self.ui.textBrowser.setText(f"{attaquant.name} attaque ! Choisissez votre attaque")
        
 
            
                
                ## Choix de l'attaque
            self.ui.pushButton_3.setText("Attaque Neutre")
            self.ui.pushButton_4.setText("Attaque Spéciale")
                
                ## Connecter les signaux des boutons à des fonctions qui gèrent les attaques
                ## Désactive les boutons en attendant l'attaque automatique 
            
            
            ##Action bouton 1
            self.ui.pushButton_3.clicked.connect(lambda: self.set_text_attaque_neutre(attaquant, defenseur,PV_def))
            self.ui.pushButton_3.clicked.connect(self.desac_boutons_down)
            self.ui.pushButton_3.clicked.connect(lambda: QTimer.singleShot(2000, lambda: self.attaque_auto(defenseur,attaquant,PV_att)))
            
            ### GROS TEST 
            # self.ui.pushButton_3.clicked.connect(lambda:QTimer.singleShot(4000, lambda: self.activ_boutons_down()))
            self.ui.pushButton_3.clicked.connect(lambda:QTimer.singleShot(4000, lambda: self.combat()))
            
            ##Action bouton 2
            self.ui.pushButton_4.clicked.connect(lambda: self.set_text_attaque_speciale(attaquant, defenseur,PV_def))
            self.ui.pushButton_4.clicked.connect(self.desac_boutons_down)
            self.ui.pushButton_4.clicked.connect(lambda: QTimer.singleShot(2000, lambda: self.attaque_auto(defenseur, attaquant, PV_att)))
            
            ### GROS TEST
            self.ui.pushButton_4.clicked.connect(lambda:QTimer.singleShot(4000, lambda: self.combat()))
            

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
        # self.simpleSig.emit()
        

        
        
        self.attackFinished.emit()

        

        return()
        
        
    def combat(self):
        self.attack()
        self.activ_boutons_down()


    def combat_gagne(self):
        self.ui.textBrowser.setText(f"Le {bulbasaur.name} ennemi est K.O ! ")
        self.desac_boutons_down()
        self.desac_boutons()
        
        QTimer.singleShot(3000, lambda: self.close())
        
    def combat_perdu(self):
        self.ui.textBrowser.setText(f"{pikachu.name}est K.O ! ")
        QTimer.singleShot(3000, lambda: self.close())
        

    
    
    def fuite(self):
        self.ui.textBrowser.setText("Vous avez choisi de fuir !")
        QTimer.singleShot(3000, lambda: self.close())
        # self.close()
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
    