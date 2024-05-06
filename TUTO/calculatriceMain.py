# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:34:02 2024

@author: Formation
"""
#! /usr/bin/python
#*coding: utf8 *
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import os,sys
from calculatrice import *
class calculatrice(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self)
        self.ui=Ui_calculatrice()
        self.ui.setupUi(parent)
        #Ici, personnalisez vos widgets si nécessaire
        #Réalisez les connexions supplémentaires entre signaux et slots
    def main(args):
        a=QApplication(args)
        f=QWidget()
        c=calculatrice(f)
        f.show()
        r=a.exec_()
        return r
if __name__=="__main__":
    main(sys.argv)