// "Bienvenido a Funciones y prototipos de JavaScript. Tras ver este vídeo, podrá describir las funciones en JavaScript, describir los prototipos en JavaScript y demostrar cómo
//     crear un objeto personalizado.

// Una función es un bloque de código al que se puede llamar desde cualquier punto de un script después de declararse. Una función se compone de las siguientes partes: La función
//     de palabra clave. El nombre de la función. Paréntesis, con argumentos de parámetros opcionales. Corchetes rizados, según la lógica. La última sentencia de un bloque de
//     funciones es la sentencia de retorno opcional que devuelve el control a lo que se llame la función.

// Este ejemplo es una función que se denomina add. Esta función toma dos argumentos de parámetro y devuelve la suma de los argumentos o concatena los dos argumentos si son cadenas.
// Tenga en cuenta que no especifica el tipo de datos de los argumentos de la función. Los tipos de datos vienen determinados por los valores de los argumentos que se pasan a la
//     función. No se ha declarado ningún tipo de retorno específico; la función devuelve el tipo que sea necesario. En este caso, la devolución es una simple suma o concatenación
//     de los parámetros de entrada.

// La acción elegida depende de los datos que se proporcionen a la función. Si los valores se pueden interpretar como números, se suman. Si se pueden interpretar como cadenas, se
//     concatenan.

// Este es un ejemplo de declaración de una función llamada Car que acepta tres argumentos como parámetros. Un poco más abajo, se pide específicamente a la función que se ejecute,
//     declarando la sentencia: var c = new Car con los argumentos «meridian», «Sabre GT» y 2012.
// En la función Car, la palabra clave «this» hace referencia a la instancia actual del objeto Car que se está creando.
// En otras palabras, una instancia de Car asociada a la variable denominada c.
// El uso de la palabra clave «this» permite diferenciar si se refiere a la instancia global o local de una variable.
// El uso de «model» en este ejemplo se refiere al argumento que se pasó a la función, mientras que el uso de «this.model» se refiere a la variable global «model» asociada a esta
//     instancia del objeto Car. La función getName de Car devuelve la marca, el modelo y el año del objeto Car recién creado.

// Los prototipos permiten definir fácilmente las propiedades y los métodos para todas las instancias de un objeto concreto. Todos los objetos de JavaScript que se pueden crear con
//     la palabra clave «nuevo» heredan las propiedades y los métodos de un «prototipo». Por ejemplo, el objeto «Coche» que creamos anteriormente hereda las propiedades de marca,
//     modelo y año de la función constructora, que están definidas implícitamente en el prototipo de coche.
// Cuando se crea un objeto de automóvil, ese objeto hereda todas las propiedades y métodos definidos por este prototipo. A diferencia de los objetos, los métodos y propiedades de
//     los prototipos se pueden cambiar con una sola llamada. Si quiere añadir una nueva propiedad a la función constructora de un objeto, por ejemplo, debe añadirla directamente a
//     la función añadiéndola como argumento adicional. No se puede hacer simplemente llamando al objeto en sí. Sin embargo, con un prototipo es posible añadir una propiedad o un
//     método con una sola llamada.
// Como todos los objetos tienen una propiedad de prototipo, esta es una forma más sencilla de añadir propiedades y funciones a los objetos. Cualquier objeto que se instancie
//     hereda el estado actual del prototipo. Si un prototipo cambia, todos los objetos que lo utilicen heredarán automáticamente las nuevas propiedades y funciones de ese
//     prototipo.
// Una forma de cambiar un prototipo es mediante un script, que puede anular las propiedades y funciones del prototipo.
// Este es otro ejemplo en el que se usa un prototipo para cambiar las instancias de Car. Esta vez, agregas una función de método llamada getName al prototipo de Car. Ahora, cuando
//     se crea una instancia de un objeto Car, también se incluye la función GetName, que devuelve la marca, el modelo y el año. Todas las instancias existentes del objeto Car
//     también heredan el método getName. Por lo general, las funciones se declaran primero y no se ejecutan hasta que se les pida específicamente que lo hagan, como se ha visto
//     en algunos de los ejemplos anteriores.
// Las funciones de invocación automática o ejecución automática comienzan a ejecutarse inmediatamente después de declararse. Las funciones y variables incluidas en las funciones
//     autoejecutables solo están disponibles para el código incluido en la función autoejecutable. Las funciones de invocación automática también pueden ser funciones anónimas o
//     sin nombre y tienen el formato que se muestra en el bloque de código de la diapositiva. Las funciones de ejecución automática se suelen utilizar para inicializar datos o
//     declarar elementos DOM en la página.

// En este vídeo, aprendiste: una función es un bloque de código al que se puede llamar desde cualquier punto de un script después de declararlo.
// Las funciones pueden tomar los argumentos pasados como parámetros y devolver resultados.
// Al usar prototipos, puede definir fácilmente las propiedades y los métodos para todas las instancias de un objeto específico.
// Existen prototipos para todos los objetos de JavaScript que se pueden crear con la nueva palabra clave.
// Para añadir una nueva función a la plantilla del objeto, modifique el prototipo del objeto.
// Las funciones de ejecución automática (invocación automática) comienzan a ejecutarse inmediatamente después de declararse.
// Las funciones y variables están aisladas del resto del script.

function add(a, b) {
    return a + b; // Devuelve la suma de los argumentos
}

// Ejemplo de uso de la función "add"
var result = add(2, 3); // Llama a la función "add" con argumentos 2 y 3
console.log(result); // Imprimirá 5

var textResult = add("Hello", " World"); // Llama a la función "add" con cadenas
console.log(textResult); // Imprimirá "Hello World"


function Car(make, model, year) {
    this.make = make;
    this.model = model;
    this.year = year;
}

// Función de prototipo que devuelve información del coche
Car.prototype.getName = function () {
    return this.make + " " + this.model + " " + this.year;
};

// Creación de una instancia de un objeto Car
var c = new Car("Meridian", "Sabre GT", 2012);

console.log(c.getName()); // Imprimirá "Meridian Sabre GT 2012"


// Agregando una función de método "getName" al prototipo de Car
Car.prototype.getName = function () {
    return this.make + " " + this.model + " " + this.year;
};

// Creación de una nueva instancia de un objeto Car
var newCar = new Car("Another", "Model", 2023);

console.log(newCar.getName()); // Imprimirá "Another Model 2023"
