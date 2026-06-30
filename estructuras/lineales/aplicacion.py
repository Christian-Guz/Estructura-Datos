from estructuras.lineales.Pila_Stack import Stack


class ConversorPosfija:

    def __init__(self):
        self.pila = Stack()

    def prioridad(self, operador):

        prioridades = {
            '$': 3,
            '*': 2,
            '/': 2,
            '+': 1,
            '-': 1
        }

        return prioridades.get(operador, 0)

    def convertir(self, expresion):

        salida = ""

        for caracter in expresion:

            if caracter.isalnum():
                salida += caracter

            elif caracter == "(":
                self.pila.push(caracter)

            elif caracter == ")":

                while (not self.pila.is_empty()) and self.pila.peek() != "(":
                    salida += self.pila.pop_data()

                self.pila.pop_data()

            else:

                while (not self.pila.is_empty()) and self.pila.peek() != "(" and \
                      self.prioridad(self.pila.peek()) >= self.prioridad(caracter):

                    salida += self.pila.pop_data()

                self.pila.push(caracter)

        while not self.pila.is_empty():
            salida += self.pila.pop_data()

        return salida