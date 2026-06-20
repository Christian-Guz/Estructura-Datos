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
        self.x = ""
        self.x = "Head -> "
        while temp is not None:
            if temp.next is None:
                self.x += f"{temp.data} <- Tail"
                temp = temp.next
            else:
                self.x += f"{temp.data} -> "
                temp = temp.next
        print(self.x)
        
    def insert_at_end(self, data):
        #Paso 1: Crear un nuevo nodo con el dato proporcionado
        new_node = Node(data)
        #Paso 2: Verificar si la lista esta vacia
        if self.head:
            #Si la lista no esta vacia, el nuevo nodo se convierte en la cola
            #En nodo actual de la cola apunta al nuevo nodo que se creó
            self.tail.next = new_node
            #Luego, la cola se actualiza para ser el nuevo nodo
            self.tail = new_node
        else:
            #Si la lista esta vacia, el nuevo nodo se convierte en la cabeza y la cola
            self.head = new_node
            self.tail = new_node
    
    def search(self, data):
        #Paso 1: Iniciar un nodo temporal con la dirección de la cabeza del nodo
        current_node = self.head
        self.x = ""
        while current_node:
            #Paso 2: Verificar si el dato del nodo actual es igual al dato buscado
            if current_node.data == data:
                #Si el dato del nodo actual es igual al dato buscado, se devuelve True
                self.x = f"El dato {current_node.data} se encuentra en la lista"
                return True
                #Si no, el nodo temporal cambia al siguiente nodo
            else:
                current_node = current_node.next
        #Si el dato buscado no se encuentra en la lista, se devuelve False
        self.x =f"El dato {data} no se encuentra en la lista"
        print(self.x)
        return False
    
    def delete_at_beginning(self):
        self.x = ""
        #Paso 1: Verificar si la lista no está vacia
        if self.head == None and self.tail == None:
            self.x = "No existen nodos en la lista"
        #Paso 2: Verificar si la lista tiene un solo nodo
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.x = "El primer elemento se ha eliminado"
            else:
                #Paso 3: Actualizar la cabeza para ser el siguiente nodo y eliminar el nodo inicial
                self.head = self.head.next
                self.x = "El primer elemento se ha eliminado"
        print(self.x)
    
    def delete_at_end(self):
        self.x = ""
        #Paso 1: Verificar si la lista no está vacia
        if self.head == None and self.tail == None:
            self.x ="No existen nodos en la lista"
        #Paso 2: Verificar si la lista tiene un solo nodo
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
                self.x = "El ultimo elemento se ha eliminado"
            else:
                #Paso 3: Actualizar la cola para ser el nodo anterior a la cola y eliminar la cola
                temp = self.head
                while temp.next != self.tail:
                    temp = temp.next
                temp.next = None
                self.tail = temp
                self.x = "El ultimo elemento se ha eliminado"
        print(self.x)