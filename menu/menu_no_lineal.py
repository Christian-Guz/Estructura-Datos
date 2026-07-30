from estructuras.no_lineales.Binary_tree import BinaryTree
from estructuras.no_lineales.Arbol_expresiones import NodeExpression
from estructuras.lineales.aplicacion import ConversorPosfija

class menu_arbol(object):
    def __init__(self):
        self.arbol = BinaryTree()
        self.opc = 0
    
    def mostrar_menu(self):
            print("\nMenú no lineales\n1.- Arbol de nodos\n2.- Arbol de expresiones\n3.- Salir")
    
    def menu(self):
        while True:
            self.mostrar_menu()
            self.opc = input("Selecciona una opcion: ")
            if self.opc == "1":
                self.mostrar_arbolNodos()
                self.menu()
            elif self.opc == "2":
                self.mostrar_arbolExpresiones()
                self.menu()
            elif self.opc == "3":
                print("Programa finalizado.")
                break
            else:
                print("Opcion no valida. Intente nuevamente")
        
    def mostrar_arbolNodos(self):
        self.opc = 0
        tree = BinaryTree()
        while True:
            print("\nArbol de nodos\n")
            print("1.- Insertar un valor\n2.- Buscar un valor\n3.- Mostrar recorrido en Preorden\n4.- Mostrar recorrido en Inorden\n5.- Mostrar recorrido en Posorden\n6.- Conteo de Nodos\n7.- Salir")
            self.opc = input("Selecciona una opción: ")
            if self.opc == "1":
                try:
                    value = int(input("Ingresa el valor que deseas insertar: "))
                    tree.insertar(value)
                except ValueError:
                    print("Debes ingresar un número entero.")
            elif self.opc == "2":
                try:
                    value = int(input("Ingresa el valor que deseas buscar: "))
                    if tree.buscar(value):
                        print("El valor se encuentra en el árbol.")
                    else:
                        print("El valor no se encuentra en el árbol.")
                except ValueError:
                    print("Debes ingresar un número entero.")
            elif self.opc == "3":
                print("Recorrido en preorden:")
                print(tree.preorden())
            elif self.opc == "4":
                print("Recorrido en inorden:")
                tree.inorden()
            elif self.opc == "5":
                print("Recorrido en posorden:")
                print(tree.posorden())
            elif self.opc == "6":
                print("Cantidad de nodos:", tree.contarNodos())
            elif self.opc == "7":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")
                
    def mostrar_arbolExpresiones(self):
        self.opc = 0
        tree = BinaryTree()
        treeEx = NodeExpression()
        pos = ConversorPosfija()
        while True:
            print("\nArbol de nodos\n")
            print("1.- Insertar expresión posfija\n2.- Mostrar preorden\n3.- Mostrar inorden\n4.- Mostrar posorden\n5.- Mostrar árbol\n6.- Salir")
            self.opc = input("Selecciona una opcion: ")
            if self.opc == "1":
                expression = input("Ingresa la expresión posfija: ")
                simbolo = expression.split()
                tree.root = (treeEx.build_expression_tree(simbolo))
                if tree.root is None:
                    print("Expresión inválida.")
                elif tree.root.left is None or tree.root.right is None:
                    print("Expresión inválida.")
                    tree.root = None
                else:
                    print("Se ha insertado la expresión en el árbol.")
                    resultado = pos.evaluar(simbolo)
                    print("Resultado de la operacion: ", resultado)
            elif self.opc == "2":
                print("Recorrido en preorden:")
                print(tree.preorden())
            elif self.opc == "3":
                print("Recorrido en inorden:")
                print(tree.inorden_expresion())
            elif self.opc == "4":
                print("Recorrido en posorden:")
                print(tree.posorden())
            elif self.opc == "5":
                print("Árbol:")
                print(tree.mostrar_arbol())
            elif self.opc == "6":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")