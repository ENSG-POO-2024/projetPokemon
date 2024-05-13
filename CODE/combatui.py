from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1221, 808)
        Form.setMouseTracking(False)
        Form.setWindowOpacity(1.0)
        self.field = QtWidgets.QLabel(Form)
        self.field.setGeometry(QtCore.QRect(387, 148, 601, 611))
        self.field.setText("")
        self.field.setPixmap(QtGui.QPixmap("image tiles/field2.png"))
        self.field.setScaledContents(True)
        self.field.setObjectName("field")
        self.progressBar_adv = QtWidgets.QProgressBar(Form)
        self.progressBar_adv.setGeometry(QtCore.QRect(537, 198, 131, 16))
        self.progressBar_adv.setProperty("value", 100)
        self.progressBar_adv.setObjectName("progressBar_adv")
        self.progressBar_pv = QtWidgets.QProgressBar(Form)
        self.progressBar_pv.setGeometry(QtCore.QRect(777, 351, 91, 16))
        self.progressBar_pv.setProperty("value", 100)
        self.progressBar_pv.setObjectName("progressBar_pv")
        self.progressBar_XP = QtWidgets.QProgressBar(Form)
        self.progressBar_XP.setGeometry(QtCore.QRect(746, 382, 126, 16))
        self.progressBar_XP.setAutoFillBackground(False)
        self.progressBar_XP.setProperty("value", 100)
        self.progressBar_XP.setObjectName("progressBar_XP")
        self.nom_adv = QtWidgets.QLabel(Form)
        self.nom_adv.setGeometry(QtCore.QRect(467, 174, 81, 16))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(16)
        self.nom_adv.setFont(font)
        self.nom_adv.setObjectName("nom_adv")
        self.nom_adv_2 = QtWidgets.QLabel(Form)
        self.nom_adv_2.setGeometry(QtCore.QRect(717, 331, 81, 16))
        font = QtGui.QFont()
        font.setFamily("American Typewriter")
        font.setPointSize(14)
        self.nom_adv_2.setFont(font)
        self.nom_adv_2.setObjectName("nom_adv_2")
        self.dialogue = QtWidgets.QTextBrowser(Form)
        self.dialogue.setGeometry(QtCore.QRect(447, 418, 451, 81))
        font = QtGui.QFont()
        font.setKerning(True)
        self.dialogue.setFont(font)
        self.dialogue.setOverwriteMode(False)
        self.dialogue.setObjectName("dialogue")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(607, 175, 19, 14))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(820, 334, 21, 16))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(469, 267, 201, 171))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("image tiles/pokemon_Combat/back/2.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(727, 208, 141, 121))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("image tiles/pokemon_Combat/front/2.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(437, 508, 471, 261))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("../../../Downloads/1000_F_189138228_Khn6fbgC2zaTi90hsnTZqFc3MHPcQVib.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(697, 708, 171, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(447, 528, 211, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(687, 528, 211, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(477, 708, 171, 51))
        font = QtGui.QFont()
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setAutoDefault(False)
        self.pushButton_3.setDefault(False)
        self.pushButton_3.setObjectName("pushButton_3")
        self.cadre = QtWidgets.QLabel(Form)
        self.cadre.setGeometry(QtCore.QRect(-130, 0, 1609, 920))
        self.cadre.setText("")
        self.cadre.setPixmap(QtGui.QPixmap("image tiles/cadre.png"))
        self.cadre.setScaledContents(True)
        self.cadre.setObjectName("cadre")
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.nom_adv.setText(_translate("Form", "Pokemon"))
        self.nom_adv_2.setText(_translate("Form", "Pokemon"))
        self.dialogue.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Le pokémon sauvage apparaît !</span>    </p></body></html>"))
        self.label.setText(_translate("Form", "21"))
        self.label_2.setText(_translate("Form", "23"))
        self.pushButton_4.setText(_translate("Form", "POKEMON"))
        self.pushButton.setText(_translate("Form", "ATTAQUE"))
        self.pushButton_2.setText(_translate("Form", "ATTAQUE SP2"))
        self.pushButton_3.setText(_translate("Form", "FUITE"))
