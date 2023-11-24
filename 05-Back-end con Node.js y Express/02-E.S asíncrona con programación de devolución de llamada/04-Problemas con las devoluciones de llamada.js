// Bienvenido a Issues with Callbacks. Tras ver este vídeo, podrá: explicar por qué se producen las devoluciones de llamadas anidadas, explicar las dificultades de las
//  devoluciones anidadas, describir la inversión del control, explicar las dificultades que conlleva la inversión del control e identificar varias formas de mitigar las
//  devoluciones anidadas y la inversión del control.

// Recuerde que una devolución de llamada es una función que se pasa como argumento a otra función que ejecuta la devolución de llamada en función del resultado. Básicamente son
//  funciones que se ejecutan solo después de que se produzca un resultado. Los callbacks nos ayudan a desarrollar código JavaScript asíncrono. Los callbacks garantizan que una
//  función no se ejecute antes de completar una tarea previa.


const mensage = function(){
    console.log ("Este mensaje se muestra después de 3 segundos");
}
setTimeout (mensage, 3000);
// En este ejemplo, el mensaje es un ejemplo de función de devolución de llamada. Cuando se llama, escribe: «Este mensaje se muestra después de 3 segundos» en la consola.
// Hay un método integrado en JavaScript llamado «setTimeout», que espera un tiempo específico en milisegundos antes de realizar una acción. En este ejemplo, el mensaje se pasa
//  a la función setTimeout. Por lo tanto, después de esperar 3 segundos, setTimeout escribe un «mensaje» en la consola. Por lo general, estas devoluciones de llamada asíncronas,
//  o asíncronas para abreviar, se utilizan para acceder a los valores de las bases de datos, descargar imágenes, leer archivos, etc.

// A menudo, estos recursos los proporcionan otros servicios ajenos a la aplicación que los necesita. Las funciones de devolución de llamada esperan una respuesta y, cuando se
//  envía la respuesta, se ejecutan. Por ejemplo, supongamos que está haciendo un pastel. Estos son los pasos: Compra los ingredientes del pastel. Combine los ingredientes.
// Hornea el pastel. Decora el pastel. Sirve el pastel. Estos pasos no se pueden completar al mismo tiempo. En otras palabras, estos pasos no se pueden completar de forma
//  asíncrona. El siguiente paso solo se puede iniciar después de completar el paso anterior. Cuando se utilizan callbacks para hacer que algo ocurra de forma secuencial, las
//  funciones deben estar anidadas una dentro de otra.


const hacerPastel = siguientePaso => {
    comprarIngredientes(function (listaDeCompras) {
        combinarIngredientes(tazón, batidora, function (ingredientes) {
            hornearPastel(horno, molde, function (masa) {
                decorar(azúcarglas, function (pastel) {
                    siguientePaso(pastel);
                });
            });
        });
    });
};
// El pseudocódigo de nuestro ejemplo de pastel podría terminar teniendo este aspecto: cada función subsiguiente se convierte en el argumento que se pasa a la siguiente función.
// Cada devolución de llamada depende de la devolución de llamada anterior y espera a que se produzca, por lo que se forma una estructura piramidal que afecta a la legibilidad y
//  al mantenimiento del código. Este anidamiento de funciones de devolución de llamada suele denominarse «infierno de devolución de llamadas» y consiste básicamente en
//  devoluciones de llamadas anidadas apiladas una debajo de la otra, formando una estructura piramidal. A esta estructura también se la denomina a veces «La Pirámide de la
//  Perdición».
// Otro problema con las devoluciones de llamadas es la inversión del control, también denominada IoC. La inversión del control se produce cuando el flujo de control, como la
//  ejecución de instrucciones, es externo al código. Muchas veces, las llamadas devueltas ceden el control a un tercero. Sin embargo, los problemas y errores relacionados con
//  ese código de terceros pueden ser difíciles de detectar. Te ves obligado a confiar en el código de un tercero o tienes que escribir código adicional para garantizar que el
//  código de terceros no lo haga: recibe llamadas demasiadas o muy pocas veces, recibe llamadas demasiado pronto o demasiado tarde, pierde contexto o transmite argumentos
//  incorrectos. Por ejemplo, supongamos que el código de un tercero tiene un error en el que se invoca varias veces cuando el usuario hace clic en un botón por error más de una
//  vez. Puedes intentar resolver este problema con una marca booleana. Cuando la bandera es falsa y se hace clic en el botón, se carga a la carta y la bandera pasa a ser
//  verdadera. Ahora, cuando la marca es verdadera y se vuelve a hacer clic en el botón, la lógica de ramificación no hace ningún cargo a la tarjeta del cliente otra vez. Pero
//  entonces, ¿qué pasa si la persona que devuelve la llamada nunca recibe la llamada? Esa bandera sigue siendo falsa y ahora hay otro caso de uso que hay que tener en cuenta.
// Para detectar este tipo de errores, tu código está plagado de código extraño para garantizar que el código de terceros no falle. Existen varias formas de mitigar los
//  problemas de devolución de llamadas y de confianza: puedes escribir comentarios, dividir las funciones en funciones más pequeñas, usar Promises o puedes usar async/await.

// En próximos vídeos analizaremos Promises y async/await. En este vídeo, aprendiste que: la necesidad de funciones de devolución de llamada anidadas puede surgir cuando varias
//  de las tareas de devolución de llamada dependen unas de otras y deben completarse secuencialmente.
// El término «infierno de devolución de llamada» se refiere a las funciones de devolución de llamada anidadas.
// Cuando utilizas código de terceros, a menudo tienes problemas de inversión de control que hacen que no puedas confiar en el código de terceros.
// Y las formas de mitigar los problemas de confianza y las dificultades de devolución de llamadas incluyen escribir comentarios, dividir las funciones en funciones más pequeñas,
//  usar promesas y usar async/await.