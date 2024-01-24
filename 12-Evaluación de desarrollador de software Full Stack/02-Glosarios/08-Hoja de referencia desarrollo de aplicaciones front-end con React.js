// Arrow function
// Las funciones de flecha le permiten escribir una sintaxis de función más corta.	
hello = () => { return "Hello World!"; }


// class
// La clase es una plantilla o modelo para crear un objeto.	
function Car(name, year) {
    this.name = name;
    this.year = year;
    return this;
}

let myCar = new Car("Ford", 2014);

console.log(myCar);
console.log(myCar.name);
console.log(myCar.year);


// Hooks
// Las funciones llamadas enlaces permiten "conectarse" a características del estado y ciclo de vida de React desde los componentes de la función.	
import React, { useState } from 'react';

function CntApp() {
    const [count, setCount] = useState(0);

    return (
        <div>
            You clicked {count} times
            <button onClick={() => setCount(count + 1)}>Click me</button>
        </div>
    );
}

export default CntApp;


// Inheritance
// Una clase creada con herencia de clases hereda todos los métodos de otra clase.
class Square extends Rectangle {
    constructor(height, width) {
        if (height === width) {
            super(height, width);
        } else {
            super(width, width);
        }
    }
}

let mySquare = new Square(5, 5);


// let and const
// let le permite restringir el alcance de las variables dentro del bloque donde se declaran. const le permite declarar constantes cuyos valores no se pueden cambiar.
{
    let a = 10;
    console.log(a);
    a = 15;
    console.log(a);
}
// console.log(a);

const num = 5;
console.log(num);
// num = 8;


// Mounting - Montaje
// Cuando se crea y agrega una instancia de componente al DOM, estos métodos se invocan en el siguiente orden:
//                                                                                                              constructor(), getDerivedStateFromProps(),
//                                                                                                              render(), componenteDidMount().
import React from 'react';

class Header extends React.Component {
constructor(props) {
    super(props);
    console.log("Inside the constructor");
}

componentDidMount() {
    console.log("Inside component did mount");
}

render() {
    console.log("Inside render method");
    return (
        <div>
            The component is rendered
        </div>
    );
}
}

export default Header;


// onClick
// 	Cuando se activa un evento, los controladores de eventos deciden qué debe suceder a continuación. Esto podría implicar presionar un botón o alterar una entrada de texto.
import React from 'react';
import ReactDOM from 'react-dom';

function ChangeColor() {
    const shoot = () => {
        alert("Color Changed!");
    }

    return (
        <button onClick={shoot}>Change the Color!</button>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<ChangeColor />);

// Promises - Promesas
// 	El objeto Promise representa la eventual finalización (o falla) de una operación asincrónica y su valor resultante.	
let promiseArgument = (resolve, reject) =>
    setTimeout(() => {
        let currTime = new Date().getTime();

        if (currTime % 2 === 0) {
            resolve("Success");

        } else {
            reject("Failed!!!");
        }
    }, 2000);

let myPromise = new Promise(promiseArgument);


// Props - Accesorios
// Props es la abreviatura de propiedades y se utiliza para pasar datos entre componentes de React.
class TestComponent extends React.Component {
    render() {
        return (
            <div>
                Hi {this.props.name}
            </div>
        );
    }
}


{/* <TestComponent name='John' /> */}
{/* <TestComponent name='Jill' /> */}


// React class Component -Componente de clase reaccionar
// El componente de clase React contiene: accesorios: establecidos desde fuera de la clase, estado: interno de la clase
import React from "react";

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = { change: true };
    }

    render() {
        return (
        <div>
            <button onClick={() => { this.setState({ change: !this.state.change }); }}>
                Click Here!
            </button>
            {this.state.change ? "Hello!!" : "Welcome to the React Course"}
        </div>
        );
    }
}

export default App;


// React components
// Los componentes son segmentos de código reutilizables que se incluyen en los tipos de componentes funcionales y de clase.
import React from 'react';
import { Text } from 'react-native';

const Helloworld = () => {
    return (
        <Text>
            Hello, World!
        </Text>
    );
}

export default Helloworld;


// React Forms
// React hace uso de formularios para permitir la interacción del usuario con el sitio web.
import React, { useState } from "react";

export default function App() {
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = (event) => {
        console.log(`Email: ${email} Password: ${password}`);
        event.preventDefault();
    }

    return (
        <form onSubmit={handleSubmit}>
            <h1>Registration</h1>
            <label>
                Email:
                <input
                name="email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
                />
            </label>

            <label>
                Password:
                <input
                name="password"
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                required
                />
            </label>

            <button type="submit">Submit</button>

        </form>
    );
}


// React state
// 	El objeto de estado es donde se guardan los valores de propiedad del componente.
import React, { Component } from "react";

class TestComponent extends React.Component {
    constructor() {
        super();
        this.state = {
            id: 1,
            name: "John",
            age: 28,
        };
    }

    render() {
        return (
            <div>
                {this.state.name} {this.state.age}
            </div>
        );
    }
}

export default TestComponent;


// Redux
// Redux es una biblioteca de administración de estado que se usa a menudo con React para manejar el estado de su aplicación. El estado de una aplicación es como un objeto
//  global que contiene información que se utiliza para diversos fines más adelante en la aplicación.

// $ npm install redux react-redux --save


// Unmounting - Desmontaje
// Cuando un componente se elimina o desmonta del DOM, el método componenteWillUnmount() nos permite ejecutar código React.	
import React from 'react';

class ComponentOne extends React.Component {
    componentWillUnmount() {
        console.log('The component is going to be unmounted');
    }

    render() {
        return <div>Inner component</div>;
    }
    }

    class App extends React.Component {
    state = { innerComponent: <ComponentOne /> };

    componentDidMount() {
        setTimeout(() => {
            this.setState({ innerComponent: null });
        }, 5000);
    }

    render() {
        console.log("Inside render");
        return <div>{this.state.innerComponent}</div>;
    }
}

export default App;


// Updating - Actualizando
// Cuando se actualiza un componente, se llaman cinco métodos en el mismo orden: getDerivedStateFromProps(), deberíaComponentUpdate(), render(), getSnapshotBeforeUpdate(),
//  componenteDidUpdate()	
import React from 'react';

class App extends React.Component {
    state = { counter: "0" };

    incrementCounter = () => {
        this.setState({ counter: parseInt(this.state.counter) + 1 });
    };

    shouldComponentUpdate() {
        console.log("Inside shouldComponentUpdate");
        return true;
    }

    getSnapshotBeforeUpdate(prevProps, prevState) {
        console.log("Inside getSnapshotBeforeUpdate");
        console.log("Prev counter is " + prevState.counter);
        console.log("New counter is " + this.state.counter);
        return prevState;
    }

    componentDidUpdate() {
        console.log("Inside componentDidUpdate");
    }

    render() {
        console.log("Inside render");
        return (
            <div>
                <button onClick={this.incrementCounter}>Click Me!</button>
                {this.state.counter}
            </div>
        );
    }
}

export default App;