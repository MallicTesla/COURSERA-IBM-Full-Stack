// "Bienvenido a Authentication in Node.js. Tras ver este vídeo, podrá: Analizar las ventajas de la autenticación basada en fichas en Node.js e implementar la autenticación y la
//     autorización basadas en fichas en Node.js.

// Por lo tanto, la autenticación es el proceso de confirmar la identidad de un usuario mediante la obtención de credenciales y su uso para validar su identidad. La autenticación
//     tiene por objeto identificar a los usuarios y proporcionar derechos de acceso y contenido en función de su identidad. Como se explica en otro vídeo, la autenticación se puede
//     lograr mediante los siguientes enfoques: autenticación basada en sesiones, autenticación basada en token y autenticación sin contraseña.

// La autenticación basada en token es el método más popular para implementar la autenticación en Node.js. Y las siguientes son algunas de las ventajas de usar la autenticación
//     basada en token.
// La autenticación basada en token es más escalable, ya que el token solo necesita almacenarse en el lado del cliente.
// Además, dado que el servidor solo necesita verificar el token junto con la información del usuario, es más fácil gestionar varios usuarios.
// La autenticación basada en token ofrece flexibilidad, ya que se puede utilizar en varios servidores y puede ofrecer autenticación para diversos sitios web y aplicaciones a la vez.
// Además, los JWT utilizados en la autenticación basada en token se pueden firmar y cifrar, lo que significa que no se pueden manipular ni leer sin la clave de cifrado privada.

// Ahora vamos a configurar un servidor API de Express.js que proporcione acceso a la información de los empleados en función de sus derechos de uso. La aplicación tendrá 2 API,
//     cada una con sus propios puntos finales. Primero utilizaremos una API POST para iniciar sesión que devolverá un token web para iniciar sesión enviando el nombre de usuario y
//     la contraseña en el cuerpo de la solicitud. La llamada a este punto final de la API debe realizarse desde el servidor web que aloja la interfaz de la aplicación. Y una
//     segunda API GET será el punto final del recurso para obtener la información de los empleados a la que solo podrán acceder los usuarios autenticados. Consideremos qué aspecto
//     podría tener este código.


const express = require ("express");
const myapp = express();
// Este código crea un módulo de servidor web llamando a la función «express ()» y asignándola a la constante «myapp».

myapp.get ("/employees", (req, res) => {
    return res.status(401).json({mesagge:"Inicie sesión para acceder a este recurso"});
});
// La función myapp.get crea un punto final de la API GET para la API de empleados, y cualquier llamada a este punto final devuelve actualmente un código de estado HTTP de 401.
//  401 significa No autorizado y aparece el mensaje «Inicie sesión para acceder a este recurso».

myapp.listen(5000, () => {
    console.log ("El servidor API es localhost:8080");
});
// « El servidor también escucha en el puerto 8080 cualquier llamada HTTP al servidor y registra el mensaje «El servidor API es localhost:8080" en la consola.


// Para ejecutar primero la API, guarde el archivo y asígnele el nombre API server dot js. Ahora ejecuta el comando: node api server dot js. Para comprobar que no se puede
//  acceder al punto final seguro a menos que el usuario esté autorizado, ejecute este comando curl en la pantalla. En el resultado, debería aparecer el mensaje:
//  «Inicie sesión para acceder a este recurso según su código».

// En la siguiente parte del código, permitimos a los usuarios iniciar sesión y enviar un token generado y verificado siempre que el nombre de usuario y la contraseña sean
//  correctos. Por lo general, los nombres de usuario y las contraseñas se almacenan en la base de datos. Sin embargo, dado que configurar una conexión a una base de datos está
//  fuera del alcance de esta demostración de código, codificaremos «usuario» y «contraseña» como nombre de usuario y contraseña en este ejemplo de código. Para generar el JWT
//  verificado, utilice el paquete npm «jsonwebtoken». Instálelo con el comando «npm install option save jsonwebtoken».

const express = require ("express");
const jsonwebtoken = require ("jsonwebtoken")

const JWT_SECRET = "aVeryVerySecretString"
// Al principio, necesitará el módulo «jsonwebtoken» del paquete «jsonwebtoken». Este módulo se utiliza para generar el JWT utilizando el secreto del
//  JWT. A continuación, se declara una constante para almacenar el secreto del JWT.


const myapp1 = express();
myapp1.use (express.json());


myapp1.post("/signin", (req, res) => {
    // const {uname, pwb} = req.body;
// })
// El método myapp dot use permite devolver una respuesta JSON mediante los métodos de la API. Para mostrar el código de este vídeo, estamos codificando el nombre de usuario y
//  la contraseña. Sin embargo, ten en cuenta que el secreto de JWT siempre debe generarse mediante un generador de contraseñas y almacenarse en el archivo de configuración como
//  una variable de entorno y no estar codificado en la API, como se muestra aquí.

if (uname === "user" && pwd === "password") {
    return res.json({
        token: jsonwebtoken.sign ({user:"user"}, JWT_SECRET),
    });
}
return res.status(401).json({message:"usuario o password invalidos"});
});

// A continuación, el nombre de usuario y la contraseña del cuerpo de la solicitud se comparan con los valores obtenidos de la base de datos. Una vez que el nombre de usuario y
//  la contraseña coinciden, el JWT se genera mediante la función «jsonwebtoken.sign ()», que incluye el nombre de usuario y el secreto de JWT como parámetros, y se devuelve
//  como una respuesta JSON desde la API «signin». Si el nombre de usuario y la contraseña no coinciden, se devuelve el código de estado HTTP 401 con el mensaje «Nombre de usuario
//  o contraseña no válidos».

myapp1.get ("/employees", (req, res) => {
    let tkn = req.header ("Authorization");
// A continuación, definimos el método GET API con el punto final de los empleados. El token obtenido de la llamada a la API de «inicio de sesión» se pasa al encabezado de
//  autorización. La API GET («empleados») se actualiza para leer el encabezado de autorización de la solicitud de API entrante mediante la función de encabezado de puntos de la
//  solicitud.
if (! tkn) return 
res.status (401).send("no Token");
// Si no se encuentra ningún encabezado en la solicitud, la API GET devuelve el código de estado 401 con el mensaje «No hay token».

if (tkn.startsWith("Bearer ")){
    tokenValue = tkn.slice (7, tkn.length).trimLeft();
// El encabezado de autorización siempre comienza con la cadena «BEARER» al principio del encabezado y, por lo tanto, este token también se conoce como Bearer Token.
    }
})


// El JWT obtenido se verifica mediante la función «jsonwebtoken.verify ()» pasando el token obtenido y el secreto del JWT. El valor devuelto por esta función se usa luego para
//  verificar si la propiedad del usuario coincide con el nombre de usuario obtenido de la base de datos y, si esa coincidencia ocurre, el usuario se autentica y se le
//  proporciona acceso a la API del empleado. A continuación, la API devuelve el código de estado de éxito 200 con el mensaje «Acceso exitoso» a Employee Endpoint. « Si se
//  produce un error en la verificación, el código de estado no autorizado 401 se devuelve al cliente con el mensaje «Inicie sesión para acceder a este recurso».

// Por último, escriba una función de escucha que escuche la respuesta en el puerto 5000 y, a continuación, registre la frase «El servidor API es el host local 5000» en el
//  registro de la consola.

// Recuerde que el código que acaba de escribir tiene un punto final de API de «inicio de sesión» que lee el nombre de usuario y la contraseña del cuerpo de la solicitud y, a
//  continuación, los valida con el nombre de usuario y la contraseña almacenados en la base de datos. Si hay una coincidencia, utiliza el método jsonwebtoken.sign () para
//  generar el token y devolverlo en la respuesta.

// En este vídeo, aprendió lo siguiente: las ventajas de la autenticación basada en token incluyen la escalabilidad, la flexibilidad y la seguridad.
// La API POST se utiliza durante la autenticación para que un usuario inicie sesión en una aplicación.
// La API GET se utiliza en la autorización para determinar a qué recursos puede acceder un usuario.
// Un token web JSON se usa para autenticar a un usuario y autorizar qué recursos puede usar."