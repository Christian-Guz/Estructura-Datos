from estructuras.lineales.lista_enlazada_simple import Lunkedlist

class Menu(object):
    def __init__(self):
        self.lunkedlist = Lunkedlist()
        self.opcion = 0
    
    def mostrar_menu(self):
        #Se muestran las opciones
        print("\nLista Enlazada\n")
        print("1.-Insertar Inicio\n2.-Insertar Final\n3.- Buscar\n4.-Imprimir\n5.-Eliminar Inicio\n6.-Eliminar Final\n7.-Salir")

    def menu(self):
        #Se elige la opción
        self.opcion = input("Opción: ")
        match self.opcion:
            case "1":
                elemento = input("Ingrese el elemento a agregar: ")
                self.lunkedlist.insert_at_beginning(elemento)
                print(f"Elemento {elemento} agregado al inicio de la lista")
            case "2":
                elemento = input("Ingrese el elemento a agregar: ")
                self.lunkedlist.insert_at_end(elemento)
                print(f"Elemento {elemento} agregado al final de la lista")
            case "3":
                elemento = input("Ingrese el elemento a buscar: ")
                self.lunkedlist.search(elemento)
            case "4":
                print("\nContenido de la lista enlzazada:")
                self.lunkedlist.print_linked_list()
            case "5":
                print("Eliminando primer elemento de la lista...")
                self.lunkedlist.delete_at_beginning()
            case "6":
                print("Eliminando ultimo elemento de la lista...")
                self.lunkedlist.delete_at_end()
                
    
    def ejecutar(self):
        #Esto será lo prmero en ejecutarse de la clase, si el usuario elige 5 saldrá de todo
        while self.opcion != "7":
            self.mostrar_menu()
            self.menu()