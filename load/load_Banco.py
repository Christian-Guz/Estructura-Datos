from datetime import datetime
from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from estructuras.lineales.Banco import Banco

class DialogBanco(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Banco.ui", self)
        self.banco = Banco()
        self.btn_turno.clicked.connect(self.turno)
        self.btn_atender.clicked.connect(self.atender)
        self.btn_cerrar.clicked.connect(self.cerrar)
    
    def turno(self):
        if self.txt_turno.text() == "":
            self.lbl_duda.setText("Ingrese un turno")
        else:
            self.lbl_duda.setText("")
            turno = self.txt_turno.text()
            if turno not in self.banco.turnos:
                lista = self.banco.agregarCliente(turno)
                texto_actual = self.lbl_lista.text()
                self.lbl_lista.setText(texto_actual + "\n" + lista)
            else:
                self.lbl_duda.setText("Ya hay un cliente con \n ese turno")
            self.txt_turno.setText("")
    
    def atender(self):
        if not self.banco.cola.isEmpty():
            lista = self.banco.atenderCliente()
            texto = self.lbl_lista.text()
            lineas = texto.split("\n")
            linea_eliminar = lista.turno + " | " + lista.hora_entrada.strftime('%H:%M:%S')
            if linea_eliminar in lineas:
                lineas.remove(linea_eliminar)
            self.lbl_lista.setText("\n".join(lineas))
            self.lbl_atendido.setText(lista.turno + " | " + datetime.now().strftime('%H:%M:%S') + " -> " + str(self.banco.tiempo_espera) + "s")
        else:
            pass
    
    def cerrar(self):
        self.lbl_abierto.setText(self.banco.cerrarBanco())
        if self.banco.abierto:
            self.btn_turno.setEnabled(False)
        else:
            if self.banco.total_clientes == 0:
                self.btn_turno.setEnabled(False)
                self.btn_atender.setEnabled(False)
                self.btn_cerrar.setEnabled(False)
                self.lbl_atendido.setText("")
                self.lbl_clientes.setText("Total de clientes atendidos: " + str(0))
                self.lbl_tiempo.setText("Tiempo promedio: " + str(0) + "s")
            else:
                self.btn_turno.setEnabled(False)
                self.btn_atender.setEnabled(False)
                self.btn_cerrar.setEnabled(False)
                self.lbl_atendido.setText("")
                self.lbl_clientes.setText("Total de clientes atendidos: " + str(self.banco.total_clientes))
                self.lbl_tiempo.setText("Tiempo promedio: " + str(self.banco.promedio) + "s") 
