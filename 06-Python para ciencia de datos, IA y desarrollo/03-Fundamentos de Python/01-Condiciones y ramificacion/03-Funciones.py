""" 
Explorando las funciones de Python
Objetivos:
Al final de esta lectura, debería poder:

    Describir el concepto de función y la importancia de las funciones en la programación.
    Escribe una función que tome entradas y realice tareas.
    Utilice funciones integradas como len(), sum() y otras de forma eficaz
    Defina y use sus funciones en Python
    Diferenciar entre alcances de variables globales y locales
    Usar bucles dentro de la función.
    Modificar estructuras de datos usando funciones.

Introducción a las funciones
Una función es un bloque de construcción fundamental que encapsula acciones o cálculos específicos. Como en matemáticas, donde las funciones toman entradas y producen salidas,
    las funciones de programación funcionan de manera similar. Toman entradas, ejecutan acciones o cálculos predefinidos y luego devuelven una salida.

Objeto de las funciones
Las funciones promueven la modularidad y la reutilización del código. Imagine que tiene una tarea que debe realizarse varias veces dentro de un programa. En lugar de duplicar el
    mismo código en varios lugares, puede definir una función una vez y llamarla cuando necesite esa tarea. Esto reduce la redundancia y hace que el código sea más fácil de
    administrar y mantener.

Beneficios de usar funciones
Modularidad: las funciones dividen las tareas complejas en componentes manejables
Reutilizabilidad: las funciones se pueden usar varias veces sin tener que reescribir el código
Legibilidad: las funciones con nombres significativos mejoran la comprensión del código
Depuración: el aislamiento de funciones facilita la resolución de problemas y la solución de problemas
Abstracción: las funciones simplifican los procesos complejos detrás de un diseño fácil de usar interfaz
Colaboración: los miembros del equipo pueden trabajar en diferentes funciones simultáneamente
Mantenimiento: los cambios realizados en una función se aplican automáticamente dondequiera que se utilice

Cómo las funciones toman entradas, realizan tareas y producen resultados
Entradas (parámetros)
Las funciones operan con datos y pueden recibir datos como entrada. Estas entradas se conocen como parámetros o argumentos . Los parámetros proporcionan a las funciones la
    información necesaria para realizar sus tareas. Considere los parámetros como valores que pasa a una función, permitiéndole trabajar con datos específicos.

Realizando tareas
Una vez que una función recibe su entrada (parámetros), ejecuta acciones o cálculos predefinidos. Estas acciones pueden incluir cálculos, operaciones con datos o incluso tareas
    más complejas. El propósito de una función determina las tareas que realiza. Por ejemplo, una función podría calcular la suma de números, ordenar una lista, formatear texto
    o recuperar datos de una base de datos.

Produciendo resultados
Después de realizar sus tareas, una función puede producir una salida. Esta salida es el resultado de las operaciones realizadas dentro de la función. Es el valor que la
    función “devuelve” al código que la llamó. Piense en el resultado como el producto final del trabajo de la función. Puede utilizar este resultado en su código, asignarlo a
    variables, pasarlo a otras funciones o incluso imprimirlo para mostrarlo.

Ejemplo:

Considere una función denominada calculate_totalque toma dos números como entrada (parámetros), los suma y luego produce la suma como salida. Así es como funciona:

"""
def calculate_total(a, b):  # Parameters: a and b
    total = a + b           # Task: Addition
    return total            # Output: Sum of a and b
result = calculate_total(5, 7)  # Calling the function with inputs 5 and 7
print(result)  # Output: 12
"""
Funciones integradas de Python
Python tiene un rico conjunto de funciones integradas que brindan una amplia gama de funcionalidades. Estas funciones están disponibles para su uso y no necesita preocuparse
    por cómo se implementan internamente. En su lugar, puede concentrarse en comprender qué hace cada función y cómo usarla de manera efectiva.

Uso de funciones integradas o funciones predefinidas
Para utilizar una función incorporada, simplemente llame al nombre de la función seguido de paréntesis. Todos los argumentos o parámetros necesarios se pasan a la función dentro
    de estos paréntesis. Luego, la función realiza su tarea predefinida y puede devolver un resultado que puede usar en su código.

A continuación se muestran algunos ejemplos de funciones integradas de uso común:

len(): Calcula la longitud de una secuencia o colección

"""
string_length = len("Hello, World!")  # Output: 13
list_length = len([1, 2, 3, 4, 5])   # Output: 5
"""
sum(): suma los elementos en un iterable (lista, tupla, etc.)
"""
total = sum([10, 20, 30, 40, 50])  # Output: 150
"""
max(): Devuelve el valor máximo en un iterable
"""
highest = max([5, 12, 8, 23, 16])  # Output: 23
"""
min(): Devuelve el valor mínimo en un iterable
"""
lowest = min([5, 12, 8, 23, 16])  # Output: 5
"""
Las funciones integradas de Python ofrecen una amplia gama de funcionalidades, desde operaciones básicas como len() y sum() hasta tareas más especializadas.

Definiendo tus funciones
Definir una función es como crear tu miniprograma:

Uso defseguido del nombre de la función y paréntesis.
Aquí está la sintaxis para definir una función:
"""
def function_name():
    pass
"""
Una "pass"declaración en una función de programación es un marcador de posición o una declaración no operativa (sin operación). Úselo cuando desee definir una función o un}
    bloque de código sintácticamente pero no desee especificar ninguna funcionalidad o implementación en ese momento.

Marcador de posición: "pass" actúa como un marcador de posición temporal para el código futuro que desea escribir dentro de una función o bloque de código.

Requisito de sintaxis: en muchos lenguajes de programación como Python, el uso "pass"es necesario cuando se define una función o un bloque condicional. Garantiza que el código
    siga siendo sintácticamente correcto, incluso si aún no hace nada.

Sin operación: "pass" por sí solo no realiza ninguna acción significativa. Cuando el intérprete encuentra "aprobar", simplemente pasa a la siguiente declaración sin ejecutar
    ningún código.

Parámetros de función:
Los parámetros son como entradas para funciones.
Van entre paréntesis al definir la función.
Las funciones pueden tener múltiples parámetros.
Ejemplo:
"""
def greet(name):
    print("Hello, " + name)
result = greet("Alice")
print(result)  # Output: Hello, Alice
"""
Docstrings (cadenas de documentación)
Docstrings explica lo que hace una función
Colocado entre comillas triples debajo de la definición de función.
Ayuda a otros desarrolladores a comprender su función
Ejemplo:
"""
def multiply(a, b):
    """
    This function multiplies two numbers.
    Input: a (number), b (number)
    Output: Product of a and b
    """
    print(a * b)
multiply(2,6)
"""
Declaración de devolución
El retorno devuelve un valor de una función.
Finaliza la ejecución de la función y envía el resultado.
Una función puede devolver varios tipos de datos.
Ejemplo:
"""
def add(a, b):
    return a + b
sum_result = add(3, 5)  # sum_result gets the value 8
"""
Comprender los alcances y las variables
El alcance es donde se puede ver y utilizar una variable:

Alcance Global: Variables definidas fuera de funciones; accesible en todas partes
Alcance local: variables dentro de funciones; sólo utilizable dentro de esa función
Ejemplo:

Parte 1: declaración de variable global
"""
global_variable = "I'm global"
"""
Esta línea inicializa una variable global llamada global_variabley le asigna el valor "Soy global".

Las variables globales son accesibles a lo largo de todo el programa, tanto dentro como fuera de las funciones.

Parte 2: Definición de función
"""
def example_function():
    local_variable = "I'm local"
    print(global_variable)  # Accessing global variable
    print(local_variable)   # Accessing local variable
"""
Aquí, usted define una función llamada example_function().

Dentro de esta función:

Una variable local denominada local_variable se declara e inicializa con el valor de cadena "Soy local". Esta variable es local de la función y solo se puede acceder a ella
    dentro del alcance de la función.

Luego, la función imprime los valores tanto de la variable global (global_variable) como de la variable local (local_variable) . Demuestra que puede acceder a variables
    globales y locales dentro de una función.

Parte 3: llamada a función
"""
example_function()
"""
En esta parte, llamas al example_function()invocándolo. Esto da como resultado que se ejecute el código de la función.
Como resultado de esta llamada a función, imprimirá los valores de las variables globales y locales dentro de la función.

Parte 4: acceder a la variable global fuera de la función
"""
print(global_variable)  # Accessible outside the function
"""
Después de llamar a la función, imprime el valor de la variable global global_variablefuera de la función. Esto demuestra que las variables globales son accesibles dentro y
    fuera de las funciones.

Parte 5: intentar acceder a la variable local fuera de la función
"""
# print(local_variable)  # Error, local variable not visible here
"""
En esta parte, intenta imprimir el valor de la variable local local_variablefuera de la función. Sin embargo, esta línea daría como resultado un error.

Las variables locales solo son visibles y accesibles dentro del alcance de la función donde están definidas.

Intentar acceder a ellos fuera de ese ámbito generaría un archivo "NameError".

Usar funciones con bucles
Funciones y bucles juntos.
Las funciones pueden contener código con bucles.
Esto hace que las tareas complejas estén más organizadas.
El código de bucle se convierte en una función repetible.
Ejemplo:
"""
def print_numbers(limit):
    for i in range(1, limit+1):
        print(i)
print_numbers(5)  # Output: 1 2 3 4 5
"""
Mejora de la organización y reutilización del código
Las funciones agrupan acciones similares para una fácil comprensión.
El bucle dentro de las funciones mantiene el código limpio
Puedes reutilizar una función para repetir acciones.
Ejemplo
"""
def greet(name):
    return "Hello, " + name
for _ in range(3):
    print(greet("Alice"))
"""
Modificar la estructura de datos usando funciones
Utilizará Python y una lista como estructura de datos para esta ilustración. En este ejemplo, creará funciones para agregar y eliminar elementos de una lista.

Parte 1: inicializar una lista vacía
"""
# Define an empty list as the initial data structure
my_list = []
"""
En esta parte, comenzará creando una lista vacía llamada my_list. Esta lista vacía sirve como estructura de datos que modificará a lo largo del código.

Parte 2: Definir una función para agregar elementos
"""
# Function to add an element to the list
def add_element(data_structure, element):
    data_structure.append(element)
"""
Aquí, usted define una función llamada add_element. Esta función toma dos parámetros:

data_structure: Este parámetro representa la lista a la que desea agregar un elemento
element: Este parámetro representa el elemento que desea agregar a la lista
Dentro de la función, utiliza el appendmétodo para agregar el elemento proporcionado a la estructura de datos, que se supone que es una lista.

Parte 3: definir una función para eliminar elementos
"""
# Function to remove an element from the list
def remove_element(data_structure, element):
    if element in data_structure:
        data_structure.remove(element)
    else:
        print(f"{element} not found in the list.")
"""
En esta parte, define otra función llamada remove_element. También toma dos parámetros:

data_structure: La lista de la que queremos eliminar un elemento.
element: El elemento que queremos eliminar de la lista.
Dentro de la función, utiliza declaraciones condicionales para verificar si el elemento está presente en la estructura de datos. Si es así, utilice el removemétodo para
    eliminar la primera aparición del elemento. Si no se encuentra, imprime un mensaje indicando que el elemento no se encontró en la lista.

Parte 4: Agregar elementos a la lista
"""
# Add elements to the list using the add_element function
add_element(my_list, 42)
add_element(my_list, 17)
add_element(my_list, 99)
"""
Aquí, utiliza la add_elementfunción para agregar tres elementos (42, 17 y 99) al archivo my_list. Estos se agregan uno a la vez mediante llamadas a funciones.

Parte 5: Imprimir la lista actual
"""
# Print the current list
print("Current list:", my_list)
"""
Esta parte simplemente imprime el estado actual de my_listla consola, permitiéndonos ver los elementos que se han agregado hasta el momento.

Parte 6: Eliminar elementos de la lista
"""
# Remove an element from the list using the remove_element function
remove_element(my_list, 17)
remove_element(my_list, 55)  # This will print a message since 55 is not in the list
"""
En esta parte, utiliza la remove_elementfunción para eliminar elementos de my_list. Primero, intenta eliminar 17 (que está en la lista) y luego intenta eliminar 55 (que no está
    en la lista). La segunda llamada remove_elementimprimirá un mensaje indicando que no se encontró 55.

Parte 7: Imprima la lista actualizada
"""
# Print the updated list
print("Updated list:", my_list)
"""
Finalmente, imprimes lo actualizado my_listen la consola. Esto nos permite observar las modificaciones realizadas en la lista agregando y eliminando elementos usando las
    funciones definidas."""