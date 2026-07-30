from estructuras.lineales.Pila_Stack import Stack
from estructuras.no_lineales.Binary_tree import NodeTree, BinaryTree

class NodeExpression(object):
    def __init__(self):
        self.pila = Stack()
        self.root = BinaryTree()
    
    def build_expression_tree(self, expresion):
        for caracter in expresion:
            if caracter.isalnum():
                nodo = NodeTree(caracter)
                self.pila.push(nodo)
            else:
                nodo = NodeTree(caracter)
                nodo.right = self.pila.pop_data()
                nodo.left = self.pila.pop_data()
                self.pila.push(nodo)
        raiz = self.pila.pop_data()
        return raiz
