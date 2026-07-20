# Simulación de Cola de Impresión

## Descripción

Este proyecto implementa una simulación de una cola de impresión
utilizando **Python**, **Programación Orientada a Objetos (POO)** y una
interfaz gráfica desarrollada con **Qt Designer**.

La aplicación permite registrar trabajos de impresión y procesarlos
respetando estrictamente el principio **FIFO (First In, First Out)**: el
primer trabajo que entra a la cola es el primero que será procesado.

Cada trabajo de impresión contiene:

-   **Consecutivo**
-   **Usuario**
-   **Nombre del documento**
-   **Número de páginas**

La interfaz permite agregar trabajos, visualizar los trabajos
pendientes, consultar el trabajo que se encuentra al frente de la cola y
procesar el siguiente trabajo.

------------------------------------------------------------------------

## Estructura general del proyecto

``` text
Interfaz gráfica
      │
      ▼
DialogImpresion
      │
      ▼
GestorImpresion
      │
      ▼
Queue
      │
      ▼
Node
      │
      ▼
TrabajoImpresion
```

La interfaz gráfica recibe las acciones del usuario y muestra la
información. La clase `GestorImpresion` contiene una instancia de
`Queue` y administra los trabajos. La clase `TrabajoImpresion`
representa cada trabajo almacenado en la cola.

------------------------------------------------------------------------

# Clase TrabajoImpresion

La clase `TrabajoImpresion` representa un trabajo individual de
impresión.

Cada objeto contiene:

``` python
class TrabajoImpresion(object):

    def __init__(self, consecutivo, usuario, documento, paginas):
        self.consecutivo = consecutivo
        self.usuario = usuario
        self.documento = documento
        self.paginas = paginas
```

El objeto completo se almacena dentro de la estructura `Queue`.

------------------------------------------------------------------------

# Clase GestorImpresion

La clase `GestorImpresion` administra la cola de trabajos de impresión:

``` python
class GestorImpresion(object):

    def __init__(self):
        self.cola = Queue()
        self.consecutivo = 1
```

La línea `self.cola = Queue()` permite utilizar la implementación
existente de la cola. No se utiliza una lista como sustituto de la
estructura principal.

------------------------------------------------------------------------

# Funcionamiento del algoritmo

El algoritmo general funciona de la siguiente manera:

``` text
1. El usuario introduce sus datos.
          │
          ▼
2. Se validan los datos.
          │
          ▼
3. Se crea un TrabajoImpresion.
          │
          ▼
4. El trabajo se agrega a la Queue.
          │
          ▼
5. La interfaz muestra los trabajos pendientes.
          │
          ▼
6. El primer trabajo puede consultarse.
          │
          ▼
7. Al imprimir, se elimina el primer trabajo.
          │
          ▼
8. La interfaz se actualiza.
```

La cola siempre conserva el orden en el que fueron agregados los
trabajos.

------------------------------------------------------------------------

# Principio FIFO

FIFO significa **First In, First Out**, es decir, **primero en entrar,
primero en salir**.

Si los trabajos se agregan en este orden:

``` text
1. Reporte.pdf
2. Tarea.docx
3. Examen.pdf
```

La cola será:

``` text
Reporte.pdf → Tarea.docx → Examen.pdf
```

Y el orden de impresión será exactamente el mismo.

------------------------------------------------------------------------

# Operaciones de la Queue utilizadas

## Enqueue

Agrega un nuevo elemento al final de la cola.

En el proyecto:

``` python
self.cola.enQueue(trabajo)
```

Cada nuevo trabajo se coloca después del último trabajo pendiente.

------------------------------------------------------------------------

## Dequeue

Elimina el elemento que se encuentra al frente.

En el proyecto:

``` python
trabajo = self.cola.head.data
self.cola.deQueue()
```

Primero se obtiene el trabajo que se procesará y después se elimina de
la cola.

------------------------------------------------------------------------

## Front / Peek

Permite consultar el primer elemento sin eliminarlo:

``` python
def consultarFrente(self):

    if self.cola.isEmpty():
        return None

    return self.cola.head.data
```

La consulta muestra qué trabajo será procesado a continuación, pero el
trabajo permanece dentro de la cola.

------------------------------------------------------------------------

## IsEmpty

Verifica si la cola no contiene elementos:

``` python
self.cola.isEmpty()
```

Se utiliza antes de consultar o procesar trabajos para evitar
operaciones sobre una cola vacía.

------------------------------------------------------------------------

## Size

Permite conocer cuántos trabajos están pendientes.

Como la `Queue` existente no contiene un método `size()`, el gestor
recorre sus nodos y cuenta los elementos:

``` python
def size(self):

    contador = 0
    temp = self.cola.head

    while temp is not None:
        contador += 1
        temp = temp.next

    return contador
```

------------------------------------------------------------------------

# Flujo para agregar un trabajo

Cuando el usuario presiona **Agregar a la cola**:

1.  Se obtienen los datos del usuario.
2.  Se verifica que el usuario no esté vacío.
3.  Se verifica que el documento no esté vacío.
4.  Se verifica que el número de páginas sea válido.
5.  Se crea un objeto `TrabajoImpresion`.
6.  Se agrega mediante `enQueue`.
7.  Se actualiza la tabla y el total de trabajos.

Ejemplo:

``` text
Usuario: Christian
Documento: Practica.pdf
Páginas: 5
```

Resultado:

``` text
1 | Christian | Practica.pdf | 5
```

------------------------------------------------------------------------

# Flujo para imprimir el siguiente trabajo

Cuando el usuario presiona **Imprimir siguiente**:

``` text
1. Se verifica si la cola está vacía.
          │
          ▼
2. Se obtiene el trabajo del frente.
          │
          ▼
3. Se ejecuta dequeue.
          │
          ▼
4. El trabajo se considera procesado.
          │
          ▼
5. Se actualiza la interfaz.
```

Si la cola es:

``` text
Trabajo 1 → Trabajo 2 → Trabajo 3
```

después de procesar el primero queda:

``` text
Trabajo 2 → Trabajo 3
```

------------------------------------------------------------------------

# Flujo para consultar el frente

Cuando se presiona **Consultar frente**:

1.  Se verifica si la cola está vacía.
2.  Se obtiene el primer trabajo.
3.  Se muestra su información.
4.  El trabajo permanece en la cola.

Por lo tanto, `front/peek` no modifica la estructura.

------------------------------------------------------------------------

# Validaciones

La aplicación valida:

-   Usuario vacío.
-   Documento vacío.
-   Número de páginas menor que 1.
-   Intento de imprimir cuando la cola está vacía.

Ejemplo:

``` text
No existen trabajos pendientes.
```

Esto evita realizar operaciones inválidas sobre una cola sin elementos.

------------------------------------------------------------------------

# Ejemplo de ejecución

Inicialmente:

``` text
Cola vacía
Total pendientes: 0
```

Se agrega:

``` text
1 | Christian | Practica.pdf | 5
```

Después se agrega:

``` text
2 | Ana | Tarea.docx | 10
```

La cola queda:

``` text
1 | Christian | Practica.pdf | 5
2 | Ana | Tarea.docx | 10
```

El frente es:

``` text
1 | Christian | Practica.pdf | 5
```

Al presionar **Imprimir siguiente**, se procesa el trabajo 1 y la cola
queda:

``` text
2 | Ana | Tarea.docx | 10
```

El segundo trabajo se convierte en el nuevo frente.

------------------------------------------------------------------------

# Conclusión

La aplicación implementa una simulación de una cola de impresión
utilizando una estructura de datos `Queue` y el principio FIFO.

La clase `TrabajoImpresion` representa cada trabajo, mientras que
`GestorImpresion` administra la cola y controla las operaciones
principales.

Las operaciones utilizadas son:

-   `enQueue`: agregar trabajos.
-   `deQueue`: procesar y eliminar el trabajo del frente.
-   `front/peek`: consultar el siguiente trabajo sin eliminarlo.
-   `isEmpty`: verificar si la cola está vacía.
-   `size`: contar los trabajos pendientes.

La interfaz gráfica permite observar visualmente el estado de la cola y
comprobar el funcionamiento del algoritmo en tiempo real.
