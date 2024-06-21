# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tedragen.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PyQt5.QtSvg import QSvgRenderer, QGraphicsSvgItem, QSvgWidget
from PyQt5.QtWidgets import QGraphicsScene



class Ui_principal(object):
    def setupUi(self, principal):
        if not principal.objectName():
            principal.setObjectName(u"principal")
        principal.resize(800, 679)
        self.centralwidget = QWidget(principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(30, 20, 500, 100))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.comboBox.setFont(font1)

        self.verticalLayout.addWidget(self.comboBox)

        #self.gview = QGraphicsView()
        #self.scene = QGraphicsScene()
        #self.gview.setGeometry(QRect(10, 150, 500 , 400))
        #self.renderer = QSvgRenderer("C:\generador\caixes\preview.svg")
        #self.svg_item = QGraphicsSvgItem()
        #self.svg_item.setSharedRenderer(self.renderer)
        #self.scene.addItem(self.svg_item)
        #self.gview.setScene(QGraphicsScene().addItem(self.svg_item))


        #self.verticalLayout.insertWidget(2,self.gview)

        #self.graphicsView = QGraphicsView(self.centralwidget)
        #self.graphicsView.setObjectName(u"graphicsView")
        #self.graphicsView.setGeometry(QRect(30, 90, 500, 500))

        #self.scene = QGraphicsScene(self)
        #self.renderer = QSvgRenderer("c:\generador\caixes\preview.svg")
        #self.svg_item = QGraphicsSvgItem()
        #self.svg_item.setSharedRenderer(self.renderer)
        #self.scene.addItem(self.svg_item)
      



        
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(590, 90, 161, 421))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.etiq1 = QLabel(self.verticalLayoutWidget_2)
        self.etiq1.setObjectName(u"etiq1")

        self.verticalLayout_2.addWidget(self.etiq1)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.etiq2 = QLabel(self.verticalLayoutWidget_2)
        self.etiq2.setObjectName(u"etiq2")

        self.verticalLayout_2.addWidget(self.etiq2)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.etiq3 = QLabel(self.verticalLayoutWidget_2)
        self.etiq3.setObjectName(u"etiq3")

        self.verticalLayout_2.addWidget(self.etiq3)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.etiq4 = QLabel(self.verticalLayoutWidget_2)
        self.etiq4.setObjectName(u"etiq4")

        self.verticalLayout_2.addWidget(self.etiq4)

        self.lineEdit = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout_2.addWidget(self.lineEdit)

        self.etiq5 = QLabel(self.verticalLayoutWidget_2)
        self.etiq5.setObjectName(u"etiq5")

        self.verticalLayout_2.addWidget(self.etiq5)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.verticalLayout_2.addWidget(self.lineEdit_6)

        self.etiq6 = QLabel(self.verticalLayoutWidget_2)
        self.etiq6.setObjectName(u"etiq6")

        self.verticalLayout_2.addWidget(self.etiq6)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.verticalLayout_2.addWidget(self.lineEdit_5)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(600, 540, 141, 41))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 640, 631, 20))
        principal.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(principal)
        self.statusbar.setObjectName(u"statusbar")
        principal.setStatusBar(self.statusbar)

        self.retranslateUi(principal)

        QMetaObject.connectSlotsByName(principal)
    # setupUi

    def retranslateUi(self, principal):
        principal.setWindowTitle(QCoreApplication.translate("principal", u"TEDRAGEN 0.5", None))
        self.label.setText(QCoreApplication.translate("principal", u"Selecciona la plantilla:", None))
        self.etiq1.setText(QCoreApplication.translate("principal", u"TextLabel", None))
        self.etiq2.setText(QCoreApplication.translate("principal", u"TextLabel", None))
        self.etiq3.setText(QCoreApplication.translate("principal", u"TextLabel", None))
        self.etiq4.setText(QCoreApplication.translate("principal", u"TextLabel", None))
        self.etiq5.setText(QCoreApplication.translate("principal", u"TextLabel", None))
        self.etiq6.setText(QCoreApplication.translate("principal", u"TextLabel", None))
        self.pushButton.setText(QCoreApplication.translate("principal", u"GUARDA SVG", None))
        self.label_2.setText(QCoreApplication.translate("principal", u"TEchnical DRAwing GENerator. Generador de dise\u00f1os personalizados a partir de modelos param\u00e9tricos \u00a9 Miquel Real Dic 2022 ", None))
    # retranslateUi

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    principal = QMainWindow()
    ui = Ui_principal()
    ui.setupUi(principal)
    principal.show()
    sys.exit(app.exec_())