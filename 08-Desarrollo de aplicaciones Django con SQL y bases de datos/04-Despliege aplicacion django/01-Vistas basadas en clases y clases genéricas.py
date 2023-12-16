"""Bienvenido a las vistas basadas en clases de Django. Después de ver este vídeo, podrás: Crear vistas basadas en clases y vistas genéricas basadas en clases, y Compare los pros
    y los contras de las vistas basadas en funciones y las vistas basadas en clases.

La vista basada en funciones fue la implementación original de la vista en Django. Fue creada para resolver un problema específico con un parámetro de solicitud y una lógica
    explícita sobre cómo generar una respuesta. La vista basada en clases se agregó a Django para mejorar la extensibilidad y la reutilización de puntos de vista. Si una vista
    se ha creado utilizando funciones basadas en funciones vistas o vistas basadas en clases, una vista es esencialmente una función o invocable de Python. El principal problema
    de la vista basada en funciones es que normalmente es muy difícil de ampliar o personalizar.

Para abordar estos problemas, se creó la vista basada en clases. Veamos cómo crear una basada en clases vista para devolver una respuesta HTTP. En lugar de crear una función,
    defina una clase que subclasifica la clase base de Django View. A continuación, puede acceder a algunos métodos comunes resumidos mediante la clase base de View, como Get o
    Post, para gestionar una solicitud HTTP Get o Post.
A continuación, implementa tu propia lógica para gestionar las solicitudes http. Por ejemplo, para gestionar el método HTTP Get desde una URL, implementamos un método Get
    sencillo consultando primero el registro del curso en la base de datos e insertando el nombre del curso en un plantilla html y rellenando HttpResponse.
También necesitamos asignar un patrón de URL a un patrón basado en clases ver clase. Esto es como configurar la URL para la vista basada en funciones. La única diferencia es que
    para el argumento view necesitas especificar la función as_view o la clase CourseView que definimos. La función as_view se hereda de la clase base de View. La clase Django
    View es la clase base para todas las vistas basadas en clases. La clase Django View define un método as_view, que también define un método inner_view y se devolverá como
    invocable. Entonces, cuando los agregamos a la URLconf usando el método de la clase view.as_view, devuelve una función. Tras ser llamada, la vista invocable pasa la
    solicitud al método de envío, que ejecutará el método http en consecuencia, como GET o POST.

Por lo tanto, incluso una vista basada en clases es esencialmente una función para manejar un determinado método http. Por lo tanto, tanto las vistas basadas en funciones como
    las basadas en clases son funciones. En el desarrollo de aplicaciones web, necesitamos realizar tareas comunes, como mostrar una lista o mostrar los detalles de un objeto de
    forma desglosada.

Para acelerar el desarrollo y resolver los problemas comunes Django proporciona algunas clases de vista integradas llamadas vistas genéricas para desarrolladores para reutilizar
    y ampliar con cambios mínimos en el código.

Veamos un ejemplo de una clase genérica basada en vista para mostrar los detalles de un curso como lo hemos hecho antes. En primer lugar, necesitamos definir un CourseView que
    amplíe el DetailView genérico.
Luego especificamos el modelo como Course y proporcionamos una ruta de archivo de plantilla html. Los métodos proporcionados por DetailView saben cómo obtener el objeto y
    rellenar la página html. Por lo tanto, los desarrolladores solo necesitan escribir dos líneas de código para mostrar un objeto del curso en un navegador basado en una
    plantilla html, sin escribir ningún código para gestionar la solicitud http."""

from django.views import generic
from .models import Mi_modelo

# aca realisa los metodos de forma automatica
class Mi_modelo_Views (generic.DetailView):
    # coloca el modelo
    model = Mi_modelo
    # la ruta el html
    template_name = "ruta al html"

"""
Veamos algunos ejemplos de vistas genéricas basadas en clases.
ListView representa una lista de objetos.
DetailView representa los detalles de un objeto.
FormView representa un formulario y un grupo de vistas de fecha gestiona los datos basados en fechas.

Hasta ahora, has aprendido sobre las vistas basadas en funciones, basadas en clases y genéricas basadas en clases. Vamos a resumir los pros y los contras para ayudarte a decidir
    cuál usar en tu aplicación.

En el caso de la vista basada en funciones, las principales ventajas son que es fácil escribir código y es fácil para entender. Puedes escribir tu lógica de forma explícita sin
    seguir ninguna estructura adicional o diseños como los métodos definidos en la clase base de View. Si tiene una función muy específica que no es probable que se vuelva a
    utilizar, la basada en funciones la vista podría ser tu elección.
Las principales desventajas son las vistas basadas en funciones son difíciles de ampliar o reutilizar. Y manejan los métodos de solicitud http usando condiciones declaraciones,
    lo que puede aumentar la complejidad del código.

En el caso de las vistas basadas en clases, las ventajas incluyen la reutilización y extensibilidad. Además, puede gestionar las solicitudes mediante la clase métodos. Y puede
    aprovechar las vistas genéricas basadas en clases para resolver tareas comunes.
Las principales desventajas de las vistas basadas en clases son la adición de la herencia adicional de la clase base de View dificulta la lectura del código. El código implícito
    está oculto y los desarrolladores deben comprobar la fuente código para entender exactamente cómo se implementan las vistas.

En este vídeo, aprendiste:
Cómo implementar vistas basadas en clases.
Cómo usar las vistas de clase genéricas integradas en Django para resolver tareas comunes y los pros y los contras de las vistas basadas en funciones y en clases."
"""