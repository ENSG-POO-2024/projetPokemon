# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_connection.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie
import json

import os
from pokedex import Ui_FormPokedex

data =  os.path.join(os.path.dirname(__file__),'data', 'data_user.json')


fond_ecran =  os.path.join(os.path.dirname(__file__),'image', 'pikachu.gif')



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        
        #Ajouter un gif de fond
        self.labelpokedex = QtWidgets.QLabel(Form)
        self.labelpokedex.setGeometry(QtCore.QRect(0, 0, 1000, 500))
        self.labelpokedex.setText("")
        self.movie = QMovie(fond_ecran) #pour faire animer le gif
        self.labelpokedex.setMovie(self.movie)
        self.movie.start() # démarrer le gif

        
        
        self.labelTitre = QtWidgets.QLabel(Form)
        self.labelTitre.setGeometry(QtCore.QRect(35, 50, 500, 151))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.labelTitre.setFont(font)
        self.labelTitre.setObjectName("labelTitre")
        self.labelID = QtWidgets.QLabel(Form)
        self.labelID.setGeometry(QtCore.QRect(50, 200, 151, 51))
        self.labelTitre.setStyleSheet("font-weight: bold;") # mettre en gras
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelID.setFont(font)
        self.labelID.setObjectName("labelID")
        self.labelPassword = QtWidgets.QLabel(Form)
        self.labelPassword.setGeometry(QtCore.QRect(5, 320, 151, 51))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.labelPassword.setFont(font)
        self.labelPassword.setObjectName("labelPassword")
        self.lineEditID = QtWidgets.QLineEdit(Form)
        self.lineEditID.setGeometry(QtCore.QRect(110, 200, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEditID.setFont(font)
        self.lineEditID.setObjectName("lineEditID")
        self.lineEditPassword = QtWidgets.QLineEdit(Form)
        self.lineEditPassword.setGeometry(QtCore.QRect(110, 320, 341, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(330, 400, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "First_Conection"))
        self.labelTitre.setText(_translate("Form", "FIRST CONNECTION"))
        self.labelID.setText(_translate("Form", "ID :"))
        self.labelPassword.setText(_translate("Form", "Password :"))
        self.pushButton.setText(_translate("Form", "OK"))
        
        



class FirstConnection(Ui_Form):
    def __init__(self,parent=None):
        super().__init__()
        self.setupUi(parent)



    def verifyAndRegister(self):
        # Récupérer le nom d'utilisateur et le mot de passe entrés par l'utilisateur
        ID = self.lineEditID.text()
        password = self.lineEditPassword.text()

        # Vérifier si l'utilisateur a déjà été enregistré
        if self.checkUsername(ID):
            print("ID already exists. Please choose another username.")

            return "ID already exists. Please choose another username.", ID

        # Enregistrer les informations d'identification dans un fichier JSON et ouvrir la page suivante
        else:
            self.registerNewUser(ID, password)
            print("New user registered successfully.")
            return "New user registered successfully.", ID
        
        

    def checkUsername(self, ID):
        # Vérifier si le nom d'utilisateur existe déjà dans le fichier JSON
        with open(data, "r") as file:
            users = json.load(file)
            if ID in users:
                return True
        return False

    def registerNewUser(self, ID, password):
        # Enregistrer les nouvelles informations d'identification dans le fichier JSON 
        with open(data, "r") as file:
            # "r" pour lire dans le fichier
            users = json.load(file)
        users[ID] = {"password" : password, "MyPokemons": []} #format du dictionnaire
        with open(data, "w") as file:
            # "w" pour modifier dans le fichier
            json.dump(users, file)
    



    
class Ui_erreur(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(187, 116)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 161, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "message d'erreur"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8.25pt; font-weight:600;\">ID already exists. Please choose another username.</span></p></body></html>"))



        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    
    
    First_Conection = QtWidgets.QWidget()
    app.setQuitOnLastWindowClosed(True)
    ui = FirstConnection(First_Conection)
    First_Conection.show()
    sys.exit(app.exec_())
    
    #Pokédex
    Pokedex = Ui_FormPokedex()
    
    #message d'erreur
    mess = QtWidgets.QWidget()
    ui_erreur = Ui_erreur()
    ui_erreur.setupUi(mess)
    mess.show()