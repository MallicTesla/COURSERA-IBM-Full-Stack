"""
Manejo de archivos en Python
Tiempo estimado necesario: 10 minutos

El manejo de archivos es un aspecto esencial de la programación y Python proporciona funciones integradas para interactuar con los archivos. En esta guía, exploraremos cómo usar
    openla función de Python para trabajar con archivos de texto (archivos “txt”).

Objetivos
Aprenda a abrir y leer archivos de texto.
Comprenda cómo funciona la función open() en Python.
Familiarícese con el método 'with' en Python.
Descubra cómo utilizar el método read() en Python.
Explore el método readline() en Python.
Aprenda a leer caracteres específicos de un archivo.

Leer archivos de texto
Leer archivos de texto implica extraer y procesar los datos almacenados en ellos. Los archivos de texto pueden tener varias estructuras y la forma de leerlos depende de su
    formato. Aquí hay una guía general sobre cómo leer archivos de texto con diferentes estructuras:

Archivos de texto sin formato:
Los archivos de texto sin formato contienen texto sin formato y sin ninguna estructura específica.
Puede leer archivos de texto sin formato línea por línea o cargar todo el contenido en la memoria.

Usando la función opense de Python
La función de Python opense utiliza para crear un objeto de archivo y acceder a los datos dentro de un archivo de texto. Se necesitan dos parámetros principales:

Ruta del archivo : la ruta del archivo consta del nombre del archivo y el directorio donde se encuentra el archivo.

Modo : el parámetro modo especifica el propósito de abrir el archivo, como 'r' para leer, 'w' para escribir o 'a' para agregar.

"""
# Step 1: Open the file in read ('r') mode
file = open('file.txt', 'r')
# Step 2: Read the file content
content = file.read()
# Step 3: Process the content (e.g., print it)
print(content)
# Step 4: Close the file explicitly when done
file.close()
"""
Paso 1: abra el archivo en modo lectura ('r')
open('file.txt', 'r'): esta línea abre un archivo llamado 'file.txt' en modo lectura ('r'). Devuelve un objeto de archivo, que se almacena en el archivo variable. El modo 'r'
    indica que el archivo se abrirá para su lectura.

Paso 2: leer el contenido del archivo
content = file.read(): aquí, se llama al método read() en el objeto de archivo, que lee todo el contenido del archivo y lo almacena en el contenido variable. Este paso carga
    efectivamente todo el contenido de 'file.txt' en la memoria.

Paso 3: procesar el contenido (p. ej., imprimirlo)
print(content): Esta línea imprime el contenido del archivo en la salida estándar (normalmente la consola). Puede realizar cualquier procesamiento que desee en la variable de
    contenido en este punto, como analizar, buscar o analizar el texto.

Paso 4: cierre el archivo explícitamente cuando haya terminado
file.close(): Finalmente, esta línea cierra explícitamente el archivo usando el método close(). Cerrar el archivo es importante para liberar recursos del sistema y garantizar
    que el archivo se cierre correctamente después de leerlo. No cerrar el archivo puede provocar fugas de recursos.

La declaración "with"
Para simplificar el manejo de archivos y garantizar un cierre adecuado de los archivos, Python proporciona la declaración "with". Cierra automáticamente el archivo cuando se
    completan las operaciones dentro del bloque sangrado. Esto se considera una buena práctica cuando se trabaja con archivos.

"""
# Step 1: Open the file using 'with' in read ('r') mode
with open('file.txt', 'r') as file:
    # Step 2: Read the file content within the 'with' block
    content = file.read()
    # Step 3: Process the content (e.g., print it)
    print(content)
# Step 4: The file is automatically closed when the 'with' block exits
"""
Paso 1: abra el archivo usando 'con' en modo lectura ('r')
with open('file.txt', 'r') as file:: esta línea abre un archivo llamado 'file.txt' en modo lectura ('r') usando la instrucción with, que es un administrador de contexto. El
    archivo se cierra automáticamente cuando sale el bloque de código dentro de la declaración with.

Paso 2: lea el contenido del archivo dentro del bloque 'con'
content = file.read(): dentro del bloque with, se llama al método read() en el objeto de archivo. Esto lee todo el contenido del archivo y lo almacena en el contenido variable.
    La lectura del contenido del archivo se produce dentro del contexto protegido, lo que garantiza una gestión adecuada de los recursos.

Paso 3: procesar el contenido (p. ej., imprimirlo)
print(content): Después de leer el contenido del archivo, esta línea imprime el contenido en la salida estándar (generalmente la consola). Puede realizar cualquier procesamiento
    en la variable de contenido en este punto, como análisis, búsqueda o manipulación de texto.

Paso 4: El archivo se cierra automáticamente cuando sale el bloque 'with'
Una vez que el bloque de código dentro de la instrucción with termina de ejecutarse (incluido cualquier procesamiento o impresión), el archivo se cierra automáticamente. No es
    necesario llamar explícitamente a file.close() porque la instrucción with garantiza que el archivo se cierre correctamente, incluso si se produce una excepción durante la
    ejecución del bloque de código.

Ventajas de utilizar Withel método:
Las ventajas clave de utilizar el método with son:

Gestión automática de recursos: se garantiza que el archivo se cerrará cuando salga del bloque with, incluso si se produce una excepción durante el procesamiento.
Código más limpio y conciso: no es necesario llamar explícitamente a close() , lo que hace que su código sea más legible y menos propenso a errores.
Para la mayoría de las operaciones de lectura y escritura de archivos en Python, se recomienda el método with.

método de lectura en Python:
Puede leer el contenido completo de un archivo utilizando el método de lectura, que almacena los datos como una cadena en una variable. Este contenido se puede imprimir o
    manipular aún más según sea necesario.
"""
# Reading and Storing the Entire Content of a File
# Using the read method, you can retrieve the complete content of a file
# and store it as a string in a variable for further processing or display.
# Step 1: Open the file you want to read
with open('File1.txt', 'r') as file:
    
    # Step 2: Use the read method to read the entire content of the file
    file_stuff = file.read()
    
    # Step 3: Now that the file content is stored in the variable 'file_stuff',
    # you can manipulate or display it as needed.
    
    # For example, let's print the content to the console:
    print(file_stuff)
# Step 4: The 'with' block automatically closes the file when it's done,
# ensuring proper resource management and preventing resource leaks.
"""
El paso 1 implica abrir el archivo, especificando 'File1.txt' como el archivo que se abrirá para el modo de lectura ('r') usando el administrador de contexto.

El paso 2 utiliza el read()método en el objeto de archivo (archivo) para leer el contenido completo del archivo. Este contenido luego se almacena en la variable file_stuff.

El paso 3 explica que con el contenido ahora almacenado en file_stuff, tienes la flexibilidad de realizar varias operaciones en él. En el ejemplo proporcionado, el código
    imprime el contenido en la consola, pero puede manipular, analizar, buscar o procesar los datos de texto en file_stuff según sus necesidades específicas.

El paso 4 enfatiza que el bloque with cierra automáticamente el archivo cuando termina, lo que garantiza una gestión adecuada de los recursos y evita fugas de recursos. Este es
    un aspecto crucial del uso de la declaración with cuando se trabaja con archivos.

Líneas de lectura
Python proporciona métodos para leer archivos línea por línea:

El método readlines lee el archivo línea por línea y almacena cada línea como un elemento en una lista. El orden de las líneas en la lista corresponde a su orden en el archivo.

El método readline lee líneas individuales del archivo. Se puede llamar varias veces para leer las líneas siguientes.

En Python, el método readline() es como un detective que lee un libro línea por línea. Imagina que tienes un libro grande y quieres leerlo página por página. readline() te ayuda
    a hacer precisamente eso, pero con líneas de texto en lugar de páginas.

Así es como funciona:

Abrir un archivo: primero, debe abrir el archivo que desea leer usando la función open().

"""
file = open('my_file.txt', 'r')
"""
Lectura línea por línea: ahora puede usar readline() para leer una línea del archivo a la vez. Es como pasar las páginas de un libro, pero aquí obtienes una oración (o línea) en
    cada paso.

"""
line1 = file.readline()  # Reads the first line
line2 = file.readline()  # Reads the second line
"""
Usando las líneas: puedes hacer cosas con cada línea que leas. Por ejemplo, puedes imprimirlo, comprobar si contiene palabras específicas o guardarlo en otro lugar.

"""
print(line1)  # Print the first line
if 'important' in line2:
    print('This line is important!')
"""
Bucle a través de líneas: normalmente, utiliza un bucle para leer líneas hasta que no queden más líneas. Es como leer el libro completo, línea por línea.
"""
while True:
    line = file.readline()
    if not line:
        break  # Stop when there are no more lines to read
    print(line)
"""
Cerrar el libro: cuando haya terminado de leer, es esencial cerrar el archivo usando file.close() para asegurarse de no desperdiciar recursos.

"""
file.close()
"""
Entonces, en términos simples, readline() te ayuda a leer un archivo de texto línea por línea, permitiéndote trabajar con cada línea de texto a medida que avanzas. Es como tomar
    una oración a la vez de un libro y hacer algo con ella antes de pasar a la siguiente. ¡No olvides cerrar el libro cuando hayas terminado!

Leer caracteres específicos
Puede especificar la cantidad de caracteres a leer utilizando el método readlines. Por ejemplo, leer los primeros cuatro caracteres, luego los cinco siguientes, y así
    sucesivamente.

Leer caracteres específicos de un archivo de texto en Python implica abrir el archivo, navegar a la posición deseada y luego leer los caracteres que necesita. Aquí hay una
    explicación detallada de cómo leer caracteres específicos de un archivo:

Abre el archivo:
Primero, debe abrir el archivo que desea leer. Utilice la función open() con la ruta y el modo de archivo adecuados. Para leer, utilice el modo 'r'.

"""
file = open('my_file.txt', 'r')
"""
Navegue hasta la posición deseada (opcional):
Si desea leer caracteres desde una posición específica en el archivo, puede utilizar el método seek(). Este método mueve el puntero del archivo (como un cursor) a una posición
    particular. La posición se especifica en bytes, por lo que necesitará saber el desplazamiento de bytes de los caracteres que desea leer.

"""
file.seek(10)  # Move to the 11th byte (0-based index)
"""
Leer personajes específicos:
Para leer caracteres específicos, puede utilizar el método read() con un argumento que especifica la cantidad de caracteres a leer. Lee caracteres a partir de la posición actual
    del puntero del archivo.

"""
characters = file.read(5)  # Read the next 5 characters
"""
En este ejemplo, lee los siguientes 5 caracteres desde la posición actual del puntero del archivo.

Utilice los caracteres de lectura:
Ahora puedes usar la variable de caracteres para trabajar con los caracteres específicos que has leído. Puedes imprimirlos, guardarlos, manipularlos o realizar cualquier otra
    acción.

"""
print(characters)
"""
Cerrar el archivo:
Es esencial cerrar el archivo cuando haya terminado para liberar recursos del sistema y garantizar el manejo adecuado del archivo.

"""
file.close()
"""
Conclusión
En conclusión, esta lectura ha proporcionado una descripción general completa del manejo de archivos en Python, con un enfoque en la lectura de archivos de texto. El manejo de
    archivos es un aspecto fundamental de la programación y Python ofrece poderosas funciones y métodos integrados para interactuar con archivos sin problemas.
"""