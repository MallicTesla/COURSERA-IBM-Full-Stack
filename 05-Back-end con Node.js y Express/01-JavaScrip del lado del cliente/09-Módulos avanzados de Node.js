// Después de completar esta lectura, podrá describir los tres tipos de módulos de Node.js. También podrá explicar para qué se pueden utilizar varios módulos principales 
//  destacados.

// Las bibliotecas son lo mismo que los módulos con respecto a Node.js. Las bibliotecas contienen código desarrollado que se puede reutilizar en toda una aplicación.
// Hay tres tipos de módulos: principales, locales y de terceros.

// Los módulos principales de Node.js forman una biblioteca mínima. Contienen la funcionalidad mínima necesaria para desarrollar aplicaciones Node.js.

// Los módulos locales son el siguiente tipo de módulo Node.js. Los módulos locales son los módulos escritos por usted y el equipo de desarrollo como parte de la creación de su
//  aplicación Node.js.

// Los módulos de terceros están disponibles en línea y han sido creados por la comunidad back-end de Node.js. Estas bibliotecas están disponibles para su uso según lo
//  establecido en sus licencias. Muchos módulos de terceros son de dominio público, lo que no requiere licencia, o son de código abierto. Los recursos de código abierto
//  generalmente se rigen por la licencia "copyleft", que permite al desarrollador usar y modificar el código pero también requiere que el desarrollador comparta su trabajo bajo
//  esa misma licencia.

// Los módulos principales más importantes son http, path, fs, os, util, url y querystring. Analicemos brevemente cada uno de estos y proporcionemos ejemplos de código.

// El módulo http proporciona métodos para transferir datos a través de HTTP. Para incluir el módulo http en su aplicación, debe solicitarlo.

// Aquí hay un código de muestra que crea una instancia de un servidor usando el módulo http. Este código utiliza el método http.createServer() para crear la instancia del
//  servidor.
let http = require('http');
http.createServer(function (req, res) {
    res.write('hello from server');//Escribe una respuesta al cliente
    res.end();//fin de la respuesta del servidor
}).listen(6000);//la instancia del servidor escucha solicitudes http en el puerto 6000


// El módulo fs se utiliza para interactuar con un sistema de archivos. No es necesario instalarlo porque es parte del núcleo de Node.js y simplemente puede ser necesario.
// El siguiente ejemplo de código lee un archivo local de forma sincrónica utilizando el módulo fs e imprime el contenido del archivo en la consola.

// código de muestra para leer un archivo sincrónicamente usando el método fs.readFile()
const fs = require('fs');
const data = fs.readFile('sample.txt', 'utf8');
// imprimir el contenido del archivo "sample.txt" a la consola
console.log(data);


// El módulo fs también se puede utilizar para entrada y salida, lo que se conoce como E/S.
// Los métodos del módulo fs se pueden utilizar para recuperar información o escribir datos en un archivo externo.

const fs = require('fs');
const data1 = fs.readFileSync('/content.md'); // se bloquea aquí hasta que se lee el archivo
console.log(data1); // imprime los datos en el archivo content.md en la consola


// El módulo OS proporciona métodos para recuperar información del sistema operativo en el que se ejecuta la aplicación e interactuar con él.
// Este es un código de muestra del módulo del sistema operativo que obtiene la plataforma y la arquitectura de la computadora.

let os = require('os');
console.log("Computer OS Platform Info : " + os.platform());
console.log("Computer OS Architecture Info: " + os.arch());


// El módulo de ruta le permite recuperar y manipular rutas de directorios y archivos.
// El siguiente código recupera la última parte de una ruta de archivo determinada e imprime ese valor en la consola:

const path = require('path');
let result = path.basename('/content/index/home.html');
console.log(result); //envía home.html a la consola


// El módulo de utilidades de Node.js está diseñado para uso interno para realizar tareas como depurar y desaprobar funciones.
// Supongamos que desea depurar un programa para contar el número de iteraciones en un bucle. Podrías usar el método util.format() de la siguiente manera:

let util = require('util');
let str = 'El bucle se ha ejecutado %d veces.';
for (let i = 1; i <= 10; i++) {
    console.log(util.format(str, i)); //genera 'El bucle se ha ejecutado i veces'
}


// El módulo URL se utiliza para dividir una dirección web en partes legibles.
// Aquí hay un código de muestra que devuelve el valor del objeto de consulta "firstName" de la URL proporcionada.

const url = require('url');
let webAddress = 'http://localhost:2000/index.html?lastName=Kent&firstName=Clark';
let qry = url.parse(webAddress, true);
let qrydata = qry.query; //devuelve un objeto: {apellido: 'Kent', nombre: 'Clark'}
console.log(qrydata.firstName); //outputs Clark

// El módulo querystring proporciona métodos para analizar la cadena de consulta de una URL. Por ejemplo,

let qry = require('querystring');
let qryParams = qry.parse('lastName=Kent&firstName=Clark');
console.log(qryParams.firstName); //returns Clark

// También hay varios paquetes de terceros útiles para usar con Node.js. Algunos de ellos incluyen AsyncJS, Axios y Express. Estas bibliotecas se analizarán más adelante en el curso.