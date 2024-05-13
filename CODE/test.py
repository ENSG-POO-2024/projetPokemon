import sys
from PyQt5.uic import loadUi
from PyQt5.QtGui import QPixmap, QFont, QFontDatabase
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt
import pandas as pd
from combatui import Ui_Form
from monat import Rencontre, Dresseur, Starter

class FightWindow(QDialog):
    def __init__(self):
        super(FightWindow, self).__init__()
        loadUi("CODE/welcome2.ui", self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.init_battle()

        self.ui.pushButton.clicked.connect(self.round)
        self.ui.pushButton_2.clicked.connect(self.attaquer_sp2)
        self.ui.pushButton_3.clicked.connect(self.fuite)
        self.ui.pushButton_4.clicked.connect(self.changer_pokemon)

    def init_battle(self):
        df = pd.read_csv("data/merged_data_fr.csv")

        Dresseur1 = Dresseur("Sacha")
        Starter(Dresseur1, 'Charmander', 'Bulbasaur', 'Squirtle')
        self.cb = Rencontre(Dresseur1, (16, 57))

        num_pok_sauv = df.loc[(df['coord_x'] == 16) & (df['coord_y'] == 57), '#'].values
        self.label_3.clear()
        self.changer_image_pok_adv(num_pok_sauv[0])

        self.phrases_intro = [
            f"Le combat entre {self.cb.joueur.name} et {self.cb.combat.pokemon_adversaire.name} commence !",
            f"Un {self.cb.combat.pokemon_adversaire.name} sauvage apparait !",
            f"{self.cb.joueur.pokemon_equipe[0]} ! Go!", ]
        self.compteur = 0
        self.set_dialogue_text(self.phrases_intro[self.compteur])
        self.compteur += 1

        self.ui.progressBar_adv.setValue(self.cb.combat.pokemon_adversaire.pv)
        self.ui.progressBar_pv.setValue(self.cb.joueur.pokemon_equipe[0].pv)
        self.ui.progressBar_adv.setStyleSheet("QProgressBar::chunk { background-color: red; }")
        self.ui.progressBar_pv.setStyleSheet("QProgressBar::chunk { background-color: blue; }")

    def attaquer(self):
        self.cb.combat.attaquer(self.cb.joueur.pokemon_equipe[0], self.cb.combat.pokemon_adversaire)
        self.afficher_autre_texte(f"{self.cb.joueur.pokemon_equipe[0].name} attaque !\n next..")
        if self.cb.combat.pokemon_adversaire.tout_est_ko():
            self.afficher_autre_texte(f"{self.cb.combat.pokemon_adversaire.name} est KO !\n next..")
            if self.cb.combat.est_fini():
                self.afficher_autre_texte(f"Vous avez gagné !\n next..")
            else:
                self.afficher_autre_texte(f"{self.cb.joueur.pokemon_equipe[0].name} est KO !\n next..")
                self.afficher_autre_texte(f"Vous avez perdu !\n next..")

    def round(self):
        if self.cb.joueur.pokemon_equipe[0].stats['Sp. Atk'] >= self.cb.combat.pokemon_adversaire.stats['Sp. Atk']:
            self.utiliser_charge()
            self.defendre()
            self.set_dialogue_text("Vous avez été plus rapide!")
        else:
            self.defendre()
            self.utiliser_charge()
            self.set_dialogue_text("Il a été plus rapide!")

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            if self.compteur < len(self.phrases_intro):
                self.set_dialogue_text(self.phrases_intro[self.compteur])
                self.compteur += 1
            else:
                self.set_dialogue_text("Que voulez-vous faire ?")

    def attaquer_sp2(self):
        self.set_dialogue_text("Deuxième attaque spéciale lancée")

    def fuite(self):
        if self.cb.combat.fuir():
            self.set_dialogue_text("Fuite réussie !")
        else:
            self.set_dialogue_text("Impossible de fuir !")

    def utiliser_charge(self):
        if self.cb.combat.utiliser_charge():
            self.set_dialogue_text("Votre Pokémon utilise Charge !")
            self.ui.progressBar_adv.setValue(self.ui.progressBar_adv.value() - 6)
        else:
            self.set_dialogue_text("Impossible d'utiliser l'attaque Charge !")

    def defendre(self):
        self.cb.combat.attaquer_adversaire()
        self.ui.progressBar_pv.setValue(self.ui.progressBar_pv.value() - 6)

    def changer_image_pok_adv(self, numero):
        self.label_4.setPixmap(QPixmap(f"CODE/image tiles/pokemon_Combat/front/{numero}.png"))
        self.label_4.setScaledContents(True)
    def changer_pokemon(self):
        # Code pour l'action de changer de Pokémon
        self.set_dialogue_text("Changement de Pokémon")

    def set_dialogue_text(self, text):
        self.ui.dialogue.setPlainText(text)
        font_id = QFontDatabase.addApplicationFont("/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/data/police.ttf")
        #font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        #font = QFont(font_family)
        #self.ui.dialogue.setFont(font)
        self.ui.dialogue.setStyleSheet("background-color: rgba(0,0,0,0); margin: 10px; padding: 0px;")


def start_battle_simulation():
    app = QApplication(sys.argv)
    dialog = FightWindow()
    dialog.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_battle_simulation()
