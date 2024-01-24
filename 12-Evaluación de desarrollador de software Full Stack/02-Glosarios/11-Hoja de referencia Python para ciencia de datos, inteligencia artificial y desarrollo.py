# .read_csv()
# Lee datos de un archivo `.CSV` y crea un DataFrame.	
dataframe_name = pd.read_csv("filename.csv")

df = pd.read_csv("data.csv")


# .read_excel()
# Lee datos de un archivo de Excel y crea un DataFrame.	
dataframe_name = pd.read_excel("filename.xlsx")

df = pd.read_excel("data.xlsx")


# .to_csv()
# Escribe DataFrame en un archivo CSV.	
dataframe_name.to_csv("output.csv", index=False)

df.to_csv("output.csv", index=False)


# Acceso a columnas
# Accede a una columna específica usando [] en el DataFrame.	
dataframe_name["column_name"] # Accede a una sola columna 
dataframe_name[["column1", "column2"]] # Accede a varias columnas 

df["age"]
df[["name", "age"]]


# Accessing Values
# Puede acceder a los valores de un diccionario utilizando sus claves correspondientes.	

Value = dict_name["key_name"]

name = person["name"]
age = person["age"]


# Agregar o modificar	
# Inserta un nuevo par clave-valor en el diccionario. Si la clave ya existe, el valor se actualizará; de lo contrario, se crea una nueva entrada.	

dict_name[key] = value

person["Country"] = "USA" # Se creará una nueva entrada.   
person["city"] = "Chicago" # Actualizar el valor existente para la misma clave 


# add()
# Se pueden agregar elementos a un conjunto usando el método `add()`. Los duplicados se eliminan automáticamente, ya que los conjuntos solo almacenan valores únicos.

set_name.add(element)

fruits.add("mango")


# AND
# Devuelve "Verdadero" si tanto la declaración1 como la declaración2 son "Verdadero". De lo contrario, devuelve "Falso".	

statement1 and statement2

marks = 90
attendance_percentage = 87
if marks >= 80 and attendance_percentage >= 85:
    print("qualify for honors")
else:
    print("Not qualified for honors")


# Definición de clase	
# Define un modelo para crear objetos y definir sus atributos y comportamientos.	
class ClassName: # atributos y métodos de clase
    ...

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# clear()
# El método clear() vacía el diccionario, eliminando todos los pares clave-valor que contiene. Después de esta operación, el diccionario aún está accesible y se puede utilizar
    # más.

dict_name.clear()

grades.clear()


# clear()
# El método `clear()` elimina todos los elementos del conjunto, lo que da como resultado un conjunto vacío. Actualiza el conjunto in situ.
set_name.clear()

fruits.clear()


# Comentarios
# Los comentarios son líneas de texto que el intérprete de Python ignora al ejecutar el código.	

# This is a comment


# Concatenación
# Combina (concatena) cadenas.	
concatenated_string = string1 + string2

result = "Hello" + " John"


# copy()
# Crea una copia superficial del diccionario. El nuevo diccionario contiene los mismos pares clave-valor que el original, pero siguen siendo objetos distintos en la memoria.	
new_dict = dict_name.copy()

new_person = person.copy()
new_person = dict(person)  # otra forma de crear una copia del diccionario


# copy()
# El método `copy()` crea una copia superficial del conjunto. Cualquier modificación a la copia no afectará el conjunto original.
new_set = set_name.copy()

new_fruits = fruits.copy()


# Creando un diccionario
# Un diccionario es un tipo de datos integrado que representa una colección de pares clave-valor. Los diccionarios están entre llaves {}.	
dict_name = {} #Creates an empty dictionary
person = { "name": "John", "age": 30, "city": "New York"}


# Tipos de datos
# - Entero - Flotante - Booleano - Cadena
x=7
# Valor entero
y=14
# Valor flotante
is_valid = True
# Valor booleano
is_valid = False
# Valor booleano
F_Name = "John"
# Valor de cadena


# Definir función
# Una "función" es un bloque de código reutilizable que realiza una tarea específica o un conjunto de tareas cuando se llama.	
def function_name(parameters): 
    # Cuerpo de la función 
    ...
def greet(name):
    print("Hello,", name)


# Definición de conjuntos
# Un conjunto es una colección desordenada de elementos únicos. Los conjuntos están encerrados entre llaves `{}`. Son útiles para almacenar valores distintos y realizar
    # operaciones de conjuntos.	
empty_set = set() #Creando un vacío 
fruits = {"apple", "banana", "orange"}


# del
# Elimina el par clave-valor especificado del diccionario. Genera un KeyError si la clave no existe.	
del dict_name[key]

del person["Country"]


# describe()
# Genera un resumen estadístico de columnas numéricas en el DataFrame.	
dataframe_name.describe()
df.describe()


# discard()
# Utilice el método `discard()` para eliminar un elemento específico del conjunto. Se ignora si no se encuentra el elemento.
set_name.discard(element)

fruits.discard("apple")


# drop()
# Elimina filas o columnas especificadas del DataFrame. eje = 1 indica columnas. eje = 0 indica filas.	
dataframe_name.drop(["column1", "column2"], axis=1, inplace=True)
dataframe_name.drop(index=[row1, row2], axis=0, inplace=True)

df.drop(["age", "salary"], axis=1, inplace=True) # Will drop columns
df.drop(index=[5, 10], axis=0, inplace=True) # Will drop rows


# dropna()
# Elimina filas con valores NaN faltantes del DataFrame. eje = 0 indica filas.
dataframe_name.dropna(axis=0, inplace=True)
df.dropna(axis=0, inplace=True)


# duplicated()
# Valores o registros duplicados o repetitivos dentro de un conjunto de datos.
dataframe_name.duplicated()
duplicate_rows = df[df.duplicated()]


# Igual(==)
# Comprueba si dos valores son iguales.
variable1 == variable2

5 == 5 # devuelve True
age = 25 age == 30 # devuelve False


# Modos de apertura de archivos
# Diferentes modos para abrir archivos para operaciones específicas.	
# r ( leyendo ) w ( escritura ) a ( añadiendo ) + ( actualizando : lectura / escritura ) b ( binario , en caso contrario texto )

with open("data.txt", "r") as file: content = file.read()
print(content)
with open("output.txt", "w") as file: file.write("Hello, world!")
with open("log.txt", "a") as file: file.write("Log entry: Something happened.")
with open("data.txt", "r+") as file: content = file.read()
file.write("Updated content: " + content)


# Métodos de lectura de archivos
# Diferentes métodos para leer el contenido del archivo de varias maneras.
archivo . readlines () # lee todas las líneas como una lista 
readline () # lee la siguiente línea como una cadena 
archivo . read () # lee todo el contenido del archivo como una cadena 

with open("data.txt", "r") as file:
    lines = file.readlines()
    next_line = file.readline()
    content = file.read()


# Métodos de escritura de archivos
# Diferentes métodos de escritura para escribir contenido en un archivo.
file.write(content) # escribe una cadena en el archivo 
file.writelines(lines) # escribe una lista de cadenas en el archivo 

lines = ["Hello\n", "World\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)


# Filtrar filas
# Crea un nuevo DataFrame con filas que cumplen las condiciones especificadas.	
filtered_df = dataframe_name[(Conditional_statements)]

filtered_df = df[(df["age"] > 30) & (df["salary"] < 50000)]


# For Loop
# Un bucle `for` ejecuta repetidamente un bloque de código durante un número específico de iteraciones o sobre una secuencia de elementos (lista, rango, cadena, etc.).

for variable in sequence:
    # Código a repetir 
    ...
for num in range(1, 10):
    print(num)

fruits = ["apple", "banana", "orange", "grape", "kiwi"]
for fruit in fruits:
    print(fruit)


# Llamada de función
# Una llamada a función es el acto de ejecutar el código dentro de la función utilizando los argumentos proporcionados.	
function_name(arguments)
greet("Alice")


# Mayor o igual que(>=)
# Comprueba si el valor de la variable1 es mayor o igual que la variable2.	
variable1 >= variable2
5 >= 5 and 9 >= 5 # devuelve True

quantity = 105
minimum = 100
quantity >= minimum
# devuelve True


# Mayor que(>)
# Comprueba si el valor de la variable1 es mayor que el de la variable2.
variable1 > variable2
9 > 6  # devuelve True
age = 20
max_age = 25
age > max_age
# devuelve False


# groupby()
# Divide un DataFrame en grupos según criterios específicos, lo que permite la agregación, transformación o análisis posteriores dentro de cada grupo.	
grouped = dataframe_name.groupby(by, axis=0, level=None, as_index=True, sort=True, group_keys=True, squeeze=False, observed=False, dropna=True)

grouped = df.groupby(["category", "region"]).agg({"sales": "sum"})


# head()
# Muestra las primeras n filas del DataFrame.	
dataframe_name.head(n)
df.head(5)


# If Statement
# Ejecuta el bloque de código "if" si la condición es "Verdadera".	
if condition:
    #   codigo
    ...

if temperature > 30:
    print("It's a hot day!")


# If-Elif-Else
# Ejecuta el primer bloque de código si la condición1 es "Verdadera"; de lo contrario, verifica la condición2, y así sucesivamente. Si ninguna condición es "Verdadera", se
    # ejecuta el bloque else.
if condition1:
    # Code if condition1 is True
    ...
elif condition2:
    # Code if condition2 is True
    ...
else:
    # Code if no condition is True
    ...

score = 85 # Example score
if score >= 90:
    print("You got an A!")
elif score >= 80:
    print("You got a B.")
else:
    print("You need to work harder.")
# Output = You got a B.


# If-Else Statement
# Ejecuta el primer bloque de código si la condición es `True`, de lo contrario, el segundo bloque.
if condicion: 
    # Código, si la condición es True
    ...
else: 
    # Código, si la condición es False
    ...

if edad >= 18:
    print("Eres un adulto.")
else:
    print("Todavía no eres un adulto.")


# Importar pandas
# Importa la biblioteca Pandas con el alias pd.
import pandas as pd
import pandas as pd


# Importar NumPy	Importa la biblioteca NumPy.
import numpy as np
import numpy as np


# Indexación
# Accede al carácter en un índice específico.
mi_cadena = "Hola"
caracter = mi_cadena[0]


# info()
# Proporciona información sobre el DataFrame, incluidos los tipos de datos y el uso de memoria.
nombre_del_dataframe.info()
df.info()


# issubset()
# El método `issubset()` verifica si el conjunto actual es un subconjunto de otro conjunto. Devuelve True si todos los elementos del conjunto actual están presentes en el otro
    # conjunto, de lo contrario, False.
es_subconjunto = conjunto1.issubset(conjunto2)
es_subconjunto = frutas.issubset(colores)


# issuperset()
# El método `issuperset()` verifica si el conjunto actual es un superconjunto de otro conjunto. Devuelve True si todos los elementos del otro conjunto están presentes en el
    # conjunto actual, de lo contrario, False.
es_superconjunto = conjunto1.issuperset(conjunto2)
es_superconjunto = colores.issuperset(frutas)


# items()
# Recupera todos los pares clave-valor como tuplas y los convierte en una lista de tuplas. Cada tupla consta de una clave y su valor correspondiente.
lista_de_items = list(diccionario_nombre.items())
info = list(persona.items())


# Iterar sobre líneas
# Itera a través de cada línea en el archivo usando un `bucle`.
for linea in archivo: 
    # Código para procesar cada línea
    ...
with open("data.txt", "r") as archivo:
    for linea in archivo:
        print(linea)
    ...


# Existencia de clave
# Puedes verificar la existencia de una clave en un diccionario usando la palabra clave `in`.
if "nombre" in persona:
    print("El nombre existe en el diccionario.")


# keys()
# Recupera todas las claves del diccionario y las convierte en una lista. Útil para iterar o procesar claves utilizando métodos de lista.
lista_de_claves = list(diccionario_nombre.keys())
claves_persona = list(persona.keys())


# len()
# Devuelve la longitud de una cadena.
longitud_cadena = len(nombre_de_cadena)
longitud = len(mi_cadena)


# Menor o igual que (<=)
# Verifica si el valor de variable1 es menor o igual que variable2.
variable1 <= variable2


# Menor que (<)
# Verifica si el valor de variable1 es menor que variable2.
variable1 < variable2


# Controles de bucle
# `break` sale prematuramente del bucle. `continue` omite el resto de la iteración actual y pasa a la siguiente iteración.
for articulo in lista:  # Código para repetir
    if articulo == 10:  # declaración booleana
        break
for articulo in lista:  # Código para repetir
    if articulo == 10:  # declaración booleana
        continue


# lower()
# Convierte la cadena a minúsculas.
texto_en_minúsculas = mi_cadena.lower()


# merge()
# Fusiona dos DataFrames basados en varias columnas comunes.
dataframe_fusionado = pd.merge(df1, df2, on=["columna1", "columna2"])
dataframe_fusionado = pd.merge(ventas, productos, on=["product_id", "category_id"])


# NOT
# Devuelve `True` si la variable es `False`, y viceversa.
not variable


# No igual (!=)
# Verifica si dos valores no son iguales.
variable1 != variable2


# np.array()
# Crea un array unidimensional o multidimensional.
array_1d = np.array([valores_lista1])  # Array 1D
array_2d = np.array([[valores_lista1], [valores_lista2]])  # Array 2D
array_1d = np.array([1, 2, 3])  # Array 1D
array_2d = np.array([[1, 2], [3, 4]])  # Array 2D


# Atributos del array de Numpy
# Calcula la media de los elementos del array.
np.mean(array)
np.sum(array)
np.min(array)
np.max(array)
np.dot(array_1, array_2)


# Creación de objetos
# Crea una instancia de una clase (objeto) usando el constructor de la clase.
nombre_objeto = NombreClase(argumentos)
persona1 = Persona("Alice", 25)


# open() y close()
# Abre un archivo, realiza operaciones y cierra explícitamente el archivo utilizando el método close().
archivo = open(nombre_archivo, modo) 
# Código que utiliza el archivo
archivo.close()
archivo = open("data.txt", "r")
contenido = archivo.read()
archivo.close()


# OR
# Devuelve `True` si statement1 o statement2 (o ambos) son `True`. De lo contrario, devuelve `False`.
declaracion1 or declaracion2

# Invitación a la fiesta de despedida
grado = 12
grado == 11 or grado == 12
# Devuelve True


# pop()
# El método `pop()` elimina y devuelve un elemento arbitrario del conjunto. Genera un `KeyError` si el conjunto está vacío. Úsalo para quitar elementos cuando el orden no importa.
elemento_eliminado = set_nombre.pop()
removed_fruit = frutas.pop()


# print DataFrame
# Muestra el contenido del DataFrame.
print(df)  # o simplemente escribe df
print(df)
df


# print()
# Imprime el mensaje o la variable dentro de `()`.
print("Hola, mundo")
print(a + b)


# Operadores de Python
# - Adición (+): Suma dos valores juntos.
x = 9
y = 4
resultado_suma = x + y  # Suma
resultado_resta = x - y  # Resta
resultado_multiplicacion = x * y  # Multiplicación
resultado_division = x / y  # División
resultado_division_entera = x // y  # División entera
resultado_modulo = x % y  # Módulo


# range()
# Genera una secuencia de números dentro de un rango especificado.
range(detener)
range(inicio, detener)
range(inicio, detener, paso)

range(5)  # genera una secuencia de enteros desde 0 hasta 4
range(2, 10)  # genera una secuencia de enteros desde 2 hasta 9
range(1, 11, 2)  # genera enteros impares desde 1 hasta 10


# remove()
# Utiliza el método `remove()` para eliminar un elemento específico del conjunto. Genera un `KeyError` si el elemento no se encuentra.
set_nombre.remove(elemento)
frutas.remove("banana")


# replace()
# Reemplaza subcadenas.
mi_cadena = "Hola"
nuevo_texto = mi_cadena.replace("Hola", "Hola")


# replace()
# Reemplaza valores específicos en una columna con nuevos valores.
dataframe_nombre["nombre_columna"].replace(valor_antiguo, valor_nuevo, inplace=True)
df["estado"].replace("En Progreso", "Activo", inplace=True)


# Declaración de retorno
# `Return` es una palabra clave utilizada para enviar un valor de vuelta desde una función a su llamador.
# return valor
def sumar(a, b):
    return a + b
resultado = sumar(3, 5)


# Operaciones de conjunto
# Realiza varias operaciones en conjuntos: `unión`, `intersección`, `diferencia`, `diferencia simétrica`.
union_set = set1.union(set2)
interseccion_set = set1.intersection(set2)
diferencia_set = set1.difference(set2)
sym_diff_set = set1.symmetric_difference(set2)

combined = frutas.union(colores)
common = frutas.intersection(colores)
unique_to_fruits = frutas.difference(colores)
sym_diff = frutas.symmetric_difference(colores)


# Slicing
# Extrae una porción de la cadena.
subcadena = nombre_cadena[inicio:fin]
mi_cadena = "Hola"
subcadena = mi_cadena[0:5]


# split()
# Separa una cadena en una lista basada en un delimitador.
mi_cadena = "Hola"
texto_dividido = mi_cadena.split(",")


# strip()
# Elimina los espacios en blanco al principio/final.
mi_cadena = "Hola"
recortado = mi_cadena.strip()


# tail()
# Muestra las últimas n filas del DataFrame.
dataframe_nombre.tail(n)
df.tail(5)


# Bloque Try-Except
# Intenta ejecutar el código en el bloque try. Si ocurre una excepción del tipo especificado, se ejecuta el código en el bloque except.
try:
    # Código que podría generar una excepción
    ...
except TipoDeExcepcion:
    # Código para manejar la excepción
    ...
try:
    num = int(input("Ingrese un número: "))
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número válido.")


# Bloque Try-Except con bloque Else
# El código en el bloque `else` se ejecuta si no ocurre ninguna excepción en el bloque try.
try: 
    # Código que podría generar una excepción
    ...
except TipoDeExcepcion:
    # Código para manejar la excepción
    ...
else: 
    # Código para ejecutar si no hay ninguna excepción
    ...

try:
    num = int(input("Ingrese un número: "))
except ValueError:
    print("Entrada no válida. Por favor, ingrese un número válido.")
else:
    print("Ingresaste:", num)


# Bloque Try-Except con bloque Finally
# El código en el bloque `finally` siempre se ejecuta, independientemente de si ocurrió una excepción.
try: 
    ... # Código que podría generar una excepción
except TipoDeExcepcion:
    ... # Código para manejar la excepción
finally: 
    ... # Código que siempre se ejecuta

try:
    archivo = open("data.txt", "r")
    datos = archivo.read()
except FileNotFoundError:
    print("Archivo no encontrado.")
finally:
    archivo.close()


# update()
# El método `update()` fusiona el diccionario proporcionado en el diccionario existente, agregando o actualizando pares clave-valor.
diccionario_nombre.update({clave: valor})
persona.update({"Profesión": "Doctor"})


# update()
# El método `update()` agrega elementos de otro iterable al conjunto. Mantiene la unicidad de los elementos.
set_nombre.update(iterable)
frutas.update(["kiwi", "uva"])


# upper()
# Convierte la cadena a mayúsculas.
mi_cadena = "Hola"
texto_en_mayusculas = mi_cadena.upper()


# values()
# Extrae todos los valores del diccionario y los convierte en una lista. Esta lista se puede usar para un procesamiento o análisis adicionales.
lista_de_valores = list(diccionario_nombre.values())
valores_persona = list(persona.values())


# Asignación de variable
# Asigna un valor a una variable.
nombre_variable = valor
nombre = "John"  # asignando John a la variable nombre
x = 5  # asignando 5 a la variable x


# Bucle While
# Un bucle `while` ejecuta repetidamente un bloque de código siempre que una condición especificada permanezca `True`.
while condicion:
    ... # Código para repetir

count = 0
while count < 5:
    print(count)
    count += 1

# with open()
# Abre un archivo utilizando un bloque `with`, asegurando el cierre automático del archivo después de su uso.
with open(nombre_archivo, modo) as archivo:
    # Código que utiliza el archivo
    ...

with open("data.txt", "r") as archivo:
    contenido = archivo.read()