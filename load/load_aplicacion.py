from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.aplicacion import ConversorPosfija

class DialogAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/aplicacion.ui", self)

        self.conversor = ConversorPosfija()
        self.btn_conver.clicked.connect(self.convertir)
        self.btn_evaluar.clicked.connect(self.evaluar)
    
    def convertir(self):
        expresion = self.txt_infja.text()
        self.resultado = self.conversor.convertir(expresion)
        self.lbl_posfija.setText(self.resultado)
    
    def evaluar(self):
        expresion_infija = self.txt_infja.text()
        expresion_posfija = self.conversor.convertir(expresion_infija)
        resultado = self.conversor.evaluar(expresion_posfija)
        self.lbl_evaluacion.setText(str(resultado))