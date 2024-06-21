"""
Generador del dibuix de troquel de caixes
versió beta amb interface grafica d'escriptori
a partir de les dades de l'usuari de les mides d'una caixa,
genera l'arxiu del dibuix del troqulel necesari en SVG,
diferenciant hendit i tall en dos colors de linea
"""

import os #per a manejar fitxers
import svgwrite # per escrire SVG
import sys
import json
import pyperclip
from math import pi, sin, cos, asin, sqrt, pow

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSvg import QSvgRenderer , QGraphicsSvgItem 
from PyQt5.QtCore import QRect 

AI_rate  = 2.834643883688892  #proporcio d'unitats svg / mm    RDworks v8.01.60
CDR_rate  = 3.77953232067064    #proporcio d'unitats svg / mm  CorelDraw

tamany_miniatura_px=450 #miniatura

pth = os.path.dirname(os.path.abspath(__file__)) #ruta de eixida fitxer

models_pth = os.path.join(pth,"models")
eixida = os.path.join(pth ,"caixes")
fitxer =os.path.join(eixida,"preview.svg")

with os.scandir(models_pth) as modes:
    modes = [model.name[:-5] for model in modes if model.is_file() and model.name.endswith('.json')]



class MainWindow(QMainWindow):
    
    def __init__(self):
        
        super().__init__()
        self.fitxer=fitxer    
        
        self.verticalLayoutWidget = QWidget(self)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(30, 20, 500, 100)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setText(u"Selecciona la plantilla:")
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.verticalLayoutWidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.addItems(list(modes))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(12)
        self.comboBox.setFont(font1)
        self.verticalLayout.addWidget(self.comboBox)
        
        self.comboBox.activated[str].connect(self.onSelected)


        self.label_2 = QLabel(self)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 655, 631, 20))
        self.label_2.setText( u"TEchnical DRAwing GENerator. Generador de disenys personalitzats a partir de models param\u00e8trics \u00a9 Miquel Real Dec 2022 ")
    

        self.setFixedSize(800,700)
        self.setWindowTitle('TEDRAGEN beta 1.04')
        # Beta 1.01 s'af3egeix l'evaluacio de codi a mes de formules, substituint el caracter ' ' per '_'
        # Beta 1.02 s'afegeix la seleccio de l'escala d'eixida cdr/ai
        # Beta 1.04 s'importen funcions trigonomètriques, s'actualitza el preview nomes en canviar de focus, es limiten els rangs de les dades desde descripció json



        # Crea un widget QGraphicsView y una escena QGraphicsScene
        self.view = QGraphicsView(self)
        self.scene = QGraphicsScene(self)
        self.view.setGeometry(QRect(30, 150, 500 , 500))



        self.verticalLayoutWidget_2 = QWidget(self)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(590, 90, 161, 521))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.etiq0 = QLabel(self.verticalLayoutWidget_2)
        self.etiq0.setObjectName(u"etiq0")
        self.verticalLayout_2.addWidget(self.etiq0)

        self.lineEdit_0 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_0.setObjectName(u"lineEdit_0")
        self.lineEdit_0.editingFinished.connect(self.edicio)
        #self.lineEdit_0.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_0)

        self.etiq1 = QLabel(self.verticalLayoutWidget_2)
        self.etiq1.setObjectName(u"etiq1")

        self.verticalLayout_2.addWidget(self.etiq1)

        self.lineEdit_1 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.editingFinished.connect(self.edicio)
        #self.lineEdit_1.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_1)

        self.etiq2 = QLabel(self.verticalLayoutWidget_2)
        self.etiq2.setObjectName(u"etiq2")

        self.verticalLayout_2.addWidget(self.etiq2)

        self.lineEdit_2 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.editingFinished.connect(self.edicio)
        #self.lineEdit_2.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.etiq3 = QLabel(self.verticalLayoutWidget_2)
        self.etiq3.setObjectName(u"etiq3")

        self.verticalLayout_2.addWidget(self.etiq3)

        self.lineEdit_3 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.editingFinished.connect(self.edicio)
        #self.lineEdit_3.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.etiq4 = QLabel(self.verticalLayoutWidget_2)
        self.etiq4.setObjectName(u"etiq4")

        self.verticalLayout_2.addWidget(self.etiq4)

        self.lineEdit_4 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.editingFinished.connect(self.edicio)
        #self.lineEdit_4.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.etiq5 = QLabel(self.verticalLayoutWidget_2)
        self.etiq5.setObjectName(u"etiq5")

        self.verticalLayout_2.addWidget(self.etiq5)

        self.lineEdit_5 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.editingFinished.connect(self.edicio)
        #self.lineEdit_5.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_5)

        self.etiq6 = QLabel(self.verticalLayoutWidget_2)
        self.etiq6.setObjectName(u"etiq6")

        self.verticalLayout_2.addWidget(self.etiq6)

        self.lineEdit_6 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.editingFinished.connect(self.edicio)
        #self.lineEdit_6.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_6)

        self.etiq7 = QLabel(self.verticalLayoutWidget_2)
        self.etiq7.setObjectName(u"etiq7")
        

        self.verticalLayout_2.addWidget(self.etiq7)

        self.lineEdit_7 = QLineEdit(self.verticalLayoutWidget_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.editingFinished.connect(self.edicio)
        #self.lineEdit_7.setValidator(QDoubleValidator(0.99,999.99,2))

        self.verticalLayout_2.addWidget(self.lineEdit_7)

        self.selector = QRadioButton("escala AI / CDR")
        self.selector.setText("escala AI / CDR")
        self.verticalLayout_2.addWidget(self.selector)

        self.boto = QPushButton('GENERA SVG', self)
        self.boto.setToolTip('GENERA SVG')
        self.boto.setFixedSize(150,50)
        self.verticalLayout_2.addWidget(self.boto)

        

        self.boto.clicked.connect(self.guarda)

        self.triacaixa(self.comboBox.currentText())
        self.edicio()

     


    def mostraSVG(self):
        self.scene.clear()
        self.renderer = QSvgRenderer(self.fitxer)
        self.svg_item = QGraphicsSvgItem()
        self.svg_item.setSharedRenderer(self.renderer)
        self.scene.addItem(self.svg_item)
        self.view.setScene(self.scene)

    def triacaixa(self,txtVal):
            self.v=[]
            self.p=[]
            self.m=[]
            selected_model_pth = os.path.join(models_pth,txtVal+'.json')
            with open(selected_model_pth, "r") as file: #importa una caixa paramentrizada en 
                self.caixa = json.load(file)
            for i in self.caixa["variables"]:
                self.p.append(self.caixa["variables"][i]["eti"])
                self.v.append(self.caixa["variables"][i]["val"])
                self.m.append(self.caixa["variables"][i]["rang"])
            while len(self.v)<9:
                self.p.append("------")
                self.v.append(0)
                self.m.append([0.99,99.99,2])
        
            for e in range(8):
                exec(f"self.etiq{e}.setText(self.p[{e}].upper())")
                exec(f'self.lineEdit_{e}.setEnabled(self.p[{e}]!="------")')
                exec(f'self.lineEdit_{e}.clear()')
                exec(f'self.lineEdit_{e}.setText(str(self.v[{e}]))')
                exec(f'self.lineEdit_{e}.setValidator(QDoubleValidator(self.m[{e}][0],self.m[{e}][1],self.m[{e}][2]))')
    
    
        
    def onSelected(self, txtVal):
        self.triacaixa(txtVal)
        self.edicio()

    def genera_path(self,grup,obje,escala,v): #genera el path d'un grup evaluant les formules 
        cadena=""
        for j in obje["grupsSVG"][grup]["path"]: # j es una llista de ordres de un path svg parametritzades amb variables
            cadena+=j[:2] #els dos primers caracter son: ordre svg + espai en blanc
            for k in j[2:].split():
                if k[0] == "l":         # la lletra l evita evaluar el que li seguisca
                    cadena += k[1:] +" "
                else:
                    k=str(k).replace('_',' ') #substitueix '_' per ' ' per a poder posar codi dins duna iteracció
                    print(k)
                    vl=eval(k)
                    cadena+=str(vl*escala)+" " #evalua cada fórmula aplicant els valors v[]
        return cadena

    def escriu_svg(self,fitxer,model, escala,v):
        dwg = svgwrite.Drawing(fitxer, profile='tiny' , size=(0,0)) # Crea un SVG Nom fitxer i ruta 
        for i in model["grupsSVG"].keys():    
            group = dwg.add(dwg.g(id=i)) #afegeix grup al SVG 
            group.add(dwg.path(self.genera_path(i,model,escala,v)).stroke(color=model["grupsSVG"][i]["color"]).fill(color="none")) #afegeix path al grup

        dwg.save() #tanca el fitxer SVG

    def getVs(self): # Llig els valors dels paràmetres desde l'interface
        v=8*[0]
        for e in range(8):
            try:
                val=eval(f'float(self.lineEdit_{e}.text())')

                if val < self.m[e][0] :
                    v[e] = self.m[e][0]
                    exec(f'self.lineEdit_{e}.setText(str(self.m[{e}][0]))')
                elif val > self.m[e][1]:
                    v[e] = self.m[e][1]
                    exec(f'self.lineEdit_{e}.setText(str(self.m[{e}][1]))')
                else:
                    v[e]=val
                

            except ValueError:
                v[e]=self.m[e][0]
        return v


    
    def edicio(self):
        v=self.getVs()
        horizontal=eval(self.caixa["maxx"].replace('_',' '))-(eval(self.caixa["minx"].replace('_',' ')))
        vertical=eval(self.caixa["maxy"].replace('_',' '))-(eval(self.caixa["miny"].replace('_',' ')))
        gran= horizontal if horizontal> vertical else vertical
        rate_min=tamany_miniatura_px/gran
        self.escriu_svg(fitxer,self.caixa,rate_min,v)
        self.mostraSVG()
    
    def guarda(self):
        v=self.getVs()

        fname=os.path.join(eixida,self.caixa["nom"]+str(int(v[0]))+"x"+str(int(v[1]))+"x"+str(int(v[2]))+".svg")
        
        rate = CDR_rate if self.selector.isChecked() else AI_rate

        self.escriu_svg(fname,self.caixa,rate,v)
        msg = QMessageBox()
        msg.setWindowTitle("TeDraGen")
        msg.setText("Arxiu reultant en "+fname+"  ")
        msg.setToolTip('YA ESTÀ COPIAT AL PORTAPAPERS!')
        pyperclip.copy(fname)
        p=msg.exec_()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())