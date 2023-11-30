"""
Manejo de excepciones en Python
Objetivos
    Comprender las excepciones
    Distinguir errores de excepciones
    Familiaridad con las excepciones comunes de Python
    Gestionar excepciones de forma eficaz
En el mundo de la programación los errores y las situaciones inesperadas son seguras. Python, un lenguaje de programación popular y versátil, equipa a los desarrolladores con
    un potente conjunto de herramientas para gestionar estos escenarios imprevistos mediante excepciones y manejo de errores.
¿Cuáles son las excepciones?
Las excepciones son las alertas cuando sucede algo inesperado mientras se ejecuta un programa. Podría ser un error en el código o una situación que no estaba prevista. Python
    puede generar estas alertas automáticamente, pero también podemos activarlas intencionalmente usando el comando elevar. Lo bueno es que podemos evitar que nuestro programa
    falle manejando excepciones.

Errores versus excepciones
Espera, ¿cuál es la diferencia entre errores y excepciones? Bueno, errorsnormalmente son grandes problemas que provienen del ordenador o del sistema. A menudo hacen que el
    programa deje de funcionar por completo. Por otro lado, exceptionsson más bien cuestiones que podemos controlar. Ocurren debido a algo que hicimos en nuestro código y
    generalmente se pueden solucionar, por lo que el programa continúa.

Aquí está la diferencia entre Errors and exceptions: -

Aspecto	Errores	Excepciones
Origen	Los errores suelen ser causados ​​por el	Las excepciones suelen ser el resultado de
entorno, hardware o sistema operativo.	Ejecución problemática de código dentro del programa.
Naturaleza	Los errores suelen ser graves y pueden llevar a	Las excepciones son generalmente menos graves y pueden
El programa falla o termina anormalmente.	ser capturado y manipulado para evitar que el programa
terminación.
Manejo	Los errores no suelen detectarse ni gestionarse	Las excepciones se pueden detectar usando try-except
por el propio programa.	bloques y tratados con gracia, permitiendo
el programa para continuar con la ejecución.
Ejemplos	Los ejemplos incluyen "SyntaxError" debido a	Los ejemplos incluyen "ZeroDivisionError" cuando
sintaxis incorrecta o “NameError” cuando un	dividiendo por cero, o "FileNotFoundError" cuando
La variable no está definida.	intentando abrir un archivo inexistente.
Categorización	Los errores no se clasifican en categorías.	Las excepciones se clasifican en varios
clases, como “ArithmeticError”, “IOError”
“ValueError”, etc., según su naturaleza.
Excepciones comunes en Python
A continuación se muestran algunos ejemplos de excepciones con las que nos encontramos a menudo y que podemos manejar con esta herramienta:

ZeroDivisionError: este error surge cuando se intenta dividir un número por cero. La división por cero no está definida en matemáticas, lo que provoca un error aritmético. Por
    ejemplo:
Por ejemplo:
"""
result = 10 / 0 
print(result)
# Raises ZeroDivisionError
"""
ValueError: este error ocurre cuando se utiliza un valor inadecuado dentro del código. Un ejemplo de esto es cuando se intenta convertir una cadena no numérica en un número
    entero:
por ejemplo:
"""
num = int("abc")
# Raises ValueError
"""
FileNotFoundError: esta excepción se produce cuando se intenta acceder a un archivo que no existe.
Por ejemplo:
"""
with open("nonexistent_file.txt", "r") as file:
        content = file.read()   # Raises FileNotFoundError
"""
IndexError: se produce un IndexError cuando se utiliza un índice para acceder a un elemento en una lista que está fuera del rango de índice válido.
Por ejemplo:
"""
my_list = [1, 2, 3]
value = my_list[1]  # No IndexError, within range
missing = my_list[5]  # Raises IndexError
"""
KeyError: El KeyError surge cuando se intenta acceder a una clave inexistente en un diccionario.
Por ejemplo:
"""
my_dict = {"name": "Alice", "age": 30}
value = my_dict.get("city")  # No KeyError, using .get() method
missing = my_dict["city"]  # Raises KeyError
"""
TypeError: El TypeError ocurre cuando un objeto se usa de manera incompatible. Un ejemplo incluye intentar concatenar una cadena y un número entero:
Por ejemplo:
"""
result = "hello" + 5   
# Raises TypeError
"""
AttributeError: un AttributeError ocurre cuando se accede a un atributo o método en un objeto que no posee ese atributo o método específico. Por ejemplo:
Por ejemplo:
"""
text = "example"
length = len(text)  # No AttributeError, correct method usage
missing = text.some_method()  # Raises AttributeError
"""
ImportError: este error se produce cuando se intenta importar un módulo que no está disponible. Por ejemplo:import non_existent_module
Nota: Recuerde que las excepciones que encontrará no se limitan solo a estas. Hay muchos más en Python. Sin embargo, no hay necesidad de preocuparse. Al utilizar la técnica que
    se proporciona a continuación y seguir la sintaxis correcta, podrá manejar cualquier excepción que se le presente.

Manejo de excepciones:
Python tiene una herramienta útil llamada try and exceptque nos ayuda a gestionar excepciones.

Pruebe y excepto : puede utilizar los bloques try y except para evitar que su programa falle debido a excepciones.

Así es como funcionan:

El código que puede resultar en una excepción está contenido en el bloque try.
Si ocurre una excepción, el código salta directamente al bloque excepto.
En el bloque de excepción, puede definir cómo manejar la excepción de manera elegante, como mostrar un mensaje de error o tomar acciones alternativas.
Después del bloque excepto, el programa continúa ejecutando el código restante.
Ejemplo: intentar dividir por cero
"""
# using Try- except 
try:
    # Attempting to divide 10 by 0
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")
"""
Próximo paso
Cuando terminemos esta lectura, estará listo para pasar a la siguiente parte donde practicará el manejo de errores. Para un mejor aprendizaje, pruebe diferentes tipos de datos
    en el laboratorio. De esta manera, encontrará varios errores y aprenderá a solucionarlos de forma eficaz. Este conocimiento le ayudará a escribir código más sólido y fiable
    en el futuro."""