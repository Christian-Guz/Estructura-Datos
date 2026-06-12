from estructuras.lineales.nodo import Node

class Lunkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_at_beginning(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionad
        new_node = Node(data)
        #Paso 2: Verificar si la lista está vacía
        if self.head is None and self.tail is None:
            #Si la lista está vacía, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
        else:
            #Si la lista no está vacia, el nuevo nodo se convierte en la cabeza
            new_node.next = self.head
            #Luego, la cabeza se actualiza para ser el nuevo nodo
            self.head = new_node
    
    def print_linked_list(self):
        temp = self.head
        print("Head ->", end="")
        while temp is not None:
            print(temp.data,"->", end=" ")
            temp = temp.next
        print("<- Tail")