from estructuras.lineales.nodo import Node

class Queue(object):
    def __init__(self):
        self.head = None
        self.tail = None
    
    def enQueue(self, data):
        new_node = Node(data) #Se crea nodo con el dato otorgado
        if self.head is None and self.tail is None: #Si ambos están vacíos, ambos apuntarán al nodo
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node #Si no, el next de la cola apuntará al nodo y la cola cola hará lo mismo
            self.tail = new_node
        return "Se ha agregado el nodo a la fila"
    
    def deQueue(self):
        if self.head is None and self.tail is None: #En caso de no haber nada en fila, solo mostrará el mensaje
            return "No existen valores en la fila"
        else:
            self.head = self.head.next #Head apuntará al nodo siguiente eliminando el anterior
            if self.head is None:
                self.tail = None
            return "Se ha eliminado el nodo de la fila" 
    
    def firstQueue(self):
        if self.head is None and self.tail is None:
            return "No existen valores en la fila"
        else:
            return f"Head -> {self.head.data}" #Imprime la cabeza
    
    def lastQueue(self):
        if self.head is None and self.tail is None:
            return "No existen valores en la fila"
        else:
            return f"Tail -> {self.tail.data}" #Imprime la cola
    
    def printQueue(self): 
        if self.head is None and self.tail is None:
            return "No existen valores en la fila"
        else:
            temp = self.head #Se crea un temporal
            x = "Head -> " #Se crea un texto
            while temp != None: #Se hace un bucle hasta que temporal sea un None
                if temp.next is None: #Si el siguiente de temporal es None se agrega el dato y termina el texto con tail
                    x += f"{temp.data} <- Tail"
                    temp = temp.next #Avanza el temporal apuntando a su next
                else:
                    x += f"{temp.data} -> " #En caso de no ser None se agrega el dato con una flecha
                    temp = temp.next #El temp apuntará a su next hasta que su valor sea None
            return x #Imprime todo lo que encontró
        
    def isEmpty(self):
        if self.head is None and self.tail is None: #Si está vacía la lista
            return True #Imprime True
        else:
            return False #Imprime None
        
    def listaQueue(self): 
        temp = self.head 
        x = [] 
        while temp != None: 
            if temp.next is None: 
                x.append(temp.data)
                temp = temp.next 
        return x 