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
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui
import random
import pokemon
from pokemon import Pokemon, dico_poke
from new_combat import Ui_MainWindow  
from PyQt5.QtCore import QTimer,QObject, pyqtSignal
# from Marche import xan
# from image1_rc import *  # Import du module contenant les ressources

    
    
pikachu = dico_poke["Pikachu"]
bulbasaur = dico_poke["Bulbasaur"]

class CombatMain(QMainWindow):
    attackFinished = pyqtSignal()

    
    def __init__(self,arg1,arg2,photo1,photo2):
        super(CombatMain, self).__init__()
        loadUi('combat.ui', self)  
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Interface combat') 
        self.setWindowIcon(QIcon('votre_icone.ico')) 
        
        
        self.ui.label.setPixmap(QtGui.QPixmap(photo1))
        self.ui.label_2.setPixmap(QtGui.QPixmap(photo2))
        
        
        pokemon1 = dico_poke[arg1]
        pokemon2 = dico_poke[arg2]

        ## Set le nom des pokémons
        self.ui.label_8.setText(f"{pokemon1.name}")
        self.ui.label_5.setText(f"{pokemon2.name}")
        self.ui.textBrowser.setText(f"{pokemon2.name} vous attaque ! Voulez vous l'attaquer ou fuir ?")
        
        ##Définit les pv 
        self.ui.progressBar_2.setProperty("value",100)
        self.ui.progressBar_3.setProperty("value",100)
        
        
        
        PVfixe1 = pokemon1.HP
        PVfixe2 = pokemon2.HP
        self.PVfixe1 = PVfixe1
        self.PVfixe2 = PVfixe2
        

        self.ui.lcdNumber.display(PVfixe2)#Bouge pas
        self.ui.lcdNumber_3.display(PVfixe1)#Bouge pas 
        
        
        
        self.ui.lcdNumber_2.display(pokemon2.HP)
        self.ui.lcdNumber_4.display(pokemon1.HP)
        
        # self.simpleSig.connect(self.simpleSlot)#############test
        # self.attackFinished.connect(self.attack)
        
        ## Choix attaque/fuite
        ##Attaque
        self.ui.pushButton.setText("Attaque")
        self.ui.pushButton.clicked.connect(lambda: self.combat(pokemon1,pokemon2))
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
        
        
        
        

    def attaque_neutre(self,pokemon1,pokemon2,PVfixe2):
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
            percent = int(100*pokemon2.HP/PVfixe2)
            self.ui.progressBar_2.setProperty("value",percent)
            self.ui.lcdNumber_2.display(pokemon2.HP)
            

        else:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Neutre
                                        \n C'est inefficace...
                                    \n{pokemon2.name} ne perd aucun PV """)
                                    
        
                        
        
    def attaque_speciale(self,pokemon1,pokemon2,PVfixe2):
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

            percent = int(100*pokemon2.HP/PVfixe2)
            self.ui.progressBar_2.setProperty("value",percent)
            self.ui.lcdNumber_2.display(pokemon2.HP)
            
           
        else:
            self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                        \n C'est inefficace...
                                    \n{pokemon2.name} ne perd aucun PV !""")
        
                    
        
    def attaque_auto(self,pokemon1,pokemon2,PVfixe2):
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
                percent = int(100*pokemon2.HP/PVfixe2)
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
                percent = int(100*pokemon2.HP/PVfixe2)
                self.ui.progressBar_3.setProperty("value",percent)
                self.ui.lcdNumber_4.display(pokemon2.HP)
               
            else:
                self.ui.textBrowser.setText(f"""{pokemon1.name} lance Attaque Spéciale
                                            \n C'est inefficace...
                                        \n{pokemon2.name} ne perd aucun PV !
                                        """)
       
        self.ui.textBrowser.append("fin attaque auto")
        
    def attack(self,arg1,arg2):
        print(f"{arg1.HP} POKEMON 1")
        print(f"{arg2.HP} POKEMON 2")
        print("test_attaque")
        ## Début du combat
        joueur = arg1  # Pokemon du joueur
        sauvage = arg2 # Pokemon sauvage
        
        if arg1.HP ==0:
                QTimer.singleShot(1000, lambda: self.combat_gagne(arg2))
        elif arg2.HP ==0:
                QTimer.singleShot(1000, lambda: self.combat_perdu(arg1))
        else:
            pass
            
                
        
        # self.
        self.ui.pushButton.setEnabled(False)
        
    
        # print("test")
        # print(f"{pikachu.HP}  PV DE PIKACHU")
        
        
        self.ui.pushButton_3.setText("Attaque Neutre")
        self.ui.pushButton_4.setText("Attaque Spéciale")
            ## Cas où le joueur commence :
        

        if joueur.speed >= sauvage.speed:
            pass

        else:
            attaquant = sauvage
            defenseur = joueur
            QTimer.singleShot(2000, lambda: self.attaque_auto(defenseur,attaquant,self.PVfixe1))
            
        
        
        print(f"Test PV fixe : {self.PVfixe1}")
        print(f"Test PV fixe : {self.PVfixe2}")
        self.activ_boutons_down()
        attaquant = joueur
        defenseur = sauvage
        
        ##Action bouton 1
        QTimer.singleShot(4000, lambda : self.ui.textBrowser.setText(f"Vous attaquez ! \nQue doit faire {arg1.name} ?"))
        self.ui.pushButton_3.clicked.connect(lambda: self.attaque_neutre(attaquant, defenseur,self.PVfixe2))
        self.ui.pushButton_3.clicked.connect(self.desac_boutons_down)
        self.ui.pushButton_3.clicked.connect(lambda: QTimer.singleShot(3000, lambda: self.attaque_auto(defenseur,attaquant,self.PVfixe1)))
        
            ### GROS TEST 
            # self.ui.pushButton_3.clicked.connect(lambda:QTimer.singleShot(4000, lambda: self.activ_boutons_down()))
        self.ui.pushButton_3.clicked.connect(lambda:QTimer.singleShot(4000, lambda: self.combat(arg1,arg2)))
        
        ##Action bouton 2
        self.ui.pushButton_4.clicked.connect(lambda: self.attaque_speciale(attaquant, defenseur,self.PVfixe2))
        self.ui.pushButton_4.clicked.connect(self.desac_boutons_down)
        self.ui.pushButton_4.clicked.connect(lambda: QTimer.singleShot(3000, lambda: self.attaque_auto(defenseur, attaquant, self.PVfixe1)))
        
        ### GROS TEST
        self.ui.pushButton_4.clicked.connect(lambda:QTimer.singleShot(4000, lambda: self.combat(arg1,arg2)))
        
        print("fin de tour if")
        
        self.attackFinished.emit()

        return()
        
        
    def combat(self,arg1,arg2):
        self.attack(arg1,arg2)
        self.activ_boutons_down()


    def combat_gagne(self,arg1):
        self.ui.textBrowser.setText(f"Le {arg1.name} ennemi est K.O ! ")
        self.desac_boutons_down()
        self.desac_boutons()
        
        QTimer.singleShot(5000, lambda: self.close())
        
    def combat_perdu(self,arg2):
        self.ui.textBrowser.setText(f"{arg2.name} est K.O ! ")
        self.desac_boutons_down()
        self.desac_boutons()
        QTimer.singleShot(5000, lambda: self.close())
        

    
    
    def fuite(self):
        self.ui.textBrowser.setText("Vous avez choisi de fuir !")
        QTimer.singleShot(3000, lambda: self.close())
        # self.close()
        ## Voir comment on peut sortir de la fenetre + fin du combat 


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = CombatMain('Bulbasaur','Ivysaur',photo1,photo2)
    app.setQuitOnLastWindowClosed(True)  
    sys.exit(app.exec_())


if __name__ == "__main__":
    
    pikachu = dico_poke["Pikachu"]
    bulbasaur = dico_poke["Bulbasaur"]
    pigeon = dico_poke['Pidgeot']

    main()
    