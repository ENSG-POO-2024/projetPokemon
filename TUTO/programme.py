# -*- coding: utf-8 -*-
"""
Created on Mon May  6 13:36:38 2024

@author: Formation
"""



import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from interface import Ui_MainWindow

##Slots 






app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
app.setQuitOnLastWindowClosed(True)  ##Important 
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

    # Exécution de la boucle principale de l'application
sys.exit(app.exec_())