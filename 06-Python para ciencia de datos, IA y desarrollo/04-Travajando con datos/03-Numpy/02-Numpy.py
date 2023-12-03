"""
NumPy es una biblioteca de Python que se utiliza para trabajar con matrices, álgebra lineal, transformada de Fourier y matrices. NumPy significa Numerical Python y es un
    proyecto de código abierto. El objeto de matriz en NumPy se llama ndarray y proporciona muchas funciones de soporte que hacen que trabajar con ndarray sea muy fácil.

Los arrays se utilizan con mucha frecuencia en la ciencia de datos, donde la velocidad y los recursos son muy importantes.

NumPy generalmente se importa con el alias np.

Suele tener un tamaño fijo y cada elemento es del mismo tipo. Podemos convertir una lista en una matriz numpy importando primero numpy:
"""

import numpy as np 

"""
Luego elaboramos la lista de la siguiente manera:
"""

a = np.array([0, 1, 2, 3, 4])

"""
Cada elemento es del mismo tipo, en este caso enteros:
Al igual que con las listas, podemos acceder a cada elemento mediante un corchete:
"""

# Print each element
print("a[0]:", a[0])
print("a[1]:", a[1])
print("a[2]:", a[2])
print("a[3]:", a[3])
print("a[4]:", a[4])

"""
Comprobando la versión de NumPy 
La cadena de versión se almacena en el atributo de versión .
"""

# Check the type of the array
type(a)

"""
Como las matrices numerosas contienen datos del mismo tipo, podemos usar el atributo "dtype" para obtener el tipo de datos de los elementos de la matriz. En este caso, es un
    entero de 64 bits:
"""

# Check the type of the values stored in numpy array
a.dtype

"""
Inténtalo tú mismo 
Verifique el tipo de matriz y el tipo de valor para la matriz dada c
"""

b = np.array([3.1, 11.02, 6.2, 213.2, 5.2])
# Enter your code here

"""
Asignar valor 
Podemos cambiar el valor de la matriz. Considere la matriz c:
"""

c = np.array([20, 1, 2, 3, 4])

"""
Podemos cambiar el primer elemento de la matriz a 100 de la siguiente manera:
"""

# Assign the first element to 100
c[0] = 100

"""
Podemos cambiar el quinto elemento de la matriz a 0 de la siguiente manera:
"""

# Assign the 5th element to 0
c[4] = 0

"""
Al igual que las listas, podemos dividir la matriz numpy. Cortar en Python significa llevar los elementos del índice dado a otro índice dado.

Pasamos un segmento como este: [inicio: fin]. El elemento al final del índice no se incluye en la salida.

Podemos seleccionar los elementos del 1 al 3 y asignarlos a una nueva matriz numpy dde la siguiente manera:
"""

# Slicing the numpy array
d = c[1:4]

"""
Podemos asignar los índices correspondientes a nuevos valores de la siguiente manera:
"""

# Set the fourth element and fifth element to 300 and 400

c[3:5] = 300, 400

"""
También podemos definir los pasos del corte, así: [inicio:fin:paso].
"""

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2])

"""
Si no pasamos el inicio se considera 0.
"""

print(arr[:4])

"""
Si no pasamos el final, se considera hasta la longitud de la matriz.
"""

print(arr[4:])

"""
Si no pasamos el paso se considera 1
"""

print(arr[1:5:])

"""
Asignar valor con lista 
De manera similar, podemos usar una lista para seleccionar más de un índice específico. La lista selectcontiene varios valores:
"""

# Create the index list
select = [0, 2, 3, 4]

"""
Podemos usar la lista como argumento entre paréntesis. La salida son los elementos correspondientes a los índices particulares:
"""

# Use List to select elements
d = c[select]

"""
Podemos asignar los elementos especificados a un nuevo valor. Por ejemplo, podemos asignar los valores a 100 000 de la siguiente manera:
"""

# Assign the specified elements to new value
c[select] = 100000

"""
Otros atributos 
Repasemos algunos atributos básicos de una matriz usando la matriz a:
"""

# Create a numpy array
a = np.array([0, 1, 2, 3, 4])

"""
El atributo sizees el número de elementos de la matriz:
"""
a.size

"""
Numerosas funciones estadísticas 
"""

# Create a numpy array
a = np.array([1, -1, 1, -1])

# Get the mean of numpy array
mean = a.mean()

# Get the standard deviation of numpy array
standard_deviation=a.std()

# Create a numpy array
b = np.array([-1, 2, 3, 4, 5])

# Get the biggest value in the numpy array
max_b = b.max()

# Get the smallest value in the numpy array
min_b = b.min()

"""
Operaciones de matriz Numpy 
Podrías usar operadores aritméticos directamente entre matrices NumPy
Adición de matriz 
Considere la matriz numerosa u:
"""

u = np.array([1, 0])

"""
Considere la matriz numerosa v:
"""

v = np.array([0, 1])

"""
Podemos sumar las dos matrices y asignarlas a z:
"""

# Numpy Array Addition
z = np.add(u, v)

"""
La operación es equivalente a la suma de vectores:
"""
# Plotting functions


import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
# %matplotlib inline  

def Plotvec1(u, z, v):
    
    ax = plt.axes() # to generate the full window axes
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)# Add an arrow to the  U Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(u + 0.1), 'u')#Adds the text u to the Axes 
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)# Add an arrow to the  v Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(v + 0.1), 'v')#Adds the text v to the Axes 
    
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')#Adds the text z to the Axes 
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)

# Plot numpy arrays
Plotvec1(u, z, v)

"""
Resta de matriz
Considere la matriz numpy a:
"""

a = np.array([10, 20, 30])

"""
Considere la matriz numerosa b:
"""

b = np.array([5, 10, 15])

"""
Podemos restar las dos matrices y asignarlas a c:
"""

c = np.subtract(a, b)
print(c)

"""
Multiplicación de matrices 
Considere la matriz vectorial numpy y:
"""

# Create a numpy array
x = np.array([1, 2])

# Create a numpy array
y = np.array([2, 1])

"""
Podemos multiplicar cada elemento del array por 2:
"""

# Numpy Array Multiplication
z = np.multiply(x, y)

"""
Esto equivale a multiplicar un vector por un escalador:

División de matriz
Considere la matriz vectorial numpy a:
"""

a = np.array([10, 20, 30])

"""
Considere la matriz vectorial numpy b:
"""

b = np.array([2, 10, 5])

# Podemos dividir las dos matrices y asignarlas a c:

c = np.divide(a, b)

# Producto escalar
# El producto escalar de las dos matrices numpy uestá vdado por:

X = np.array([1, 2])
Y = np.array([3, 2])

# Calculate the dot product
np.dot(X, Y)

#Elements of X
print(X[0])
print(X[1])

#Elements of Y
print(Y[0])
print(Y[1])


# Estamos realizando el producto escalar que se muestra a continuación.

# Agregar constante a una matriz Numpy
# Considere la siguiente matriz:

# Create a constant to numpy array
u = np.array([1, 2, 3, -1]) 

# Agregando la constante 1 a cada elemento de la matriz:

u + 1

# -------------------------------------------------------------------------
# Funciones matemáticas
# Podemos acceder al valor de pi en numpy de la siguiente manera:

np.pi

# Podemos crear la siguiente matriz numpy en radianes:

# Create the numpy array in radians
x = np.array([0, np.pi/2 , np.pi])


# Podemos aplicar la función sin a la matriz x y asignar los valores a la matriz y; esto aplica la función seno a cada elemento de la matriz:

# Calculate the sin of each elements
y = np.sin(x)

# ---------------------------------------------------------------------------------
# Espacio lineal 
# Una función útil para trazar funciones matemáticas es linspace. Linspace devuelve números espaciados uniformemente en un intervalo específico.
# numpy.linspace (inicio, parada, num = valor int)

# inicio: inicio del rango de intervalo
# parada: fin del rango de intervalo
# num: número de muestras a generar.

# Makeup a numpy array within [-2, 2] and 5 elements
np.linspace(-2, 2, num=5)

# Si cambiamos el parámetro num a 9, obtenemos 9 números espaciados uniformemente en el intervalo de -2 a 2:

# Make a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)

# Podemos usar la función linspace para generar 100 muestras espaciadas uniformemente desde el intervalo 0 a 2π:

# Make a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)

# Podemos aplicar la función seno a cada elemento de la matriz x y asignarla a la matriz y:

# Calculate the sine of x list
y = np.sin(x)

# Plot the result
plt.plot(x, y)

# ----------------------------------------------------------------------------------------------
# Iterando matrices 1-D 
# Iterar significa recorrer elementos uno por uno.
# Si iteramos en una matriz 1-D, pasará por cada elemento uno por uno.
# Si ejecutamos la matriz numpy, obtenemos el formato de matriz

arr1 = np.array([1, 2, 3])
print(arr1)

# Pero si desea obtener el resultado en forma de lista, puede usar el bucle for:

for x in arr1:
    print(x)

# Import the libraries

import time 
import sys
import numpy as np 

import matplotlib.pyplot as plt
# %matplotlib inline

def Plotvec2(a,b):
    ax = plt.axes()# to generate the full window axes
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)#Add an arrow to the  a Axes with arrow head width 0.05, color red and arrow head length 0.1
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)#Add an arrow to the  b Axes with arrow head width 0.05, color blue and arrow head length 0.1
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)#set the ylim to bottom(-2), top(2)
    plt.xlim(-2, 2)#set the xlim to left(-2), right(2)