// "Bienvenido a Introducción a los componentes. Después de ver este vídeo, podrás explicar qué son los componentes de React, describir las características de los componentes de
//     React, comparar y contrastar los cuatro tipos de componentes y crear un componente de Hello World React.

// Un componente es uno de los pilares fundamentales de React. En otras palabras, cada aplicación que desarrolle en React estará compuesta por piezas llamadas componentes.
// Los componentes facilitan la tarea de crear una interfaz de usuario. Puede dividir la interfaz de usuario en varias partes individuales denominadas componentes y fusionarlas
//     todas en un componente principal que forme la interfaz de usuario final.
// Los componentes de React te permiten dividir la interfaz de usuario en elementos separados. Luego, se pueden reutilizar y manipular de forma independiente.
// Un componente de React toma una entrada opcional y devuelve un objeto de React que se representa en la pantalla. Un componente de React representa una pequeña parte de la
//     interfaz de usuario de una página web.

// La función principal de un componente de React es renderizar su interfaz de usuario y actualizarla cada vez que se modifique su estado interno. Además de renderizar la interfaz
//     de usuario, administra los eventos que pertenecen a su interfaz de usuario, como un componente de botón que tiene un evento de clic. El estado es un objeto que describe cómo
//     se comportará y renderizará el componente en ese momento. Un componente de React puede ser «con estado» o «sin estado».

// Un componente con estado actualiza su interfaz de usuario con respecto a su estado. Los componentes «con estado» son del tipo de clase,
// Mientras que los componentes «sin estado» son del tipo de función.

// Los componentes de React cumplen estas funciones utilizando tres conceptos, propiedades, eventos y estados.
// Las propiedades se utilizan para pasar datos de un componente principal a un componente secundario.
// Los eventos permiten que el componente gestione los eventos y las acciones del modelo de objetos del documento (DOM) como resultado de la interacción del usuario en el sistema.
// Los estados permiten que el componente mantenga su estado y actualice la interfaz de usuario con respecto al estado actual del componente.

// En React, hay principalmente componentes funcionales, de clase, puros y de alto orden.
// Los componentes funcionales se pueden crear escribiendo una función de JavaScript. Estas funciones pueden o no recibir datos como parámetros.
// Los componentes funcionales son funciones que reciben accesorios y devuelven JSX. No tienen métodos nativos de estado o ciclo de vida, pero esta funcionalidad se puede agregar
//     implementando React Hooks, que es una nueva característica de React. Te permite usar las funciones de React sin tener que escribir la clase.
// Los métodos del ciclo de vida son métodos de React incorporados que funcionan en los componentes durante toda su duración en el DOM. Los componentes funcionales se utilizan
//     normalmente para mostrar información. Son fáciles de leer, depurar y probar. Los componentes funcionales no tienen estado. Y esto significa que un componente funcional no
//     tiene un estado y es una función simple de JavaScript.


const Documento = () => {
    return <h1> Funciono </h1>;
}
// Este ejemplo de código muestra un componente funcional válido en React. En el código, la función Democomponent devuelve un «Funciono».

// Los componentes de clase son un poco más complejos que los componentes funcionales. Puede pasar datos de un componente de clase a otros componentes de clase. Puedes usar las
//  clases ES6 de JavaScript para crear componentes basados en clases en React. Los componentes de clase se utilizan con más frecuencia que otros tipos de componentes. Esto se
//  debe a que los componentes de clase tienen algunas funciones adicionales en comparación con otros componentes. Pueden usar las principales funciones de React, como los
//  métodos de estado, accesorios y ciclo de vida. Los componentes de la clase tienen estado. Esto significa que tienen un estado que se puede volver a renderizar.


import React from 'react';
import DemoComponent from './DemoComponent'; // Asegúrate de tener la ruta correcta al archivo

const App = () => {
    return (
        <div>
            <h1>Aplicación React</h1>
            <DemoComponent />
        </div>
);
};
// export default App;

// Este código de ejemplo muestra un componente válido basado en clases en React. En el código, la clase Democomponent amplía React Component y, dentro de la clase, la función
//  de renderización devuelve un «Mensaje de bienvenida».

// Los componentes puros son mejores que los componentes funcionales. Los componentes puros se utilizan principalmente para proporcionar optimizaciones. Son los componentes más
//  sencillos y rápidos de escribir. No dependen ni modifican el estado de las variables fuera de su ámbito. Por lo tanto, los componentes puros pueden reemplazar a los
//  componentes funcionales simples.

// Un componente de orden superior (HOC) es una técnica avanzada en React para reutilizar la lógica de los componentes. Este componente no es un componente de React que esté
//  disponible en la API. Es un patrón que surgió de la naturaleza compositiva de React. Básicamente, los HOC son funciones que devuelven un componente o componentes que se
//  utilizan para compartir la lógica con otros componentes.


import React, { Component } from 'react';

// HOC que agrega una prop "saludo" al componente envuelto
const withSaludo = (WrappedComponent) => {
    return class extends Component {
    render() {
        return <WrappedComponent saludo="¡Hola, mundo!" {...this.props} />;
        }
    };
};

// Componente funcional Helloworld
const Helloworld = ({ saludo }) => {
    return <div>{saludo}</div>;
};

// Uso del HOC para envolver el componente Helloworld
const HelloworldConSaludo = withSaludo(Helloworld);

export default HelloworldConSaludo;
// Este es un ejemplo de un componente funcional para crear un componente Helloworld de muestra. Para definir tu componente Helloworld, utiliza primero la sentencia de
//  importación de JavaScript para importar React y el componente Text Core de React Native.
// Definimos un componente como una función «Helloworld». La función devuelve el texto «¡Hola, mundo!» A continuación, puede exportar el componente de su función, «Helloworld»,
//  con la exportación predeterminada de JavaScript para usarlo en toda la aplicación. Luego, la función se puede importar a cualquier aplicación.
// Este código es una de las muchas formas en las que puede definir su componente personalizado y exportarlo para usarlo en la aplicación.

// En este video aprendiste que: cada aplicación que desarrollarás en React estará compuesta por piezas llamadas componentes.
// Los componentes de React te permiten dividir la interfaz de usuario en partes separadas que luego se pueden reutilizar y manipular de forma independiente.
// Un componente de React proporciona estas funcionalidades: renderizar la interfaz de usuario inicial, gestionar y gestionar los eventos y actualizar la interfaz de usuario
//  cada vez que se cambia el estado interno.
// Y, por último, los cuatro tipos de componentes de React son los componentes funcionales, de clase, puros y de alto orden."