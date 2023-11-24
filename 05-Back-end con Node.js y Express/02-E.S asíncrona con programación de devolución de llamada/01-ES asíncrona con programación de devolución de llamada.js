// "Bienvenido a la E/S asíncrona con programación de devolución de llamada. Tras ver este vídeo, debería poder: explicar el concepto de funciones de devolución de llamadas
//     asíncronas y gestionar las llamadas entrantes a métodos del protocolo de transferencia de hipertexto (HTTP) para un recurso de servidor.

// Las operaciones de red se ejecutan de forma asíncrona. Por ejemplo, es posible que la respuesta de una llamada a un servicio web no se devuelva inmediatamente. Cuando una
//     aplicación bloquea (o espera) a que se complete una operación de red, esa aplicación desperdicia tiempo de procesamiento en el servidor. Node.js realiza todas las
//     operaciones de red de forma no bloqueante. Todas las operaciones de red se reanudan inmediatamente.

// Para gestionar el resultado de una llamada de red, escriba una función de devolución de llamada a la que Node.js llame cuando se complete la operación de red.

// Este diagrama de secuencia de un escenario muestra la interacción entre la aplicación, el marco Node.js, la llamada del servicio web al servidor remoto y la llamada de
//     devolución de llamada a la función de devolución de llamada.
// En el primer paso, la aplicación realiza una llamada a HTTP.Request. Esta función realiza una llamada al servidor web remoto y solicita el servicio web. Antes de que el
//     framework Node.js reciba el mensaje de respuesta HTTP del servidor web remoto, devuelve inmediatamente un resultado para la llamada a la función HTTP.Request. Este resultado
//     simplemente indica que el mensaje de solicitud se envió correctamente. No dice nada sobre el mensaje de respuesta. Cuando el marco Node.js recibe un mensaje de respuesta
//     HTTP del servidor remoto, llama a la función de devolución de llamada que definió durante la llamada a la función http.Request.

// Esta función gestiona el mensaje de respuesta HTTP. En un escenario un poco más complejo, la aplicación llama a un módulo Node.js personalizado y, a continuación, realiza una
//     llamada a la función HTTP.Request. A continuación, el marco Node.js llama al servicio web del servidor remoto mediante el envío de un mensaje de solicitud HTTP. Del mismo
//     modo que en el primer escenario, el marco Node.js devuelve un valor a la llamada a la función HTTP en el módulo Node.js. Esta respuesta simplemente indica que la solicitud
//     HTTP se envió correctamente. A continuación, el módulo Node.js regresa de la llamada a la función exportada. En este punto, la aplicación continúa con el siguiente paso,
//     mientras que el mensaje de respuesta aún no se ha enviado. Cuando el servidor remoto devuelve un mensaje de respuesta HTTP, el marco Node.js llama a la función de devolución
//     de llamada definida por el módulo Node.js personalizado.

// El objetivo de la función callback es gestionar dos eventos: request.on ('data') y request.on ('end'). En este caso, la función de devolución de llamada simplemente imprime el
//     cuerpo del mensaje de respuesta HTTP en el registro de la consola.

let options = {
    host:"w1weather.gov",
    path:"/xml/currnt_obs/KSFo.xml"
};

http.request(
    options, function(response){
        let buffer = "";
        let result = "";

        response.on ("data", function(chunk){
            buffer += chunk;
        });
        
        response.on("end",function(){
            console.log (buffer);
        });
    }).end();
// Este ejemplo de código muestra cómo realizar una llamada de solicitud HTTP desde una función incluida en un módulo de Node.js. El primer parámetro de la función de solicitud
//  HTTP es una variable de opciones. La variable options incluía al menos dos variables: el nombre de host del servidor remoto y una ruta de recursos del localizador uniforme
//  de recursos (URL) sobre la que se quería actuar. En este ejemplo, está haciendo una llamada al Servicio Meteorológico Nacional de EE. UU. para obtener la observación
//  meteorológica del Aeropuerto Internacional de San Francisco (KSFO).
// El segundo parámetro de la función de solicitud HTTP es una función de devolución de llamada. En este caso, se trata de una función anónima que recibe un parámetro: el objeto
//  de respuesta. Cuando el módulo Node.js llama a esta función anónima, se producen eventos mientras recibe partes del objeto de respuesta HTTP. En este ejemplo, hay dos eventos
//  específicos: un evento de «datos» y un evento de «finalización». Para estos dos eventos, defina más funciones de devolución de llamada para gestionar cada tipo de evento.
// En la codificación actual, es posible que tengas que usar HTTPS en lugar de HTTP.

// El objeto resultante se pasa a la función de devolución de llamada de un módulo ParseString. La función http.Request incluye una URL y un conjunto de opciones. Si se aprueban
//  ambas, se fusionan y las opciones tienen prioridad. Puede definir el host, los puertos, la autenticación, el protocolo y otros encabezados en el objeto de opciones.
// El método http.Request también acepta una función de devolución de llamada opcional que se invoca inmediatamente una vez que se recibe la respuesta.

// Cuando http.Request llama a la función de devolución de llamada, pasa un objeto de respuesta al primer parámetro de la función de devolución de llamada. Esta función de
//  devolución de llamada tiene el objeto de respuesta como primer parámetro. El marco Node.js emite varios eventos durante el transcurso de la función de solicitud.
// Para escuchar estos eventos, utilice el método object.on () e introduzca el nombre del evento como primer parámetro. Si la solicitud se realiza correctamente, se emite un
//  evento de «datos» en el objeto de respuesta cada vez que se reciben datos, seguido de un evento de «finalización» cuando finaliza la respuesta.


let options1 = {
    hostname:"www.ibm.com",
    port:80,
    method:"POST",
    headers:{
        "Content-Type":"application/x-www-form-urlencoded",
        "contenr-Length":data.length
    }
};
let req = http.request(options1,function(res){})
// Si la solicitud falla, se produce un evento de «error» seguido del evento de «cierre». Veamos cómo gestionar estos errores. El método de solicitud devuelve un objeto del tipo
//  http.ClientRequest. Este objeto representa la solicitud en curso. Puede añadirlo al cuerpo de la solicitud, realizar cambios en los encabezados y detectar eventos de error,
//  como se muestra aquí. El código simplemente muestra el mensaje de error si hay un error. Para finalizar la solicitud, llama a ClientRequest.end ().

// En este vídeo, aprendió lo siguiente: cuando una aplicación se bloquea para completar una operación de red, esa aplicación pierde tiempo de procesamiento en el servidor.
// Node.js realiza todas las operaciones de red de forma no bloqueante. y cuando el marco Node.js recibe un mensaje de respuesta HTTP del servidor remoto, llama a la función de
//  devolución de llamada que gestiona el mensaje de respuesta HTTP"