# Para esta práctica de laboratorio, usaremos Python y varias bibliotecas de Python. Algunas de estas bibliotecas pueden estar instaladas en su entorno de laboratorio o en SN
#   Labs. Es posible que usted deba instalar otros. Las celdas siguientes instalarán estas bibliotecas cuando se ejecuten.

# Importe los módulos y funciones necesarios
from bs4 import BeautifulSoup #este módulo ayuda en el web scraping.
import requests  # este módulo nos ayuda a descargar una página web

# Beautiful Soup es una biblioteca de Python para extraer datos de archivos HTML y XML; nos centraremos en los archivos HTML. Esto se logra representando el HTML como un
#   conjunto de objetos con métodos utilizados para analizar el HTML. Podemos navegar por el HTML como un árbol y/o filtrar lo que estamos buscando.

# Considere el siguiente HTML:

"""
%%html
<!DOCTYPE html>
<html>
    <head>
        <title>Page Title</title>
    </head>
    <body>
        <h3><b id='boldest'>Lebron James</b></h3>
        <p> Salary: $ 92,000,000 </p>
        <h3> Stephen Curry</h3>
        <p> Salary: $85,000, 000 </p>
        <h3> Kevin Durant </h3>
        <p> Salary: $73,200, 000</p>
    </body>
</html>
"""
html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"

# Para analizar un documento, páselo al constructor <code>BeautifulSoup</code>. El objeto <code>BeautifulSoup</code> representa el documento como una estructura de datos anidada:

soup = BeautifulSoup(html, 'html5lib')

# Primero, el documento se convierte a Unicode (similar a ASCII) y las entidades HTML se convierten a caracteres Unicode. Beautiful Soup transforma un documento HTML complejo en
#   un árbol complejo de objetos Python. El objeto <code>BeautifulSoup</code> puede crear otros tipos de objetos. En esta práctica de laboratorio, cubriremos los objetos
#   <code>BeautifulSoup</code> y <code>Tag</code>, que para los propósitos de esta práctica de laboratorio son idénticos. Finalmente, veremos los objetos
#   <code>NavigableString</code>.

# Podemos usar el método <code>prettify()</code> para mostrar el HTML en la estructura anidada:

print(soup.prettify())

# Digamos que queremos el título de la página y el nombre del jugador mejor pagado. Podemos usar la <code>Etiqueta</code>. El objeto <code>Tag</code> corresponde a una etiqueta
#   HTML en el documento original, por ejemplo, el título de la etiqueta.

tag_object=soup.title
print("tag object:",tag_object)

# podemos ver el tipo de etiqueta bs4.element.Tag

print("tag object type:",type(tag_object))

# Si hay más de una <code>Etiqueta</code> con el mismo nombre, se llama al primer elemento con ese nombre <code>Etiqueta</code>. Esto corresponde al jugador más pagado:

tag_object=soup.h3

# Encerrado en el atributo en negrita <code>b</code>, ayuda el uso de la representación de árbol. Podemos navegar hacia abajo en el árbol usando el atributo secundario para
#   obtener el nombre.

# Hijos, padres y hermanos

# Como se indicó anteriormente, el objeto <code>Tag</code> es un árbol de objetos. Podemos acceder al hijo de la etiqueta o navegar hacia abajo en la rama de la siguiente manera:

tag_child =tag_object.b

# Puede acceder al padre con el <código> padre</código>.

parent_tag=tag_child.parent

# esto es idéntico a:

tag_object

# tag_object parent es el elemento del cuerpo.

tag_object.parent

# El hermano tag_object es el elemento de párrafo.

sibling_1=tag_object.next_sibling

# sibling_2 es el elemento de encabezado, que también es hermano de sibling_1 y tag_object.

sibling_2=sibling_1.next_sibling

# <h3 id="first_question">Exercise: <code>next_sibling</code></h3>

# Utilice el objeto <code>sibling\_2</code> y el método <code>next_sibling</code> para encontrar el salario de Stephen Curry:


# HTML Attributes

# Si la etiqueta tiene atributos, la etiqueta <code>id="boldest"</code> tiene un atributo <code>id</code> cuyo valor es <code>boldest</code>. Puede acceder a los atributos de
#   una etiqueta tratándola como un diccionario:

tag_child['id']

# Puedes acceder a ese diccionario directamente como atributos:

tag_child.attrs

# También puedes trabajar con atributos multivalor. Consulte [1] para obtener más información.
# También podemos obtener el contenido del atributo de la etiqueta usando el método get() de Python.

tag_child.get('id')

# Cadena navegable
# Una cadena corresponde a un fragmento de texto o contenido dentro de una etiqueta. Beautiful Soup usa la clase NavigableString para contener este texto. En nuestro HTML
#   podemos obtener el nombre del primer jugador extrayendo la cadena del objeto Tag tag_child de la siguiente manera:

tag_string=tag_child.string

# Nosotros podemos verificar que el tipo es Cadena Navegable

type(tag_string)

# Una NavigableString es similar a una cadena de Python o Unicode. Para ser más precisos, la principal diferencia es que también admite algunas funciones de BeautifulSoup.
#   Podemos convertirlo en un objeto de cadena en Python:

unicode_string = str(tag_string)


# Filtrar
# Los filtros le permiten encontrar patrones complejos, el filtro más simple es una cadena. En esta sección pasaremos una cadena a un método de filtro diferente y Beautiful Soup
#   realizará una comparación con esa cadena exacta. Considere el siguiente HTML de lanzamientos de cohetes:

"""
%%html
<table>
    <tr>
        <td id='flight' >Flight No</td>
        <td>Launch site</td> 
        <td>Payload mass</td>
    </tr>
    <tr> 
        <td>1</td>
        <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida</a></td>
        <td>300 kg</td>
    </tr>
    <tr>
        <td>2</td>
        <td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td>
        <td>94 kg</td>
    </tr>
    <tr>
        <td>3</td>
        <td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td>
        <td>80 kg</td>
    </tr>
</table>
"""

# Podemos almacenarlo como una cadena en la variable <code>table</code>:

table="<table><tr><td id='flight'>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr> <td>1</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a></td><td>300 kg</td></tr><tr><td>2</td><td><a href='https://en.wikipedia.org/wiki/Texas'>Texas</a></td><td>94 kg</td></tr><tr><td>3</td><td><a href='https://en.wikipedia.org/wiki/Florida'>Florida<a> </td><td>80 kg</td></tr></table>"
table_bs = BeautifulSoup(table, 'html5lib')

# encuentra todos
# El método find_all() busca en los descendientes de una etiqueta y recupera todos los descendientes que coinciden con sus filtros.

# La firma del método para find_all(nombre, atributos, recursivo, cadena, límite, **kwargs)

# Nombre
# Cuando configuramos el parámetro de nombre en un nombre de etiqueta, el método extraerá todas las etiquetas con ese nombre y sus hijos.

table_rows=table_bs.find_all('tr')

# El resultado es un iterable de Python como una lista, cada elemento es un objeto de etiqueta:

first_row =table_rows[0]

# El tipo es <code>etiqueta</code>

print(type(first_row))

# Nosotros podemos obtener al niño

first_row.td

# Si iteramos por la lista, cada elemento corresponde a una fila de la tabla:

for i,row in enumerate(table_rows):
    print("row",i,"is",row)

# Como la fila es un objeto de celda, podemos aplicarle el método find_all y extraer celdas de la tabla en las celdas del objeto usando la etiqueta td, estos son todos los
#   elementos secundarios con el nombre td. El resultado es una lista, cada elemento corresponde a una celda y es un objeto Tag, también podemos recorrer esta lista. Podemos
#   extraer el contenido usando el atributo de cadena.

for i,row in enumerate(table_rows):
    print("row",i)
    cells=row.find_all('td')
    for j,cell in enumerate(cells):
        print('colunm',j,"cell",cell)

# Si usamos una lista, podemos compararla con cualquier elemento de esa lista.

list_input=table_bs .find_all(name=["tr", "td"])

# Atributos
# Si no se reconoce el argumento, se convertirá en un filtro de los atributos de la etiqueta. Por ejemplo, con el argumento id, Beautiful Soup filtrará según el atributo id de
#   cada etiqueta. Por ejemplo, los primeros elementos td tienen un valor de id de vuelo, por lo tanto podemos filtrar en función de ese valor de id.

table_bs.find_all(id="flight")

# Podemos encontrar todos los elementos que tienen enlaces a la página de Wikipedia de Florida:

list_input=table_bs.find_all(href="https://en.wikipedia.org/wiki/Florida")

# Si configuramos el atributo href en Verdadero, independientemente de cuál sea el valor, el código encuentra todas las etiquetas con valor href:

table_bs.find_all(href=True)

# Existen otros métodos para tratar atributos y otros métodos relacionados. Echa un vistazo al siguiente enlace 
# https://www.crummy.com/software/BeautifulSoup/bs4/doc/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkPY0101ENSkillsNetwork19487395-2021-01-01#css-selectors

# cadena
# Con string puedes buscar cadenas en lugar de etiquetas, donde encontramos todos los elementos con Florida:

table_bs.find_all(string="Florida")

# encontrar
# El método find_all() escanea todo el documento en busca de resultados. Es útil si buscas un elemento, ya que puedes usar el método find() para encontrar el primer elemento en
#   el documento. Considere las siguientes dos tablas:


"""
%%html
<h3>Rocket Launch </h3>

<p>
    <table class='rocket'>
        <tr>
            <td>Flight No</td>
            <td>Launch site</td> 
            <td>Payload mass</td>
        </tr>
        <tr>
            <td>1</td>
            <td>Florida</td>
            <td>300 kg</td>
        </tr>
        <tr>
            <td>2</td>
            <td>Texas</td>
            <td>94 kg</td>
        </tr>
        <tr>
            <td>3</td>
            <td>Florida </td>
            <td>80 kg</td>
        </tr>
    </table>
</p>
<p>

<h3>Pizza Party  </h3>

<table class='pizza'>
    <tr>
        <td>Pizza Place</td>
        <td>Orders</td> 
        <td>Slices </td>
    </tr>
    <tr>
        <td>Domino's Pizza</td>
        <td>10</td>
        <td>100</td>
    </tr>
    <tr>
        <td>Little Caesars</td>
        <td>12</td>
        <td >144 </td>
    </tr>
    <tr>
        <td>Papa John's </td>
        <td>15 </td>
        <td>165</td>
    </tr>
"""

# Almacenamos el HTML como una cadena de Python y asignamos <code>two_tables</code>:

two_tables="<h3>Rocket Launch </h3><p><table class='rocket'><tr><td>Flight No</td><td>Launch site</td> <td>Payload mass</td></tr><tr><td>1</td><td>Florida</td><td>300 kg</td></tr><tr><td>2</td><td>Texas</td><td>94 kg</td></tr><tr><td>3</td><td>Florida </td><td>80 kg</td></tr></table></p><p><h3>Pizza Party  </h3><table class='pizza'><tr><td>Pizza Place</td><td>Orders</td> <td>Slices </td></tr><tr><td>Domino's Pizza</td><td>10</td><td>100</td></tr><tr><td>Little Caesars</td><td>12</td><td >144 </td></tr><tr><td>Papa John's </td><td>15 </td><td>165</td></tr>"

# Creamos un objeto <code>BeautifulSoup</code> <code>two_tables_bs</code>

two_tables_bs= BeautifulSoup(two_tables, 'html.parser')

# Podemos encontrar la primera tabla usando la tabla de nombres de etiquetas.

two_tables_bs.find("table")

# Podemos filtrar por el atributo de clase para encontrar la segunda tabla, pero como clase es una palabra clave en Python, agregamos un guión bajo para diferenciarlas.

two_tables_bs.find("table",class_='pizza')


# Descargar y eliminar el contenido de una página web
# Descargamos el contenido de la página web:

url = "http://www.ibm.com"

# Usamos get para descargar el contenido de la página web en formato de texto y almacenarlo en una variable llamada datos:

data  = requests.get(url).text 

# Creamos un objeto BeautifulSoup usando el constructor BeautifulSoup

soup = BeautifulSoup(data,"html5lib")  # create a soup object using the variable 'data'

# Raspe todos los enlaces

for link in soup.find_all('a',href=True):  # in html anchor/link is represented by the tag <a>
    print(link.get('href'))

# Raspe todas las imágenes Tags

for link in soup.find_all('img'):# in html image is represented by the tag <img>
    print(link)
    print(link.get('src'))


# Extraer datos de tablas HTML

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

# Antes de proceder a eliminar un sitio web, es necesario examinar el contenido y la forma en que se organizan los datos en el sitio web. Abra la URL anterior en su navegador y
#   verifique cuántas filas y columnas hay en la tabla de colores.

data  = requests.get(url).text
soup = BeautifulSoup(data,"html5lib")
table = soup.find('table')

for row in table.find_all('tr'): # in html table row is represented by the tag <tr>
    # Get all columns in each row.
    cols = row.find_all('td') # in html a column is represented by the tag <td>
    color_name = cols[2].string # store the value in column 3 as color_name
    color_code = cols[3].text # store the value in column 4 as color_code
    print("{}--->{}".format(color_name,color_code))


# Eliminación de tablas de una página web usando Pandas
# Particularmente para extraer datos tabulares de una página web, también puede utilizar el método read_html() de la biblioteca Pandas.

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DA0321EN-SkillsNetwork/labs/datasets/HTMLColorCodes.html"

import pandas as pd

tables = pd.read_html(url)

# `tables` es ahora una lista de marcos de datos que representan las tablas de la página web, en la secuencia de su aparición. En la URL actual, solo hay una tabla, por lo que
#   se puede acceder a la misma como se muestra a continuación.

tables[0]