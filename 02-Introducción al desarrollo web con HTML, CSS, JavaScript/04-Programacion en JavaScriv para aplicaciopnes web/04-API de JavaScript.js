// "Bienvenido a las API de JavaScript. Tras ver este vídeo, podrá explicar cómo trabajar con los nodos, describir cómo modificar el contenido de un elemento, explicar cómo
//     modificar el estilo y los atributos integrados de un objeto y describir cómo utilizar los métodos y eventos de los objetos Window.

// Las especificaciones básicas del DOM de nivel 1 y del HTML de nivel 1 contienen demasiados detalles para una sola unidad. En cambio, el resto de la unidad se centra en las
//     funciones y propiedades del script que se utilizan habitualmente al trabajar con páginas HTML.
// En la diapositiva se muestran algunas de estas API comunes que se utilizan para acceder a los elementos DOM HTML de las páginas web.

// A continuación, se analizan los elementos del DOM.
// Para recuperar una referencia de nodo para un elemento de un documento con un identificador, utilice la función document.getElementById y pase el valor del identificador como
//     argumento. Esto devuelve un elemento HTML o XML específico si se encuentra un identificador único coincidente en la página web.

// La función getElementsByTagName recupera una NodeList de elementos con un nombre de etiqueta específico.
// La NodeList contiene una serie de elementos del documento. Usted proporciona el nombre del elemento que le interesa y se devuelve una matriz de todos los elementos con ese
//     nombre que se encuentran en el documento. En el caso de los elementos HTML, el parámetro tagName es el nombre literal de la etiqueta HTML. Si ejecuta la función
//     getElementsByTagName con una «p» como argumento de parámetro, se devuelve una lista de nodos con todos los párrafos del documento.

var imgSet = document.getElementsByTagName("img");
// En este ejemplo, se muestra cómo recuperar todos los elementos de imagen de una página web mediante la función getElementsByTagName y pasando «img» como argumento del
//  parámetro. El resultado es una lista de nodos que se asigna a la variable imgSet.
// En la siguiente parte del código, recorres la NodeList y concatenas los resultados en un flujo de salida del DOM. El atributo src es una propiedad común de la etiqueta img.
// El atributo src indica la ubicación de la fuente de la imagen. La función document.write () añade al documento el HTML generado por el script.
// Puede usar la función de la API DOM document.createElement (tagName) para crear un elemento en el documento actual. Tras crear el elemento, puede utilizar cualquier número de
    // funciones para colocarlo en la ubicación adecuada del documento. Entre los ejemplos de estas funciones se incluyen las funciones insertBefore, appendChild o replaceChild,
    // que se pueden utilizar para añadir el elemento recién creado al documento.

var nuevoParrafo = document.createElement("p"); // Crea un nuevo elemento de párrafo.
var texto = document.createTextNode("¡Hola mundo!"); // Crea un nodo de texto con el contenido.
nuevoParrafo.appendChild(texto); // Añade el nodo de texto como elemento secundario del párrafo.
document.body.appendChild(nuevoParrafo); // Añade el párrafo al cuerpo del documento.
// En este ejemplo se muestra el código fuente para añadir un nodo a un documento. Se está creando un nuevo elemento de párrafo que incluye un nodo de texto con la cadena
    // «¡Hola mundo!» A continuación, el nodo de texto se añade como elemento secundario del elemento de párrafo.
// Por último, todo el párrafo con texto se añade como un nodo secundario al final del nodo del cuerpo de la página HTML.

var elementoHTML = document.getElementById("miElemento"); // Recupera un elemento HTML por su ID.
elementoHTML.innerHTML = "Nuevo contenido con <strong>etiqueta HTML</strong>"; // Cambia el contenido del elemento.
// La función element.innerHTML recupera o establece el contenido de un elemento HTML. La propiedad innerHTML devuelve todos los elementos secundarios como una cadena de texto.
// Con la función Element.innerHTML, puede cambiar el contenido de un elemento HTML configurándolo en una cadena de texto que puede incluir etiquetas HTML.
// Si se establece el valor innerHTML de un elemento en una cadena, se eliminan todos los elementos secundarios actuales. A continuación, el navegador analiza la cadena y
    // establece el contenido del elemento HTML.

var elemento = document.getElementById("miElemento"); // Recupera un elemento por su ID.
elemento.style.color = "blue"; // Establece el estilo CSS de color.
elemento.style.backgroundColor = "yellow"; // Establece el fondo.
// Puede utilizar el método element.style para recuperar o establecer el estilo CSS integrado de un elemento concreto. Si utilizas element.style para establecer el estilo de un
    // elemento, sustituirá cualquier configuración de una hoja de estilos CSS por un estilo específico.
// La forma de establecer el estilo en JavaScript es con el formato element.style.propertyName = value.
// Por ejemplo, si tuvieras un elemento div style="color:blue». Aquí, la <div>etiqueta se usa para agrupar elementos de bloque y darles un formato con un estilo de color.
// Puedes cambiar el estilo de esta etiqueta div con la sentencia de JavaScript: div.style.color = 'red'; por el contrario, Element.setAttribute ('style',...) borra todos los
    // estilos CSS integrados previamente establecidos.

var elemento = document.getElementById("miElemento"); // Recupera un elemento por su ID.
elemento.setAttribute("src", "nuevaImagen.jpg"); // Cambia el atributo 'src'.
var srcValue = elemento.getAttribute("src"); // Recupera el valor del atributo 'src'.
// La función element.setAttribute con parámetros (attrName, attrValue) modifica dinámicamente el atributo de un elemento. En el ejemplo, el atributo src de un elemento con el
    // identificador theImage se establece en una imagen de destino diferente. La función element.removeAttribute (attrName) elimina un atributo de un elemento.
// La función Element.getAttribute (attrName) recupera el valor del atributo especificado en el elemento, si existe.

// A continuación, se muestran algunas funciones y eventos de los objetos de ventana. Para abrir una nueva ventana del navegador, utilice la función window.open (). Este método
    // devuelve una referencia al objeto de la nueva ventana. Puede utilizar esta referencia más adelante para cerrar la ventana, con el nombre_referencia seguido de la función
    // close (). Los parámetros de la función window.open son: URL: cadena que indica la ubicación de la página web que se mostrará en la nueva ventana. Puede pasar una cadena
    // vacía si va a escribir algún contenido generado por scripts en la nueva ventana en el contexto de URL actual. Nombre: cadena que especifica el nombre de la ventana.
// Características: cadena opcional que especifica las características de la ventana, como su ubicación y dimensiones. La cadena de características es una lista de pares
    // nombre-valor separados por comas. Reemplazar: un valor booleano opcional. Si es verdadero, la nueva ubicación reemplaza a la página actual del historial del navegador.

// La función window.onload se puede utilizar para iniciar una función después de cargar la página. La función window.dump («mensaje») escribe una cadena en la consola del
    // navegador web. La función dump () es una forma menos intrusiva de mostrar información de diagnóstico que el método alert ().

// Por último, el window.scrollTo (valor x, valor y ) desplaza el navegador web hasta un conjunto concreto de coordenadas de una página. El controlador de eventos onload se
    // ejecuta en la ventana actual después de que los documentos carguen la página web. En el ejemplo, el evento onload provoca la ejecución de una función anónima. Esta función,
    // a su vez, ejecuta la función addPara ().

// En este vídeo, aprendiste que puedes recuperar una referencia a un nodo mediante: document.getElementById (id): devuelve un elemento específico que se basa en el atributo id.
    // document.getElementsByTagName (tagName): recupera un conjunto de elementos con la etiqueta especificada.
// Puedes crear un elemento usando: document.createElement (tagName) y colocarlo usando: insertBefore, appendChild o replaceChild.
// Puede modificar los elementos mediante: element.innerHTML para recuperar o establecer el contenido de un elemento HTML, element.style para recuperar o establecer el estilo
    // CSS integrado, element.setAttribute para modificar los atributos de un elemento.

// Puede administrar un objeto de ventana mediante funciones que incluyen: window.open para devolver la referencia a un nuevo objeto de ventana para el navegador web,
    // window.dump («mensaje») para escribir una cadena en la consola del navegador web.

// Esta lista no es exhaustiva, ya que existen muchas más funciones que permiten trabajar con elementos y nodos HTML."