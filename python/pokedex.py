
from PyQt5 import QtCore, QtGui, QtWidgets
import os
import json
from pokemon import dico_poke
from statPokemon import statPoke


#importer l'image du pokedex
pokedex = os.path.join(os.path.dirname(__file__), 'image', 'pokedex.jpg')
data =  os.path.join(os.path.dirname(__file__),'data', 'data_user.json')


class FormPokedex(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(439, 636)
        
        #ajouter une image
        self.labelpokedex = QtWidgets.QLabel(Form)
        self.labelpokedex.setGeometry(QtCore.QRect(10, 10, 421, 611))
        self.labelpokedex.setText("")
        self.labelpokedex.setPixmap(QtGui.QPixmap(pokedex))
        self.labelpokedex.setScaledContents(True)
        self.labelpokedex.setObjectName("labelpokedex")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(50, 120, 335, 320))
        self.tabWidget.setAccessibleName("")
        self.tabWidget.setObjectName("tabWidget")
        self.widget = QtWidgets.QWidget()
        self.widget.setObjectName("widget")
        self.listWidgetPokemon = QtWidgets.QListWidget(self.widget)
        self.listWidgetPokemon.setGeometry(QtCore.QRect(0, 0, 329, 309))
        self.listWidgetPokemon.setObjectName("listWidgetPokemon")
        self.tabWidget.addTab(self.widget, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.listWidgetMesPokemons = QtWidgets.QListWidget(self.tab_2)
        self.listWidgetMesPokemons.setGeometry(QtCore.QRect(0, 0, 329, 309))
        self.listWidgetMesPokemons.setObjectName("listWidgetMesPokemons")
        self.tabWidget.addTab(self.tab_2, "")
        self.NomPoke = QtWidgets.QLabel(Form)
        self.NomPoke.setGeometry(QtCore.QRect(50, 470, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.NomPoke.setFont(font)
        self.NomPoke.setScaledContents(False)
        self.NomPoke.setObjectName("NomPoke")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setGeometry(QtCore.QRect(140, 510, 191, 81))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 189, 79))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.infoPoke = QtWidgets.QTextBrowser(self.scrollAreaWidgetContents)
        self.infoPoke.setGeometry(QtCore.QRect(0, 0, 191, 81))
        self.infoPoke.setObjectName("infoPoke")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.pushButtonTop = QtWidgets.QPushButton(Form)
        self.pushButtonTop.setGeometry(QtCore.QRect(70, 512, 31, 21))
        self.pushButtonTop.setText("")
        self.pushButtonTop.setCheckable(False)
        self.pushButtonTop.setDefault(False)
        self.pushButtonTop.setFlat(True)
        self.pushButtonTop.setObjectName("pushButtonTop")
        self.pushButtonTop.clicked.connect(self.up)
        
        self.pushButtonRight = QtWidgets.QPushButton(Form)
        self.pushButtonRight.setGeometry(QtCore.QRect(100, 540, 21, 21))
        self.pushButtonRight.setText("")
        self.pushButtonRight.setCheckable(False)
        self.pushButtonRight.setDefault(False)
        self.pushButtonRight.setFlat(True)
        self.pushButtonRight.setObjectName("pushButtonRight")
        self.pushButtonRight.clicked.connect(self.right)
        
        self.pushButtonDown = QtWidgets.QPushButton(Form)
        self.pushButtonDown.setGeometry(QtCore.QRect(70, 560, 21, 21))
        self.pushButtonDown.setText("")
        self.pushButtonDown.setCheckable(False)
        self.pushButtonDown.setDefault(False)
        self.pushButtonDown.setFlat(True)
        self.pushButtonDown.setObjectName("pushButtonDown")
        self.pushButtonDown.clicked.connect(self.down)
        
        self.pushButtonLeft = QtWidgets.QPushButton(Form)
        self.pushButtonLeft.setGeometry(QtCore.QRect(50, 540, 21, 21))
        self.pushButtonLeft.setText("")
        self.pushButtonLeft.setCheckable(False)
        self.pushButtonLeft.setDefault(False)
        self.pushButtonLeft.setFlat(True)
        self.pushButtonLeft.setObjectName("pushButtonLeft")
        self.pushButtonLeft.clicked.connect(self.left)
        
        self.Delete = QtWidgets.QPushButton(Form)
        self.Delete.setGeometry(QtCore.QRect(350, 510, 21, 21))
        self.Delete.setText("")
        self.Delete.setCheckable(False)
        self.Delete.setDefault(False)
        self.Delete.setFlat(True)
        self.Delete.setObjectName("Delete")
        self.Delete.clicked.connect(self.remove)
        
        self.Check = QtWidgets.QPushButton(Form)
        self.Check.setGeometry(QtCore.QRect(370, 550, 31, 31))
        self.Check.setText("")
        self.Check.setCheckable(False)
        self.Check.setDefault(False)
        self.Check.setFlat(True)
        self.Check.setObjectName("Check")
        self.Check.clicked.connect(self.getItem)
        
        
        
        #ajouter le nom de tous les pokémons dans le pokédex
        nom_poke = list(dico_poke.keys())
        for k in range(len(nom_poke)):
            nomPoke = list(dico_poke.keys())[k]
            self.listWidgetPokemon.addItem(QtWidgets.QListWidgetItem(nomPoke))
        self.listWidgetPokemon.itemClicked.connect(self.getItem)
        self.listWidgetMesPokemons.itemClicked.connect(self.getItem)
        
        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pokedex"))
        __sortingEnabled = self.listWidgetPokemon.isSortingEnabled()
        self.listWidgetPokemon.setSortingEnabled(False)
        self.listWidgetPokemon.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.widget), _translate("Form", "Pokemon"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "My Pokemons"))
        self.NomPoke.setText(_translate("Form", ""))
    
    def getItem(self):
        """
        La fonction affiche les caractéristiques des pokémons sélectionnés dans le pokédex


        """
        fenetre = self.tabWidget.currentIndex()
        #Pour savoir sur quel table Widget je suis
        
        if fenetre == 0:
        #Fenêtre de Pokemon
            item = self.listWidgetPokemon.currentItem()

        else:
        #Fenêtre my Pokemons
            item = self.listWidgetMesPokemons.currentItem()
        
        self.NomPoke.setText(str(item.text()))
        #Récupéraration du nom des pokémons clickés
            
        text = statPoke(str(item.text()))
        #Récupération des données des pokémons
        
        self.infoPoke.setText(text)

        
        
        
    def remove(self):
        """
        La fonction fait un retour en arrière du pokédex

        """
        self.NomPoke.clear()
        self.infoPoke.clear()

    def up(self):
        """
        La fonction permet au curseur de se déplacer vers le haut dans la listWidget
        """

        item = self.listWidgetPokemon.currentRow()# indice du curseur sélectionner
        self.listWidgetPokemon.setCurrentRow(item - 1)

        
    def down(self):
        """
        La fonction permet au curseur de se déplacer vers le bas dans la listWidget

        """
        item = self.listWidgetPokemon.currentRow()# indice du curseur sélectionner
        self.listWidgetPokemon.setCurrentRow(item + 1)

    
    def left(self):
        """
        La fonction ouvre ma fenêtre de Pokémon

        """
        self.tabWidget.setCurrentIndex(0) #on se place sur la fenêtre la plus à gauche
    
    def right(self):
        """
        La fonction ouvre ma fenêtre de droite (Mon Pokémon)
        """
        self.tabWidget.setCurrentIndex(1) #on se place sur la fenêtre la plus à droite
        
class Ui_FormPokedex(FormPokedex):
    
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(parent)
        self.pokemon_combat = None
        

       

        
    def laoding(self, ID):
        """
        la fonction recharger la partie du joueur à partir du fichier json
        """
        with open(data, "r") as file:
            users = json.load(file)
            listPoke = users[ID]["MyPokemons"]
            for k in range(len(listPoke)):
                nomPoke = listPoke[k]
                self.listWidgetMesPokemons.addItem(QtWidgets.QListWidgetItem(nomPoke))
    
    
    def choisir_pokemon(self):
        """
        la fonction enregistre le nom du pokémon choisit pour le combat

        """
        
        #si on est pas dans Mes pokémons on ne peut pas sélectionner le pokémon pour le combat
        try:
            item = self.listWidgetMesPokemons.currentItem() #choisir dans Mes pokémons
            self.pokemon_combat = item.text()
            
        except:
            pass


        
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    app.setQuitOnLastWindowClosed(True)
    ui_Pokedex = Ui_FormPokedex(Form)
    ui_Pokedex.setupUi(Form)
    ui_Pokedex.Check.clicked.connect(ui_Pokedex.choisir_pokemon)
    Form.show()
    sys.exit(app.exec_())
