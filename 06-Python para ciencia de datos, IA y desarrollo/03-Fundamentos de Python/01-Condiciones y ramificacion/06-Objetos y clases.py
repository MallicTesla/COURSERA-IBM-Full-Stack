"""
Laboratorio de clases y objetos de Python
Tiempo estimado necesario: 10 minutos

Objetivo:
Al final de esta lectura, debería poder:

Aprenda los conceptos fundamentales de los objetos y clases de Python.
Comprender la estructura de clases y el código objeto.
Comprender el concepto con ejemplos del mundo real
Introducción a clases y objetos.
Python es un lenguaje de programación orientada a objetos (OOP), lo que significa que utiliza un paradigma centrado en objetos y clases. A continuación te explicamos estos
    conceptos fundamentales:

Clases:
Una clase es un modelo o plantilla para crear objetos. Define la estructura y comportamiento que tendrán sus objetos.

Piense en una clase como un cortador de galletas y en los objetos como las galletas cortadas de esa plantilla.

En Python, las clases se crean usando la classpalabra clave.

Creando clases:
Cuando creas una clase, especificas los attributes(datos) y methods(funciones) que tendrán los objetos de esa clase.
Attributesse definen como variables dentro de la clase y methodsse definen como funciones.
Por ejemplo, puedes diseñar una clase "Coche" con atributos como "color" y "velocidad", junto con métodos como "acelerar".

Objetos:
Un objeto es una unidad fundamental en Python que representa una entidad o concepto del mundo real.
Los objetos pueden ser tangibles (como un automóvil) o abstractos (como la calificación de un estudiante).

Cada objeto tiene dos características principales:

Estado:
Los atributos o datos que describen el objeto. Para nuestro objeto "Coche", esto podría incluir atributos como "color", "velocidad" y "nivel de combustible".

Comportamiento:
Las acciones o métodos que el objeto puede realizar. En Python, los métodos son funciones que pertenecen a objetos y pueden cambiar el estado del objeto o realizar operaciones
    específicas.

Creación de instancias de objetos:
Una vez que haya definido una clase, puede crear objetos individuales (instancias) basados ​​en esa clase.
Cada objeto es independiente y tiene su propio conjunto de atributos y métodos.
Para crear un objeto, usa el nombre de la clase seguido de paréntesis, por lo tanto: "my_car = Car()"
Interactuar con objetos:
Interactúa con objetos llamando a sus métodos o accediendo a sus atributos mediante notación de puntos.

Por ejemplo, si tienes un objeto Car llamado my_car , puedes establecer su color con my_car.color = "blue" y acelerarlo con my_car.accelerate() si hay un método de aceleración
    definido en la clase.

Estructura de clases y código objeto.
No copie ni utilice directamente este código, ya que está pensado como una plantilla para explicación y no está diseñado para resultados específicos.

Declaración de clase (clase ClassName):
La palabra clave class se utiliza para declarar una clase en Python.
ClassName es el nombre de la clase, normalmente siguiendo las convenciones de nomenclatura de CamelCase.
"""
class ClassName:
    pass
"""
Atributos de clase (class_attribute = valor):
Los atributos de clase son variables que se comparten entre todas las instancias (objetos) de la clase.
Se definen dentro de la clase pero fuera de cualquier método.
"""
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
"""
Método constructor (def init (self, atributo1, atributo2,…):):
El __init__método es un método especial conocido como constructor.
Inicializa los atributos de instancia (también llamados variables de instancia) cuando se crea un objeto.
El selfparámetro es el primer parámetro del constructor y hace referencia a la instancia que se está creando.
atributo1 , atributo2 , etc. son parámetros que se pasan al constructor al crear un objeto.
Dentro del constructor, self.attribute1, self.attribute2etc. se utilizan para asignar valores a los atributos de la instancia.
"""
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ):
        pass
        # ...
"""
Atributos de instancia (self.attribute1 = atributo1):
Los atributos de instancia son variables que almacenan datos específicos de cada instancia de la clase.
Se inicializan dentro del método init utilizando la palabra clave self seguida del nombre del atributo.
Estos atributos contienen datos únicos para cada objeto creado a partir de la clase.
"""
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2,):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...
"""
Métodos de instancia (def método1(self, parámetro1, parámetro2,…):):
Los métodos de instancia son funciones definidas dentro de la clase.
Operan con los datos de la instancia (atributos de la instancia) y pueden realizar acciones específicas de las instancias.
El parámetro self es necesario en los métodos de instancia, lo que les permite acceder a los atributos de la instancia y llamar a otros métodos dentro de la clase.
"""
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2,):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...
    # Instance methods (functions)
    def method1(self, parameter1, parameter2, ):
        # Method logic
        pass
    
"""
Siguiendo los mismos pasos, puede definir varios métodos de instancia.

"""
class ClassName:
    # Class attributes (shared by all instances)
    class_attribute = value
    # Constructor method (initialize instance attributes)
    def __init__(self, attribute1, attribute2, ):
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        # ...
    # Instance methods (functions)
    def method1(self, parameter1, parameter2, ):
        # Method logic
        pass
    def method2(self, parameter1, parameter2, ):
        # Method logic
        pass
"""
Nota: – Ahora hemos creado con éxito una clase ficticia.

Creación de objetos (instancias):
Para crear objetos (instancias) de la clase, se llama a la clase como una función y se proporcionan los argumentos requeridos por el constructor.
Cada objeto es una instancia distinta de la clase, con su propio conjunto de atributos de instancia y la capacidad de llamar a métodos definidos en la clase.
"""
# Create objects (instances) of the class
object1 = ClassName(arg1, arg2, ...)
object2 = ClassName(arg1, arg2, ...)
"""
Llamar a métodos en objetos:
En esta sección llamaremos métodos sobre objetos, específicamente object1y object2.
Los métodos método1 y método2 están definidos en la clase ClassName y los llamas en objeto1 y objeto2 respectivamente.
Pasa los valores param1_value y param2_value como argumentos a estos métodos. Estos argumentos se utilizan dentro de la lógica del método.
Método 1: usar notación de puntos:
Esta es la forma más sencilla de llamar al método de un objeto. En esto usamos la notación de puntos (object.method()) para invocar directamente el método en el objeto.
Por ejemplo, result1 = object1.method1(param1_value, param2_value, ...)llama al método1 en el objeto1.
"""
# Calling methods on objects
# Method 1: Using dot notation
result1 = object1.method1(param1_value, param2_value, ...)
result2 = object2.method2(param1_value, param2_value, ...)
"""
Método 2: Asignar métodos de objeto a variables:
Aquí hay una forma alternativa de llamar al método de un objeto asignando la referencia del método a una variable.
method_reference = object1.method1asigna el método método1 del objeto1 a la variable referencia_método .
Luego, llamamos al método usando la variable de esta manera: resultado3 = referencia_método(valor_param1, valor_param2,…) .
"""
# Method 2: Assigning object methods to variables
method_reference = object1.method1  # Assign the method to a variable
result3 = method_reference(param1_value, param2_value, ...)
"""
Accediendo a los atributos del objeto:
Aquí accedemos al atributo de un objeto mediante notación de puntos.
attribute_value = object1.attribute1recupera el valor del atributo atributo1 del objeto1 y lo asigna a la variable valor_atributo .
"""
# Accessing object attributes
attribute_value = object1.attribute1  # Access the attribute using dot notation
"""
Modificar atributos de objeto:
Estamos modificando el atributo de un objeto usando notación de puntos.
object1.attribute2 = new_valueestablece el atributo atributo2 del objeto1 en el nuevo valor nuevo_valor .
"""
# Modifying object attributes
object1.attribute2 = new_value  # Change the value of an attribute using dot notation
"""
Accediendo a los atributos de clase (compartidos por todas las instancias):
Finalmente, accedemos a un atributo de clase, que es compartido por todas las instancias de la clase.
class_attr_value = ClassName.class_attributeaccede al atributo de clase class_attributedesde ClassName classy asigna su valor a la variable
class_attr_value.
"""
# Accessing class attributes (shared by all instances)
class_attr_value = ClassName.class_attribute
"""
Ejemplo del mundo real
Escribamos un programa en Python que simule una clase de automóvil simple, permitiéndole crear instancias de automóviles, acelerarlas y mostrar sus velocidades actuales.

Comencemos definiendo una clase Car que incluya los siguientes atributos y métodos:
Atributo de clase max_speed, que se establece en 120 km/h .

Método de construcción __init__que toma parámetros para la marca, modelo, color y una velocidad opcional del automóvil (por defecto 0) . Este método inicializa los atributos de
    instancia para marca, modelo, color y velocidad.

Método accelerate(self, acceleration)que permite acelerar el coche. Si la aceleración no excede el max_speed, actualice el atributo de velocidad del automóvil . De lo contrario,
    establezca la velocidad en max_speed .

Método get_speed(self)que devuelve la velocidad actual del coche.

"""
class Car:
    # Class attribute (shared by all instances)
    max_speed = 120  # Maximum speed in km/h
    # Constructor method (initialize instance attributes)
    def __init__(self, make, model, color, speed=0):
        self.make = make
        self.model = model
        self.color = color
        self.speed = speed  # Initial speed is set to 0
    # Method for accelerating the car
    def accelerate(self, acceleration):
        if self.speed + acceleration <= Car.max_speed:
            self.speed += acceleration
        else:
            self.speed = Car.max_speed
    # Method to get the current speed of the car
    def get_speed(self):
        return self.speed
"""
Ahora, instanciaremos dos objetos de la clase Car, cada uno con las siguientes características:
auto1: Marca = "Toyota", Modelo = "Camry", Color = "Azul"

auto2: Marca = "Honda", Modelo = "Civic", Color = "Rojo"

"""
# Create objects (instances) of the Car class
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")
"""
Utilizando el acceleratemétodo, aumentaremos la velocidad del coche1 en 30 km/h y la del coche2 en 20 km/h.
"""
# Accelerate the cars
car1.accelerate(30)
car2.accelerate(20)
"""
Por último, mostraremos la velocidad actual de cada automóvil utilizando el método `get_speed.
"""
# Print the current speeds of the cars
print(f"{car1.make} {car1.model} is currently at {car1.get_speed()} km/h.")
print(f"{car2.make} {car2.model} is currently at {car2.get_speed()} km/h.")
"""
Próximos pasos
En conclusión, esta lectura proporciona una comprensión fundamental de los objetos y clases en Python, conceptos esenciales en la programación orientada a objetos. Las clases
    sirven como modelos para crear objetos, encapsulando tanto atributos de datos como métodos. Los objetos representan entidades del mundo real y poseen su propio estado y
    comportamiento únicos. El ejemplo de código estructurado presentado en la lectura describe los elementos clave de una clase, incluidos los atributos de clase, el método
    constructor para inicializar los atributos de instancia y los métodos de instancia para definir la funcionalidad específica del objeto.

Puede aplicar los conceptos de objetos y clases en la próxima sesión de laboratorio para adquirir experiencia práctica.
"""