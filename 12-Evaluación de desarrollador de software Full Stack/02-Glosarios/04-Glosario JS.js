// Child()
// Un método del DOM de HTML que, después de crear un elemento, puedes usar esta función para ubicar el elemento en la ubicación adecuada dentro del documento. El único
//  parámetro es el elemento que se va a agregar.	-->
// Crea el elemento <p> y el texto "Hello World". Agrega Hello World <p> al documento HTML.
// <head>
// <script>
function agregarParrafo() {
var nuevoParrafo = document.createElement("p");
var nuevoTexto = document.createTextNode("¡Hola Mundo!");
nuevoParrafo.appendChild(nuevoTexto);
document.body.appendChild(nuevoParrafo);
}
// </script>
// </head>
{/* <body onload="agregarParrafo()"> </body> */}
// ---------------------------------------------------------------------------------------------------------------------------------
// Arrays
// Se crean declarando los elementos del array entre [ ]. Un array puede asignarse a una variable, generalmente usando la palabra clave const o var. Los arrays usan una
//  indexación basada en cero para acceder a sus elementos.	-->
const Beatles = ["Ringo", "Paul", "George", "John"];
// Aquí Beatles[0] es "Ringo".
// ---------------------------------------------------------------------------------------------------------------------------------
// Date()
// El constructor es new Date([parámetros opcionales]). Si se declara el constructor sin parámetros, devuelve la fecha y hora locales actuales. Nuevas fechas pueden crearse
//  pasando parámetros a la función new Date.	
// Crea una nueva fecha a partir de una cadena
var nuevaFecha = new Date("2021-1-17 13:15:30");

// Crea una nueva instancia de fecha que representa el 17 de enero de 2021 a las 00:00:00
// ten en cuenta que el número del mes comienza desde cero
var nuevaFecha = new Date(2021, 0, 17);
// ---------------------------------------------------------------------------------------------------------------------------------
// document.createElement()
// Toma un parámetro de nombre de etiqueta y crea un elemento con ese nombre. Puede colocar el elemento en otra parte de la página usando funciones como insertBefore(),
//  appendChild(), replaceChild().	

// Crea el elemento <p> y el texto "Hello World". Agrega Hello World <p> al documento HTML.
{/* <head> */}
{/* <script> */}
function agregarParrafo() {
var nuevoParrafo = document.createElement("p");
var nuevoTexto = document.createTextNode("¡Hola Mundo!");
nuevoParrafo.appendChild(nuevoTexto);
document.body.appendChild(nuevoParrafo);
}
// </script>
// </head>
{/* <body onload="agregarParrafo()"> </body> */}
// ---------------------------------------------------------------------------------------------------------------------------------
// document.createTextNode()
// Toma una cadena como entrada de texto y devuelve un nodo de texto con el texto de entrada.	
// Crea el elemento <p> y el texto "Hello World". Agrega Hello World <p> al documento HTML.
{/* <head> */}
{/* <script> */}
function agregarParrafo() {
var nuevoParrafo = document.createElement("p");
var nuevoTexto = document.createTextNode("¡Hola Mundo!");
nuevoParrafo.appendChild(nuevoTexto);
document.body.appendChild(nuevoParrafo);
}
// </script>
// </head>
{/* <body onload="agregarParrafo()"></body> */}
// ---------------------------------------------------------------------------------------------------------------------------------
// document.getElementByID()
// Un método del DOM que toma un parámetro de valor de ID y devuelve un elemento que coincide con el ID.	
// Cambia el contenido del div a "¡Hola Mundo!"
{/* <div id="div1">
<p>Hola</p>
<p>Hola</p>
</div>

<script> */}
document.getElementById("div1").innerHTML = "<p>¡Hola Mundo!</p>";
// </script>
// ---------------------------------------------------------------------------------------------------------------------------------
// document.getElementsByTagName()
// Un método del DOM que toma un parámetro de nombre de etiqueta y devuelve un array llamado "NodeList" que contiene elementos con el nombre de etiqueta especificado.	
// Obtiene un array de todos los elementos en un documento con la etiqueta <p>.
var arrayNombreEtiqueta = document.getElementsByTagName("p");
// ---------------------------------------------------------------------------------------------------------------------------------
// document.write()
// Escribe HTML o JavaScript en un documento. Ten en cuenta que sobrescribe cualquier otro texto en el documento, por lo que se utiliza principalmente con fines de prueba
//  solamente.	
// Escribe "¡Hola Mundo" en la secuencia de salida.
document.write("¡Hola Mundo");
// ---------------------------------------------------------------------------------------------------------------------------------
// element.getAttribute()
// Devuelve el valor del atributo especificado. Toma un parámetro: el nombre del atributo cuyo valor se va a devolver.	
// Elimina el estilo CSS color azul
{/* <div id="div1" style="color: blue"></div> */}
{/* <script> */}
var div1 = document.getElementById("div1").getAttribute("style");
// </script>
// ---------------------------------------------------------------------------------------------------------------------------------
// element.innerHTML()
// Una propiedad de la clase Element que devuelve o altera el contenido de un elemento HTML como una cadena de texto.
// Cambia el contenido del div a "¡Hola Mundo!"
{/* <div id="div1"> */}
{/* <p>Hola</p>
<p>Hola</p>
</div>

<script> */}
document.getElementById("div1").innerHTML = "<p>¡Hola Mundo!</p>";
// </script>
// ---------------------------------------------------------------------------------------------------------------------------------
// element.removeAttribute()
// Una propiedad de la clase Element que elimina todos los estilos CSS en línea previamente establecidos para un elemento en particular. Toma un parámetro: el nombre del
//  atributo que se está eliminando.	
// Elimina el estilo CSS color azul
{/* <div id="div1" style="color: blue"></div> */}
{/* <script> */}
var div1 = document.getElementById("div1").getAttribute("style");
// </script>
// ---------------------------------------------------------------------------------------------------------------------------------
// element.setAttribute()
// Una propiedad de la clase Element que sobrescribe todos los estilos CSS en línea previamente establecidos para un elemento en particular. Toma dos parámetros: el nombre del
//  atributo que se está estableciendo y el valor del atributo al que se establece.	
// En todos los elementos llamados "theImage" establece el nombre de todos los atributos src en "another.gif"
document.getElementById("theImage").setAttribute("src", "another.gif");
// ---------------------------------------------------------------------------------------------------------------------------------
// element.style()
// Una propiedad de la clase Element que devuelve o altera los estilos CSS en línea. La sintaxis es element.style.nombrePropiedad = valor	
// Cambia el estilo CSS color de azul a rojo
{/* <div id="div1" style="color: blue"></div> */}
{/* <script> */}
var div1 = document.getElementById("div1");
div1.style.color = "red";
// </script>
// ---------------------------------------------------------------------------------------------------------------------------------
// Error Objects
// La instancia crea dos propiedades sobre el error: message que contiene la descripción del error y la propiedad name que identifica el tipo de error. Error genérico más 6
//  errores principales adicionales: TypeError, RangeError, URIError, EvalError, ReferenceError, SyntaxError.
// El objeto Error se puede extender para crear mensajes de error personalizados utilizando
