from estructuras.lineales.Cola_Queue import Queue


class TrabajoImpresion(object):

    def __init__(self, consecutivo, usuario, documento, paginas):
        self.consecutivo = consecutivo
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas

    def __str__(self):
        return (str(self.consecutivo) + " | " +
                self.usuario + " | " +
                self.documento + " | " +
                str(self.paginas))


class GestorImpresion(object):

    def __init__(self):
        self.cola = Queue()
        self.consecutivo = 1

    # Agrega un nuevo trabajo a la cola (enqueue)
    def agregarTrabajo(self, usuario, documento, paginas):

        trabajo = TrabajoImpresion(
            self.consecutivo,
            usuario,
            documento,
            paginas
        )

        self.cola.enQueue(trabajo)
        self.consecutivo += 1

        return trabajo

    # Procesa el primer trabajo (dequeue)
    def imprimirSiguiente(self):

        if self.cola.isEmpty():
            return None

        trabajo = self.cola.head.data
        self.cola.deQueue()

        return trabajo

    # Consulta el frente de la cola (peek/front)
    def consultarFrente(self):

        if self.cola.isEmpty():
            return None

        return self.cola.head.data

    # Devuelve la cantidad de trabajos pendientes
    def size(self):

        contador = 0
        temp = self.cola.head

        while temp is not None:
            contador += 1
            temp = temp.next

        return contador

    # Devuelve True si no existen trabajos
    def isEmpty(self):

        return self.cola.isEmpty()

    # Devuelve todos los trabajos para llenar la tabla
    def obtenerTrabajos(self):

        trabajos = []

        temp = self.cola.head

        while temp is not None:
            trabajos.append(temp.data)
            temp = temp.next

        return trabajos