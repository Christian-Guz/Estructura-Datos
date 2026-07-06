# Conversión de Expresiones Infijas a Posfijas y Evaluación de Expresiones Posfijas

## Objetivo

El objetivo de esta práctica es utilizar la estructura de datos **Pila (Stack)** para resolver dos problemas:

1. Convertir una expresión escrita en notación infija a notación posfija.
2. Evaluar una expresión escrita en notación posfija para obtener su resultado.

La implementación se realizó utilizando programación orientada a objetos en Python, reutilizando la clase `Stack` desarrollada previamente.

---

# ¿Qué es una expresión infija?

Es la forma tradicional en la que las personas escriben las operaciones matemáticas.

Ejemplos:

```
2+3
```

```
2+3*4
```

```
(2+3)*4
```

En este tipo de expresión los operadores se encuentran entre los operandos.

---

# ¿Qué es una expresión posfija?

También conocida como **Notación Polaca Inversa (RPN)**.

En este tipo de expresión los operadores siempre se escriben después de sus operandos.

Ejemplos:

| Infija | Posfija |
|--------|----------|
| 2+3 | 23+ |
| 2+3*4 | 234*+ |
| (2+3)*4 | 23+4* |

La ventaja de esta notación es que elimina la necesidad de utilizar paréntesis y facilita la evaluación utilizando una pila.

---

# Conversión de Infija a Posfija

Para realizar la conversión se recorre la expresión carácter por carácter.

## Paso 1

Si el carácter es un operando (letra o número), se agrega directamente al resultado.

Ejemplo:

```
A+B
```

Se lee:

```
A
```

Resultado:

```
A
```

---

## Paso 2

Si aparece un operador (+, -, *, /, $), se compara su prioridad con el operador que está en la cima de la pila.

Si el operador de la pila tiene mayor o igual prioridad, primero se extrae de la pila y se agrega al resultado.

Después se inserta el nuevo operador.

---

## Paso 3

Si aparece un paréntesis izquierdo:

```
(
```

Se inserta directamente en la pila.

---

## Paso 4

Si aparece un paréntesis derecho:

```
)
```

Se extraen operadores de la pila y se agregan al resultado hasta encontrar el paréntesis izquierdo.

El paréntesis izquierdo se elimina de la pila pero no se agrega al resultado.

---

## Paso 5

Cuando termina de recorrerse toda la expresión, todos los operadores restantes de la pila se agregan al resultado.

---

# Ejemplo de conversión

Expresión infija:

```
A+B*C
```

Proceso:

| Carácter | Acción | Salida | Pila |
|----------|--------|--------|------|
| A | Operando | A | |
| + | Push | A | + |
| B | Operando | AB | + |
| * | Push | AB | * + |
| C | Operando | ABC | * + |
| Fin | Vaciar pila | ABC*+ | |

Resultado:

```
ABC*+
```

---

# Evaluación de una Expresión Posfija

Una vez obtenida la expresión posfija, puede calcularse su resultado.

El algoritmo vuelve a recorrer la expresión carácter por carácter.

---

## Paso 1

Si el carácter es un número, se inserta en la pila.

Ejemplo:

```
234*+
```

Después de leer:

```
2
```

La pila contiene:

```
2
```

---

## Paso 2

Cuando aparece un operador, se extraen los dos elementos superiores de la pila.

Es importante respetar el orden:

```
operando1 operador operando2
```

Por ejemplo, si aparece:

```
*
```

y la pila contiene:

```
4
3
2
```

Se extraen:

```
4
```

y después

```
3
```

Se realiza:

```
3*4
```

El resultado:

```
12
```

se vuelve a insertar en la pila.

Ahora la pila queda:

```
12
2
```

---

## Paso 3

El proceso continúa hasta terminar de recorrer toda la expresión.

Al finalizar solamente queda un elemento en la pila.

Ese elemento corresponde al resultado final.

---

# Ejemplo de evaluación

Expresión posfija:

```
234*+
```

Proceso:

| Carácter | Acción | Pila |
|----------|--------|------|
|2|Push|2|
|3|Push|3 2|
|4|Push|4 3 2|
|*|3×4=12|12 2|
|+|2+12=14|14|

Resultado final:

```
14
```

---

# ¿Cómo se utiliza la pila durante la conversión?

Durante la conversión de infija a posfija, la pila **almacena temporalmente los operadores y los paréntesis**.

Los operandos nunca permanecen en la pila; se envían directamente al resultado.

La pila permite respetar la prioridad de los operadores y el orden indicado por los paréntesis.

En este proceso la pila funciona como un almacenamiento temporal para decidir cuándo un operador debe agregarse a la expresión posfija.

---

# ¿Cómo se utiliza la pila durante la evaluación?

Durante la evaluación ocurre lo contrario.

La pila ya no almacena operadores.

Ahora almacena únicamente **operandos numéricos y resultados parciales**.

Cada vez que aparece un operador:

1. Se extraen los dos operandos superiores.
2. Se realiza la operación correspondiente.
3. El resultado vuelve a insertarse en la pila.

Este procedimiento se repite hasta terminar la expresión.

Gracias al comportamiento **LIFO (Last In, First Out)** de la pila, siempre se recuperan primero los operandos más recientes, lo que garantiza que las operaciones se realicen en el orden correcto.

---

# Conclusión

En esta práctica se comprobó que la estructura de datos **Pila (Stack)** es una herramienta fundamental para el manejo de expresiones matemáticas.

Durante la conversión de una expresión infija a posfija, la pila permite organizar los operadores de acuerdo con su prioridad y el uso de paréntesis.

Posteriormente, durante la evaluación de la expresión posfija, la misma estructura se utiliza para almacenar operandos y resultados intermedios, permitiendo calcular el resultado final sin necesidad de utilizar la función `eval()` de Python.

De esta manera se demuestra una aplicación práctica de la estructura de datos pila, reutilizando la implementación desarrollada previamente mediante programación orientada a objetos.