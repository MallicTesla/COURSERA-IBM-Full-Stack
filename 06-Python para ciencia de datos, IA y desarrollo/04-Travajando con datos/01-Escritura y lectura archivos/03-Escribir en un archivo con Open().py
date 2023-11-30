"""
Escribir en un archivo con Open()
Tiempo estimado necesario: 10 minutos

Objetivo
Crear y escribir datos en un archivo en Python
Escriba varias líneas de texto en un archivo usando listas y bucles
Agregar nueva información a un archivo ya existente sin borrar su contenido
Compare y contraste los diferentes modos de archivo en Python, qué significan y cuándo usarlos
Escribir en un archivo
Puede crear un nuevo archivo de texto y escribirle datos usando la open() función de Python. La  open() función toma dos argumentos principales: la ruta del archivo (incluido el
    nombre del archivo) y el parámetro de modo, que especifica la operación que desea realizar en el archivo. Para escribir, debes usar el modo 'w'. Aquí tienes un ejemplo:
"""
# Create a new file Example2.txt for writing
with open('Example2.txt', 'w') as File1:
    File1.write("This is line A\n")
    File1.write("This is line B\n")
    # File1 is automatically closed when the 'with' block exits
"""
Explicación de la línea 2:**with open('Example2.txt', 'w') as File1:
Comenzamos usando la función open para abrir o crear un archivo llamado Example2.txtpara escritura (modo 'w').
El 'w'modo especifica que pretendemos escribir datos en el archivo.
Usamos la with declaración para asegurarnos de que el archivo se cierre automáticamente cuando salga el bloque de código. Esto ayuda a gestionar los recursos de manera eficiente.
Explicación de la línea 3:File1.write("This is line A\n")
Aquí, usamos el write() método en el objeto de archivo, File1para agregar el texto This is line Aal archivo.
El \nal final representa un carácter de nueva línea, que inicia una nueva línea en el archivo.
Explicación de la línea 4File1.write("This is line" B\n")
De manera similar, usamos el write() método nuevamente para agregar el texto This is line Bal archivo en una nueva línea.
Escribir varias líneas en un archivo usando una lista y un bucle
En Python, puedes usar una lista para almacenar varias líneas de texto y luego escribir estas líneas en un archivo usando un bucle. Aquí hay un fragmento de código de ejemplo
    que demuestra esto:
"""
# List of lines to write to the file
Lines = ["This is line 1", "This is line 2", "This is line 3"]
# Create a new file Example3.txt for writing
with open('Example3.txt', 'w') as File2:
    for line in Lines:
        File2.write(line + "\n")
    # File2 is automatically closed when the 'with' block exits
"""
Aquí hay una explicación del código:

Línea 2: comenzamos definiendo una lista llamada Lines, que contiene varias líneas de texto que queremos escribir en el archivo. Cada línea es una cadena.

Línea 5: A continuación, usamos la open() función para crear un nuevo archivo de texto llamado modo Example3.txtde escritura 'w'. El 'w'modo indica que pretendemos escribir
    datos en el archivo.

Línea 6: luego ingresamos un bucle for para recorrer cada elemento (línea) de la Lineslista.

Línea 7: dentro del bucle, usamos el write()método en el objeto de archivo File2para escribir la línea de texto actual (línea) en el archivo. Agregamos \nal final de cada línea
    para asegurarnos de que a cada línea le siga un carácter de nueva línea, que las separa en el archivo.

Línea 8: Finalmente, agregamos un comentario que indica que el archivo File2se cerrará automáticamente cuando salga el bloque de código dentro de la instrucción with. Cerrar
    correctamente el expediente es fundamental para una buena gestión de los recursos.

Agregar datos a un archivo existente
En Python, puede usar el 'a' modo al abrir un archivo para agregar nuevos datos a un archivo existente sin sobrescribir su contenido. Aquí hay un fragmento de código de ejemplo
    que demuestra esto:
"""
# Data to append to the existing file
new_data = "This is line C"
# Open an existing file Example2.txt for appending
with open('Example2.txt', 'a') as File1:
    File1.write(new_data + "\n")
    # File1 is automatically closed when the 'with' block exits
"""
Aquí hay una explicación del código:

Línea 2: comenzamos definiendo una variable new_dataque contiene el texto que queremos agregar al archivo existente. En este caso, es la cadena `Esta es la línea C.``

Línea 5: A continuación, usamos la open() función para abrir un archivo existente llamado Example2.txtpara agregarlo, 'a' modo. El 'a' modo indica que pretendemos agregar datos
    al archivo y, si el archivo no existe, se creará.

Línea 6: dentro del bloque with, usamos el write() método en el objeto de archivo File1para agregarlo new_dataal archivo. Agregamos "\n"al final para garantizar que los datos
    agregados comiencen en una nueva línea, manteniendo la legibilidad del archivo.

Finalmente, agregamos un comentario que indica que el archivo File1se cerrará automáticamente cuando with salga el bloque de código dentro de la declaración. Cerrar correctamente
    el expediente es fundamental para una buena gestión de los recursos.

Copiar contenidos de un archivo a otro
En Python, puede copiar el contenido de un archivo a otro leyendo desde el archivo fuente y escribiendo en el archivo de destino. Aquí hay un fragmento de código de ejemplo que
    demuestra esto:
"""
# Open the source file for reading
with open('source.txt', 'r') as source_file:
    # Open the destination file for writing
    with open('destination.txt', 'w') as destination_file:
        # Read lines from the source file and copy them to the destination file
        for line in source_file:
            destination_file.write(line)
    # Destination file is automatically closed when the 'with' block exits
# Source file is automatically closed when the 'with' block exits
"""
Aquí hay una explicación del código:

Línea 2: Comenzamos abriendo el archivo fuente, source.txtpara lectura, rmodo, usando la with declaración y la open() función. Esto nos permite leer datos del archivo fuente.

Línea 4: Dentro del primer bloque with, abrimos el archivo de destino, destination.txt para escribir, wmodo, usando otra with declaración y la open() función. Esto prepara el
    archivo de destino para la escritura.

Línea 6: utilizamos un forbucle para recorrer cada línea del archivo fuente source_file. Este bucle lee cada línea del archivo fuente una por una.

Línea 7: dentro del bucle, utilizamos el write() método para escribir cada línea desde el archivo de origen al archivo de destino destination_file. Esto copia efectivamente el
    contenido del archivo de origen en el archivo de destino.

Líneas 8 y 9: después de copiar todas las líneas, tanto el archivo de origen como el de destino se cierran automáticamente cuando salen sus respectivos bloques. El cierre
    adecuado de archivos es crucial para gestionar los recursos de manera eficiente.

Modos de archivo en Python (sintaxis y casos de uso)
La siguiente tabla proporciona una descripción general de los diferentes modos de archivo, su sintaxis y casos de uso comunes. Comprender estos modos es esencial cuando se
    trabaja con archivos en Python para diversas tareas de manipulación de datos.

Modo	Sintaxis	Descripción
'r'	    'r'	        Modo de lectura. Abre un archivo existente para leer. Genera un error si el archivo no existe.
'w'	    'w'	        Modo de escritura. Crea un nuevo archivo para escribir. Sobrescribe el archivo si ya existe.
'a'	    'a'	        Modo anexar. Abre un archivo para agregar datos. Crea el archivo si no existe.
'X'	    'x'	        Modo de creación exclusivo. Crea un nuevo archivo para escribir pero genera un error si el archivo ya existe.
'rb'	'rb'	    Leer modo binario. Abre un archivo binario existente para leer.
'wb'	'wb'	    Escribe en modo binario. Crea un nuevo archivo binario para escribir.
'ab'	'ab'	    Agregar modo binario. Abre un archivo binario para agregar datos.
'xb'	'xb'	    Modo exclusivo de creación binaria. Crea un nuevo archivo binario para escribir pero genera un error si ya existe.
'rt'	'rt'	    Modo lectura de texto. Abre un archivo de texto existente para leer. (Predeterminado para archivos de texto)
'wt'	'wt'	    Modo de escritura de texto. Crea un nuevo archivo de texto para escribir. (Predeterminado para archivos de texto)
'at'	'at'	    Agregar modo texto. Abre un archivo de texto para agregar datos. (Predeterminado para archivos de texto)
'xt'	'xt'	    Modo exclusivo de creación de texto. Crea un nuevo archivo de texto para escribir pero genera un error si ya existe.
'r+'	'r+'	    Modo lectura y escritura. Abre un archivo existente para lectura y escritura.
'w+'	'w+'	    Modo escritura y lectura. Crea un nuevo archivo para lectura y escritura. Sobrescribe el archivo si ya existe.
'a+'	'a+'	    Modo anexar y leer. Abre un archivo para agregarlo y leerlo. Crea el archivo si no existe.
'x+'	'x+'	    Modo exclusivo de creación y lectura/escritura. Crea un nuevo archivo para lectura y escritura pero genera un error si ya existe.

Conclusión
Trabajar con archivos es un aspecto fundamental de la programación y Python proporciona herramientas poderosas para realizar diversas operaciones con archivos.
En este resumen, cubrimos conceptos clave y ejemplos de código relacionados con el manejo de archivos en Python, incluida la escritura, adición y copia de archivos.
"""
