# "Bienvenido al mapeo relacional de objetos u ORM. En este vídeo, explicaremos cómo ORM puede simplificar el desarrollo de aplicaciones con bases de datos. Después de ver este
#   vídeo, podrá para: Describir la diferencia entre el paradigma SQL y el paradigma de la programación orientada a objetos, o POO, por sus siglas en inglés. Explique los
#   conceptos básicos de ORM y enumere los pros y los contras de ORM.

# Los desarrolladores de software suelen utilizar una base de datos como el repositorio de datos principal de su aplicación, por lo que necesitan integrar SQL en su aplicación
#   código. Las sentencias SQL se deben ensamblar en la aplicación código y ejecución en el sistema de base de datos mediante las API de base de datos. Las filas de la base de
#   datos recuperadas se devuelven a código de aplicación como Cursor, una estructura de datos de control especial para iterar sobre las filas de una base de datos.

# Esta base de datos de cursos en línea contiene solo dos entidades, Course y Learner. La relación entre ellas es de Muchos a Muchos. Un curso puede tener muchos alumnos
#   inscritos y un alumno puede inscribirse en varios cursos. Esta relación persiste en una asociación tabla.

# Veamos un ejemplo de ejecución de SQL en Código Python. Primero, creamos una conexión a un embebido Base de datos SQLite. Esta es la base de datos de cursos en línea vacía.
#  A continuación, creamos un objeto Cursor a partir de la conexión contexto. Luego podemos enviar y ejecutar SQL.

# from sqlite3 import
import sqlite3

# Establecer conexión a la base de datos
conexion = sqlite3.connect("curso.db")
# Obtener un objeto cursor
cursor = conexion.cursor()

# Comenzamos con una instrucción Insert para crear e inserte un registro de alumno. Una vez que la instrucción Insert esté ensamblada, llamamos a Cursor para ejecutar métodos
#   para ejecutar el SQL.

insertar = "INSERT INTO data_lerner (Nombre, Apellido, dob, ocupacion) VALUES('Mallic', 'Tesla', '1990/12/12', 'Developer');"
cursor.execute (insertar)

# Por último, creamos otra instrucción SELECT para consultar el registro del alumno que acabamos de insertar y utilizamos Cursor-Fetch-One para recuperar el primera fila.

cursor.execute ("SELECT * FROM data_lerner")
leer = cursor.fetchone()
# El resultado muestra la fila de alumnos que acabamos de insertar.

# En el entorno de desarrollo de aplicaciones moderno, La programación orientada a objetos es la corriente principal y es muy diferente de SQL. A diferencia de SQL, que modela
#   entidades mediante tablas, filas y columnas, un lenguaje orientado a objetos modela las entidades mediante clases y objetos. En OOP, la entidad del curso se definiría como
#   una clase con dos atributos primitivos: nombre y descripción; y un atributo de referencia, la lista de alumnos.

# Los métodos para la manipulación de datos también necesitan definirse junto con los atributos de la clase. Aquí definimos un método simple: get Learners. La entidad de
#   aprendizaje también se definiría como clase con cuatro atributos: nombre, apellidos, fecha de nacimiento y ocupación. Un método simple de impresión de perfiles también sería
#   definido. Vamos a crear un objeto Learner a partir de una base de datos utilizando los paradigmas de SQL y OOP.

# Primero, ejecutamos una sentencia SQL select y obtenemos la primera fila de Learn. Para cargar los datos en el objeto de Learn, creamos un objeto llamando a su constructor
#   predeterminado. Luego actualizamos el objeto con los valores de los atributos consultado desde el cursor. Necesitamos asignar manualmente cada columna a cada atributo
#   primitivo de clase. Esto puede complicarse si tenemos complejos relaciones de datos. Por último, denominamos al método de impresión del perfil para imprimir el objeto.

# Hemos visto que los paradigmas de OOP y SQL modele los datos de manera diferente. OOP modela entidades utilizando clases, objetos, y atributos, mientras que SQL modela las
#   entidades mediante tablas, filas y columnas. Además, OOP modela las relaciones utilizando la clase patrones como la herencia, la asociación y la agregación, mientras que SQL
#   modela las relaciones utilizando JOIN y FOREIGN KEY.
# Por último, OOP ejecuta CRUD en los datos utilizando métodos, mientras que SQL ejecuta CRUD en los datos utilizando un lenguaje de manipulación de datos, como las sentencias
#   SQL insertar, eliminar y actualizar.

# Dado que generalmente creamos aplicaciones modernas usando OOP, ¿podemos acceder también a las bases de datos usando OOP en lugar de SQL? De esa manera, podemos ceñirnos a una
#   programación paradigma para nuestro desarrollo. La razón principal por la que la gente inventó la relación objeto-relacional el mapeo tenía como objetivo cerrar la brecha
#   entre la programación orientada a objetos y el SQL y hacer posible el uso de lenguajes de programación orientada a objetos para acceder a las bases de datos.

# Las bibliotecas o herramientas ORM pueden mapear y transferir datos almacenados en una base de datos relacional como filas en objetos u objetos en filas.

# Supongamos que hemos creado un modelo de objetos de aprendizaje por un desarrollador que usa OOP. ORM puede ayudar a transferir el objeto Learner a una fila de alumnos en una
#   tabla de alumnos y vuelve a leerla en un objeto de aprendizaje. Esto reduce la carga de trabajo de los desarrolladores porque solo necesitan centrarse en las operaciones de
#   los objetos.

# Así es como ORM puede transferir una unión de tres tablas Consulta SQL como una sola línea de código. Supongamos que queremos obtener todos los alumnos que están inscritos en
#   el curso de «Introducción a Python». En SQL, tendríamos que unirnos a Course, Learner, y sus tablas de búsqueda para obtener toda la información. También tendríamos que
#   mezclar tanto el OOP como Paradigmas de SQL. Pero con la ayuda de ORM, solo necesitamos primero llame al método get en la clase Course para buscar el curso por su nombre y,
#   a continuación, recupere todos sus alumnos.

# ¡HECHO! Ahora que has aprendido lo conveniente que es el ORM es decir, es posible que desee usarlo en su aplicación. Hay bibliotecas ORM para casi todos los populares idiomas.
# Para Python, puede usar Django Model y SQLAlchemy.

# Para Java, puede usar Hibernate y OpenJPA y para JavaScript, puede usar Sequelize y TypeORM. Estos son solo algunos ejemplos. En este curso, nos centraremos en el modelo de
#   Django. Como todas las bibliotecas de software de terceros, ORM tiene sus pros y sus contras.

# En el lado positivo: Con ORM, los diseños de tus clases definen las bases de datos. Para el desarrollo de aplicaciones de programación orientada a objetos, simplemente
#   necesita definir clases y crear objetos. Puede usar bases de datos sin escribir SQL. Además, puede utilizar una única interfaz ORM para administre varios sistemas de bases
#   de datos sin preocuparse por las diferencias en la sintaxis de SQL. Todos estos beneficios acelerarán su aplicación entrega.

# En el lado negativo: SQL y OOP siguen siendo dos lenguajes diferentes con conceptos de modelado diferentes, y ORM es posible que no pueda realizar el mapeo de los objetos en
#   las tablas de la base de datos. Además, dado que ORM combina la lógica de acceso a los datos con el código de la aplicación, cualquier cambio en la base de datos requerirá
#   cambios en ambas aplicaciones la lógica y la lógica de acceso a los datos. Como ORM oculta los detalles de la implementación, la depuración puede ser un desafío.
#   Por último, ORM puede reducir el rendimiento de la aplicación. ORM añade una capa de traducción adicional, pero no puede garantizar que las sentencias SQL traducidas estén
#   optimizadas.

# En este vídeo, aprendiste que: SQL y OOP modelan los datos de manera diferente.
# ORM cierra la brecha entre SQL y OOP.
# ORM permite a los desarrolladores de aplicaciones utilizar bases de datos sin escribir el código de Sequel.
# ORM puede acelerar el desarrollo de aplicaciones
# y las desventajas de ORM incluyen la imperfección mapeo, aumento del acoplamiento de código y dificultad para depurar."