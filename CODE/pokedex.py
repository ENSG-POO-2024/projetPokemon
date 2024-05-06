import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy,QProgressBar,QComboBox,QScrollArea,QWidget
from PyQt5.QtGui import QPainter, QColor, QPixmap,QFontDatabase,QFont
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtWidgets import QMessageBox,QDialog, QLabel, QVBoxLayout,QDesktopWidget

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QListView, QVBoxLayout, QLabel, QHBoxLayout, QFrame, QScrollArea
from PyQt5.QtCore import QStringListModel
from PyQt5.QtGui import QPixmap

import csv

def get_first_gen_pokemon_list(csv_file_path):
    with open(csv_file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=';')
        next(reader)
        pokemon_list = []
        for row in reader:
            if row[-1] == '1':
                pokemon_str = f"{row[0]} - {row[1]}"
                pokemon_list.append(pokemon_str)
    return pokemon_list



class Pokedex(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
        


    def initUI(self):
        self.setWindowTitle('Pokedex')
        
        self.setGeometry(100, 100, 400, 400)
        

        # Liste de Pokémon avec leurs numéros
        self.pokemon_list = get_first_gen_pokemon_list("data/pokemons_fr.csv")

        self.model = QStringListModel()
        self.model.setStringList(self.pokemon_list)

        self.list_view = QListView()
        self.list_view.setModel(self.model)

        self.label_header = QLabel(" n° - NOM")

        layout = QVBoxLayout()
        layout.addWidget(self.label_header)

        # Ajout d'un espacement vertical entre chaque ligne
        layout.addSpacing(5)

        # Ajouter les frames pour chaque Pokémon
        for pokemon in self.pokemon_list:
            frame = self.create_pokemon_frame(pokemon)
            layout.addWidget(frame)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        
        container = QWidget()
        container.setLayout(layout)
        scroll_area.setWidget(container)

        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)

        self.setLayout(main_layout)

    def create_pokemon_frame(self, pokemon):
        frame = QFrame()
        frame_layout = QHBoxLayout()

        # Ajouter le texte du Pokémon
        pokemon_label = QLabel(pokemon)
        frame_layout.addWidget(pokemon_label)

        # Récupérer le numéro de Pokémon
        pokemon_number = pokemon.split(' - ')[0]
        image_path = f"/Users/samy/PROJET_POO_REAL/DAN_MONAT_SAMY/CODE/image tiles/pokemon_Combat/front/{pokemon_number}.png"

        # Charger l'image et l'afficher dans un QLabel
        pixmap = QPixmap(image_path)
        if not pixmap.isNull():
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            frame_layout.addWidget(image_label)

        frame.setLayout(frame_layout)
        return frame

if __name__ == '__main__':
    app = QApplication(sys.argv)
    pokedex = Pokedex()
    pokedex.show()
    sys.exit(app.exec_())
