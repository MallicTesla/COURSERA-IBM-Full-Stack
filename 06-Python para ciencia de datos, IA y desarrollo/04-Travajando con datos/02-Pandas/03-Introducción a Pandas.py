"""
Introducción a Pandas para el análisis de datos
Objetivo:
    Aprende qué son las Serie Pandas y cómo crearlas.
    Comprender cómo acceder y manipular datos dentro de una serie.
    Descubra los conceptos básicos para crear y trabajar con Pandas DataFrames.
    Aprenda cómo acceder, modificar y analizar datos en DataFrames.
    Obtenga información sobre los atributos y métodos comunes de DataFrame.

¿Qué son los pandas?
Pandas es una popular biblioteca de análisis y manipulación de datos de código abierto para el lenguaje de programación Python. Proporciona un conjunto de herramientas potente y
    flexible para trabajar con datos estructurados, lo que la convierte en una herramienta fundamental para científicos, analistas e ingenieros de datos.
Pandas está diseñado para manejar datos en varios formatos, como datos tabulares, datos de series temporales y más, lo que lo convierte en una parte esencial del flujo de
    trabajo de procesamiento de datos en muchas industrias.

Estas son algunas de las características y funcionalidades clave de Pandas :

Estructuras de datos : Pandas ofrece dos estructuras de datos principales: DataFrame y Series.

Un DataFrame es una estructura de datos tabulares bidimensional, de tamaño variable y potencialmente heterogénea con ejes etiquetados (filas y columnas).
Una serie es una matriz etiquetada unidimensional, esencialmente una sola columna o fila de datos.
Importación y exportación de datos : Pandas facilita la lectura de datos de diversas fuentes, incluidos archivos CSV, hojas de cálculo de Excel, bases de datos SQL y más.
    También puede exportar datos a estos formatos, lo que permite un intercambio de datos fluido.

Fusión y unión de datos : puede combinar varios DataFrames utilizando métodos como fusionar y unir, similares a las operaciones SQL, para crear conjuntos de datos más complejos
    de diferentes fuentes.

Indexación eficiente : Pandas proporciona métodos de selección e indexación eficientes, lo que le permite acceder rápidamente a filas y columnas de datos específicas.

Estructuras de datos personalizadas : puede crear estructuras de datos personalizadas y manipular datos de manera que se adapten a sus necesidades específicas, ampliando las
    capacidades de Pandas.

Importación de pandas:
Importe Pandas usando el comando de importación, seguido del nombre de la biblioteca.
Por lo general, Pandas se importa como pd para mayor brevedad en el código.

"""
import pandas as pd
"""
Carga de datos:
Pandas se puede utilizar para cargar datos de diversas fuentes, como archivos CSV y Excel.
La función read_csv se utiliza para cargar datos de un archivo CSV en un Pandas DataFrame.
Para leer un archivo CSV (valores separados por comas) en Python usando la biblioteca Pandas, puede usar la función pd.read_csv(). Aquí está la sintaxis para leer un archivo CSV:

"""
import pandas as pd
# Read the CSV file into a DataFrame
df = pd.read_csv('your_file.csv')
"""
Reemplace 'your_file.csv' con la ruta real del archivo CSV. Asegúrese de que el archivo esté ubicado en el mismo directorio que su secuencia de comandos Python o proporcione la
    ruta de archivo correcta.

¿Qué es una serie?
Una serie es una matriz etiquetada unidimensional en Pandas. Se puede considerar como una única columna de datos con etiquetas o índices para cada elemento. Puede crear una
    serie a partir de varias fuentes de datos, como listas, matrices NumPy o diccionarios.
Aquí hay un ejemplo básico de creación de una serie en Pandas:

"""
import pandas as pd
# Create a Series from a list
data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)
"""
En este ejemplo, hemos creado una serie denominada s con datos numéricos. Tenga en cuenta que Pandas asignó automáticamente índices numéricos (0, 1, 2, 3, 4) a cada elemento,
    pero también puede especificar etiquetas personalizadas si es necesario.

Accediendo a elementos de una serie
Puede acceder a los elementos de una Serie utilizando las etiquetas de índice o las posiciones de los números enteros. A continuación se muestran algunos métodos comunes para
    acceder a los datos de la serie:

Accediendo por etiqueta
"""
print(s[2])     # Access the element with label 2 (value 30)
"""
Accediendo por posición
"""
print(s.iloc[3]) # Access the element at position 3 (value 40)
"""
Accediendo a múltiples elementos
"""
print(s[1:4])   # Access a range of elements by label
"""
Atributos y métodos de la serie
La serie Pandas viene con varios atributos y métodos para ayudarlo a manipular y analizar datos de manera efectiva. Aquí hay algunos esenciales:

values :                        devuelve los datos de la serie como una matriz NumPy.
index :                         Devuelve el índice (etiquetas) de la Serie.
shape :(forma)                  Devuelve una tupla que representa las dimensiones de la Serie.
size :(tamaño)                  Devuelve el número de elementos de la Serie.
mean(), sum(), min(), max() :   calcula las estadísticas resumidas de los datos.
Unique(), nunique() :           obtiene valores únicos o el número de valores únicos.
sort_values(), sort_index() :   Ordena la serie por valores o etiquetas de índice.
isnull(), notnull() :           comprueba si hay valores faltantes (NaN) o no faltantes.
apply() :                       aplica una función personalizada a cada elemento de la serie.

¿Qué es un marco de datos?
Un DataFrame es una estructura de datos bidimensional etiquetada con columnas de tipos de datos potencialmente diferentes. Piense en ello como una tabla donde cada columna
    representa una variable y cada fila representa una observación o un punto de datos. Los DataFrames son adecuados para una amplia gama de datos, incluidos datos estructurados
    de archivos CSV, hojas de cálculo de Excel, bases de datos SQL y más.

Creación de marcos de datos a partir de diccionarios:
Los DataFrames se pueden crear a partir de diccionarios, con claves como etiquetas de columnas y valores como listas que representan filas.

"""
import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
"""
Selección de columnas:
Puede seleccionar una sola columna de un DataFrame especificando el nombre de la columna entre corchetes dobles.
Se pueden seleccionar varias columnas de manera similar, creando un nuevo DataFrame.

"""
print(df['Name'])  # Access the 'Name' column
"""
Accediendo a filas:
Puede acceder a las filas por su índice usando .iloc[] o por etiqueta usando .loc[].

"""
print(df.iloc[2])   # Access the third row by position
print(df.loc[1])    # Access the second row by label
"""
Rebanar:
Puede dividir DataFrames para seleccionar filas y columnas específicas.

"""
print(df[['Name', 'Age']])  # Select specific columns
print(df[1:3])             # Select specific rows
"""
Encontrar elementos únicos:
Utilice el método único para determinar los elementos únicos en una columna de un DataFrame.

"""
unique_dates = df['Age'].unique()
"""
Filtrado condicional:
Puede filtrar datos en un DataFrame según las condiciones utilizando operadores de desigualdad.
Por ejemplo, puedes filtrar álbumes publicados después de un año determinado.

"""
high_above_102 = df[df['Age'] > 25]
"""
Guardar marcos de datos:
Para guardar un DataFrame en un archivo CSV, use el método to_csv y especifique el nombre del archivo con una extensión ".csv". Pandas proporciona otras funciones para guardar
    DataFrames en diferentes formatos.

"""
df.to_csv('trading_data.csv', index=False)
"""
Atributos y métodos del marco de datos
Los DataFrames proporcionan numerosos atributos y métodos para la manipulación y análisis de datos, que incluyen:

forma :                         evuelve las dimensiones (número de filas y columnas) del DataFrame.
info() :                        proporciona un resumen del DataFrame, incluidos los tipos de datos y los recuentos no nulos.
describe() :                    Genera estadísticas resumidas para columnas numéricas.
head(), tail() :                muestra la primera o la última n filas del DataFrame.
mean(), sum(), min(), max() :   calcula estadísticas resumidas para columnas.
sort_values() :                 Ordena el DataFrame por una o más columnas.
groupby() :                     agrupa datos en función de columnas específicas para su agregación.
fillna(), drop(), rename() :    Maneja valores faltantes, elimina columnas o cambia el nombre de las columnas.
apply() :                       aplica una función a cada elemento, fila o columna del DataFrame.

Pandas ofrece una amplia gama de métodos más allá de estos ejemplos. Para obtener información más detallada, consulte la documentación oficial disponible en el sitio web oficial
    de Pandas . https://pandas.pydata.org/docs/

Conclusión
En conclusión, dominar el uso de Pandas Series y DataFrames es esencial para una manipulación y análisis de datos efectivos en Python. Las series proporcionan una base para
    manejar datos unidimensionales con etiquetas, mientras que los DataFrames ofrecen una estructura versátil similar a una tabla para trabajar con datos bidimensionales. Ya sea
    que esté limpiando, explorando, transformando o analizando datos, estas estructuras de datos de Pandas, junto con sus atributos y métodos, le permiten manipular datos de
    manera eficiente y flexible para obtener información valiosa. Al incorporar Series y DataFrames en su conjunto de herramientas de ciencia de datos, estará bien preparado
    para abordar una amplia gama de tareas relacionadas con datos y mejorar sus capacidades de análisis de datos.
Para mejorar sus habilidades en el análisis de datos con Pandas, considere los siguientes pasos:

Práctica:
Trabaje con conjuntos de datos reales para aplicar lo que ha aprendido y adquirir experiencia práctica.

Explorar la documentación:
Visite el sitio web oficial de Pandas para explorar la documentación extensa y descubrir más funciones y métodos.
"""