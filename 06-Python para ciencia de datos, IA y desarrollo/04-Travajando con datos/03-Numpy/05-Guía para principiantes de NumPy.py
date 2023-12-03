# Guía para principiantes de NumPy
# Objetivo:
#   Introduzca a los principiantes a NumPy.
#   Explique cómo crear matrices NumPy.
#   Familiarizar a los usuarios con los atributos de la matriz y la indexación.
#   Operaciones básicas como suma y multiplicación.

# ¿Qué es Numpy?
# NumPy, abreviatura de Numerical Python, es una biblioteca fundamental para la computación numérica y científica en Python. Proporciona soporte para matrices y arreglos
#   multidimensionales grandes, junto con una colección de funciones matemáticas de alto nivel para operar en estos arreglos. NumPy sirve como base para muchas bibliotecas de
#   ciencia de datos y aprendizaje automático, lo que lo convierte en una herramienta esencial para el análisis de datos y la investigación científica en Python.

# Aspectos clave de NumPy en Python:
# Estructuras de datos eficientes : NumPy introduce estructuras de matrices eficientes, que son más rápidas y eficientes en memoria que las listas de Python. Esto es crucial
#   para manejar grandes conjuntos de datos.

# Arreglos multidimensionales : NumPy le permite trabajar con arreglos multidimensionales, permitiendo la representación de matrices y tensores. Esto es particularmente útil en
#   informática científica.

# Operaciones por elementos : NumPy simplifica las operaciones matemáticas por elementos en matrices, lo que facilita la realización de cálculos en conjuntos de datos completos
#   de una sola vez.

# Generación de números aleatorios : proporciona una amplia gama de funciones para generar números aleatorios y datos aleatorios, lo cual es útil para simulaciones y análisis
#   estadísticos.

# Integración con otras bibliotecas : NumPy se integra perfectamente con otras bibliotecas de ciencia de datos como SciPy, Pandas y Matplotlib, mejorando su utilidad en varios
#   dominios.

# Optimización del rendimiento : las funciones de NumPy se implementan en lenguajes de bajo nivel como C y Fortran, lo que aumenta significativamente su rendimiento. Es una
#   opción ideal cuando la velocidad es esencial.

# Instalación
# Si aún no has instalado NumPy, puedes hacerlo usando pip:

# pip install numpy

# ------------------------------------------------------------------------------
# Creando matrices NumPy
# Puede crear matrices NumPy a partir de listas de Python. Estas matrices pueden ser unidimensionales o multidimensionales.

# ------------------------------------------------------------------------------
# Creando una matriz 1D

import numpy as np

# importar numpy como np : en esta línea importamos la biblioteca NumPy y le asignamos un alias "np" para que sea más fácil hacer referencia a ella en el código.

# # Creating a 1D array
arr_1d = np.array([1, 2, 3, 4, 5]) 

# en esta línea, estamos creando una matriz NumPy unidimensional llamada arr_1d. Utiliza la función np.array() para convertir una lista de Python [1, 2, 3, 4, 5] en una matriz
#   NumPy. Esta matriz contiene cinco elementos, que son 1, 2, 3, 4 y 5. arr_1d es una matriz 1D porque tiene una sola fila de elementos.

# Creando una matriz 2D

# # Creating a 2D array
arr_2d = np.array([ [1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# En esta línea, estamos creando una matriz NumPy bidimensional llamada arr_2d. Utiliza la función np.array() para convertir una lista de listas en una matriz NumPy 2D.
# La lista externa contiene tres listas internas, cada una de las cuales representa una fila de elementos. Entonces, arr_2d es una matriz 2D con tres filas y tres columnas.
# Los elementos de esta matriz forman una matriz con valores del 1 al 9, organizados en una cuadrícula de 3x3.

# ------------------------------------------------------------------------------
# Atributos de matriz
# Las matrices NumPy tienen varios atributos útiles:

# # Array attributes
print(arr_2d.ndim)  # ndim : Represents the number of dimensions or "rank" of the array.
# # output : 2
print(arr_2d.shape)  # shape : Returns a tuple indicating the number of rows and columns in the array.
# # Output : (3, 3)
print(arr_2d.size) # size: Provides the total number of elements in the array.  
# # Output : 9

# ------------------------------------------------------------------------------
# Indexación y corte
# Puede acceder a elementos de una matriz NumPy mediante indexación y división:

# En esta línea, accedemos al tercer elemento (índice 2) de la matriz 1D 'arr_1d'.

print(arr_1d[2])          # Accessing an element (3rd element)
# En esta línea, accedemos al elemento de la segunda fila (índice 1) y la tercera columna (índice 2) de la matriz 2D 'arr_2d'.

print(arr_2d[1, 2])       # Accessing an element (2nd row, 3rd column)
# En esta línea accedemos a la 2ª fila (índice 1) del array 2D 'arr_2d'.

print(arr_2d[1])          # Accessing a row (2nd row)
# En esta línea accedemos a la 2ª columna (índice 1) del array 2D 'arr_2d'.

print(arr_2d[:, 1])       # Accessing a column (2nd column)

# ------------------------------------------------------------------------------
# Operaciones básicas
# NumPy simplifica las operaciones básicas en matrices:

# Operaciones aritméticas por elementos:
# Suma, resta, multiplicación y división de matrices con escalares u otras matrices.

# Adición de matriz
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # [5 7 9

# Multiplicación escalar
array = np.array([1, 2, 3])
result = array * 2 # each element of an array is multiplied by 2
print(result)  # [2 4 6]

# Multiplicación por elementos (producto de Hadamard)
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 * array2
print(result)  # [4 10 18]

# Multiplicación de matrices
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
result = np.dot(matrix1, matrix2)
print(result)
# [[19 22]
#  [43 50]]

# NumPy simplifica estas operaciones, haciéndolas más fáciles y eficientes que las listas tradicionales de Python.

# ------------------------------------------------------------------------------
# Operación con Numpy
# Aquí está la lista de operaciones que se pueden realizar con Numpy


# Operación	                    Descripción	                                Ejemplo

# Creación de matrices	        Creando una matriz NumPy.	                matriz = np.matriz([1, 2, 3, 4, 5])

# Aritmética por elementos	    Suma, resta, etc. por elementos.	        resultado = arr1 + arr2

# Aritmética escalar	        Suma, resta escalar, etc.	                resultado = llegada * 2

# Funciones por elementos	    Aplicando funciones a cada elemento.	    resultado = np.sqrt(arr)

# Suma y media	                Calcular la suma y la media de una matriz.  Calcular la suma y la media de una matriz.	total = np.suma(arr)
#                                                                           promedio = np.media(arr)

# Valores máximos y mínimos	    Encontrar los valores máximo y mínimo.	    valor_max = np.max(arr)
#                                                                           valor_min = np.min(arr)

# Reorganización	            Cambiar la forma de una matriz.	            remodelado_arr = arreglo.reformado(2, 3)

# Transposición	                Transponer una matriz multidimensional.	    transposed_arr = arreglo.T

# Multiplicación de matrices	Realizar multiplicación de matrices.	    resultado = np.punto(matriz1, matriz2)


# ------------------------------------------------------------------------------
# Conclusión
# NumPy es una biblioteca fundamental para la ciencia de datos y los cálculos numéricos.
# Esta guía cubre los conceptos básicos de NumPy y hay mucho más para explorar. Visita numpy.org para obtener más información y ejemplos.