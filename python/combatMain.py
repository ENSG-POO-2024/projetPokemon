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

# from image1_rc import *  # Import du module contenant les ressources

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi('combat.ui', self)  # Remplacez 'votre_fichier.ui' par le nom de votre fichier .ui
        self.setWindowTitle('Votre titre')  # Changez le titre selon vos besoins
        self.setWindowIcon(QIcon('votre_icone.ico'))  # Changez le nom de l'icône selon vos besoins
        self.show()

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    app.setQuitOnLastWindowClosed(True)  #
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()