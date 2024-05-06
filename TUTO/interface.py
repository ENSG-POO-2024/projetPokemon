# -*- coding: utf-8 -*-
"""
Created on Mon May  6 12:26:18 2024

@author: Formation
"""


import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(344, 439)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.nombre_1 = QtWidgets.QSpinBox(self.centralwidget)
        self.nombre_1.setGeometry(QtCore.QRect(10, 100, 42, 22))
        self.nombre_1.setObjectName("nombre_1")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(60, 100, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.nombre_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.nombre_2.setGeometry(QtCore.QRect(130, 100, 42, 22))
        self.nombre_2.setObjectName("nombre_2")
        self.egal = QtWidgets.QPushButton(self.centralwidget)
        self.egal.setGeometry(QtCore.QRect(180, 100, 75, 23))
        self.egal.setObjectName("egal")
        self.resultat = QtWidgets.QLabel(self.centralwidget)
        self.resultat.setGeometry(QtCore.QRect(270, 100, 47, 20))
        self.resultat.setObjectName("resultat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 344, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "+"))
        self.comboBox.setItemText(1, _translate("MainWindow", "-"))
        self.comboBox.setItemText(2, _translate("MainWindow", "*"))
        self.comboBox.setItemText(3, _translate("MainWindow", "/"))
        self.egal.setText(_translate("MainWindow", "="))
        self.resultat.setText(_translate("MainWindow", "TextLabel"))
