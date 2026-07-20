from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5 import uic
from PyQt5.QtWidgets import QHeaderView

from estructuras.lineales.Cola_Impresion import GestorImpresion


class DialogImpresion(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Impresion.ui", self)
        self.gestor = GestorImpresion()
        
        self.tbl_trabajos.verticalHeader().setVisible(False)
        self.tbl_trabajos.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tbl_trabajos.verticalHeader().setDefaultSectionSize(30)
        self.tbl_trabajos.setEditTriggers(self.tbl_trabajos.NoEditTriggers)

        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_imprimir.clicked.connect(self.imprimir)
        self.btn_frente.clicked.connect(self.consultarFrente)

        self.actualizarTabla()

    # Agregar trabajo
    def agregar(self):
        usuario = self.txt_usuario.text().strip()
        documento = self.txt_documento.text().strip()
        paginas = self.spn_paginas.value()
        if usuario == "":
            self.lbl_mensaje.setText("Ingrese el nombre del usuario.")
            return
        if documento == "":
            self.lbl_mensaje.setText("Ingrese el nombre del documento.")
            return
        if paginas < 1:
            self.lbl_mensaje.setText("Las páginas deben ser mayores que cero.")
            return
        trabajo = self.gestor.agregarTrabajo(
            usuario,
            documento,
            paginas
        )
        self.lbl_mensaje.setText(
            "Trabajo agregado correctamente.\n\n"
            "Consecutivo: " + str(trabajo.consecutivo)
        )
        self.txt_usuario.clear()
        self.txt_documento.clear()
        self.spn_paginas.setValue(1)
        self.actualizarTabla()
        
    # Imprimir siguiente
    def imprimir(self):
        trabajo = self.gestor.imprimirSiguiente()
        if trabajo is None:
            self.lbl_mensaje.setText(
                "No existen trabajos pendientes."
            )
            self.lbl_frente.setText(
                "Frente: Sin trabajos"
            )
            return
        self.lbl_mensaje.setText(
            "Trabajo procesado:\n\n"
            + str(trabajo)
        )
        self.actualizarTabla()
        self.lbl_frente.setText(
                "Frente: Presiones 'Consultar frente'"
            )

    # Consultar frente
    def consultarFrente(self):
        trabajo = self.gestor.consultarFrente()
        if trabajo is None:
            self.lbl_frente.setText(
                "Frente: Sin trabajos"
            )
            return
        self.lbl_frente.setText(
            "Frente: "
            + str(trabajo.consecutivo)
            + " | "
            + trabajo.usuario
            + " | "
            + trabajo.documento
            + " | "
            + str(trabajo.paginas)
            + " páginas"
        )

    # Actualizar tabla
    def actualizarTabla(self):
        trabajos = self.gestor.obtenerTrabajos()
        self.tbl_trabajos.setRowCount(len(trabajos))
        fila = 0
        for trabajo in trabajos:
            self.tbl_trabajos.setItem(
                fila,
                0,
                QTableWidgetItem(str(trabajo.consecutivo))
            )
            self.tbl_trabajos.setItem(
                fila,
                1,
                QTableWidgetItem(trabajo.usuario)
            )
            self.tbl_trabajos.setItem(
                fila,
                2,
                QTableWidgetItem(trabajo.documento)
            )
            self.tbl_trabajos.setItem(
                fila,
                3,
                QTableWidgetItem(str(trabajo.paginas))
            )
            fila += 1
        self.lbl_total.setText(
            "Total pendientes: "
            + str(self.gestor.size())
        )
        self.consultarFrente()