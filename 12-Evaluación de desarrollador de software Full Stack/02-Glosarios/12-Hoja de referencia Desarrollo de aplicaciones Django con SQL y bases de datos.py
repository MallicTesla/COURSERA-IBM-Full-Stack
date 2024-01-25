# all()
# Recupera todas las instancias del modelo 'MyModel' de la base de datos.
MyModel.objects.all()


# AVG
# Calcula el valor promedio de una columna.
# SELECT AVG(column1) FROM table_name;


# Avg()
# Calcula el promedio de un campo.
MyModel.objects.aggregate(Avg('field'))


# Basic View Function
# Vista basada en funciones que devuelve "Hola, Mundo!"
from django.http import HttpResponse
def mi_vista(request):
    # Lógica de tu vista aquí
    return HttpResponse("¡Hola, Mundo!")


# Bootstrap classes and components
# Crea páginas web visualmente atractivas y receptivas sin tener que escribir estilos CSS manualmente.
# <a href="#" class="btn btn-primary">Haz clic</a>


# Bootstrap CSS	Enlace para incluir Bootstrap CSS en la plantilla base.
# Agrega el siguiente enlace a la sección <head> de tu plantilla base (generalmente base.html):
# <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">


# Bootstrap JavaScript
# Etiqueta de script para incluir la biblioteca de JavaScript de Bootstrap.
# Incluye la biblioteca de JavaScript de Bootstrap al final de la sección <body> para habilitar ciertas características (por ejemplo, menús desplegables, modales):
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.min.js"></script>


# Collecting static files
# Cuando implementas tu proyecto, necesitas recopilar todos los archivos estáticos en una ubicación única.
# python manage.py collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


# Configuration – App Dirs
# Una opción de configuración utilizada dentro de la configuración TEMPLATES. Cuando se establece en TRUE, Django buscará archivos de plantilla dentro de los directorios de la
    # aplicación.
# Asegúrate de que la configuración APP_DIRS esté establecida en True en la lista TEMPLATES. Esto permite que Django busque archivos estáticos dentro de los directorios de las
    # aplicaciones.
TEMPLATES = [
{
'APP_DIRS': True,
},
]


# Configuration – Installed apps
# Define una lista de todas las aplicaciones instaladas en el proyecto.
# Agrega 'django.contrib.staticfiles' a tus INSTALLED_APPS en settings.py:
INSTALLED_APPS = [
'django.contrib.staticfiles',
]


# Configuration – Static files
# Configuración de archivos estáticos en Django.
# En tu configuración de Django (settings.py), define las siguientes configuraciones:
STATIC_URL = 'https://prod-edx-edxapp-assets.edx-cdn.org/static/studio/edx.org-next/' # URL para acceder a archivos estáticos
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')] # Directorio para buscar archivos estáticos


# contains
# Verifica si el valor es una subcadena dentro del campo.
MyModel.objects.filter(field__contains="value")


# COUNT
# Cuenta el número de filas o valores no nulos en una columna.
# SELECT COUNT(*) FROM table_name; o SELECT COUNT(column1) FROM table_name;


# count()
# Cuenta el número de objetos.
MyModel.objects.count()


# CreateView
# Muestra un formulario para crear un nuevo objeto.
class MiCreateView(CreateView):
    model = MyModel
    template_name = 'mi_template.html'
    fields = '__all__' # o especifica una lista de campos


# DELETE FROM
# Elimina datos de una tabla según condiciones especificadas.
# DELETE FROM table_name WHERE condition;


# delete()
# Elimina un objeto.
obj.delete()


# DeleteVie
# Muestra una página de confirmación para eliminar un objeto.
class MiDeleteView(DeleteView):
    model = MyModel
    template_name = 'mi_template.html'
    success_url = '/success-url/'
    pk_url_kwarg = 'my_model_id' # predeterminado: pk


# DetailView
# Muestra detalles de un solo objeto.
class MiDetailView(DetailView):
    model = MyModel
    template_name = 'mi_template.html'
    context_object_name = 'object' # predeterminado: object
    pk_url_kwarg = 'my_model_id' # predeterminado: pk


# DISTINCT
# Devuelve valores únicos de una columna.
# SELECT DISTINCT column1 FROM table_name;


# django.db.models.Model
# Define un modelo.
from django.db import models
class MiModelo(models.Model):
    campo1 = models.CharField(max_length=100)
    campo2 = models.IntegerField()


# endswith
# Determina si una cadena termina con el sufijo especificado.
MyModel.objects.filter(field__endswith="value")


# exact
# Recupera instancias del modelo 'MyModel' de la base de datos donde el valor del atributo 'field' es exactamente igual a "value".
MyModel.objects.filter(field__exact="value")


# field
# Realiza una operación de filtrado en las instancias del modelo 'MyModel' según el valor del campo de un modelo relacionado.
MyModel.objects.filter(related_model__field="value")


# filter()
# Filtra objetos usando condiciones.
MyModel.objects.filter(field1="value")
MyModel.objects.filter(field2__gt=5)


# filter(ForeignKey)
# Realiza uniones condicionales.
MyModel.objects.filter(related_model__isnull=True)


# FROM
# Especifica la tabla desde la cual se recuperan los datos.
# SELECT column1, column2 FROM table_name;


# FULL JOIN
# Devuelve todas las filas de ambas tablas, independientemente de la coincidencia.
# SELECT column1, column2 FROM table1 FULL JOIN table2 ON table1.column = table2.column;


# get()
# Recupera una sola instancia del modelo 'MyModel' de la base de datos donde el valor de 'field1' es "value".
MyModel.objects.get(field1="value")


# GROUP BY
# Agrupa filas basadas en una columna especificada.
# SELECT column1, COUNT(*) FROM table_name GROUP BY column1;


# gt
# Verifica si el valor de 'field' es numéricamente mayor que 5.
MyModel.objects.filter(field__gt=5)


# Handle a Form Submission
# Vista basada en funciones para manejar la presentación de formularios.
from django.shortcuts import render
def mi_vista_formulario(request):
    if request.method == 'POST':
        ...# Procesa los datos del formulario aquí
    else:
        # Muestra el formulario
        return render(request, 'mi_formulario_template.html', context)


# Handle URL Parameters
# Vista basada en funciones que accede a los parámetros de la URL.
def mi_vista_parametros(request, param):
    ...# Accede al valor 'param' desde la URL


# HAVING
# Filtra datos agrupados según condiciones especificadas.
# SELECT column1, COUNT(*) FROM table_name GROUP BY column1 HAVING COUNT(*) > 1;


# iexact
# La búsqueda iexact no distingue entre mayúsculas y minúsculas, lo que significa que coincidirá con los valores sin importar si son mayúsculas o minúsculas y proporcionará una
    # coincidencia insensible a mayúsculas y minúsculas.
MyModel.objects.filter(field__iexact="value")


# in
# Verifica si el valor del campo está presente en la lista dada de valores.
MyModel.objects.filter(field__in=["value1", "value2"])


# INNER JOIN
# Devuelve solo las filas coincidentes de ambas tablas.
# SELECT column1, column2 FROM table1 INNER JOIN table2 ON table1.column = table2.column;


# INSERT INTO
# Inserta datos en una tabla.
# INSERT INTO table_name (column1, column2) VALUES (value1, value2);


# JOIN
# Combina filas de múltiples tablas según columnas relacionadas.
# SELECT column1, column2 FROM table1 JOIN table2 ON table1.column = table2.column;


# LEFT JOIN
# Devuelve todas las filas de la tabla izquierda y las filas coincidentes de la tabla derecha.
# SELECT column1, column2 FROM table1 LEFT JOIN table2 ON table1.column = table2.column;


# ListView:
# Muestra una lista de objetos.
class MiListView(ListView):
    model = MyModel
    template_name = 'mi_template.html'
    context_object_name = 'object_list' # predeterminado: object_list


# lt
# Verifica si el valor de 'field' es numéricamente menor que 10.
MyModel.objects.filter(field__lt=10)


# makemigrations/migrate
# Crea tablas de base de datos según modelos.
# python manage.py makemigrations

# python manage.py migrate


# many_to_many
# Realiza una unión de muchos a muchos.
obj.many_to_many_field.all()


# MAX
# Encuentra el valor máximo en una columna.
# SELECT MAX(column1) FROM table_name;


# Max()
# Proporciona el valor máximo de un campo.
MyModel.objects.aggregate(Max('field'))


# MIN
# Encuentra el valor mínimo en una columna.
# SELECT MIN(column1) FROM table_name;


# Min()
# Proporciona el valor mínimo de un campo.
MyModel.objects.aggregate(Min('field'))


# obj = MyModel(field1="value", field2=5)
# Crea una nueva instancia del modelo 'MyModel' con los valores "value" para 'field1' y 5 para 'field2', y luego guarda la instancia en la base de datos.
obj = MyModel(field1="value", field2=5)
obj.save()


# obj.save()
# Actualiza el valor de 'field1' para la instancia 'obj' a "new value" y guarda los cambios en la base de datos.
obj.field1 = "new value"
obj.save()


# obj.model_set.all()
# Recupera todos los objetos relacionados asociados con la instancia 'obj'. Accede a objetos relacionados en reversa (Clave externa).
obj.model_set.all()


# obj.related_model
# Recupera el modelo relacionado asociado con la instancia 'obj'. Accede a objetos relacionados (Clave externa o OneToOneField).
obj.related_model


# ORDER BY
# Ordena el conjunto de resultados según columnas especificadas en orden ascendente o descendente.
# SELECT column1, column2 FROM table_name ORDER BY column1 ASC;


# order_by()
# Ordena objetos basados en un campo.
MyModel.objects.order_by('field')


# order_by(-)
# Ordena objetos basados en campos en orden descendente.
MyModel.objects.order_by('-field')


# prefetch_related
# Realiza una unión externa izquierda.
MyModel.objects.prefetch_related('related_model')


# Protecting Views (Restrict Access) using @login_required Decorator
# Vista basada en funciones protegida con el decorador login_required.
from django.contrib.auth.decorators import login_required
@login_required
def mi_vista_protegida(request):
    ...# Lógica de tu vista aquí


# Redirect to a URL
# Vista basada en funciones para redirigir a una URL específica.
from django.shortcuts import redirect
def mi_vista_redireccion(request):
    return redirect('nombre_url_o_ruta')


# Render a Template
# Vista basada en funciones para renderizar una plantilla con contexto.
from django.shortcuts import render
def mi_vista_plantilla(request):
    contexto = {'variable': valor}
    return render(request, 'mi_plantilla.html', contexto)


# RIGHT JOIN
# Devuelve todas las filas de la tabla derecha y las filas coincidentes de la tabla izquierda.
# SELECT column1, column2 FROM table1 RIGHT JOIN table2 ON table1.column = table2.column;


# SELECT
# Recupera datos de una o más tablas según columnas especificadas.
# SELECT column1, column2 FROM table_name;


# select_related
# Realiza una unión interna.
MyModel.objects.select_related('related_model')


# startswith
# Determina si una cadena comienza con los caracteres de una cadena especificada.
MyModel.objects.filter(field__startswith="value")


# SUM
# Calcula la suma de los valores en una columna.
# SELECT SUM(column1) FROM table_name;


# Sum()
# Proporciona la suma de un campo.
MyModel.objects.aggregate(Sum('field'))


# UPDATE
# Modifica datos en una tabla según condiciones especificadas.
# UPDATE table_name SET column1 = value1 WHERE condition;


# UpdateView
# Muestra un formulario para actualizar un objeto existente.
class MiVistaActualizar(UpdateView):
    model = MyModel
    template_name = 'mi_template.html'
    fields = '__all__' # o especifica una lista de campos
    pk_url_kwarg = 'my_model_id' # predeterminado: pk


# Usage – Static content
# Código para estilizar las plantillas HTML y proporcionar interactividad a las páginas web.
# <link href="{% static 'tu_aplicacion/css/style.css' %}" rel="stylesheet">
# <script src="{% static 'tu_aplicacion/js/script.js' %}"></script>
# <img src="{% static 'tu_aplicacion/img/logo.png' %}" alt="Logo">


# WHERE
# Filtra datos según condiciones especificadas.
# SELECT column1, column2 FROM table_name WHERE condition;