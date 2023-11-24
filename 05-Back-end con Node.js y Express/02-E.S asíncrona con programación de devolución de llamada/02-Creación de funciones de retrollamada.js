// "Bienvenido a Creating Callback Functions. Tras ver este vídeo, debería poder crear una función de devolución de llamada para interceptar las llamadas a los métodos del
//     protocolo de transferencia de hipertexto (HTTP).

// Como marco asíncrono, Node.js utiliza ampliamente las funciones de devolución de llamada para devolver el resultado a la función que realiza la llamada. Los módulos Node.js del
//     kit de desarrollo de software (SDK) transfieren un objeto de error como primer parámetro de una función de devolución de llamada. En este caso, la función se define con un
//     error como primer parámetro. Con esta convención, la función callback comprueba si el primer parámetro contiene un objeto de error. Si se define un error, la función de
//     devolución de llamada gestiona el error y limpia cualquier conexión de red o base de datos abierta. Si el error no está definido, la función de devolución de llamada examina
//     el resultado de la llamada. Si el error está definido, imprima el mensaje de error. De lo contrario, la llamada a la función weather.current se completó correctamente.

// Imprime el resultado de la llamada a la función. Los códigos están en la aplicación principal, que tiene un objeto meteorológico (el módulo Node.js) que llama a la función
//     meteorológica actual. La ubicación es un parámetro de entrada: en este ejemplo, un aeropuerto. Para imprimir temp_f en el navegador, podemos usar response.end (`La
//     información meteorológica actual es de $ {temp_f} grados'). Ahora veremos un ejemplo de cómo pasar un objeto de error a la función de devolución de llamada.

// Recuerde cómo las funciones de devolución de llamada comprueban el primer parámetro para ver si se ha producido una condición de error. En lugar de imprimir el resultado en
//  la consola, se llama a la función de devolución de llamada ResultCallback con el objeto de error. El objeto de error se devuelve a la función de devolución de llamada
//  ResultCallback de la aplicación principal. Si no se ha producido ningún error, se llama a la función ResultCallback con null como primer parámetro. Los códigos se encuentran
//  en el módulo Node.js personalizado. El controlador de devolución de llamada imprimía el contenido del cuerpo del mensaje de respuesta HTTP en la consola.

// ¿Qué pasaría si quisiera que devolviera el mensaje de respuesta a la aplicación de llamada original? Si utilizas una función de devolución, Node.js podría llamar a la función
//  de devolución de llamada una vez finalizada la llamada a http.request (). La aplicación llama a la función exportada. El módulo que implementa la función llama a
//  http.request para que el framework Node.js pueda realizar una llamada a un servicio web en su nombre. Cuando la solicitud se envía correctamente, el marco devuelve el
//  control al módulo Node.js. A continuación, el módulo Node.js devuelve el control a la aplicación. Cuando el servidor remoto devuelve un mensaje de respuesta HTTP al marco
//  Node.js, el marco llama al controlador de devolución de llamadas definido por el módulo Node.js. Sin embargo, no hay conexión entre la función de devolución de llamada y la
//  aplicación principal.

// Entonces, ¿cómo se vincula la función de devolución de llamada a la aplicación principal? El patrón es que cuando una aplicación de Node.js llama a un módulo de forma no
//  bloqueante, la aplicación proporciona una función de devolución de llamada para procesar el resultado. Si la aplicación principal llama a http.request (), debe proporcionar
//  un controlador de devolución de llamada para procesar el mensaje de respuesta HTTP. Si la aplicación principal llama a una función que llama a http.request (), hay dos
//  funciones de devolución de llamada: el módulo personalizado tiene una función de devolución de llamada que gestiona el mensaje de respuesta HTTP de http.request ().
// Además, la aplicación principal tiene una función de devolución de llamada que procesa el resultado capturado en la primera función de devolución de llamada. Vamos a ver cómo
//  funciona esta solución.

// Crearemos una función de devolución de llamada para capturar el resultado de la llamada a la función http.request. La aplicación realiza una llamada al módulo Node.js. El
//  módulo Node.js realiza una llamada a la función http.request para enviar un mensaje de solicitud HTTP a un servidor remoto. Antes de que el servicio remoto devuelva un
//  mensaje de respuesta HTTP, la llamada a la función http.request devuelve el control al módulo Node.js, ya que el mensaje de solicitud se envió correctamente. A continuación,
//  el módulo Node.js responde con un valor a la aplicación principal. En el futuro, el servidor remoto devuelve un mensaje de respuesta HTTP. El marco Node.js llama a la función
//  de devolución de llamada definida por el módulo Node.js. Esta función de devolución de llamada llama a otra función de devolución de llamada definida por la aplicación
//  principal. Hacer que una función de devolución de llamada invoque otra función de devolución de llamada es la única forma de pasar un mensaje del módulo Node.js a la
//  aplicación principal cuando el módulo Node.js recibe un mensaje de respuesta. En este caso, cuando la aplicación principal llama a weather.current (), transfiere una función
//  de devolución de llamada anónima para procesar el resultado de la llamada.
// En este caso, la función anónima «function (temp_f)» toma un parámetro de entrada, temp_f. El objetivo de esta función de devolución de llamada es tomar la lectura
//  meteorológica en grados Fahrenheit e imprimir los resultados en el registro de la consola. La función de devolución de llamada resultCallback de la función del módulo Node.js
//  personalizado enlaza con la función de devolución de llamada anónima, function (temp_f), de la función .current del objeto meteorológico de la aplicación principal.
// Ahora puede ver un módulo Node.js que devuelve un resultado a la aplicación principal con una función de devolución de llamada. Aquí, se define una función para la propiedad
//  denominada «current». Esta propiedad se exportará como parte del módulo. La función anónima toma un parámetro denominado «resultCallback» de la aplicación principal.
// Así es como se pasa una referencia a la función de devolución de llamada de la aplicación principal a la función de devolución de llamada del módulo Node.js. El parámetro
//  ResultCallback almacena la función de devolución de llamada anónima de la aplicación principal. Observe la parte inferior de la propiedad actual. Un controlador de eventos
//  «response.on ('end')» gestiona la transmisión del mensaje de respuesta HTTP. Cuando el servidor remoto termina de enviar el mensaje de respuesta, el código hace una llamada
//  a ResultCallback y le pasa la lectura meteorológica actual en grados Fahrenheit. Así es como se pasa un valor de un controlador de devolución de llamada a otro.

// En este vídeo, descubrirá que Node.js utiliza ampliamente las funciones de devolución de llamada para devolver el resultado a la función que realiza la llamada.
// Los módulos Node.js del SDK pasan un objeto de error como primer parámetro de una función de devolución de llamada y hay una función de devolución de llamada en cada nivel."