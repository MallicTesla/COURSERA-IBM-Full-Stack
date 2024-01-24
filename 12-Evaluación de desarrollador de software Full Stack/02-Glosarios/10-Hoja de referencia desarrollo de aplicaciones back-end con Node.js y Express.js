// Async-await
// Podemos esperar promesas siempre que se llamen dentro de funciones asincrónicas.
const axios = require('axios').default;
let url = "alguna URL remota";
async function asyncCall() {
    console.log('llamando');

    try {
        const result = await axios.get(url);
        console.log(result.data);
    } catch (error) {
        console.error("Error al realizar la llamada:", error.message);
    }
}
asyncCall();


// callback
// Las devoluciones de llamada son métodos que se pasan como parámetros. Se invocan dentro del método al que se pasan como parámetro, de forma condicional o incondicional.
//  Usamos devoluciones de llamada con la promesa de procesar la respuesta o los errores.
// Las funciones de devolución de llamada anónimas function(res) y function(err)
axios.get(url)
    .then(function (res) {
        console.log(res);
    })
    .catch(function (err) {
        console.log(err);
});


// Default/Date
// El nuevo método Date() devuelve la fecha actual como un objeto. Puede invocar métodos en el objeto de fecha para formatearlo o cambiar la zona horaria.
module.exports.getDate = function getDate() {
    var aestTime = new Date().toLocaleString("en-US", { timeZone: "Australia/Brisbane" });
    return aestTime;
}


// express.get();
// Este método está destinado a atender las solicitudes de recuperación al servidor. El método get() se implementará con dos parámetros; el primer parámetro define el punto final
//  y el segundo parámetro es una función que toma el controlador de solicitudes y el controlador de respuestas.
// Maneja las consultas GET al endpoint /user/about/id.
app.get("/user/about/:id", (req, res) => {
    res.send("Respuesta acerca del usuario " + req.params.id);
});


// express.listen()
// El método de escucha se invoca en el objeto express con el número de puerto en el que escucha el servidor. La función se ejecuta cuando el servidor comienza a escuchar.
app.listen(3333, () => {
    console.log("Escuchando en http://localhost:3333");
});


// express.post();
// 	Este método está destinado a atender las solicitudes de creación al servidor. El método post() se implementará con dos parámetros: el primer parámetro define el punto final
//  y el segundo parámetro es una función que toma el controlador de solicitudes y el controlador de respuestas.
// Maneja consultas POST en el mismo endpoint.
app.post("user/about/:id", (req, res) => {
    res.send("Respuesta sobre el usuario " + req.params.id);
});

// express.Router()
// El middleware a nivel de enrutador no está vinculado a la aplicación. En cambio, está vinculado a una instancia de express.Router(). Puede utilizar middleware específico para
//  una ruta específica en lugar de que todas las solicitudes pasen por el mismo middleware. Aquí, la ruta es /usuario y desea que la solicitud pase por el enrutador del usuario.
//  Defina el enrutador, defina la función de middleware que utilizará el enrutador y lo que sucede a continuación, y luego vincule la ruta de la aplicación al enrutador.
const express = require("express");
const app = new express();
var userRouter = express.Router();  // Corregido: 'express' estaba mal escrito
var itemRouter = express.Router();

userRouter.use(function (req, res, next) {
    console.log("Hora de la consulta de usuario:", Date());
    next();
});

userRouter.get("/:id", function (req, res, next) {
    res.send("Usuario " + req.params.id + " último inicio de sesión exitoso " + Date());
});

app.listen(3333, () => {
    console.log("Escuchando en http://localhost:3333");
});


// express.static()
// Este es un ejemplo de middleware estático que se utiliza para representar imágenes y páginas HTML estáticas desde el lado del servidor. Los archivos estáticos se pueden
//  representar desde el directorio cad220_staticfiles en el nivel de la aplicación. Observe que la URL solo tiene la dirección del servidor y el número de puerto seguidos del
//  nombre del archivo.
const express = require("express");
const app = new express();
app.use(express.static("cad220_staticfiles"));  // Corregido: se añadió el punto y coma
app.listen(3333, () => {
    console.log("Escuchando en http://localhost:3333");
});

// express.use()
// Este método toma middleware como parámetro. El middleware actúa como guardián en el mismo orden en que se utiliza antes de que la solicitud llegue a los controladores get() y
//  post(). El orden en que se encadena el middleware depende del orden en que se utiliza el método .use() para vincularlos. La función myLogger() del middleware toma tres
//  parámetros, que son solicitud, respuesta y siguiente. Puede definir un método que tome estos tres parámetros y luego vincularlo con express.use() o router.use(). Aquí, está
//  creando un middleware llamado myLogger y haciendo que la aplicación lo utilice. El resultado generado incluye la hora en que se recibe la solicitud.
const express = require("express");
const app = new express();

function myLogger(req, res, next) {
    req.timeReceived = Date();
    next();
}

app.get("/", (req, res) => {
    res.send("Request received at " + req.timeReceived + " is a success!");
});


// express-react-views.createEngine() and express.engine()
// Este ejemplo utiliza express-react-views, que representa los componentes de React desde el servidor. Usted establece la propiedad del motor de visualización, que es
//  responsable de crear HTML a partir de sus vistas. Las vistas son código JSX. Las vistas están en un directorio llamado myviews. El motor de visualización buscará un archivo
//  JSX llamado index en el directorio myviews y le pasará el nombre de la propiedad. La salida renderizada tendrá el nombre del usuario.
const express = require("express");
const app = new express();
const expressReactViews = require("express-react-views");
const jsxEngine = expressReactViews.createEngine();

app.set("view engine", "jsx");
app.set("views", "myviews");
app.engine("jsx", jsxEngine);

app.get("/:name", (req, res) => {
    res.render("index", { name: req.params.name });
});

app.listen(3333, () => {
    console.log("Listening at http://localhost:3333");
});


// http/createServer
// El paquete http se utiliza para establecer conexiones remotas a un servidor o para crear un servidor que escuche al cliente. CreateServer: toma requestListener, una función
//  que toma parámetros de solicitud y respuesta, donde solicitud es el identificador de la solicitud del cliente y respuesta es el identificador que se enviará al cliente.	
const http = require('http');

const requestListener = function(req, res) {
    res.writeHead(200);
    res.end('Hello, World!');
}

const port = 8080;
const server = http.createServer(requestListener);
server.listen(port, () => {
    console.log('Server listening on port: ' + port);
});


// Import()
// La declaración de importación se utiliza para importar módulos que algún otro módulo ha exportado. Un archivo que incluye código reutilizable se conoce como módulo.
// addTwoNos.mjs
function addTwo(num) {
    return num + 4;
}

export { addTwo };

  // app.js
import { addTwo } from './addTwoNos.mjs';

  // Prints: 8
console.log(addTwo(4));


// new express()
// Crea un objeto expreso que actúa como una aplicación de servidor.	
const express = require("express");
const app = new express();


// Promise
// Un objeto devuelto por algunos métodos, que representa una eventual finalización o falla. El código continúa ejecutándose sin bloquearse hasta que se cumpla la promesa o se
//  produzca una excepción.	

axios.get(url)
.then(
//do something
)
.catch(
//do something
)


// Promise use case
// Las promesas se utilizan cuando el tiempo de procesamiento de la función que invocamos lleva tiempo, como acceso remoto a URL, lectura de archivos de operaciones de E/S, etc.
var prompt = require('prompt-sync')();
var fs = require('fs');

const methCall = new Promise((resolve, reject) => {
    var filename = prompt('What is the name of the file?');
    try {
        const data = fs.readFileSync(filename, { encoding: 'utf8', flag: 'r' });
        resolve(data);
    } catch (err) {
        reject(err);
    }
});

console.log(methCall);

methCall.then(
    (data) => console.log(data),
    (err) => console.log("Error reading file")
);


// Require()
// El método incorporado de NodeJS require() se utiliza para incorporar módulos externos que se incluyen en diferentes archivos. La declaración require() esencialmente lee y
//  ejecuta un archivo JavaScript antes de devolver el objeto de exportación.	
module.exports = 'Hello Programmers';
message.js;var msg = require('./messages.js');console.log(message);