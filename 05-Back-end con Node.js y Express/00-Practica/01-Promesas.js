// // Creando un método de promesa. La promesa se resolverá cuando el temporizador agote los 6 segundos.
// let miPromesa = new Promise((resolver, rechazar) => {
//     setTimeout(() => {
//         resolver("Promesa resuelta")
//     }, 6000);
// });

// // Console log antes de llamar a la promesa
// console.log("Antes de llamar a la promesa");

// // Llama a la promesa y espera a que se resuelva y luego imprime un mensaje.
// miPromesa.then((mensajeExitoso) => {
//     console.log("Desde el Callback " + mensajeExitoso)
// });

// // Console log después de llamar a la promesa
// console.log("Después de llamar a la promesa");


// --------------------------------------------------------------------------------------------------------------
// let miPromesa1 = new Promise((resolver, rechazar) => {
//     setTimeout(() => {
//         resolver("Promesa 1 resuelta");
//     }, 6000);
// });

// let miPromesa2 = new Promise((resolver, rechazar) => {
//     setTimeout(() => {
//         resolver("Promesa 2 resuelta");
//     }, 3000);
// });

// miPromesa1.then((mensajeExitoso1) => {
//     console.log("Desde el Callback " + mensajeExitoso1);
//     miPromesa2.then((mensajeExitoso2) => {
//         console.log("Desde el Callback " + mensajeExitoso2);
//     });
// });


// --------------------------------------------------------------------------------------------------------------
let miPromesa1 = new Promise((resolver, rechazar) => {
    setTimeout(() => {
        resolver("Promesa 1 resuelta");
    }, 6000);
});

let miPromesa2 = new Promise((resolver, rechazar) => {
    setTimeout(() => {
        resolver("Promesa 2 resuelta");
    }, 3000);
});

miPromesa1.then((mensajeExitoso1) => {
    console.log("Desde el Callback de la Promesa 1: " + mensajeExitoso1);
});

miPromesa2.then((mensajeExitoso2) => {
    console.log("Desde el Callback de la Promesa 2: " + mensajeExitoso2);
});
