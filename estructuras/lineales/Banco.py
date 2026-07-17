from estructuras.lineales.Cola_Queue import Queue
from datetime import datetime
from datetime import timedelta

class Nodo_Banco(object):
    def __init__(self, turno):
        self.turno = turno
        self.hora_entrada = datetime.now()

class Banco(object):
    def __init__(self):
        self.cola = Queue()
        self.total_clientes = 0
        self.tiempo_espera = timedelta()
        self.tiempo_total = 0
        self.turnos = []
        self.abierto = True
    
    def agregarCliente(self,turno):
        cliente = Nodo_Banco(turno)
        self.cola.enQueue(cliente)
        self.total_clientes += 1
        self.turnos.append(turno)
        return f"{cliente.turno} | {cliente.hora_entrada.strftime('%H:%M:%S')}" 
    
    def atenderCliente(self):
        temp1 = self.cola.head
        self.cola.deQueue()
        self.tiempo = datetime.now() - temp1.data.hora_entrada
        self.tiempo_espera = int(self.tiempo.total_seconds())
        self.tiempo_total += self.tiempo_espera
        self.turnos.remove(temp1.data.turno)
        return temp1.data

    def cerrarBanco(self):
        if self.total_clientes == 0:
            self.abierto = False
        else:
            if self.cola.isEmpty():
                self.abierto = False
                self.promedio = int(self.tiempo_total / self.total_clientes)
                return "No hay clientes por atender"
            else:
                return "Aún hay clientes por atender"
            