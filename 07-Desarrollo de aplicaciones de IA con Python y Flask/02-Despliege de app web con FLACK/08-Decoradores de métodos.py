# Después de leer esta página, podrá:

#   Entender qué son los decoradores
#   Comprenda los dos tipos de decoradores que encontrará en una aplicación Python.
#   Cuándo y cómo utilizar los decoradores.
# que son los decoradores
# Los decoradores ayudan a anotar los métodos y dicen para qué sirve un método en particular. Estos son diferentes de los comentarios. El intérprete lo utiliza mientras ejecuta
#   el código.

# Decoradores de métodos
# Digamos que tenemos un código Python donde queremos que toda la salida esté en formato JSON. No tiene sentido incluir código para estos en cada uno de los métodos, ya que hace
#   que las líneas de código sean redundantes. En tales casos, podemos encargarnos de esto con un decorador.

def jsonify_decorator(function):
    def modifyOutput():
        return {"output":function()}
    return modifyOutput

@jsonify_decorator
def hello():
    return 'hello world'

@jsonify_decorator
def add():
    num1 = input("Enter a number - ")
    num2 = input("Enter another number - ")
    return int(num1)+int(num2)

print(hello())
print(add())

# El decorador de métodos también se conoce como contenedor, que envuelve la salida de la función que decora. En el ejemplo de código anterior, jsonify-decoratorse encuentra el
#   método decorador. Hemos agregado este decorador a hello()y add(). La salida de estas llamadas a métodos ahora se empaquetará y decorará con jsonify_decorator.

# El resultado de invocar el código Python anterior será:
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/decorated_output.png

# Como puede ver, la llamada al método se ha ajustado con el decorador. El codificador tiene libre albedrío para elegir el nombre del decorador. Aquí el nombre elegido es jsonify_decorator.

# -------------------------------------------------------------------------------------------
# Decoradores de ruta
# Es posible que haya observado que cuando visita cualquier dominio, tiene la raíz y luego tiene otros puntos finales a los que puede acceder. Vea los ejemplos a continuación.

# https://mydomain.com/

# https://mydomain.com/about

# https://mydomain.com/register

# Analizaremos la creación de estos puntos finales cuando creemos una aplicación web usando el módulo flask en los laboratorios siguientes.

# Pero para definir estos puntos finales en Python usamos lo que llamamos decoradores de rutas .
# https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0222EN-SkillsNetwork/labs/module_1/images/route_decorator.png

# @app.route(“/“) es un decorador de Python que Flask proporciona para asignar URL en nuestra aplicación a funciones fácilmente. Puede darse cuenta fácilmente de que el
#   decorador le está diciendo a nuestra @app que cada vez que un usuario visite el dominio de nuestra aplicación, en nuestro caso, ejecute la home()función.

# Podemos manejar múltiples rutas con una sola función simplemente apilando decoradores de ruta adicionales sobre el método que debe invocarse cuando se llama a la ruta. El
#   siguiente es un ejemplo válido de cómo servir el mismo mensaje "¡Hola mundo!" mensaje para 3 rutas separadas:

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return "Hello World!"

# Los decoradores de ruta también toman methodcomo segundo parámetro, que se puede configurar según el tipo de métodos HTTP que admitirá la ruta. Aprenderemos sobre esto en las
#   secciones posteriores.

# El decorador de ruta también puede ser más específico. Por ejemplo, para obtener los detalles de un usuario cuyo ID de usuario es U0001, puede ir a
# http://mydomain.com/userdetails/U0001. No tiene sentido definir una ruta diferente para cada usuario con el que esté tratando. En tales casos, definimos la ruta así.

@app.route("/userdetails/<userid>")
def getUserDetails(userid):
    return "User Details for  "+userid

# ¡Felicidades! Acabas de aprender sobre los decoradores en Python. Continúe y úselo en su código.


