# Crear una matriz Numpy 2D

# Import the libraries
import numpy as np

# Considere la lista a, que contiene tres listas anidadas, cada una de ellas del mismo tamaño .

# Create a list
a = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]


# Podemos convertir la lista a un Numpy Array de la siguiente manera:

# Convert list to Numpy Array
# Every element is the same type
A = np.array(a)

# Podemos utilizar el atributo ndim para obtener el número de ejes o dimensiones, lo que se denomina rango.

# Show the numpy array dimensions
A.ndim

# El atributo shape devuelve una tupla correspondiente al tamaño o número de cada dimensión.

# Show the numpy array shape
A.shape

# El número total de elementos de la matriz viene dado por el atributo size.

A.size

# -------------------------------------------
# Accediendo a diferentes elementos de un Numpy Array 
# Podemos utilizar corchetes rectangulares para acceder a los diferentes elementos del array. La correspondencia entre los corchetes rectangulares y la lista y la representación
#   rectangular se muestra en la siguiente figura para una matriz de 3x3:

# Podemos acceder a la segunda fila, tercera columna como se muestra en la siguiente figura:

A:[[A[0,0], A[0,1], A[0,2]], [A[1,0], A[1,1], A[1,2]], [A[2,0], A[2,1], A[2,2]]]
# lo mismo pero para visualisarlo mejor
A:[ [A[0,0], A[0,1], A[0,2]],
    [A[1,0], A[1,1], A[1,2]],
    [A[2,0], A[2,1], A[2,2]]
]
# Simplemente utilizamos los corchetes y los índices correspondientes al elemento que queramos:

# Access the element on the second row and third column
A[1, 2]

# También podemos utilizar la siguiente notación para obtener los elementos:

# Access the element on the second row and third column
A[1][2]

# También podemos usar el corte en numerosas matrices. Considere la siguiente figura. Nos gustaría obtener las dos primeras columnas de la primera fila.
# Esto se puede hacer con la siguiente sintaxis:

# Access the element on the first row and first and second columns
A[0][0:2]

# De manera similar, podemos obtener las dos primeras filas de la 3ª columna de la siguiente manera:

# Access the element on the first and second rows and third column
A[0:2, 2]

# ----------------------------------------------------------------------
# Operaciones básicas 
# También podemos agregar matrices. El proceso es idéntico a la suma de matrices. La suma matricial de X y Y se muestra en la siguiente figura:
# La matriz numpy está dada por X y Y

X = np.array([  [1, 0],
                [0, 1]])

Y = np.array([  [2, 1],
                [1, 2]]) 

# Podemos agregar las matrices numerosas de la siguiente manera.

# Add X and Y
Z = X + Y

# Multiplicar una matriz numpy por un escalador es idéntico a multiplicar una matriz por un escalador. Si multiplicamos la matriz Y por el escalador 2, simplemente multiplicamos
#   cada elemento de la matriz por 2, como se muestra en la figura.

# Podemos realizar la misma operación en numpy de la siguiente manera

Y = np.array([  [2, 1],
                [1, 2]])

Z = 2 * Y

# La multiplicación de dos matrices corresponde a un producto de elementos o producto de Hadamard . Considere la matriz X y Y. El producto de Hadamard corresponde a multiplicar
#   cada uno de los elementos que se encuentran en la misma posición, es decir, multiplicar entre sí elementos contenidos en cajas del mismo color. El resultado es una nueva
#   matriz del mismo tamaño que la matriz Yo X, como se muestra en la siguiente figura.

# Podemos realizar el producto por elementos de la matriz X de Y la siguiente manera:

Y = np.array([  [2, 1],
                [1, 2]])
X = np.array([  [1, 0],
                [0, 1]])

# También podemos realizar la multiplicación de matrices con matrices numerosas A y B de la siguiente manera:
# Primero, definimos matriz Ay B:

A = np.array([  [0, 1, 1],
                [1, 0, 1]])

B = np.array([  [1, 1],
                [1, 1],
                [-1, 1]])

# Usamos la función numpy dot para multiplicar las matrices.

Z = np.dot(A,B)
np.sin(Z)

# Usamos el atributo numpy T para calcular la matriz transpuesta.

C = np.array([  [1,1],
                [2,2],
                [3,3]])

C.T