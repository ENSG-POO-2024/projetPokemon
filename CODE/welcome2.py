import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QTextBrowser, QFrame,QDialog,QVBoxLayout

from PyQt5.QtGui import QFont, QFontDatabase,QPixmap
from PyQt5.uic import loadUi

class FightWindow(QDialog):
    def __init__(self,pokemon_data=None):
        super(FightWindow, self,).__init__()
        loadUi('/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/welcome2.ui', self)
        
        self.pokemon_data = pokemon_data
        self.showFullScreen()
        self.setWindowTitle("COMBAT !")
        
        
        # Connecter les boutons à des fonctions
        self.pushButton.clicked.connect(self.attaquer)
        self.pushButton_2.clicked.connect(self.attaquer_sp2)
        self.pushButton_3.clicked.connect(self.fuite)
        self.pushButton_4.clicked.connect(self.changer_pokemon)

        # Charger l'image du Pokémon défenseur et redimensionner le label
        self.set_image_pokemon_def("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/image tiles/pokemon_Combat/front/1.png")
        self.set_image_pokemon_att("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/image tiles/pokemon_Combat/back/1.png")
        self.set_dialogue_text("Un combat a commencé !")
        
        
    def attaquer(self):
        # Code pour l'action d'attaque
        print("Attaque lancée")

    def attaquer_sp2(self):
        # Code pour l'action de la deuxième attaque spéciale
        print("Deuxième attaque spéciale lancée")

    def fuite(self):
        # Code pour l'action de fuite
        print("Fuite lancée")

    def changer_pokemon(self):
        # Code pour l'action de changer de Pokémon
        print("Changement de Pokémon")

    def set_image_pokemon_def(self, image_path):
        pixmap = QPixmap(image_path).scaled(160, 160)
        self.label_4.setPixmap(pixmap)
        
    def set_image_pokemon_att(self, image_path):
        pass
    
    def set_dialogue_text(self, text):
        self.dialogue.setPlainText(text)
        font_id = QFontDatabase.addApplicationFont("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/data/police.ttf")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_family)
        self.dialogue.setFont(font)
        self.dialogue.setStyleSheet("background-color: rgba(0,0,0,0); margin: 10px; padding: 0px;")
    


    def load_pixmap(self, image_path, width, height):
        pixmap = QPixmap(image_path).scaled(width, height)
        return pixmap

print("oui je suis appélé")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FightWindow()
    sys.exit(app.exec_())
