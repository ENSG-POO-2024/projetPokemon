import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QDialog
from combatui import Ui_Form  
from monat import Rencontre,Dresseur,Starter,Combat
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5.QtCore import QTimer,Qt 
import random
import pandas as pd

class FightWindow(QDialog):
    def __init__(self, pokemon=None):
        super(FightWindow, self).__init__()
        loadUi("CODE/welcome2.ui", self)  # Assurez-vous de renseigner le bon chemin vers votre fichier UI
        self.ui = Ui_Form()  # Instancier l'interface utilisateur
        self.ui.setupUi(self)  # Initialiser l'interface utilisateur dans la fenêtre

        # Ajoutez des fonctionnalités de clic aux boutons en définissant des fonctions correspondantes
        self.ui.pushButton.clicked.connect(self.round)
        self.ui.pushButton_2.clicked.connect(self.attaquer_sp2)
        self.ui.pushButton_3.clicked.connect(self.fuite)
        self.ui.pushButton_4.clicked.connect(self.changer_pokemon)
 
        df = pd.read_csv("data/merged_data_fr.csv")
        
            
        
                   
        Dresseur1 = Dresseur("Sacha")
        Starter(Dresseur1,'Charmander','Bulbasaur','Squirtle')
        self.cb=Rencontre(Dresseur1,(16,57))
        
        self.num_pok_dress = df.loc[df['Name'] == 'Charmander', '#'].values  
        num_pok_sauv= df.loc[(df['coord_x'] == 16) & (df['coord_y'] == 57),'#'].values
        print(num_pok_sauv)
        self.label_3.clear()
        self.changer_image_pok_adv(num_pok_sauv[0])
        
        
        
        self.phrases_intro = [
        f"Le combat entre {self.cb.joueur.name} et {self.cb.combat.pokemon_adversaire.name} commence !",
        f"Un {self.cb.combat.pokemon_adversaire.name} sauvage apparait !",
        f"{self.cb.joueur.pokemon_equipe[0]} ! Go!",]
        self.compteur=0
        self.set_dialogue_text(self.phrases_intro[self.compteur])
        self.compteur += 1  
        
        self.ui.progressBar_adv.setValue(self.cb.combat.pokemon_adversaire.pv)
        self.ui.progressBar_pv.setValue(self.cb.joueur.pokemon_equipe[0].pv)
        self.ui.progressBar_adv.setStyleSheet("QProgressBar::chunk { background-color: red; }")
        self.ui.progressBar_pv.setStyleSheet("QProgressBar::chunk { background-color: blue; }")

        
        
        

    
    #je veux attaquer le pokemon adverse
    def attaquer(self):
        self.cb.combat.attaquer(self.cb.joueur.pokemon_equipe[0],self.cb.combat.pokemon_adversaire)
        self.afficher_autre_texte(f"{self.cb.joueur.pokemon_equipe[0].name} attaque !\n next..")
        #mettre a jour la progress bar  de l'adversaire
        
        #si le pokemon adverse est KO
        if self.cb.combat.pokemon_adversaire.tout_est_ko():
            self.afficher_autre_texte(f"{self.cb.combat.pokemon_adversaire.name} est KO !\n next..")
            #si le joueur a gagné
            if self.cb.combat.est_fini():
                self.afficher_autre_texte(f"Vous avez gagné !\n next..")
                #mettre a jour la progress bar  du joueur
                self.ui.progressBar.setValue(self.cb.joueur.pokemon_equipe[0].pv)
                #si le joueur a perdu
            else:
                self.afficher_autre_texte(f"{self.cb.joueur.pokemon_equipe[0].name} est KO !\n next..")
                self.afficher_autre_texte(f"Vous avez perdu !\n next..")
                #mettre a jour la progress bar  du joueur  



        


            
        #self.set_dialogue_text(f"Le combat entre {self.cb.joueur.name} et {self.cb.combat.pokemon_adversaire.name} commence !")
        #self.afficher_autre_texte(f"Un {self.cb.combat.pokemon_adversaire.name} sauvage apparait !\n next..")
        #self.ui.dialogue.installEventFilter(self)
        
        # Utiliser un QTimer pour mettre à jour périodiquement la boucle de combat
        #self.timer = QTimer(self)
        #self.timer.timeout.connect(self.update_combat)
        #self.timer.start(1000)  # Mettre à jour toutes les secondes

       
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Vérification si toutes les phrases ont été affichées
            
            if self.compteur < len(self.phrases_intro):
                # Affichage de la prochaine phrase d'introduction
                self.set_dialogue_text(self.phrases_intro[self.compteur])
                self.compteur += 1
            else:
                # Affichage d'un message lorsque toutes les phrases ont été affichées
                self.changer_image_pok(self.num_pok_dress[0])
                self.set_dialogue_text("Que voulez-vous faire ?")
    
    
    
    
    
    

    def attaquer_sp2(self):
        # Code pour l'action de la deuxième attaque spéciale
        self.set_dialogue_text("Deuxième attaque spéciale lancée")

    def fuite(self):
        """
        Gère l'action de fuite dans la fenêtre de combat.
        """
        if self.cb.combat.fuir():
            self.set_dialogue_text("Fuite réussie !")
        else:
            self.set_dialogue_text("Impossible de fuir !")
            
    def utiliser_charge(self):
        """
        Gère l'action d'utiliser l'attaque 'Charge' dans la fenêtre de combat.
        """
        if self.cb.combat.utiliser_charge():
            self.set_dialogue_text("Votre Pokémon utilise Charge !")
            self.ui.progressBar_adv.setValue(self.ui.progressBar_adv.value() - 6)
        else:
            self.set_dialogue_text("Impossible d'utiliser l'attaque Charge !")
            
            
    def defendre(self):
        self.cb.combat.attaquer_adversaire()
        
        self.ui.progressBar_pv.setValue(self.ui.progressBar_pv.value() - 6)
        
    def changer_image_pok(self,numero):
        self.label_3.setPixmap(QPixmap(f"CODE/image tiles/pokemon_Combat/back/{numero}.png"))
        self.label_3.setScaledContents(True)
    
    def changer_image_pok_adv(self,numero):
        self.label_4.setPixmap(QPixmap(f"CODE/image tiles/pokemon_Combat/front/{numero}.png"))
        self.label_4.setScaledContents(True)
       
            
    
    def round(self):
        # Code pour un round de combat
        # on regarde qui attaque en premier 
        if self.cb.joueur.pokemon_equipe[0].stats['Sp. Atk']>=self.cb.combat.pokemon_adversaire.stats['Sp. Atk']:
            
            self.utiliser_charge()
            self.defendre()
            self.set_dialogue_text("Vous avez été plus rapide!")
            
            
        else:
            
            self.defendre()
            self.utiliser_charge()
            self.set_dialogue_text("Il a été plus rapide!")
            
            

    def changer_pokemon(self):
        # Code pour l'action de changer de Pokémon
        self.set_dialogue_text("Changement de Pokémon")
        

    def afficher_autre_texte(self,texte):
        # Fonction pour afficher un autre texte lorsque la touche "Entrée" est pressée
        self.set_dialogue_text(texte)

    def set_dialogue_text(self, text):
        self.ui.dialogue.setPlainText(text)
        font_id = QFontDatabase.addApplicationFont("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/data/police.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family)
        self.ui.dialogue.setFont(font)
        self.ui.dialogue.setStyleSheet("background-color: rgba(0,0,0,0); margin: 10px; padding: 0px;")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = FightWindow()
    dialog.show()
    sys.exit(app.exec_())
