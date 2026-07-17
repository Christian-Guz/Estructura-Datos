from estructuras.lineales.lista_enlazada_simple import Lunkedlist
from estructuras.lineales.Cola_Queue import Queue

class Menu(object):
    def __init__(self):
        self.lunkedlist = Lunkedlist()
        self.opcion = 0
    
    def mostrar_menu(self):
        #Se muestran las opciones
        print("\nLista Enlazada\n")
        print("1.-Insertar Inicio\n2.-Insertar Final\n3.- Buscar\n4.-Imprimir\n5.-Eliminar Inicio\n6.-Eliminar Final\n7.-Cola o Queue\n8.-Salir")

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
            case "7":
                self.menu_Queue()
    
    def menu_Queue(self):
        self.queue = Queue()
        opc = 0
        while opc != "7":
            print("\n1.- Insertar nodo\n2.- Eliminar primer nodo\n3.- Imprimir primer valor\n4.- Imprimir último valor\n5.- Imprimir fila\n6.- Lista vacía\n7.- Salir")
            opc = input("Opcion: ")
            match opc:
                case "1":
                    elemento = input("Ingrese el elemento a agregar: ")
                    print(self.queue.enqueue(elemento))
                case "2":
                    print(self.queue.dequeue())
                case "3":
                    print(self.queue.firstqueue())
                case "4":
                    print(self.queue.lastqueue())
                case "5":
                    print(self.queue.printqueue())
                case "6":
                    print(self.queue.isEmpty())
    
    def ejecutar(self):
        #Esto será lo prmero en ejecutarse de la clase, si el usuario elige 5 saldrá de todo
        while self.opcion != "8":
            self.mostrar_menu()
            self.menu()