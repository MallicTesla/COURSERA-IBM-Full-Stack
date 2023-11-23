// "Bienvenido a trabajar con los módulos de Node.js. Después de ver este vídeo, podrá: Describir los paquetes de Node.js. Importe los módulos Node.js a su script. Exporte
//     funciones y propiedades de un módulo y acceda a las propiedades exportadas desde un módulo.

// Un paquete consta de uno o más módulos. El archivo package.json describe los detalles sobre un módulo de Node.js. Si un módulo no tiene un archivo package.json, Node.js supone
//     que la clase principal se llama index.js. Para especificar un script principal diferente para el módulo, especifique una ruta relativa al script Node.js desde el directorio
//     del módulo. Este es un ejemplo de un archivo package.json. Los campos de nombre y versión forman un identificador único para el módulo; por ejemplo, today-1.0.0.
// El campo principal muestra una ruta al script principal de Node.js; en este ejemplo, el script today.js del subdirectorio lib. Package.json define muchos otros campos.
// Por ejemplo, la licencia indica los derechos de uso del módulo. Puede utilizar la función require para importar un módulo de Node.js.

let today = require ("./otro_archivo")
// La instrucción require asume que los scripts tienen la extensión de archivo .js. La función require crea un objeto que representa el módulo Node.js importado. En este ejemplo,
//  un archivo de script Node, js denominado today.js, se encuentra en el mismo directorio que la aplicación. Al llamar a require con el nombre de un subdirectorio, Node.js
//  busca un archivo de script con el mismo nombre que el subdirectorio. Si el archivo de script no existe, la función asume que el nombre es el nombre de un directorio y busca
//  un script llamado index.js en ese directorio.

// Para importar un módulo Node.js que consta de un único script, utilice la función require con una ruta relativa al archivo de script. En este ejemplo, la aplicación principal
//  se encuentra en el archivo de script Node.js. Hello.js realiza una llamada a una función obligatoria al archivo de script today.js. En este ejemplo se utiliza el mismo
//  archivo hello.js Node.js. El módulo Node.js se guarda en un directorio denominado mod_today. El archivo de script actual se guarda en index.js. Cuando hello.js realiza una
//  llamada a la función requerida del directorio mod_today, el archivo de script comprueba si existe un archivo llamado index.js. Es el nombre predeterminado de un script en un
//  módulo Node.js. Cada módulo de Node.js tiene un objeto de exportación implícito. Para que una función o un valor estén disponibles para las aplicaciones de Node.js que
//  importan el módulo, añada una propiedad a las exportaciones.

exports.DayOfWeek = function(){return days [ date.getDay() - 1];};
// En este ejemplo, la propiedad DayOfWeek se añade al objeto exports. A continuación, se asigna a DayOfWeek una función anónima que devuelve el día de la semana. Por ejemplo,
//  si la función DayOfWeek devuelve 1, este valor se asigna al lunes.

// Al importar un módulo de Node.js, la función require devuelve un objeto JavaScript que representa una instancia del módulo. Por ejemplo, la variable today es una instancia
//  del módulo Node.js de today que se denomina «today». Para acceder a las propiedades del módulo, recupere la propiedad de la variable.
// En el mismo ejemplo, Today.DayOfWeek representa la propiedad exportada actualmente desde el módulo Node.js de hoy.

// En este vídeo, aprendió lo siguiente: cada paquete tiene un archivo package.json que describe los detalles de un módulo Node.js.
// Para hacer que una función o un valor estén disponibles para las aplicaciones de Node.js que importan su módulo, añada una propiedad al objeto de exportación implícito
// Al importar un módulo Node.js, la función require devolverá un objeto JavaScript que representa una instancia del módulo."