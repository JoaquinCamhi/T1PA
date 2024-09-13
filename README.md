# Tarea 1: OOP, notación O y decoradores
Alumno: Joaquín Camhi

Este repositorio es una entrega para la Tarea 1 del ramo Programación Avanzada.

## Preguntas teóricas:

### 1. ¿Qué es un paradigma de programación?

Un paradigma de programación es un conjunto de principios, conceptos y prácticas que determinan cómo se estructura y organiza el código de un programa. Es un modelo o enfoque que guía el diseño y la implementación de algoritmos y estructuras de datos en un programa.

En la programación, un paradigma define la manera en que los problemas se modelan y resuelven. Los paradigmas más comunes incluyen:

- Paradigma Imperativo: Se basa en la ejecución secuencial de instrucciones que modifican el estado del programa. Dentro de este paradigma se incluyen:
  - Programación procedimental: Organiza el código en procedimientos o funciones que actúan sobre datos.
  - Programación orientada a objetos (OOP): Organiza el código en "objetos" que agrupan datos y funciones, facilitando la reutilización y la abstracción.

- Paradigma Declarativo: En lugar de describir cómo resolver un problema, se enfoca en qué se quiere obtener. Dentro de este paradigma se incluyen:
  - Programación funcional: Basada en la evaluación de funciones matemáticas sin efectos secundarios.
  - Programación lógica: Describe relaciones entre los datos utilizando lógica formal.

Cada paradigma tiene sus ventajas y desventajas dependiendo del problema a resolver. Por ejemplo, la programación orientada a objetos es útil para modelar sistemas complejos, mientras que la programación funcional es eficiente para problemas matemáticos o de procesamiento de datos.


### 2. ¿En qué se basa la programación orientada a objetos?

La programación orientada a objetos (OOP) es un paradigma de programación que organiza el software en objetos, los cuales encapsulan tanto los datos (atributos) como los comportamientos (métodos) relacionados con esos datos. Su principal objetivo es modelar elementos del mundo real o conceptos abstractos en objetos de software que interactúan para resolver problemas complejos.

Los conceptos clave de la OOP son:

- Clases: Son plantillas o moldes que definen los atributos y métodos comunes que compartirán los objetos creados a partir de la clase.
  
- Objetos: Son instancias de una clase. Tienen un estado (valores de atributos) y un comportamiento (definido por sus métodos). Los objetos representan entidades o conceptos del mundo real dentro del programa.

- Encapsulamiento: Los datos de un objeto están protegidos del acceso directo externo, lo que permite que solo puedan ser modificados mediante los métodos del objeto. Esto asegura la integridad y consistencia de los datos.

- Herencia: Permite crear nuevas clases basadas en clases existentes, heredando atributos y métodos. Esto fomenta la reutilización del código.

- Polimorfismo: Es la capacidad de diferentes clases de implementar métodos con el mismo nombre pero con comportamientos diferentes. Esto permite que el mismo método actúe de diversas formas dependiendo del objeto que lo utilice.

- Abstracción: Consiste en ocultar los detalles internos de la implementación y exponer solo las funcionalidades esenciales, permitiendo que los usuarios de la clase trabajen a un nivel más alto sin preocuparse por cómo están implementados.

La programación orientada a objetos facilita la creación de sistemas complejos y su mantenimiento, promoviendo la reutilización de código y la modularidad mediante herencia, polimorfismo y encapsulamiento.


### 3. ¿Cuál es la diferencia entre recursividad e iteración, y cómo se relaciona esto con la notación Big O?

#### Recursividad:
La recursividad ocurre cuando una función se llama a sí misma para resolver un problema, dividiéndolo en subproblemas más pequeños hasta llegar a un caso base, que es la condición de término. La recursividad es útil en problemas que tienen una estructura naturalmente repetitiva o divisoria, como los árboles o los problemas que siguen un enfoque de "divide y vencerás". La complejidad temporal de un algoritmo recursivo depende de cuántas veces se llame a la función y cómo se reduzca el problema en cada llamada. La recursividad puede tener complejidades que van desde \( O(1) \) hasta \( O(2^n) \), dependiendo de la naturaleza del problema.

#### Iteración:
La iteración implica repetir un conjunto de instrucciones utilizando estructuras de control como bucles for o while. A diferencia de la recursividad, en la iteración no hay llamadas a funciones adicionales, y la ejecución se repite hasta que se cumpla una condición de terminación. La complejidad temporal de un algoritmo iterativo está generalmente determinada por el número de veces que el bucle se ejecuta, siendo común una complejidad de \( O(n) \). Dependiendo de la estructura del bucle, la complejidad puede variar, como en el caso de bucles anidados que pueden tener \( O(n^2) \).

#### Relación con la notación Big O:
La notación Big O se utiliza para describir la complejidad temporal y espacial de un algoritmo, es decir, el tiempo que tarda en ejecutarse en función del tamaño de la entrada y la cantidad de memoria que utiliza.

- Recursividad: La complejidad de un algoritmo recursivo depende de cuántas veces la función se llama a sí misma y de cómo se reduzca el tamaño del problema en cada llamada.  
- Iteración: La complejidad de un algoritmo iterativo está determinada por el número de iteraciones que realiza un bucle. 

Algunas diferencias clave son:

Recursividad: utiliza llamadas a funciones y es más adecuada para problemas que pueden dividirse en subproblemas más pequeños. Puede tener una mayor complejidad espacial debido a las llamadas a la pila.

Iteración: utiliza bucles y es más eficiente en cuanto al uso de espacio, ya que no depende de llamadas adicionales a funciones. Sin embargo, algunos problemas son más difíciles de resolver utilizando iteración en lugar de recursividad.


### 4. Explica la diferencia de rendimiento entre O(1) y O(n) 

La notación Big O se utiliza para expresar la complejidad temporal de un algoritmo, es decir, cuánto tiempo tarda en ejecutarse en función del tamaño de la entrada. En las clases vimos dos formas de complejidad comunes: O(1)  y  O(n) 

#### Complejidad O(1): 
Un algoritmo con complejidad  O(1)  tiene un tiempo de ejecución constante, lo que significa que no depende del tamaño de la entrada. Esto ocurre cuando el número de operaciones que realiza el algoritmo es el mismo, independientemente de cuántos datos tenga que procesar. Un ejemplo común de  O(1) es acceder a un elemento de una lista por su índice, ya que la operación de acceder a una posición específica en memoria toma el mismo tiempo, sin importar el tamaño de la lista.

Este tipo de algoritmo es muy eficiente, ya que su tiempo de ejecución no crece con el tamaño de la entrada, lo que lo convierte en el tipo de complejidad óptimo.

#### Complejidad O(n):
Un algoritmo con complejidad O(n) tiene un tiempo de ejecución que crece linealmente con respecto al tamaño de la entrada. En este caso, si el tamaño de la entrada se duplica, el tiempo de ejecución también se duplicará. Este tipo de complejidad es típico de algoritmos que recorren todos los elementos de una lista, como cuando utilizamos un bucle for para procesar cada elemento de una lista o arreglo. O(1) es mucho más eficiente que O(n).

La diferencia clave en rendimiento entre \( O(1) \) y \( O(n) \) radica en cómo el tiempo de ejecución de un algoritmo se relaciona con el tamaño de la entrada. \( O(1) \) es independiente del tamaño de la entrada; un algoritmo con esta complejidad siempre tendrá el mismo tiempo de ejecución, ya sea que la entrada tenga un solo elemento o millones de elementos. Este tipo de complejidad es ideal para operaciones rápidas como el acceso directo a memoria. Por otro lado,  O(n) describe algoritmos cuyo tiempo de ejecución crece de manera lineal con respecto al tamaño de la entrada. Si un algoritmo tiene una complejidad \( O(n) \), el tiempo de ejecución será proporcional al número de elementos en la entrada, por lo que, a medida que crece el tamaño de la entrada, también lo hará el tiempo de ejecución.


### 5. ¿Cómo se calcula el orden en un programa que funciona por etapas?

Cuando un programa tiene varias etapas o fases de ejecución, el cálculo de la complejidad temporal total se realiza evaluando la complejidad de cada etapa y combinándolas para obtener una estimación del tiempo de ejecución total.

Por principio de la suma cada etapa de un programa tiene su propia complejidad. Si un programa consta de varias etapas que se ejecutan secuencialmente, la complejidad total se obtiene sumando las complejidades de cada etapa. Por ejemplo, si el programa tiene tres etapas con complejidades \( O(f(n)) \), \( O(g(n)) \) y \( O(h(n)) \), la complejidad total será:
\[ O(f(n)) + O(g(n)) + O(h(n)) \]

Sin embargo, según las reglas generales de la notación Big O, solo se considera el término dominante para expresar la complejidad total. Es decir, se ignoran los términos de menor orden, ya que la notación Big O se enfoca en el comportamiento a largo plazo.

Por dominancia de términos de mayor orden al calcular la complejidad total, si una de las etapas tiene una complejidad mayor que las otras, esa es la que prevalecerá en el cálculo. Por ejemplo, si un programa tiene dos etapas con complejidades \( O(n) \) y \( O(n^2) \), la complejidad total será \( O(n^2) \), ya que \( n^2 \) crece más rápidamente que \( n \) a medida que el tamaño de la entrada aumenta.


### 6. ¿Cómo se determina la complejidad temporal de un algoritmo recursivo?

La complejidad temporal de un algoritmo recursivo se determina analizando cuántas veces se llama a la función recursiva y cómo cambia el tamaño del problema en cada llamada. Este análisis se realiza utilizando una recurrencia, que es una ecuación que describe el tiempo de ejecución en función del tamaño del problema.

#### Pasos para determinar la complejidad temporal de un algoritmo recursivo:

1. Identificar el caso base: El caso base es la condición que detiene la recursión. El tiempo de ejecución en el caso base suele ser \( O(1) \), ya que se resuelve directamente sin más llamadas recursivas.

2. Describir la recurrencia: La recurrencia describe cómo se divide el problema en subproblemas más pequeños. Por ejemplo, en el cálculo del número de Fibonacci, el problema se divide en dos subproblemas de tamaño menor en cada llamada, resultando en una recurrencia de la forma:
   \[
   T(n) = T(n-1) + T(n-2) + O(1)
   \]
   Aquí, el problema se descompone en dos subproblemas, uno de tamaño \( n-1 \) y otro de tamaño \( n-2 \).

3. Resolver la recurrencia: Resolver la recurrencia implica determinar el comportamiento a largo plazo de las llamadas recursivas. En el caso del algoritmo de Fibonacci, la solución de la recurrencia es exponencial, específicamente \( O(2^n) \), ya que el número de llamadas crece exponencialmente con el tamaño del problema.

4. Aplicar el teorema maestro (si es aplicable): En algunos casos, el teorema maestro puede ayudar a resolver ecuaciones de recurrencia complejas. Sin embargo, en algoritmos como Fibonacci, este no es necesario, ya que la recurrencia es simple de resolver manualmente.



## Caminos en una PCB:
