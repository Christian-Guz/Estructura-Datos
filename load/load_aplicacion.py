from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.aplicacion import ConversorPosfija

class DialogAplicacion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/aplicacion.ui", self)

        self.conversor = ConversorPosfija()
        self.btn_conver.clicked.connect(self.convertir)
    
    def convertir(self):
        expresion = self.txt_infja.text()
        resultado = self.conversor.convertir(expresion)
        self.lbl_posfija.setText(resultado)