from PyQt5.QtWidgets import QDialog
from PyQt5 import uic
from PyQt5.QtCore import Qt
from estructuras.no_lineales.Arbol_expresiones import NodeExpression
from estructuras.no_lineales.Binary_tree import BinaryTree
from estructuras.lineales.aplicacion import ConversorPosfija

class DialogArbolExpresiones(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("ui/Arbol_Expresiones.ui", self)
        self.node = NodeExpression()
        self.tree = BinaryTree()
        self.treeEx = NodeExpression()
        self.pos = ConversorPosfija()
        
        self.txtResultado.setAlignment(Qt.AlignCenter)
        
        self.btn_ingresar.clicked.connect(self.leer_expresion)
        self.btn_preorden.clicked.connect(self.mostrar_preorden)
        self.btn_inorden.clicked.connect(self.mostrar_inorden)
        self.btn_postorden.clicked.connect(self.mostrar_postorden)
        self.btn_arbol.clicked.connect(self.mostrar_arbol)
    
    def leer_expresion(self):
        if self.txt_postorden.text() == "":
            self.txtResultado.setText("Ingrese una expresión")
        else:
            expression = self.txt_postorden.text()
            simbolo = expression.split()
            self.tree.root = (self.treeEx.build_expression_tree(simbolo))
            if self.tree.root is None:
                self.txtResultado.setText("Expresión inválida.")
            elif self.tree.root.left is None or self.tree.root.right is None:
                self.txtResultado.setText("Expresión inválida.")
                self.tree.root = None
            else:
                resultado = self.pos.evaluar(simbolo)
                self.txtResultado.setText(f"Se ha insertado la expresión en el árbol.\nResultado de la operacion: {resultado}")

    def mostrar_preorden(self):
        self.txtResultado.setText(self.tree.preorden())
    
    def mostrar_inorden(self):
        self.txtResultado.setText(self.tree.inorden_expresion())
        
    def mostrar_postorden(self):
        self.txtResultado.setText(self.tree.posorden())
    
    def mostrar_arbol(self):
        self.txtResultado.setText(self.tree.mostrar_arbol())