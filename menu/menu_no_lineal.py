from estructuras.no_lineales.Binary_tree import BinaryTree

class menu_arbol(object):
    def __init__(self):
        self.arbol = BinaryTree()
        self.opc = 0
        
    def mostrar_menu(self):
        #Se muestran las opciones
        print("\nArbol de nodos\n")
        print("1.- Insertar un valor\n2.- Buscar un valor\n3.- Mostrar recorrido en Preorden\n4.- Mostrar recorrido en Inorden\n5.- Mostrar recorrido en Posorden\n6.- Conteo de Nodos\n7.- Salir")
    
    def menu(self):
        tree = BinaryTree()
        while True:
            self.mostrar_menu()
            opc = input("Selecciona una opción: ")
            if opc == "1":
                try:
                    value = int(input("Ingresa el valor que deseas insertar: "))
                    tree.insertar(value)
                except ValueError:
                    print("Debes ingresar un número entero.")
            elif opc == "2":
                try:
                    value = int(input("Ingresa el valor que deseas buscar: "))
                    if tree.buscar(value):
                        print("El valor se encuentra en el árbol.")
                    else:
                        print("El valor no se encuentra en el árbol.")
                except ValueError:
                    print("Debes ingresar un número entero.")
            elif opc == "3":
                print("Recorrido en preorden:")
                tree.preorden()
            elif opc == "4":
                print("Recorrido en inorden:")
                tree.inorden()
            elif opc == "5":
                print("Recorrido en posorden:")
                tree.posorden()
            elif opc == "6":
                print("Cantidad de nodos:", tree.contarNodos())
            elif opc == "6":
                print("Programa finalizado.")
                break
            else:
                print("Opción no válida. Intenta nuevamente.")