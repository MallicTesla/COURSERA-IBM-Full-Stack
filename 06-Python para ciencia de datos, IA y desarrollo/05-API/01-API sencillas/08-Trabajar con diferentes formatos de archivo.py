# Ingeniería de datos 
# La ingeniería de datos es una de las habilidades más críticas y fundamentales en el conjunto de herramientas de cualquier científico de datos.

# Proceso de ingeniería de datos 
# Hay varios pasos en el proceso de ingeniería de datos.

# Extraer : la extracción de datos consiste en obtener datos de múltiples fuentes. Ex. Extracción de datos de un sitio web mediante Web scraping o recopilación de información de
#   los datos almacenados en diferentes formatos (JSON, CSV, XLSX, etc.).

# Transformar : transformar los datos significa eliminar los datos que no necesitamos para un análisis posterior y convertir los datos en el formato en el que todos los datos de
#   múltiples fuentes estén en el mismo formato.

# Cargar : cargar los datos dentro de un almacén de datos. El almacén de datos esencialmente contiene grandes volúmenes de datos a los que se accede para recopilar información.

# Trabajar con diferentes formatos de archivos 
# En el mundo real, la gente rara vez obtiene datos tabulares claros. Por lo tanto, es obligatorio que cualquier científico de datos (o ingeniero de datos) conozca los
#   diferentes formatos de archivos, los desafíos comunes al manejarlos y las mejores y más eficientes formas de manejar estos datos en la vida real. Hemos revisado parte de
#   este contenido en otros módulos.

# Formato de archivo 
# Un formato de archivo es una forma estándar en la que se codifica la información para almacenarla en un archivo. Primero, el formato del archivo especifica si el archivo es
#   binario o ASCII. En segundo lugar, muestra cómo está organizada la información. Por ejemplo, el formato de archivo de valores separados por comas (CSV) almacena datos
#   tabulares en texto sin formato.

# Para identificar un formato de archivo, normalmente puedes mirar la extensión del archivo para tener una idea. Por ejemplo, un archivo guardado con el nombre "Datos" en
#   formato "CSV" aparecerá como Data.csv . Al notar la extensión .csv , podemos identificar claramente que es un archivo CSV y los datos están almacenados en formato tabular.

# Hay varios formatos para un conjunto de datos, .csv, .json, .xlsx, etc. El conjunto de datos se puede almacenar en diferentes lugares, en su máquina local o, a veces, en línea.

# En esta sección, aprenderá cómo cargar un conjunto de datos en nuestro Jupyter Notebook.

# Ahora veremos algunos formatos de archivos y cómo leerlos en Python:

# Formato de archivo de valores separados por comas (CSV) 
# El formato de archivo de valores separados por comas pertenece al formato de archivo de hoja de cálculo.

# En un formato de archivo de hoja de cálculo, los datos se almacenan en celdas. Cada celda está organizada en filas y columnas. Una columna en el archivo de hoja de cálculo
#   puede tener diferentes tipos. Por ejemplo, una columna puede ser de tipo cadena, tipo fecha o tipo entero.

# Cada línea del archivo CSV representa una observación, o comúnmente llamado registro. Cada registro puede contener uno o más campos separados por una coma.

# Leyendo datos de CSV en Python 
# La biblioteca Pandas es una herramienta útil que nos permite leer varios conjuntos de datos en un marco de datos Pandas.

# Veamos cómo leer un archivo CSV en la biblioteca Pandas.

# Usamos la función pandas.read_csv() para leer el archivo csv. Entre paréntesis, ponemos la ruta del archivo junto con una comilla como argumento, para que pandas lea el
#   archivo en un marco de datos desde esa dirección. La ruta del archivo puede ser una URL o la dirección de su archivo local.

import pandas as pd

from pyodide.http import pyfetch

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/addresses.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "addresses.csv")

df = pd.read_csv("addresses.csv", header=None)

# Agregar el nombre de la columna al DataFrame 
# Podemos agregar columnas a un DataFrame existente usando su atributo de columnas .

df.columns =['First Name', 'Last Name', 'Location ', 'City','State','Area Code']

# Seleccionar una sola columna 
# Para seleccionar la primera columna 'Nombre', puede pasar el nombre de la columna como una cadena al operador de indexación.

df["First Name"]

# Seleccionar múltiples columnas
# Para seleccionar varias columnas, puede pasar una lista de nombres de columnas al operador de indexación.

df = df[['First Name', 'Last Name', 'Location ', 'City','State','Area Code']]

# Seleccionar filas usando .iloc y .loc 
# Ahora, veamos cómo usar .loc para seleccionar filas de nuestro DataFrame.

# loc(): loc() es un método de selección de datos basado en etiquetas, lo que significa que tenemos que pasar el nombre de la fila o columna que queremos seleccionar.

df.loc[0]
df.loc[[0,1,2], "First Name" ]

# Ahora, veamos cómo usar .iloc para seleccionar filas de nuestro DataFrame.

# iloc() : iloc() es un método de selección basado en índices, lo que significa que tenemos que pasar un índice entero en el método para seleccionar una fila/columna específica.

df.iloc[[0,1,2], 0]

# Para obtener más información, lea la documentación .

# Realicemos algunas transformaciones básicas en pandas.


# Función de transformación en Pandas 
# La función Transformar de Python devuelve un marco de datos de producción propia con valores transformados después de aplicar la función especificada en su parámetro.

# Veamos cómo funciona la función Transformar.

import pandas as pd
import numpy as np

df=pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])

# Digamos que queremos agregar 10 a cada elemento en un marco de datos:

df = df.transform(func = lambda x : x + 10)

# Ahora usaremos la función DataFrame.transform() para encontrar la raíz cuadrada de cada elemento del marco de datos.

result = df.transform(func = ['sqrt'])

# Mas info https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.transform.html?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01


# Formato de archivo JSON
# JSON (Notación de objetos JavaScript) es un formato ligero de intercambio de datos. Es fácil para los humanos leer y escribir.

# JSON se basa en dos estructuras:

# Una colección de pares de nombre/valor. En varios idiomas, esto se realiza como un objeto, registro, estructura, diccionario, tabla hash, lista con clave o matriz asociativa.

# Una lista ordenada de valores. En la mayoría de los lenguajes, esto se realiza como una matriz, un vector, una lista o una secuencia.

# JSON es un formato de datos independiente del idioma. Se deriva de JavaScript, pero muchos lenguajes de programación modernos incluyen código para generar y analizar datos en
#   formato JSON. Es un formato de datos muy común con una amplia gama de aplicaciones.

# El texto en JSON se realiza mediante una cadena entrecomillada que contiene los valores en las asignaciones clave-valor dentro de {}. Es similar al diccionario en Python.

# Python admite JSON a través de un paquete integrado llamado json . Para utilizar esta función, importamos el paquete json en el script Python.

import json

# Escribir JSON en un archivo 
# Esto suele denominarse serialización. Es el proceso de convertir un objeto a un formato especial que sea adecuado para transmitir a través de la red o almacenar en un archivo
#   o base de datos.

# Para manejar el flujo de datos en un archivo, la biblioteca JSON en Python utiliza la función dump() o dumps() para convertir los objetos de Python en sus respectivos objetos
#   JSON. Esto facilita la escritura de datos en archivos.

person = {
    'first_name' : 'Mark',
    'last_name' : 'abc',
    'age' : 27,
    'address': {
        "streetAddress": "21 2nd Street",
        "city": "New York",
        "state": "NY",
        "postalCode": "10021-3100"
    }
}

# serialización usando la función dump() 
# El método json.dump() se puede utilizar para escribir en un archivo JSON.

# Sintaxis: json.dump(dict, file_pointer)

# Parámetros:

# diccionario : nombre del diccionario que debe convertirse en un objeto JSON.
# puntero de archivo : puntero del archivo abierto en modo de escritura o adición.

with open('person.json', 'w') as f:  # writing JSON object
    json.dump(person, f)

# serialización usando la función dumps()
# json.dumps() que ayuda a convertir un diccionario en un objeto JSON.

# Se necesitan dos parámetros:

# diccionario : nombre del diccionario que debe convertirse en un objeto JSON.
# sangría : define el número de unidades para la sangría

# Serializing json  
json_object = json.dumps(person, indent = 4) 

# Writing to sample.json 
with open("sample.json", "w") as outfile: 
    outfile.write(json_object) 

print(json_object)

# Nuestros objetos Python ahora están serializados en el archivo. Para deserializarlo nuevamente al objeto Python, usamos la función load().


# Leer JSON en un archivo 
# Este proceso suele denominarse Deserialización ; es lo contrario de la serialización. Convierte el formato especial devuelto por la serialización nuevamente en un objeto
#   utilizable.

# Usando json.load() 
# El paquete JSON tiene la función json.load() que carga el contenido json de un archivo json en un diccionario.

# Se necesita un parámetro:

# Puntero de archivo : un puntero de archivo que apunta a un archivo JSON

import json 

# Opening JSON file 
with open('sample.json', 'r') as openfile: 

    # Reading from json file 
    json_object = json.load(openfile) 

print(json_object) 
print(type(json_object)) 


# Formato de archivo XLSX
# XLSX es un formato de archivo XML abierto de Microsoft Excel. Es otro tipo de formato de archivo de hoja de cálculo.

# En XLSX, los datos se organizan en celdas y columnas de una hoja.

# Leyendo los datos del archivo XLSX 

# Carguemos los datos del archivo XLSX y definamos el nombre de la hoja. Para cargar los datos, puede utilizar la biblioteca Pandas en Py

import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/file_example_XLSX_10.xlsx"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "file_example_XLSX_10.xlsx")

df = pd.read_excel("file_example_XLSX_10.xlsx")


# Formato de archivo XML 
# XML también se conoce como lenguaje de marcado extensible . Como sugiere el nombre, es un lenguaje de marcado. Tiene ciertas reglas para codificar datos. El formato de archivo
#   XML es un formato de archivo legible por humanos y por máquinas.

# Pandas no incluye ningún método para leer y escribir archivos XML. Aquí, veremos cómo podemos usar otros módulos para leer datos de un archivo XML y cargarlos en un Pandas
#   DataFrame.

# Escribiendo con xml.etree.ElementTree 
# El módulo xml.etree.ElementTree viene integrado con Python. Proporciona funcionalidad para analizar y crear documentos XML. ElementTree representa el documento XML como un
#   árbol. Podemos movernos por el documento utilizando nodos que son elementos y subelementos del archivo XML.

# Para obtener más información, lea la documentación xml.etree.ElementTree .

import xml.etree.ElementTree as ET

# create the file structure
employee = ET.Element('employee')
details = ET.SubElement(employee, 'details')
first = ET.SubElement(details, 'firstname')
second = ET.SubElement(details, 'lastname')
third = ET.SubElement(details, 'age')
first.text = 'Shiv'
second.text = 'Mishra'
third.text = '23'

# create a new XML file with the results
mydata1 = ET.ElementTree(employee)
# myfile = open("items2.xml", "wb")
# myfile.write(mydata)
with open("new_sample.xml", "wb") as files:
    mydata1.write(files)

# Lectura con xml.etree.ElementTree 
# Echemos un vistazo a una forma de leer datos XML y colocarlos en un Pandas DataFrame. Puede ver el archivo XML en el Bloc de notas de su máquina local.

import xml.etree.ElementTree as etree

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/Sample-employee-XML-file.xml"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "Sample-employee-XML-file.xml")

# Primero deberá analizar un archivo XML y crear una lista de columnas para el marco de datos, luego extraer información útil del archivo XML y agregarla a un marco de datos de
#   pandas.

# Aquí hay un código de muestra que puede usar:

tree = etree.parse("Sample-employee-XML-file.xml")

root = tree.getroot()
columns = ["firstname", "lastname", "title", "division", "building","room"]

datatframe = pd.DataFrame(columns = columns)

for node in root: 

    firstname = node.find("firstname").text

    lastname = node.find("lastname").text 

    title = node.find("title").text 
    
    division = node.find("division").text 
    
    building = node.find("building").text
    
    room = node.find("room").text
    
    datatframe = pd.concat([datatframe, pd.Series([firstname, lastname, title, division, building, room], index = columns)], ignore_index = True)

# Leyendo un archivo xml usando la función pandas.read_xml
# También podemos leer el archivo xml descargado usando la función read_xml presente en la biblioteca pandas que devuelve un objeto Dataframe.

# Para obtener más información, lea la documentación de pandas.read_xml .

df=pd.read_xml("Sample-employee-XML-file.xml", xpath="/employees/details") 

# Guardar datos 
# En consecuencia, Pandas nos permite guardar el conjunto de datos en csv utilizando el método dataframe.to_csv() ; puede agregar la ruta y el nombre del archivo junto con
#   comillas entre paréntesis.

# Por ejemplo, si desea guardar el marco de datos df como empleado.csv en su máquina local, puede utilizar la siguiente sintaxis:

datatframe.to_csv("employee.csv", index=False)

# También podemos leer y guardar otros formatos de archivos, podemos usar funciones similares para pd.read_csv()y df.to_csv()para otros formatos de datos. Las funciones se
#   enumeran en la siguiente tabla:

# Leer/Guardar otros formatos de datos 
# Formato de datos	    Leer	        Ahorrar
# csv	                pd.read_csv()	df.to_csv()
# json	                pd.read_json()	df.to_json()
# sobresalir	        pd.read_excel()	df.to_excel()
# hdf	                pd.read_hdf()	df.to_hdf()
# SQL	                pd.read_sql()	df.to_sql()

# Sigamos adelante y realicemos un análisis de datos.


# Formato de archivo binario 
# Los archivos "binarios" son archivos cuyo formato no se compone de caracteres legibles. Contiene información de formato que sólo determinadas aplicaciones o procesadores
#   pueden entender. Si bien los humanos pueden leer archivos de texto, los archivos binarios deben ejecutarse en el software o procesador adecuado antes de que los humanos
#   puedan leerlos.

# Los archivos binarios pueden variar desde archivos de imagen como JPEG o GIF, archivos de audio como MP3 o formatos de documentos binarios como Word o PDF.

# Veamos cómo leer un archivo de imagen .

# Leyendo el archivo de imagen 
# Python admite herramientas muy poderosas cuando se trata de procesamiento de imágenes. Veamos cómo procesar las imágenes usando la biblioteca PIL .

# PIL es la biblioteca de imágenes de Python que proporciona al intérprete de Python capacidades de edición de imágenes.

from PIL import Image 

# Uncomment if running locally
# import urllib.request
# urllib.request.urlretrieve("https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg", "dog.jpg")

filename = "https://hips.hearstapps.com/hmg-prod.s3.amazonaws.com/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "./dog.jpg")

img = Image.open('./dog.jpg','r') 

# Output Images 
img.show()


# Análisis de los datos 
# En esta sección, aprenderá cómo abordar la adquisición de datos de varias maneras y obtener la información necesaria a partir de un conjunto de datos. Al final de esta
#   práctica de laboratorio, cargará con éxito los datos en Jupyter Notebook y obtendrá algunos conocimientos fundamentales a través de la biblioteca Pandas.

# En nuestro caso, el conjunto de datos sobre diabetes es una fuente en línea y está en formato CSV (valores separados por comas). Usemos este conjunto de datos como ejemplo para
#   practicar la lectura de datos.

# Acerca de este conjunto de datos 
# Contexto: este conjunto de datos proviene del Instituto Nacional de Diabetes y Enfermedades Digestivas y Renales . El objetivo del conjunto de datos es predecir de forma
#   diagnóstica si un paciente tiene diabetes o no, basándose en ciertas mediciones de diagnóstico incluidas en el conjunto de datos. Se impusieron varias restricciones a la
#   selección de estas instancias de una base de datos más grande. En particular, todos los pacientes aquí son mujeres de al menos 21 años de edad de ascendencia india Pima.

# Contenido: Los conjuntos de datos constan de varias variables predictoras médicas y una variable objetivo, Resultado. Las variables predictoras incluyen el número de embarazos
#   que ha tenido la paciente, su IMC, nivel de insulina, edad, etc.

# Tenemos 768 filas y 9 columnas. Las primeras 8 columnas representan las características y la última columna representa el objetivo/etiqueta.

import pandas as pd

filename = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%205/data/diabetes.csv"

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

await download(filename, "diabetes.csv")
df = pd.read_csv("diabetes.csv")

# Después de leer el conjunto de datos, podemos usar el método dataframe.head(n) para verificar las n filas superiores del marco de datos, donde n es un número entero. Al
#   contrario de dataframe.head(n) , dataframe.tail(n) le mostrará las n filas inferiores del marco de datos.

print("The first 5 rows of the dataframe") 
df.head(5)

# Para ver las dimensiones del marco de datos, usamos el .shapeparámetro.

df.shape

# Descripción estadística del conjunto de datos

df.info()

# Este método imprime información sobre un DataFrame, incluido el tipo de índice y las columnas, valores no nulos y uso de memoria.

df.describe()

# Pandas describe() se utiliza para ver algunos detalles estadísticos básicos como percentil, media, desviación estándar, etc. de un marco de datos o una serie de valores
#   numéricos. Cuando este método se aplica a una serie de cadenas, devuelve una salida diferente

# Identificar y manejar valores faltantes
# Usamos las funciones integradas de Python para identificar estos valores faltantes. Hay dos métodos para detectar datos faltantes:

# .es nulo()
# .no nulo()

# La salida es un valor booleano que indica si el valor que se pasa al argumento son en realidad datos faltantes.

missing_data = df.isnull()
missing_data.head(5)

# "Verdadero" significa valor faltante, mientras que "Falso" significa valor no faltante.

# Contar los valores faltantes en cada columna 
# Usando un bucle for en Python, podemos calcular rápidamente la cantidad de valores faltantes en cada columna. Como se mencionó anteriormente, "Verdadero" representa un valor
#   faltante, "Falso" significa que el valor está presente en el conjunto de datos. En el cuerpo del bucle for, el método ".value_counts()" cuenta el número de valores
#   "Verdaderos".

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")

# Como puede ver arriba, no faltan valores en el conjunto de datos.

# Formato de datos correcto 
# Verifique que todos los datos estén en el formato correcto (int, float, text u otro).

# En Pandas, usamos

# .dtype() para comprobar el tipo de datos

# .astype() para cambiar el tipo de datos

# Las variables numéricas deben tener tipo 'float' o 'int'.

df.dtypes

# Como podemos ver arriba, todas las columnas tienen el tipo de datos correcto.

# Visualización 
# La visualización es una de las mejores formas de obtener información del conjunto de datos. Seaborn y Matplotlib son dos de las bibliotecas de visualización más potentes de
#   Python.

import matplotlib.pyplot as plt
import seaborn as sns

labels= 'Not Diabetic','Diabetic'
plt.pie(df['Outcome'].value_counts(),labels=labels,autopct='%0.02f%%')
plt.legend()
plt.show()

# Como puede ver arriba, el 65,10% de las mujeres no son diabéticas y el 34,90% son diabéticas.