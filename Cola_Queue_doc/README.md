# Explicación de la clase Queue

## 1. ¿Qué es una cola?

Una **cola (Queue)** es una estructura de datos lineal donde los
elementos se agregan por un extremo (final o *tail*) y se eliminan por
el otro (inicio o *head*). Su funcionamiento es similar al de una fila
de personas esperando ser atendidas.

## 2. ¿Qué significa FIFO?

**FIFO** significa **First In, First Out** (Primero en entrar, primero
en salir). El primer elemento que se inserta en la cola será también el
primero en eliminarse.

## 3. ¿Qué hace cada método?

-   **enqueue(data):** Agrega un nuevo elemento al final de la cola.
-   **dequeue():** Elimina el primer elemento de la cola.
-   **printQueue():** Recorre la cola y muestra todos sus elementos
    desde `head` hasta `tail`.
-   **firstQueue():** Muestra el primer elemento de la cola sin
    eliminarlo.
-   **lastQueue():** Muestra el último elemento de la cola sin
    eliminarlo.

## 4. ¿En qué se diferencia de una pila (Stack)?

La principal diferencia está en el orden en que se eliminan los
elementos:

-   **Queue:** utiliza **FIFO**, por lo que el primer elemento agregado
    es el primero en salir.
-   **Stack:** utiliza **LIFO (Last In, First Out)**, donde el último
    elemento agregado es el primero en salir.

## 5. Ejemplo de ejecución

Supongamos la siguiente secuencia:

1.  `enqueue(10)` → Cola: `10`
2.  `enqueue(20)` → Cola: `10 -> 20`
3.  `enqueue(30)` → Cola: `10 -> 20 -> 30`
4.  `firstQueue()` → Devuelve `10`
5.  `lastQueue()` → Devuelve `30`
6.  `dequeue()` → Se elimina `10`. Cola: `20 -> 30`
7.  `printQueue()` → Muestra `Head -> 20 -> 30 <- Tail`

Este ejemplo demuestra el comportamiento FIFO, ya que el primer elemento
insertado (`10`) fue el primero en eliminarse.
