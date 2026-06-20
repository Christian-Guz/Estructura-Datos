from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.lista_enlazada_simple import Lunkedlist

class DialogListasEnlazadas(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Listas_Enlazadas.ui", self)
        self.lista = Lunkedlist()
        
        self.btn_agregar_inicio.clicked.connect(self.agregar_inicio)
        self.btn_agregar_final.clicked.connect(self.agregar_final)
        self.btn_eliminar_inicio.clicked.connect(self.eliminar_inicio)
        self.btn_eliminar_final.clicked.connect(self.eliminar_final)
        self.btn_buscar.clicked.connect(self.buscar)
        self.btn_imprimir.clicked.connect(self.imprimir)
    
    def agregar_inicio(self):
        if self.txt_dato.text() == "":
            self.lbl_lista.setText("Ingrese un dato")
        else:
            self.lista.insert_at_beginning(self.txt_dato.text())
            self.lbl_lista.setText(f"Elemento {self.txt_dato.text()} agregado al inicio de la lista")
        self.txt_dato.setText("")
    
    def agregar_final(self):
        if self.txt_dato.text() == "":
            self.lbl_lista.setText("Ingrese un dato")
        else:
            self.lista.insert_at_end(self.txt_dato.text())
            self.lbl_lista.setText(f"Elemento {self.txt_dato.text()} agregado al final de la lista")
        self.txt_dato.setText("")
        
    def eliminar_inicio(self):
        self.lista.delete_at_beginning()
        self.lbl_lista.setText(self.lista.x)
        self.txt_dato.setText("")
    
    def eliminar_final(self):
        self.lista.delete_at_end()
        self.lbl_lista.setText(self.lista.x)
        self.txt_dato.setText("")
    
    def buscar(self):
        if self.txt_dato.text() == "":
            self.lbl_lista.setText("Ingrese un dato")
        else:
            self.lista.search(self.txt_dato.text())
            self.lbl_lista.setText(self.lista.x)
        self.txt_dato.setText("")
    
    def imprimir(self):
        self.lista.print_linked_list()
        self.lbl_lista.setText(self.lista.x)
        self.txt_dato.setText("")