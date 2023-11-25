// "Bienvenido a Routing, Middleware and Templating. Después de ver este vídeo, podrá: Explicar el enrutamiento en Express. Describa el middleware y cómo se usa. Y explique la
//     representación de plantillas en Express.

// El enrutamiento es un aspecto importante de las secuencias de comandos del lado del servidor. El servidor debe gestionar las solicitudes a diferentes rutas al mismo servidor.
// Las solicitudes pueden ser GET, POST, PUT o DELETE. El servidor debe gestionar cada solicitud a cada una de las rutas o devolver los mensajes de error correspondientes.
// El enrutamiento se puede gestionar a nivel de aplicación o a nivel de router.


// En este caso, está gestionando cada método en cada ruta con métodos independientes a nivel de aplicación. Esto resulta sencillo cuando hay menos puntos finales o rutas.
const express = require("express");
const app = new express();

app.get ("user/about/:id", (req, res) => {
    res.send("Response about user "+ req.params.id)
})
// Esta aplicación. Get gestiona las consultas GET al punto final /user/about/id.
app.post ("user/about/:id", (req, res) => {
    res.send("Response about user "+ req.params.id)
})
// Esta aplicación Post gestiona las consultas POST al mismo punto final.
app.get ("item/about/:id", (req, res) => {
    res.send("Response about item "+ req.params.id)
})
// Esta aplicación. Get gestiona las consultas GET al punto final /item/about/id.
app.post ("item/about/:id", (req, res) => {
    res.send("Response about item "+ req.params.id)
})
// Y esta aplicación. Post también gestiona las consultas POST al punto final /item/about/id.

// Cuando hay muchas rutas que gestionar, el mantenimiento del código es mejor con los enrutadores. Se utiliza un router por sí solo para ramificar el manejo de consultas y
//  enrutar cada consulta de manera diferente.


const express = require("express");
const app1 = new express();

let UserRouter = express.Router()
let ItemRouter = express.Router()
// Aquí, está definiendo dos enrutadores. Uno es para un elemento y el otro es para un usuario. 
app1.user ("/user", UserRouter)
app1.user ("/item", ItemRouter)
// Todas las solicitudes que vienen con el artículo son gestionadas por el ItemRouter. 

UserRouter.get ("/about/:id", (req, res) => {
    res.send("Response about user "+ req.params.id)
})
UserRouter.get ("details/:id", (req, res) => {
    res.send("Details about user "+ req.params.id)
})

ItemRouter.get ("/about/:id", (req, res) => {
    res.send("Details about item "+ req.params.id)
})

ItemRouter.get ("details/:id", (req, res) => {
    res.send("Details about item "+ req.params.id)
})
// Se gestionan las rutas /item/about y /item/detail.
// UserRouter gestiona todas las solicitudes que vienen con /user. Aquí se gestionan las rutas /user/about y /user/detail.

app1.listen (8080, () =>{
    console.log ("Listening at http://localhost:8080")
})
// Según el localizador uniforme de recursos (URL), la respuesta cambia.

// El middleware incluye funciones que tienen acceso a los objetos de solicitud y respuesta y a la siguiente función. El siguiente parámetro determina qué se hace después de
//  ejecutar la función. Una aplicación Express puede tener más de un middleware y pueden estar encadenados entre sí. El middleware se clasifica según su propósito, uso y fuente.

// Hay cinco tipos de middleware: a nivel de aplicación, a nivel de router, de gestión de errores, integrado y de terceros. El middleware es útil para actividades como analizar
//  solicitudes, añadir autenticaciones y gestionar errores.

// El middleware a nivel de aplicación está vinculado a la aplicación mediante app.use. Todas las solicitudes de los clientes a esta aplicación de servidor se enrutan a través de
//  este middleware. Este enrutamiento es útil para actividades como la autenticación y la verificación de la información de la sesión.

const express = require("express");
const app2 = new express();

app2.use(function (req, res, next){
    if (req.query.password !== "pwd123") {
        return res.status (402).send ("The user cannot login");
    }
    
    console.log ("Time", Date.now())
    next()
})
// Aquí, está definiendo un middleware que comprobará la contraseña que se pase. Si la contraseña es igual a pwd123, registrará la hora y pasará a la siguiente acción lógica que
//  sea procesar la solicitud. Si no es así, el estado de la respuesta se establecerá en 402 y aparecerá un mensaje que indica que el usuario no puede iniciar sesión.

app2.get ("/", (rqe, res) => {
    return res.send("Funciono");
});

app2.listen (8080, () =>{
    console.log ("Listening at http://localhost:8080")
})

// Considere el middleware a nivel de aplicación como un guardián. Ninguna solicitud al servidor de aplicaciones puede superarlo. El middleware a nivel de router no está
//  vinculado a la aplicación. En su lugar, está enlazado a una instancia de Express.router (). Puede usar un middleware específico para una ruta específica en lugar de que
//  todas las solicitudes pasen por el mismo middleware.

// En este caso, si la ruta es /user, quiere que la solicitud pase por el router del usuario y si la ruta es /item, quiere que pase por el router del elemento. Defina los dos
//  enrutadores, defina la función de middleware que utilizarán los enrutadores y lo que sucederá después y, a continuación, vincule las rutas de la aplicación a cada enrutador.
// La respuesta variará según la ruta de solicitud del lado del cliente. El middleware de gestión de errores puede estar vinculado a toda la aplicación o a enrutadores
//  específicos.

// El middleware para la gestión de errores siempre utiliza cuatro argumentos: error, solicitud, respuesta y la siguiente función a la que debe estar encadenado. Aunque no
//  utilices el siguiente parámetro, tendrás que definirlo en la firma del método.

// Este es un ejemplo de middleware de gestión de errores a nivel de aplicación. Si se accede al identificador de usuario 1, aparece un error que indica que es el usuario
//  administrador. Este error lo gestiona el middleware, que devuelve una respuesta con un código de estado 500. Para todos los demás usuarios, la solicitud se procesa sin
//  problemas y se muestra un mensaje de saludo con el seudónimo.

// El middleware integrado se puede vincular a toda la aplicación o a enrutadores específicos. El middleware integrado resulta útil para actividades como renderizar páginas en
//  lenguaje de marcado de hipertexto (HTML) desde el servidor, analizar las entradas de notación de objetos de JavaScript (JSON) desde la interfaz y analizar las cookies

// Este es un ejemplo de middleware estático que se utiliza para renderizar páginas HTML estáticas y las imágenes desde el servidor. Aquí, a nivel de aplicación, está definiendo
//  que los archivos estáticos se pueden renderizar desde el directorio cad220_staticfiles. A la derecha, verá el HTML que se está renderizando desde ese directorio. Observe que
//  la URL solo tiene la dirección del servidor y el número de puerto seguidos del nombre del archivo.

// También puede definir su propio middleware o utilizar un middleware de terceros, que puede estar disponible a través de npm install. Como Node.js es de código abierto, hay
//  muchos disponibles para instalar y usar. Crear middleware es sencillo. Es una función que toma tres parámetros, que son solicitud, respuesta y siguiente. Puede definir un
//  método que tome estos tres parámetros y, a continuación, vincularlo a app.use o router.use.

// El orden en el que se encadena el middleware depende del orden en que se utilice el método.use para enlazarlos. En este caso, está creando un middleware denominado MyLogger y
//  haciendo que la aplicación lo utilice. El resultado renderizado incluye la hora en que se recibe la solicitud.
// La representación de plantillas es la capacidad del servidor para rellenar el contenido dinámico de la plantilla HTML.

// En este ejemplo, se usa express-react-views, que renderiza los componentes de React desde el servidor. Estableces la propiedad del motor de visualización, que es responsable
//  de crear HTML a partir de tus vistas.

// Las vistas son código JSX. Las vistas se encuentran en un directorio llamado myviews. El motor de visualización buscará un archivo JSX llamado index en el directorio myviews
//  y le pasará el nombre de la propiedad. La salida renderizada tendrá el nombre del usuario. En este ejemplo, se muestra el resultado para dos usuarios.

// En este vídeo, aprendió lo siguiente: Los enrutadores se utilizan para ramificar el manejo de consultas.
// Hay cinco tipos de middleware: a nivel de aplicación, a nivel de router, de gestión de errores, integrado y de terceros.
// La representación de plantillas es la capacidad del servidor para rellenar el contenido dinámico de la plantilla HTML."