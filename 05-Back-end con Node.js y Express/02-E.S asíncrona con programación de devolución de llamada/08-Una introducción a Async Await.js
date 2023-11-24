// En el siguiente ejemplo de código, hemos creado una Promesa con una devolución de llamada donde manejamos la resolución y el rechazo.

// const axios = require('axios');

// const conectarConURL = (url) => {
//     const solicitud = axios.get(url);
//     console.log(solicitud);

//     solicitud.then(respuesta => {
//         let listaDeEntradas = respuesta.data.entries;
//         listaDeEntradas.forEach((entrada) => {
//             console.log(entrada.Category);
//         });
//     })
//     .catch(error => {
//         console.log(error.toString());
//     });
// };

// console.log("Antes de conectar con la URL");
// conectarConURL('https://api.publicapis.org/entries');
// console.log("Después de conectar con la URL");



// Veremos cómo se logra lo mismo con async/await.

// const axios = require('axios');

// const conectarConURL1 = async (url) => {
//     const resultado = await axios.get(url);
//     const listaDeEntradas = resultado.data.entries;

//     listaDeEntradas.forEach((entrada) => {
//         console.log(entrada.Category);
//     });
// };

// console.log("Antes de conectar con la URL");
// conectarConURL1('https://api.publicapis.org/entries');
// console.log("Después de conectar con la URL");



// El mejor uso de async/await se puede lograr cuando tenemos un escenario en el que algunos métodos asíncronos deben realizarse en secuencia. Tomando el mismo ejemplo anterior,
//  primero obtengamos una lista de todas las entradas por categorías y según ellas, enviemos una solicitud para obtener los detalles de cada entrada en esa categoría. Entonces,
//  estas dos acciones tienen que ocurrir una tras otra pero de forma asincrónica. Esto se puede lograr con o sin async/await. Pero encadenar acciones es mucho más limpio con
//  async await, como puedes observar a continuación. En situaciones reales, el anidamiento puede ser de varios niveles y hacer que el código sea difícil de leer y mantener. En
//  tales situaciones, podríamos usar async/await.

// El siguiente código se realiza anidando el segundo conjunto de promesas en el primero.

const axios = require('axios');

/*
En el siguiente código intentamos obtener la lista de todas las entradas desde una URL remota y, 
a partir de eso, hacemos solicitudes sobre cada una de las categorías. Finalmente, las imprimimos todas.
Estamos utilizando axios.get, que devuelve una promesa.
*/
const conectarConURL2 = (url) => {
    const solicitud = axios.get(url);
    solicitud.then(respuesta => {
        let listaDeEntradas = respuesta.data.entries;
        return listaDeEntradas.map((entrada) => {
            return entrada.Category;
        });
    }).then((categorias) => {
        let categoriasUnicas = categorias.filter(function(item, pos, self) {
            return self.indexOf(item) === pos;
        });

        categoriasUnicas.forEach((categoria) => {
            const solicitudCategoria = axios.get("https://api.publicapis.org/entries?Category=" + categoria);
            solicitudCategoria.then(respuestaCategoria => {
                console.log(categoria + " - " + respuestaCategoria.data.count);
            }).catch(errorCategoria => {
                // Manejar el error si es necesario
            });
        });
    }).catch(error => {
        console.log(error.toString());
    });
};

conectarConURL2('https://api.publicapis.org/entries');



// El mismo objetivo se logra usando async/await.

const axios = require('axios');

/*
En el siguiente código intentamos obtener la lista de todas las entradas desde una URL remota y, 
a partir de eso, hacemos solicitudes sobre cada una de las categorías que comienzan con 'A'.
Finalmente, imprimimos las cantidades de API de cada categoría. Estamos utilizando axios.get, que devuelve una promesa.
*/
async function conectarConURL(url) {
    try {
        const respuesta = await axios.get(url);
        const listaDeEntradas = respuesta.data.entries;
        let categorias = listaDeEntradas.map((entrada) => {
            return entrada.Category;
        });
        categorias = [...new Set(categorias)];

        categorias.forEach(async (categoria) => {
            if (categoria.startsWith("A")) {
                try {
                    const respuestaCategoria = await axios({
                        method: 'get',
                        url: "https://api.publicapis.org/entries?Category=" + categoria,
                        responseType: 'json'
                    });
                    console.log(categoria + "   " + respuestaCategoria.data.count);
                } catch (errorCategoria) {
                    console.log(errorCategoria);
                }
            }
        });
    } catch (error) {
        console.log(error.toString());
    }
}

conectarConURL('https://api.publicapis.org/entries').catch(error => {
    console.log(error.toString());
});


// Solo puedes esperar una promesa dentro de un método asíncrono. Esto se debe a que awaitbloquea el hilo.
// Esto anulará el propósito principal. Entonces, la función dentro de la cual awaitse usa an TIENE QUE SER asíncrona.