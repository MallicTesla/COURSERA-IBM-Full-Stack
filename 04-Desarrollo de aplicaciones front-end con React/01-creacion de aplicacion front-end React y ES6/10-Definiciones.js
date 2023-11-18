// let and const
// let le permite restringir el alcance de las variables dentro del bloque donde se declaran.
// const le permite declarar constantes cuyos valores no se pueden cambiar.
{
    let a = 10
    console.log(a)
    a = 15
    console.log(a)
}
console.log(a)
const num = 5
console.log(num)
num = 8
console.log(num)
// ---------------------------------------------------------------------------------------------------------
// Arrow function
// Las funciones de flecha le permiten escribir una sintaxis de función más corta.

hello = () =>
{
    return "Hello World!";
}
// ------------------------------------------------------------------------------------------------------------
// Promises
// El objeto Promise representa la eventual finalización (o falla) de una operación asincrónica y su valor resultante.

let promiseArgument = (resolve, reject) =>{
    setTimeout (() => {
    let currTime = new Date().getTime();
    if(currTime % 2 === 0){
        resolve("Success");
    }
    else{
        reject("Failed!!!");}
    },2000);
};

let myPromise = new Promise(promiseArgument);
// ------------------------------------------------------------------------------------------------------------
// class
// La clase es una plantilla o modelo para crear objetos.

function car (name,year)
{
    this.name = name
    this.year = year
    return this;
}
let car = car("Ford", 2014)
console.log(car)
console.log(car.name)
console.log(car.year)
// ------------------------------------------------------------------------------------------------------------
// Inheritence
// Una clase creada con una herencia de clases hereda todos los métodos de otra clase.

class Square extends Rectangle
{
    constructor(height,width)
    {
        if(height === width)
        {
            super(height,width)
        }
        else
        {
            super(width,width)
        }
    }
}
let mySquare = new Square(5,5)
// ------------------------------------------------------------------------------------------------------------
// React components
// Los componentes son segmentos de código reutilizables que se incluyen en los tipos de componentes funcionales y de clase.

import React from 'react';
import {Text} from 'react-native';

const Helloworld = () => {
    return (
        <Text>Hello, World!</Text>
    );
}

export default Helloworld;
// ------------------------------------------------------------------------------------------------------------
// React class Component
// El componente de clase React contiene: Accesorios: establecidos desde fuera de la clase Estado: interno de la clase


import React from "react";

class App extends React.Component {
constructor(props) {
    super(props);
    this.state = { change: true };
}

render() {
    return (
        <div>
            <button onClick={() => { this.setState({ change: !this.state.change }); }}>Click Here!</button>
            {this.state.change ? <p>Hello!!</p> : <p>Welcome to the React Course</p>}
        </div>
        );
    }
}

// export default App;
// ------------------------------------------------------------------------------------------------------------
// onClick
// Cuando se activa un evento, los controladores de eventos deciden qué debe suceder a continuación. Esto podría implicar presionar un botón o alterar una entrada de texto.

function changeColor() {
    const shoot = () => {
        alert("Color Changed!");
    }
    return (
    <button onClick={change}>Change the Color! </button>
    );
    }
    const root = ReactDOM.createRoot(document.getElementById('root'));
    root.render(<changeColor />);
