# Descripción general
# Crear, Leer, Actualizar y Eliminar (CRUD) son funciones básicas que debe realizar cualquier aplicación con una base de datos. Para implementar eficazmente las operaciones CRUD,
#   necesitará administrar diferentes métodos HTTP, como solicitudes GETy POST. Una GETsolicitud se usa generalmente para recuperar o leer datos y, a menudo, se usa para mostrar
#   un formulario. Una POSTsolicitud se utiliza comúnmente para enviar datos para crear o actualizar datos. Un ejemplo de una solicitud POST es el envío de formulario.

# Esta lectura tiene como objetivo presentarle características adicionales de Flask, centrándose en las funciones CRUD. También aprenderá cómo se interrelacionan estas funciones
#   y cómo utilizan los diferentes archivos HTML, rutas dinámicas y varios métodos HTTP.

# Objetivos
# En esta lectura, usted:

# Acceda a los datos del formulario para capturar las entradas del usuario con flask.request.formlas POSTsolicitudes
# redirectControlar la navegación del usuario: usando la función Flask
# Genere URL dinámicamente utilizando url_forpara crear URL adaptables en su aplicación Flask
# Administre diferentes tipos de solicitudes HTTP para diseñar rutas flexibles que respondan a varios tipos de solicitudes HTTP
# Implementar operaciones CRUD para la gestión de datos en una aplicación Flask
# Nota: Cada sección incluye ejemplos de código relevantes y explicaciones para mejorar su comprensión de las características cruciales de Flask.

# Accediendo a los datos del formulario con flask.request.form
# Puede utilizarlo flask.request.formpara acceder a los datos del formulario que un usuario ha enviado a través de una POSTsolicitud. Por ejemplo, esta función se puede utilizar
#   si tiene un formulario de inicio de sesión con campos de nombre de usuario y contraseña.

# En su archivo HTML, es posible que tenga un formulario como este:

"""
HTML
<form method="POST" action="/login">
    <input type="text" name="username">
    <input type="password" name="password">
    <input type="submit" value="Submit">
</form>
"""

# El código Python para acceder al usuario y contraseña será el siguiente:


from flask import request
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    # process login here

# Redirigir a una URL con flask.redirect
# Flask proporciona una función llamada flask.redirect para guiar a los usuarios a diferentes páginas web (o puntos finales). La función flask.redirect puede resultar útil en
#   varios escenarios. Por ejemplo, puede utilizar la función flask.redirect para redirigir a un usuario a una página de inicio de sesión cuando intenta acceder a una página de
#   administración restringida.

# Código Python:

from flask import redirect
@app.route('/admin')
def admin():
    return redirect('/login')

# Generando URL dinámicas con flask.url_for
# La flask.url_forfunción genera dinámicamente URL para un punto final determinado. La generación dinámica de URL puede resultar especialmente útil cuando se modifica la URL de
#   una ruta. La flask.url_forfunción actualiza automáticamente la URL en todas sus plantillas o código, minimizando el trabajo manual. Por ejemplo, considere el escenario en el
#   que un usuario intenta acceder a la página de administración y debe ser redirigido a la página de inicio de sesión . En este escenario, url_for('login')recuperará la URL de
#   la página de inicio de sesión de las rutas existentes.

from flask import url_for
@app.route('/admin')
def admin():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "<Login Page>"

# Manejo de diferentes tipos de solicitudes HTTP
# Flask le permite definir rutas para gestionar diferentes tipos de solicitudes HTTP. Puede definir la ruta con ambos métodos de acceso, GET y POST, y en la descripción de la
#   función, definir los casos de uso para ambos métodos.

@app.route('/data', methods=['GET', 'POST'])
def data():
    if request.method == 'POST':
        # process POST request
        ...
    if request.method == 'GET':
        # process GET request
        ...

# En el archivo HTML, agregará un formulario que permita GETy POSTsolicite:
"""
<!-- For POST -->
<form method="POST" action="/data">
    <!-- Your input fields here -->
    <input type="submit" value="Submit">
</form>
<!-- For GET -->
<a href="/data">Fetch data</a>
"""
# En el último ejemplo, la /dataruta acepta solicitudes GETy POST. El tipo de solicitud se puede verificar usando flask.request.method.

# operaciones CRUD
# Las operaciones CRUD representan las cuatro funciones básicas que necesita para interactuar con cualquier almacenamiento persistente, como una base de datos. En el desarrollo
#   web, las operaciones CRUD suelen corresponder a métodos HTTP.

# Crear operación
# La creación de datos a menudo implica presentar un formulario al usuario para recopilar la información que desea almacenar en la base de datos como un nuevo registro. En Flask,
#   se accede a estos datos mediante flask.request.form.

# Formulario HTML para crear datos:

"""
<form method="POST" action="/create">
    <input type="text" name="name">
    <input type="submit" value="Create">
</form>
"""

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Create a new record with the name
        record = create_new_record(name)  # Assuming you have this function defined
        # Redirect user to the new record
        return redirect(url_for('read', id=record.id))
    # Render the form for GET request
    return render_template('create.html')

# Leer operación
# Leer datos implica acceder a los datos y presentarlos al usuario. Para acceder a entradas específicas, la solicitud debe ir con ID específicos. Por lo tanto, deberá pasar el
#   ID como argumento a la función. El siguiente ejemplo muestra que se puede acceder al ID desde la ruta.

@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    # Get the record by id
    record = get_record(id)  # Assuming you have this function defined
    # Render a template with the record
    return render_template('read.html', record=record)

# Operación de actualización
# La actualización de datos requiere el proceso de acceder a entradas específicas, como la operación Leer , e implica proporcionar nuevos datos al parámetro en cuestión, como la
#   operación Crear . Por lo tanto, la ruta debe acceder al ID y contener ambos métodos de acceso.

# Formulario HTML de muestra para actualizar datos:
"""
<form method="POST" action="/update/{{record.id}}">
    <input type="text" name="name" value="{{record.name}}">
    <input type="submit" value="Update">
</form>
"""

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        # Access form data
        name = request.form['name']
        # Update the record with the new name
        update_record(id, name)  # Assuming you have this function defined
        # Redirect user to the updated record
        return redirect(url_for('read', id=id))
    
    # Render the form for GET request with current data
    record = get_record(id)  # Assuming you have this function defined
    return render_template('update.html', record=record)

# Eliminar operación
# Eliminar datos implica eliminar un registro según su ID. La operación Eliminar normalmente requerirá que se pase el ID, según lo informado por la página HTML, en forma de
#   argumento para la función.

# Formulario HTML de muestra para eliminar datos:
"""
<form method="POST" action="/delete/{{record.id}}">
    <input type="submit" value="Delete">
</form>
"""

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    # Delete the record
    delete_record(id)  # Assuming you have this function defined
    # Redirect user to the homepage
    return redirect(url_for('home'))