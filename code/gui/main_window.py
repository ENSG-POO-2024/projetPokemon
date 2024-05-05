# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Pykemon(object):
    def setupUi(self, Pykemon):
        Pykemon.setObjectName("Pykemon")
        Pykemon.resize(640, 640)
        Pykemon.setMinimumSize(QtCore.QSize(640, 640))
        Pykemon.setMaximumSize(QtCore.QSize(640, 640))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/logos/py_symbol.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Pykemon.setWindowIcon(icon)
        Pykemon.setStyleSheet("background-color: rgb(255, 255, 255);")
        Pykemon.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(Pykemon)
        self.centralwidget.setObjectName("centralwidget")
        self.MM_PykemonLogo = QtWidgets.QLabel(self.centralwidget)
        self.MM_PykemonLogo.setGeometry(QtCore.QRect(0, 0, 640, 271))
        self.MM_PykemonLogo.setObjectName("MM_PykemonLogo")
        self.MM_ClickOnWindowStart_text = QtWidgets.QLabel(self.centralwidget)
        self.MM_ClickOnWindowStart_text.setGeometry(QtCore.QRect(0, 430, 640, 50))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MM_ClickOnWindowStart_text.setFont(font)
        self.MM_ClickOnWindowStart_text.setStyleSheet("color: rgb(55, 104, 184);")
        self.MM_ClickOnWindowStart_text.setObjectName("MM_ClickOnWindowStart_text")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(280, 370, 75, 23))
        self.pushButton.setObjectName("pushButton")
        Pykemon.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Pykemon)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Pykemon.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Pykemon)
        self.statusbar.setObjectName("statusbar")
        Pykemon.setStatusBar(self.statusbar)

        self.retranslateUi(Pykemon)
        QtCore.QMetaObject.connectSlotsByName(Pykemon)

        self.pushButton.clicked.connect(self.affiche)
        
    def affiche(self):
        QtWidgets.QMessageBox.information(self,"Info","Ça marche !")


    def retranslateUi(self, Pykemon):
        _translate = QtCore.QCoreApplication.translate
        Pykemon.setWindowTitle(_translate("Pykemon", "Pykémon : Attrapy-les tous !"))
        self.MM_PykemonLogo.setText(_translate("Pykemon", "<html><head/><body><p align=\"center\"><img src=\":/logos/main_logo.png\"/></p></body></html>"))
        self.MM_ClickOnWindowStart_text.setText(_translate("Pykemon", "<html><head/><body><p align=\"center\">CLICK ON THE WINDOW TO START</p></body></html>"))
        self.pushButton.setText(_translate("Pykemon", "PushButton"))
import gui_resources


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Pykemon = QtWidgets.QMainWindow()
    ui = Ui_Pykemon()
    ui.setupUi(Pykemon)
    Pykemon.show()
    sys.exit(app.exec_())
