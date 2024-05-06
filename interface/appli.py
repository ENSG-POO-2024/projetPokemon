# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:25:39 2024

@author: Formation
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from page_accueil import Ui_MainWindow
from first_connection import Ui_Form

import sys

def afficheFirstConnection():
    Form.show()
    
    
    



#Page d'accueil
app = QtWidgets.QApplication(sys.argv)
Window = QtWidgets.QMainWindow()
app.setQuitOnLastWindowClosed(True)
ui = MainWindow(Window)
Window.show()
sys.exit(app.exec_())

#Page first connection
Form = QtWidgets.QWidget()
firstConnect = Ui_Form()
firstConnect.setupUi(Form)

#bouton
ui.pushButton_2.clicked.connect(afficheFirstConnection)
ui.pushButtonValider.clicked.connect(verifyLogin)


MainWindow.show()
sys.exit(app.exec_())