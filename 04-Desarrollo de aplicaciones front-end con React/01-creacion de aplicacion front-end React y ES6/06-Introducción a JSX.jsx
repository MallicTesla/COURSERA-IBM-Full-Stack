// "Bienvenido a la introducción a JSX Después de ver este vídeo, podrá explicar qué es JSX, describir la sintaxis de JSX y cómo se compila, describir las ventajas de usar JSX y
//     explicar cómo crear un componente de React con JSX.

// La extensión de sintaxis JSX o JavaScript XML es una extensión de JavaScript. Proporciona una forma más sencilla de crear una interfaz de usuario o componentes de interfaz de
//     usuario en React.

// JSX produce «elementos» de React que se pueden usar para renderizar el componente en el Document Object Model o DOM. La sintaxis JSX es similar a una sintaxis similar a la de
//     XML o HTML utilizada por React y que amplía ECMAScript, un estándar utilizado para la creación de scripts del lado del cliente. Esto permite que el texto XML o similar a
//     HTML coexista con el código JavaScript o React. La sintaxis JSX está destinada a ser utilizada por preprocesadores, por ejemplo, transpiladores o compiladores como Babel,
//     para transformar el texto similar al HTML que se encuentra en los archivos JavaScript en objetos JavaScript estándar.

// A continuación, un motor de JavaScript puede analizar estos objetos. Veamos un ejemplo de código JSX.
const el1 = <h1> funciona </h1>;
// El código muestra una construcción 'el1' que muestra el encabezado 'Este es un ejemplo de fragmento de código JSX'.
// El fragmento de código se parece a HTML, pero también utiliza una variable similar a JavaScript que no es HTML ni JavaScript, es JSX. 
// SX es básicamente una extensión de sintaxis del JavaScript normal y se usa para crear elementos de React. Luego, estos elementos se renderizan en el Modelo de Objetos de
//  Documento de React o DOM. JSX es un lenguaje declarativo que combina JavaScript con HTML. JSX hace que el código de React sea mucho más fácil de leer, escribir y entender.
// Por esta razón, casi todos los equipos de desarrollo de React utilizan JSX. Los navegadores no entienden JSX, por lo que necesitas usar Babel para compilar tu código JSX.
// Afortunadamente, el comando create-react-app se encargará de esta compilación y no tienes que preocuparte por ello.

// Analicemos algunos de los beneficios de usar JSX. Para empezar, las personas menos técnicas pueden entender y modificar las piezas requeridas. Los desarrolladores y
//  diseñadores de CSS encontrarán que JSX es más familiar que solo JavaScript.
// También puede aprovechar todo el potencial de JavaScript en HTML y evitar aprender o usar un lenguaje de plantillas. Además, si añades un paso de transformación en JSX,
//  encontrarás errores en tu HTML que, de otro modo, podrías pasar por alto.
// JSX promueve la idea de los estilos en línea. Al escribir grandes fragmentos de código, JSX le ayuda a mantener su código simple y elegante. Según los documentos de React, a
//  la mayoría de las personas les resulta útil como ayuda visual cuando trabajan con la interfaz de usuario dentro del código JavaScript. Además, JSX es más rápido que el
//  JavaScript normal, ya que realiza optimizaciones mientras se traduce a JavaScript normal.
// Por último, JSX se ocupa de los problemas habituales de saneamiento de los resultados para evitar ataques como la creación de scripts entre sitios.


// Importar la biblioteca React
import React from 'react';

// Definir un componente de función llamado App
const App_jsx = () => {
  // JSX: Crea un elemento div con una lista de dos elementos
    return (
        <div>
            <h1>Lista de Números</h1>
            <ul>
                <li>1</li>
                <li>2</li>
            </ul>
        </div>
);
};
// Exportar el componente para que pueda ser utilizado en otros archivos
export default App;

// Hagamos un componente de React con JSX y veamos cómo se traduce en llamadas normales a funciones de JavaScript. Para empezar, este ejemplo de código muestra una aplicación
//  que crea un elemento div con una lista de dos elementos que muestra los elementos número 1 y 2. La función App contiene código que se parece mucho al HTML simple y utiliza
//  la misma sintaxis basada en XML.


const App_js_normal = () => {
    return React.createElement('div', null,
    React.createElement('h1', null, 'Lista de Números'),
    React.createElement('ul', null,
        React.createElement('li', null, '1'),
        React.createElement('li', null, '2')
    )
    );
};
// Así es como se ve el código compilado en las llamadas normales a funciones de JavaScript. Sin JSX, el código de React tendría que escribirse con muchos anidados, lo que hace
//  que el código sea ilegible, feo y difícil de mantener. JSX combina la belleza del HTML y el poder de Javascript.

// En este vídeo aprendiste que: JSX o JavaScript Syntax Extension o JavaScript XML es una extensión de JavaScript.
// La sintaxis JSX está pensada para que la utilicen los preprocesadores, por ejemplo, transpiladores o compiladores como Babel, para transformar el texto similar al HTML que se
//  encuentra en los archivos JavaScript en objetos JavaScript estándar.
// Las principales ventajas de usar JSX son que puedes aprovechar todo el potencial de JavaScript en HTML y evitar aprender o usar un lenguaje de plantillas, y permite a React
//  mostrar útiles mensajes de error y advertencia."