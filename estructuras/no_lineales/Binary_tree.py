from binarytree import Node as BTNode

class NodeTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree(object):
    def __init__(self):
        self.root = None
        
    def insertar(self, value):
        self.root = self._insertar(self.root, value)
    
    def _insertar(self, node, value):
        if node is None:
            print("Operación realizada.")
            return NodeTree(value)
        if value < node.value:
            node.left = self._insertar(node.left, value)
        elif value > node.value:
            node.right = self._insertar(node.right, value)
        else:
            print("Ya existe ese valor en el árbol")
        return node
    
    def buscar(self, value):
        return self._buscar(self.root, value)
        
    def _buscar(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        if value < node.value:
            return self._buscar(node.left, value)
        return self._buscar(node.right, value)
    
    def preorden(self):
        return self._preorden(self.root)
        
    def _preorden(self, node):
        if node is  None:
            return ""
        texto = str(node.value) + " "
        texto += self._preorden(node.left)
        texto += self._preorden(node.right)
        return texto
    
    def inorden(self):
        self._inorden(self.root)
        print()
        
    def _inorden(self, node):
        if node is not None:
            self._inorden(node.left)
            print(node.value, end=" ")
            self._inorden(node.right)
            
    def posorden(self):
        return self._posorden(self.root).strip()
        
    def _posorden(self, node):
        if node is None:
            return ""
        texto = ""
        texto += self._posorden(node.left)
        texto += self._posorden(node.right)
        texto += str(node.value) + " "
        return texto
    
    def contarNodos(self):
        return self._contarNodos(self.root)

    def _contarNodos(self, node):
        if node is None:
            return 0
        return (1 + self._contarNodos(node.left) + self._contarNodos(node.right))

    def inorden_expresion(self):
        return self.__inorden_expresion(self.root)

    def __inorden_expresion(self, node):
        if node is None:
            return ""
        if node.left is None and node.right is None:
            return str(node.value)
        izquierda = self.__inorden_expresion(node.left)
        derecha = self.__inorden_expresion(node.right)
        return "(" + izquierda + " " + str(node.value) + " " + derecha + ")"
    
    def convertir_binarytree(self, nodo):
        if nodo is None:
            return None
        nuevo = BTNode(nodo.value)
        nuevo.left = self.convertir_binarytree(nodo.left)
        nuevo.right = self.convertir_binarytree(nodo.right)
        return nuevo
    
    def mostrar_arbol(self):
        if self.root is None:
            return "El árbol está vacío."
        raiz = self.convertir_binarytree(self.root)
        return str(raiz)