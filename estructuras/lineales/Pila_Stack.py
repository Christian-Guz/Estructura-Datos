from estructuras.lineales.nodo import Node

class Stack:
    def __init__(self):
        self.top = None
    
    def push(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
    
    def pop(self):
        if self.top == None:
            return "No hay elementos en la pila"
        else:
            temp = self.top.data
            self.top = self.top.next
            return f"El dato que se eliminó de la pila fue: {temp}"
    
    def top_of_stack(self):
        if self.top == None:
            return "No hay elementos en la pila"
        else: 
            return f"El top de la pila es: {self.top.data}"
    
    def print_stack(self):
        self.x = "No hay elementos en la pila"
        if self.top == None:
            return self.x
        else:
            temp = self.top
            self.x = "top "
            while temp is not None:
                self.x += f"-> {temp.data} "
                temp = temp.next
            return self.x
        
    def is_empty(self):
        return self.top is None