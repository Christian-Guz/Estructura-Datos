# Conversión de Expresión Infija a Posfija

## Objetivo

Convertir una expresión escrita en notación infija a notación posfija utilizando una estructura de datos tipo pila.

## Algoritmo

La conversión recorre la expresión carácter por carácter.

- Los operandos se agregan directamente al resultado.
- Los operadores se almacenan temporalmente en una pila.
- Antes de insertar un operador, se compara su prioridad con el operador que está en la cima de la pila.
- Si la prioridad del operador en la pila es mayor o igual, este se extrae y se agrega al resultado.
- Los paréntesis sirven para controlar el orden de evaluación.
- Al finalizar el recorrido, todos los operadores restantes en la pila se agregan al resultado.

## Prioridad de operadores

| Operador | Prioridad |
|-----------|-----------|
| $ | 3 |
| * / | 2 |
| + - | 1 |

## Ejemplo

Expresión infija:

A+B*C

Proceso:

- A → salida
- + → pila
- B → salida
- * → pila
- C → salida
- Fin → sacar operadores de la pila

Resultado:

ABC*+

## Uso de la pila

La pila almacena temporalmente los operadores y los paréntesis. Gracias a su comportamiento LIFO (Last In, First Out), permite respetar la precedencia de operadores y generar correctamente la expresión en notación posfija.