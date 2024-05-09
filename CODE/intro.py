import sys
from Wilkommen import Ui_MainWindow
from pokedex import PokemonList
from travail import GameBoard
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import Qt
from introUI import Ui_Dialog
import sys
from Wilkommen import Ui_MainWindow
from pokedex import PokemonList
from travail import GameBoard
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QHBoxLayout,QScrollArea, QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QScrollArea, QWidget,
                             QLabel, QHBoxLayout, QRadioButton,QCheckBox)
from PyQt5.QtGui import QPixmap


from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QScrollArea, QWidget,
                             QLabel, QHBoxLayout, QCheckBox, QPushButton)
from PyQt5.QtCore import pyqtSignal
from monat import Dresseur,Starter,Rencontre,Soins

pokemon_names_translation = {
    "Bulbizarre": "Bulbasaur",
    "Herbizarre": "Ivysaur",
    "Florizarre": "Venusaur",
    "Salameche": "Charmander",
    "Reptincel": "Charmeleon",
    "Dracaufeu": "Charizard",
    "Carapuce": "Squirtle",
    "Carabaffe": "Wartortle",
    "Tortank": "Blastoise",
    "Chenipan": "Caterpie",
    "Chrysacier": "Metapod",
    "Papilusion": "Butterfree",
    "Aspicot": "Weedle",
    "Coconfort": "Kakuna",
    "Dardargnan": "Beedrill",
    "Roucool": "Pidgey",
    "Roucoups": "Pidgeotto",
    "Roucarnage": "Pidgeot",
    "Rattata": "Rattata",
    "Rattatac": "Raticate",
    "Piafabec": "Spearow",
    "Rapasdepic": "Fearow",
    "Abo": "Ekans",
    "Arbok": "Arbok",
    "Pikachu": "Pikachu",
    "Raichu": "Raichu",
    "Sabelette": "Sandshrew",
    "Sablaireau": "Sandslash",
    "Nidoran♀": "Nidoran♀",
    "Nidorina": "Nidorina",
    "Nidoqueen": "Nidoqueen",
    "Nidoran♂": "Nidoran♂",
    "Nidorino": "Nidorino",
    "Nidoking": "Nidoking",
    "Melofée": "Clefairy",
    "Mélodelfe": "Clefable",
    "Goupix": "Vulpix",
    "Feunard": "Ninetales",
    "Rondoudou": "Jigglypuff",
    "Grodoudou": "Wigglytuff",
    "Nosferapti": "Zubat",
    "Nosferalto": "Golbat",
    "Mystherbe": "Oddish",
    "Ortide": "Gloom",
    "Rafflesia": "Vileplume",
    "Paras": "Paras",
    "Parasect": "Parasect",
    "Mimitoss": "Venonat",
    "Aeromite": "Venomoth",
    "Taupiqueur": "Diglett",
    "Triopikeur": "Dugtrio",
    "Miaouss": "Meowth",
    "Persian": "Persian",
    "Psykokwak": "Psyduck",
    "Akwakwak": "Golduck",
    "Ferosinge": "Mankey",
    "Colossinge": "Primeape",
    "Caninos": "Growlithe",
    "Arcanin": "Arcanine",
    "Ptitard": "Poliwag",
    "Têtarte": "Poliwhirl",
    "Tartard": "Poliwrath",
    "Abra": "Abra",
    "Kadabra": "Kadabra",
    "Alakazam": "Alakazam",
    "Machoc": "Machop",
    "Machopeur": "Machoke",
    "Mackogneur": "Machamp",
    "Chétiflor": "Bellsprout",
    "Boustiflor": "Weepinbell",
    "Empiflor": "Victreebel",
    "Tentacool": "Tentacool",
    "Tentacruel": "Tentacruel",
    "Racaillou": "Geodude",
    "Gravalanch": "Graveler",
    "Grolem": "Golem",
    "Ponyta": "Ponyta",
    "Galopa": "Rapidash",
    "Ramoloss": "Slowpoke",
    "Flagadoss": "Slowbro",
    "Magneti": "Magnemite",
    "Magnéton": "Magneton",
    "Canarticho": "Farfetch'd",
    "Doduo": "Doduo",
    "Dodrio": "Dodrio",
    "Otaria": "Seel",
    "Lamantine": "Dewgong",
    "Tadmorv": "Grimer",
    "Grotadmorv": "Muk",
    "Kokiyas": "Shellder",
    "Crustabri": "Cloyster",
    "Fantominus": "Gastly",
    "Spectrum": "Haunter",
    "Ectoplasma": "Gengar",
    "Onix": "Onix",
    "Soporifik": "Drowzee",
    "Hypnomade": "Hypno",
    "Krabby": "Krabby",
    "Krabboss": "Kingler",
    "Voltorbe": "Voltorb",
    "Électrode": "Electrode",
    "Nœunœuf": "Exeggcute",
    "Noadkoko": "Exeggutor",
    "Osselait": "Cubone",
    "Ossatueur": "Marowak",
    "Kicklee": "Hitmonlee",
    "Tygnon": "Hitmonchan",
    "Excelangue": "Lickitung",
    "Smogo": "Koffing",
    "Smogogo": "Weezing",
    "Rhinocorne": "Rhyhorn",
    "Rhinoferos": "Rhydon",
    "Leveinard": "Chansey",
    "Saquedeneu": "Tangela",
    "Kangourex": "Kangaskhan",
    "Hypotrempe": "Horsea",
    "Hypocéan": "Seadra",
    "Poissirène": "Goldeen",
    "Poissoroy": "Seaking",
    "Stari": "Staryu",
    "Staross": "Starmie",
    "M. Mime": "Mr. Mime",
    "Insécateur": "Scyther",
    "Lippoutou": "Jynx",
    "Élektek": "Electabuzz",
    "Magmar": "Magmar",
    "Scarabrute": "Pinsir",
    "Tauros": "Tauros",
    "Magicarpe": "Magikarp",
    "Léviator": "Gyarados",
    "Lokhlass": "Lapras",
    "Métamorph": "Ditto",
    "Évoli": "Eevee",
    "Aquali": "Vaporeon",
    "Voltali": "Jolteon",
    "Pyroli": "Flareon",
    "Porygon": "Porygon",
    "Amonita": "Omanyte",
    "Amonistar": "Omastar",
    "Kabuto": "Kabuto",
    "Kabutops": "Kabutops",
    "Ptéra": "Aerodactyl",
    "Ronflex": "Snorlax",
    "Artikodin": "Articuno",
    "Électhor": "Zapdos",
    "Sulfura": "Moltres",
    "Minidraco": "Dratini",
    "Draco": "Dragonair",
    "Dracolosse": "Dragonite",
    "Mewtwo": "Mewtwo",
    "Mew": "Mew"
}


class MyDialog(QDialog):


    def __init__(self):
        self.pokemon_list = PokemonList("data/pokemons_fr.csv", True)
        self.selected_pokemon = []  # Ajout de l'attribut selected_pokemon
        super().__init__()
        self.ui = Ui_Dialog()
        self.setWindowFlags(Qt.FramelessWindowHint)  # Pour supprimer les bordures de la fenêtre
        self.setAttribute(Qt.WA_TranslucentBackground)  # Pour rendre la fenêtre transparente
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.open_pokedex_window)

    def open_pokedex_window(self):
        pokemon_list_data = self.pokemon_list.pokemon_list
        pokedex_window = ChoixStarter(pokemon_list_data)
        pokedex_window.pokemon_selected.connect(self.start_game_with_selected_pokemon)
        pokedex_window.exec_()
        pokedex_window.close()  
        
    

    def start_game_with_selected_pokemon(self, selected_pokemon):
        test=[]
        print("Pokémons sélectionnés:")
        for pokemon in selected_pokemon:
            print(f"Numéro: {pokemon['number']}, Nom: {pokemon['name']}")
            
            test.append(pokemon_names_translation[pokemon['name']])
        # Assigner selected_pokemon à l'attribut de classe
        self.selected_pokemon = selected_pokemon
        print(test)
        
        self.pokemon_list.add_starters(selected_pokemon)
        self.ui.pushButton.setText("GOOO !!")
        self.ui.pushButton.clicked.disconnect()  # Déconnexion de l'ancienne connexion
        joueur = Dresseur("JOUEUR")
        Starter(joueur,test)
        self.ui.pushButton.clicked.connect(self.open_game_board(joueur))  # Nouvelle connexion

    def open_game_board(self,joueur):
        self.close()
        print(self.selected_pokemon)
        game_board = GameBoard(self.selected_pokemon,joueur)  # Passer selected_pokemon à GameBoard
        game_board.exec()


class ChoixStarter(QDialog):
    # Définir un signal personnalisé pour émettre les Pokémon sélectionnés
    pokemon_selected = pyqtSignal(list)

    def __init__(self, pokemon_list):
        super().__init__()
        self.setWindowTitle("Choisissez vos 3 Pokémons pour le combat!")
        self.resize(500, 500) 
        
        layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)  
        
        content_widget = QWidget(scroll_area)
        content_layout = QVBoxLayout(content_widget)
        
        self.selected_pokemon = []

        for pokemon in pokemon_list:
            pokemon_label = QLabel(f"n° {pokemon['number']}     Nom: {pokemon['name']}")
            pokemon_image_label = QLabel()
            pokemon_image_label.setPixmap(QPixmap(pokemon['image_name'])) 
            
            pokemon_check_box = QCheckBox()  
            pokemon_check_box.pokemon_info = pokemon  
            pokemon_check_box.stateChanged.connect(self.update_selection)  
            
            pokemon_layout = QHBoxLayout()
            pokemon_layout.addWidget(pokemon_check_box)
            pokemon_layout.addWidget(pokemon_label)
            pokemon_layout.addWidget(pokemon_image_label)
            
            content_layout.addLayout(pokemon_layout)
        
        content_widget.setLayout(content_layout)
        scroll_area.setWidget(content_widget)
        layout.addWidget(scroll_area)
        
        self.start_button = QPushButton("Commencer")
        self.start_button.setEnabled(False)  # Désactive le bouton "Commencer" au début
        layout.addWidget(self.start_button)
        self.start_button.clicked.connect(self.start_game_with_selected_pokemon)  # Connecter le clic du bouton "Commencer"
        self.setLayout(layout)

    def update_selection(self, state):
        check_box = self.sender()  
        pokemon_info = check_box.pokemon_info  
        
        if state == 2:  
            if len(self.selected_pokemon) < 3:  
                self.selected_pokemon.append(pokemon_info)  
            else:
                # Si un quatrième Pokémon est sélectionné, retire le premier et ajoute le dernier
                self.selected_pokemon.pop(0)
                self.selected_pokemon.append(pokemon_info)
                # Coche le dernier Pokémon sélectionné
                check_box.setChecked(True)
        elif state == 0:  
            self.selected_pokemon.remove(pokemon_info)  
        
        if len(self.selected_pokemon) == 3:  # Vérifie si trois Pokémon sont sélectionnés
            self.start_button.setEnabled(True)  # Active le bouton "Commencer" si oui
        else:
            self.start_button.setEnabled(False)  # Désactive le bouton "Commencer" sinon

    def start_game_with_selected_pokemon(self):
        # Émettre le signal contenant les Pokémon sélectionnés
        self.pokemon_selected.emit(self.selected_pokemon)
        self.accept() 

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyDialog()
    window.show()
    sys.exit(app.exec_())
