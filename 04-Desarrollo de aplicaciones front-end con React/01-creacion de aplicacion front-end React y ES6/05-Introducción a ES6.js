// "Bienvenido a Introducción a ES6. Tras ver este vídeo, podrá: Definir ECMAScript 6 (ES6) y describir cómo utilizar las nuevas funciones que se han añadido a JavaScript como
//     parte de ES6. ES es la abreviatura de ECMAScript.

// Ecma es una organización de estándares que crea una amplia gama de estándares globales de tecnología de la información y las comunicaciones. JavaScript cumple con la
//     especificación ES6 de Ecma, que se publicó en 2015. Las versiones más recientes de ES llevan el nombre del año de lanzamiento. La más reciente es ECMAScript 2020. ES.next es
//     un nombre dinámico que se utiliza para referirse a la próxima versión de ECMAScript. ES6 es una versión con cambios que tuvieron un gran impacto. En JavaScript, los
//     principales cambios son let, const, arrow functions, promises y class.

// Está familiarizado con el uso de variables (vars). Una var tiene un alcance global. Una vez declarada, una var se puede usar o hacer referencia a ella desde cualquier parte del
//     código. Esto es un desafío, especialmente cuando se trata de proyectos de gran envergadura en los que hay que mantener muchas variables.

// En ES6, se utilizan let y const además de var.

function ejemploVariableLocal() {
    // Variable local declarada dentro de la función
    let variableLocal = "Soy una variable local";
    console.log(variableLocal);
}
// Variable global declarada fuera de cualquier función
let variableGlobal = "Soy una variable global";

// let permite restringir el alcance de las variables dentro del bloque en el que se declaran. Este ámbito limitado se denomina «ámbito local». En este ejemplo, num tiene un
//     alcance justo dentro de ese bloque.
// La línea 7 arrojará un error ya que num está fuera del alcance. const le permite declarar constantes cuyos valores no se pueden cambiar. La línea 3 arroja un error porque num
//  se define como una constante cuyo valor es 5. En la programación de React se utilizan tanto let como const.


// funcion normal
function suma(a, b) {
    return a + b;
}

// funcion flecha
const sumaFlecha = (a, b) => a + b;

// Las funciones de flecha te permiten declarar funciones del mismo modo que declaras variables. El uso de esta sintaxis es una forma más corta y limpia de trabajar con las
//  funciones. Lo que se ve aquí es cómo se escribía una función en el antiguo JavaScript de ES5. A continuación puedes ver cómo está escrita en ES6. Una función también se
//  puede declarar con let y const como si fuera una variable. Esta función no toma ningún parámetro y solo tiene una sentencia. Observe que no hay corchetes. Las funciones de
//  flecha se denominan igual que las funciones normales. También se pueden pasar como parámetros para las devoluciones de llamada. Aquí, la función de flecha, sayHello, se pasa
//  como parámetro de devolución de llamada a setTimeout. Las funciones de flecha también toman parámetros como las funciones normales.

// Pueden devolver un tipo de datos o un objeto. Aquí puede ver una función que toma un parámetro. Los corchetes de las funciones no son obligatorios. Además, solo hay una línea
//  de código. Sin embargo, dado que el código devuelve un valor, debe estar entre corchetes. Se trata de una función que utiliza dos parámetros. Los corchetes de la función
//  deben colocarse alrededor de la lista de parámetros.


// Función de flecha que toma dos parámetros y devuelve un valor
const multiplicar = (a, b) => a * b;

// Ejemplo de uso de la función
const resultado = multiplicar(3, 4);
console.log(resultado); // Salida esperada: 12
// Esta función también tiene una sola línea de código y no devuelve nada. Por lo tanto, no necesita corchetes. Se trata de una función que toma dos parámetros y devuelve un
//  valor.


// Función de flecha que toma dos parámetros y tiene dos líneas de código
const calcularPromedio = (a, b) => {
    // Realizar alguna operación
    const promedio = (a + b) / 2;
    // Devolver el resultado
    return promedio;
};
// Y esta es una función que toma dos parámetros y tiene dos líneas de código.


// Función de flecha que retorna una promesa
const promiseArgument = new Promise((resolve, reject) => {
    // Obtener el tiempo actual en milisegundos
    const tiempoActual = new Date().getTime();

    // Verificar si el tiempo actual es divisible por 2
    if (tiempoActual % 2 === 0) {
      // Cumplir la promesa si es divisible por 2
    resolve("Success");
    }
    else {
      // Rechazar la promesa si no es divisible por 2
    reject("Fallido");
    }
});

// Manejar el resultado de la promesa
promiseArgument
    .then(resultado => {
    console.log("La promesa se cumplió:", resultado);
    })
    .catch(error => {
    console.error("La promesa fue rechazada:", error);
    });
// El objeto de promesa representa la finalización final de una operación asíncrona y su valor de retorno. Cuando se invoca una operación asíncrona, una promesa está en estado
//  pendiente. Cuando la operación se ejecuta correctamente, se dice que la promesa se ha cumplido. Cuando la operación fracasa, se dice que la promesa ha sido rechazada.
// En el primer ejemplo, tenemos una función de flecha, PromiseArgument, que utiliza dos parámetros (resolver y rechazar). Si el tiempo actual en milisegundos es divisible entre
//  2, esta función de flecha invoca resolve con «Success» como parámetro; si no, invoca reject con «Fallido» como parámetro. Esta función se pasa al constructor del objeto de
//  promesa.


// Crear una promesa con una función de flecha directamente en el constructor
const promiseDirecta = new Promise((resolve, reject) => {
    // Obtener el tiempo actual en milisegundos
    const tiempoActual = new Date().getTime();
    // Verificar si el tiempo actual es divisible por 2
    if (tiempoActual % 2 === 0) {
      // Cumplir la promesa si es divisible por 2
    resolve("Success");
    }
    else {
      // Rechazar la promesa si no es divisible por 2
    reject("Fallido");
    }
});

// Manejar el resultado de la segunda promesa
promiseDirecta
    .then(resultado => {
    console.log("La segunda promesa se cumplió:", resultado);
    })
    .catch(error => {
    console.error("La segunda promesa fue rechazada:", error);
    });
// En el segundo ejemplo, en lugar de crear PromiseArgument, se crea directamente la función al compás del constructor de la promesa. El comportamiento en ambos casos es idéntico.

// La programación orientada a objetos se hizo posible en JavaScript con la introducción de la clase. La clase es una plantilla o modelo para crear objetos. Las clases en
//  JavaScript se basan en prototipos. El prototipo es una propiedad de todos los objetos de JavaScript, incluidas las funciones. Se puede usar una función para crear una
//  instancia de objeto.


// Definir una función constructora utilizando un prototipo
function Persona(nombre, edad) {
    this.nombre = nombre;
    this.edad = edad;
}

  // Agregar un método al prototipo
Persona.prototype.saludar = function() {
    console.log(`Hola, soy ${this.nombre}.`);
};

// Crear una instancia del objeto usando el constructor
const person1 = new Persona("Juan", 25);

// Imprimir el prototipo completo del objeto person1
console.log(Object.getPrototypeOf(person1));
// Imprimir el nombre de la persona
console.log(person1.nombre);
// Imprimir la edad de la persona
console.log(person1.edad);
// Llamar al método saludar
person1.saludar();
// En este caso, «esto» se refiere al objeto actual. Sin embargo, no todos los conceptos de programación orientada a objetos están disponibles con los prototipos de funciones.
// El concepto de clase se construyó sobre la premisa de un prototipo de función para extender la programación orientada a objetos a JavaScript. Aquí, el primer registro de la
//  consola imprimirá el prototipo completo del objeto person1. El segundo registro de la consola imprimirá el nombre. Y el registro de la tercera consola imprimirá la edad.


// Definir una clase llamada Rectangle
class Rectangulo {
    // Constructor que se llama al crear un objeto de la clase
    constructor(altura, anchura) {
    // Propiedades del rectángulo
    this.altura = altura;
    this.anchura = anchura;
    }

    // Método para calcular el área del rectángulo
    calcularArea() {
    return this.altura * this.anchura;
    }
}

// Crear un objeto rectangular utilizando la clase Rectangle
const miRectangulo = new Rectangulo(5, 10);

// Imprimir las propiedades del objeto
console.log(`Altura: ${miRectangulo.altura}`);
console.log(`Anchura: ${miRectangulo.anchura}`);

// Calcular y imprimir el área del rectángulo utilizando el método de la clase
console.log(`Área del rectángulo: ${miRectangulo.calcularArea()}`);
// La clase puede tener un constructor, que es un método al que se llama cuando se quiere crear un objeto de clase. El cuerpo de la clase es la parte que está entre corchetes.
// Aquí, el rectángulo es la clase general. Todos los rectángulos tienen cierta altura y anchura, que son las propiedades. Al crear un objeto rectangular, se pasan la altura y
//  la anchura como parámetros al constructor. myRectangle es un objeto construido con la clase Rectangle.
// En este ejemplo, se puede crear un objeto de la clase con la nueva palabra clave. Las propiedades se establecen en el objeto actual que se está creando, utilizando «esto»
//  como palabra clave. El rectángulo es el modelo. La palabra clave ayuda a establecer las propiedades del objeto myRectangle.


// Definir la superclase Rectangle
class Rectangulo {
    // Constructor de la superclase
    constructor(altura, anchura) {
    this.altura = altura;
    this.anchura = anchura;
    }

    // Método para calcular el área del rectángulo
    calcularArea() {
    return this.altura * this.anchura;
    }
}

// Definir la subclase Square que hereda de Rectangle
class Cuadrado extends Rectangulo {
    // Constructor de la subclase
    constructor(lado) {
    // Llamar al constructor de la superclase con super()
    super(lado, lado);
    }
}

// Crear un objeto rectangular utilizando la superclase Rectangle
const miRectangulo1 = new Rectangulo(5, 10);

// Imprimir el área del rectángulo utilizando el método de la superclase
console.log(`Área del rectángulo: ${miRectangulo1.calcularArea()}`);

// Crear un objeto cuadrado utilizando la subclase Square
const miCuadrado = new Cuadrado(5);

// Imprimir el área del cuadrado utilizando el método heredado de la superclase
console.log(`Área del cuadrado: ${miCuadrado.calcularArea()}`);

// En JavaScript ES6, una clase puede heredar de otra clase. La clase que hereda otra clase se denomina subclase. La superclase es la clase que hereda la subclase. La subclase
//  hereda todos los atributos y métodos de la superclase. Los componentes de React utilizan la herencia para crear componentes definidos por el usuario.
// La subclase tiene el privilegio especial de llamar al constructor de la superclase con la llamada al método super (). Un cuadrado es un rectángulo con el mismo valor de ancho
//  y alto. En este caso, si la altura no es la misma que la anchura especificada, la anchura será igual a la altura.



// En este vídeo, descubrió que las nuevas funciones que se introdujeron en JavaScript como parte de ES6 son let, const, arrow functions , promise y class.
// Puede crear diferentes tipos de funciones de flecha en función de los parámetros, los valores devueltos y las líneas de código.
// La programación orientada a objetos se hizo posible en JavaScript con la introducción de la clase.